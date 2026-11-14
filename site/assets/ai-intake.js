// Apollo Advising free AI cost review: validates the intake, saves a draft in this browser, sends the answers to the
// Wix form "AI Cost Review Intake" (which creates or updates the Wix contact), then opens the thank-you page.
(function () {
  var API = "https://www.wixapis.com";
  var CLIENT_ID = "de8b48ef-b9f8-4f9f-9320-eb82d8403b47";
  var DRAFT = "apollo-ai-intake";
  var form = document.getElementById("ai-intake");
  if (!form) return;
  var err = form.querySelector(".pa-err");
  var btn = form.querySelector("[data-ai-submit]");
  // Midpoints of each monthly spend range, used only for a rough total in Denver's summary.
  var MID = { "$0 (free version)": 0, "Under $100": 50, "$100 to $500": 300, "$500 to $1,000": 750, "$1,000 to $2,500": 1750, "$2,500 or more": 3000 };

  function val(n) { var el = form.elements[n]; if (!el) return ""; if (el.length && el[0] && el[0].type === "radio") { var c = form.querySelector('[name="' + n + '"]:checked'); return c ? c.value : ""; } return (el.value || "").trim(); }
  function checks(n) { return Array.prototype.map.call(form.querySelectorAll('[name="' + n + '"]:checked'), function (c) { return c.value; }); }
  function labelFor(el) { var f = el.closest(".pa-f"); return f ? f.getAttribute("data-label") : el.name; }

  function save() {
    try {
      var d = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === "submit") return;
        if (el.type === "checkbox") { if (el.checked) (d[el.name] = d[el.name] || []).push(el.value); }
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
        if (el.type === "checkbox") el.checked = [].concat(d[el.name]).indexOf(el.value) > -1;
        else if (el.type === "radio") el.checked = d[el.name] === el.value;
        else el.value = d[el.name];
      });
    } catch (x) {}
  }

  function fail(msg, el) { err.textContent = msg; err.hidden = false; if (el && el.focus) el.focus(); return false; }
  function check() {
    err.hidden = true;
    var req = form.querySelectorAll("[required]");
    for (var i = 0; i < req.length; i++) {
      var el = req[i];
      if (el.type === "checkbox" ? !el.checked : !el.value.trim()) {
        return fail(el.type === "checkbox" ? "Please confirm the first checkbox above to continue." : labelFor(el) + " is required.", el);
      }
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val("email"))) return fail("Enter a valid email address.", form.elements.email);
    return true;
  }

  function phone(p) { var d = p.replace(/\D/g, ""); if (d.length === 10) return "+1" + d; if (d.length === 11 && d[0] === "1") return "+" + d; return ""; }

  function summary() {
    var lines = [], total = 0, unknown = 0, spendLines = [], notUsed = [];
    form.querySelectorAll('[name^="spend_"]').forEach(function (s) {
      var k = s.name.slice(6), tool = val("tool_" + k), sp = s.value;
      if (sp === "We do not use this") { notUsed.push(labelFor(s).replace(": monthly cost", "")); return; }
      if (!tool && !sp) return;
      var lab = labelFor(s).replace(": monthly cost", "");
      spendLines.push("- " + lab + ": " + (tool || "(tool not given)") + ", " + (sp || "cost not given"));
      if (sp in MID) total += MID[sp]; else if (sp) unknown++;
    });
    lines.push("BUSINESS: " + [val("company"), val("industry"), val("team") && "team " + val("team"), val("city"), val("revenue") && "revenue " + val("revenue"), val("website")].filter(Boolean).join(" | "));
    lines.push("");
    lines.push("TOOLS AND MONTHLY SPEND:");
    lines = lines.concat(spendLines.length ? spendLines : ["- none given"]);
    if (spendLines.length) lines.push("Rough monthly total from ranges: about $" + total.toLocaleString() + (unknown ? " (" + unknown + " marked not sure)" : ""));
    if (notUsed.length) lines.push("Does not use: " + notUsed.join(", "));
    lines.push("");
    lines.push("HEADACHES: " + (checks("headaches").join("; ") || "none checked"));
    lines.push("Admin hours per week: " + (val("admin_hours") || "-") + " | Lead response: " + (val("response") || "-"));
    if (val("leads_from")) lines.push("Leads come from: " + val("leads_from"));
    if (val("one_thing")) lines.push("Fix in 90 days: " + val("one_thing"));
    lines.push("");
    lines.push("MEET: " + (val("meet") || "-") + " | Timeline: " + (val("timeline") || "-") + " | Heard via: " + (val("heard") || "-"));
    lines.push("Email opt-in: " + (form.querySelector('[name="optin"]').checked ? "yes" : "no"));
    return { text: lines.join("\n").slice(0, 3900), total: total, spend: spendLines.length ? "about $" + total.toLocaleString() + " per month across " + spendLines.length + " categories" : "" };
  }

  async function token() {
    var r = await fetch(API + "/oauth2/token", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ clientId: CLIENT_ID, grantType: "anonymous" }) });
    if (!r.ok) throw new Error("auth");
    return (await r.json()).access_token;
  }

  form.addEventListener("input", save);
  form.addEventListener("change", save);
  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    if (check() !== true) return;
    var sm = summary();
    var s = { first_name_ai: val("first_name"), email_ai: val("email"), industry_ai: val("industry"), intake_details_ai: sm.text };
    if (val("last_name")) s.last_name_ai = val("last_name");
    var ph = phone(val("phone")); if (ph) s.phone_ai = ph;
    if (val("company")) s.company_ai = val("company");
    if (checks("headaches").length) s.headaches_ai = checks("headaches").join("; ").slice(0, 900);
    if (sm.spend) s.software_spend_ai = sm.spend;
    btn.disabled = true;
    btn.textContent = "Sending your answers...";
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
      btn.textContent = "Send and book my free call";
      fail("Your answers could not be sent. Please try again, or email denver@apolloadvising.com. Your answers are saved in this browser.");
    }
  });

  restore();
})();
