// Apollo Advising longer-session request: preferred dates (no times) for the 3-hour block, in-person days, and travel days.
// Sends to the Wix form "In-Person Day Request" (creates or updates the Wix contact), then opens the thank-you page.
(function () {
  var API = "https://www.wixapis.com";
  var CLIENT_ID = "de8b48ef-b9f8-4f9f-9320-eb82d8403b47";
  var DRAFT = "apollo-day-request";
  var form = document.getElementById("day-request");
  if (!form) return;
  var err = form.querySelector(".pa-err");
  var btn = form.querySelector("[data-day-submit]");
  var dates = ["date1", "date2", "date3"].map(function (n) { return form.elements[n]; });

  function val(n) { var el = form.elements[n]; if (!el) return ""; if (el.length && el[0] && el[0].type === "radio") { var c = form.querySelector('[name="' + n + '"]:checked'); return c ? c.value : ""; } return (el.value || "").trim(); }
  function checked(n) { var el = form.querySelector('[name="' + n + '"]'); return !!(el && el.checked); }
  function labelFor(el) { var f = el.closest(".pa-f"); return f ? f.getAttribute("data-label") : el.name; }
  function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  // Minimum notice: 2 days for the block (24 hours plus a buffer), 7 for in-person days, 14 for travel days.
  function noticeDays() { var e = val("engagement"); return /^On site/.test(e) ? 14 : /^In person/.test(e) ? 7 : 2; }
  function minDate() { var d = new Date(); d.setDate(d.getDate() + noticeDays()); return iso(d); }
  function setMin() { var m = minDate(); dates.forEach(function (el) { if (el) el.min = m; }); }
  function pretty(s) { if (!s) return ""; var p = s.split("-"); var d = new Date(+p[0], +p[1] - 1, +p[2]); return d.toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric", year: "numeric" }); }

  function save() {
    try {
      var d = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === "submit") return;
        if (el.type === "checkbox") { if (el.checked) d[el.name] = true; }
        else if (el.type === "radio") { if (el.checked) d[el.name] = el.value; }
        else d[el.name] = el.value;
      });
      localStorage.setItem(DRAFT, JSON.stringify(d));
    } catch (x) {}
  }
  function restore() {
    try {
      var d = JSON.parse(localStorage.getItem(DRAFT) || "{}");
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || !(el.name in d)) return;
        if (el.type === "checkbox") el.checked = !!d[el.name];
        else if (el.type === "radio") el.checked = d[el.name] === el.value;
        else el.value = d[el.name];
      });
    } catch (x) {}
    var q = new URLSearchParams(location.search).get("e");
    if (q && !val("engagement")) {
      var pick = { block: 0, half: 1, full: 2, travel: 3 }[q];
      var opts = form.querySelectorAll('[name="engagement"]');
      if (pick !== undefined && opts[pick]) opts[pick].checked = true;
    }
  }

  function fail(msg, el) { err.textContent = msg; err.hidden = false; if (el && el.focus) el.focus(); return false; }
  function check() {
    err.hidden = true;
    if (!val("engagement")) return fail("Choose the session you want to book.", form.querySelector('[name="engagement"]'));
    var m = minDate();
    for (var i = 0; i < dates.length; i++) {
      var el = dates[i];
      if (i === 0 && !el.value) return fail("Pick at least one preferred date.", el);
      if (el.value && el.value < m) return fail(labelFor(el) + " needs to be " + pretty(m) + " or later for this session.", el);
      if (el.value) { var p = el.value.split("-"); var wd = new Date(+p[0], +p[1] - 1, +p[2]).getDay(); if (wd === 0 || wd === 6) return fail(labelFor(el) + " falls on a weekend. Please pick a weekday.", el); }
    }
    if (!val("first_name")) return fail("First name is required.", form.elements.first_name);
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val("email"))) return fail("Enter a valid email address.", form.elements.email);
    if (checked("sms") && !phone(val("phone"))) return fail("Add a 10-digit phone number so Denver can text you, or uncheck the text option.", form.elements.phone);
    if (!checked("consent")) return fail("Please confirm the first checkbox above to continue.", form.querySelector('[name="consent"]'));
    return true;
  }

  function phone(p) { var d = p.replace(/\D/g, ""); if (d.length === 10) return "+1" + d; if (d.length === 11 && d[0] === "1") return "+" + d; return ""; }

  function summary() {
    var ds = dates.map(function (el) { return pretty(el.value); }).filter(Boolean);
    var lines = [
      "SESSION: " + val("engagement") + (val("topic") ? " | Topic: " + val("topic") : ""),
      "PREFERRED DATES: " + ds.join("; ") + (val("daypart") ? " | Time of day: " + val("daypart") : ""),
      "WHERE: " + (val("location") || "-"),
      "COMPANY: " + (val("company") || "-"),
      "",
      "GOALS: " + (val("goals") || "-"),
      "",
      "Text messages OK: " + (checked("sms") ? "yes" : "no")
    ];
    return { text: lines.join("\n").slice(0, 3900), dates: ds.join("; ") };
  }

  async function token() {
    var r = await fetch(API + "/oauth2/token", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ clientId: CLIENT_ID, grantType: "anonymous" }) });
    if (!r.ok) throw new Error("auth");
    return (await r.json()).access_token;
  }

  form.addEventListener("input", save);
  form.addEventListener("change", function (e) { save(); if (e.target.name === "engagement") setMin(); });
  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    if (check() !== true) return;
    var sm = summary();
    var s = { first_name_day: val("first_name"), email_day: val("email"), industry_day: val("engagement"), headaches_day: sm.dates,
              software_spend_day: checked("sms") ? "Yes" : "No", intake_details_day: sm.text };
    if (val("last_name")) s.last_name_day = val("last_name");
    var ph = phone(val("phone")); if (ph) s.phone_day = ph;
    if (val("company")) s.company_day = val("company");
    btn.disabled = true;
    btn.textContent = "Sending your request...";
    try {
      var t = await token();
      var r = await fetch(API + "/form-submission-service/v4/submissions", {
        method: "POST", headers: { "Content-Type": "application/json", Authorization: t },
        body: JSON.stringify({ submission: { formId: form.getAttribute("data-form"), submissions: s } })
      });
      if (!r.ok) throw new Error("submit " + r.status);
      try { localStorage.removeItem(DRAFT); } catch (x) {}
      window.location.href = form.getAttribute("data-next");
    } catch (x) {
      btn.disabled = false;
      btn.textContent = "Send my request";
      fail("Your request could not be sent. Please try again, or email denver@apolloadvising.com. Your answers are saved in this browser.");
    }
  });

  restore();
  setMin();
})();
