// Apollo Advising property analysis intake: conditional sections, "estimate it" toggles, draft saving,
// then a Wix Forms submission and a hand-off to Wix checkout through the matching payment link.
(function () {
  var form = document.getElementById("pa");
  if (!form || !window.PA) return;
  var API = "https://www.wixapis.com";
  var CLIENT_ID = "de8b48ef-b9f8-4f9f-9320-eb82d8403b47";
  var DRAFT = "apollo-pa-draft";
  var submitBtn = form.querySelector("[data-pa-submit]");
  var errEl = form.querySelector(".pa-err");
  var progEl = document.querySelector("[data-pa-progress]");

  function vals(name) {
    return Array.prototype.map.call(form.querySelectorAll('[name="' + name + '"]:checked'), function (i) { return i.value; });
  }
  function val(name) {
    var el = form.elements[name];
    if (!el) return "";
    if (el instanceof RadioNodeList) { var c = vals(name); return c.join(", "); }
    return el.value.trim();
  }
  function test(cond) {
    return cond.split(";").every(function (part) {
      var bits = part.split(":"), key = bits[0], opts = bits.slice(1).join(":").split("|");
      var have = key === "q" ? vals("q") : [val(key)];
      return opts.some(function (o) { return have.indexOf(o) >= 0; });
    });
  }
  function visible(el) {
    for (var n = el; n && n !== form; n = n.parentElement) if (n.hidden) return false;
    return true;
  }
  function apply() {
    document.querySelectorAll("[data-show]").forEach(function (el) {
      var c = el.getAttribute("data-show");
      // Field-level conditions written as "a:x|y|q:z" mean: show if any listed key matches.
      var groups = c.split(/\|(?=[a-z_]+:)/);
      el.hidden = !groups.some(test);
    });
    var tier = val("tier") || "standard";
    submitBtn.textContent = "Submit and continue to payment, " + (tier === "rush" ? "$149" : "$99");
    progress();
  }
  function progress() {
    var fields = form.querySelectorAll(".pa-f");
    var total = 0, done = 0;
    fields.forEach(function (f) {
      if (!visible(f)) return;
      total++;
      var filled = Array.prototype.some.call(f.querySelectorAll("input,select,textarea"), function (i) {
        if (i.type === "checkbox" || i.type === "radio") return i.checked;
        return i.value.trim() !== "";
      });
      if (filled) done++;
    });
    if (progEl) progEl.textContent = total ? Math.round(done / total * 100) : 0;
  }

  // "Not sure, estimate it" toggles
  form.querySelectorAll("[data-est]").forEach(function (cb) {
    var input = form.elements[cb.getAttribute("data-est")];
    cb.addEventListener("change", function () {
      input.disabled = cb.checked;
      if (cb.checked) input.value = "";
      input.closest(".pa-f").classList.toggle("is-est", cb.checked);
    });
  });

  // Draft saving
  function save() {
    var d = {};
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === "submit") return;
      if (el.type === "checkbox" || el.type === "radio") {
        if (el.checked) (d[el.name] = d[el.name] || []).push(el.value);
      } else if (el.value) d[el.name] = el.value;
    });
    form.querySelectorAll("[data-est]:checked").forEach(function (cb) { (d.__est = d.__est || []).push(cb.getAttribute("data-est")); });
    try { localStorage.setItem(DRAFT, JSON.stringify(d)); } catch (e) {}
  }
  function restore() {
    var d;
    try { d = JSON.parse(localStorage.getItem(DRAFT) || "null"); } catch (e) { d = null; }
    if (!d) return;
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || !(el.name in d)) return;
      if (el.type === "checkbox" || el.type === "radio") el.checked = [].concat(d[el.name]).indexOf(el.value) >= 0;
      else if (el.tagName !== "BUTTON") el.value = d[el.name];
    });
    (d.__est || []).forEach(function (n) {
      var cb = form.querySelector('[data-est="' + n + '"]');
      if (cb) { cb.checked = true; cb.dispatchEvent(new Event("change")); }
    });
  }

  // Section rail highlighting
  var rail = document.querySelectorAll(".pa-rail li");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var id = e.target.id.replace("pa-", "");
        rail.forEach(function (li) { li.classList.toggle("is-on", li.getAttribute("data-rail") === id); });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    form.querySelectorAll(".pa-sec").forEach(function (s) { io.observe(s); });
  }

  // Build a readable summary of every answer
  function summary() {
    var lines = [];
    var tier = val("tier") === "rush" ? "Rush: PDF within 1 business day, $149" : "Standard: PDF within 2 business days, $99";
    lines.push("TURNAROUND: " + tier, "");
    form.querySelectorAll(".pa-sec").forEach(function (sec) {
      if (!visible(sec) || sec.id === "pa-review") return;
      var out = [];
      sec.querySelectorAll(".pa-f").forEach(function (f) {
        if (!visible(f)) return;
        var label = f.getAttribute("data-label"), v;
        var est = f.querySelector("[data-est]");
        if (est && est.checked) v = "Not sure, please estimate";
        else {
          var checks = f.querySelectorAll("input[type=checkbox]:not([data-est]):checked, input[type=radio]:checked");
          if (checks.length) v = Array.prototype.map.call(checks, function (c) { return c.getAttribute("data-text") || c.value; }).join("; ");
          else {
            var i = f.querySelector("input:not([type=checkbox]):not([type=radio]),select,textarea");
            v = i ? i.value.trim() : "";
            if (v && i.closest(".pa-affix")) {
              var a = i.closest(".pa-affix").querySelectorAll("i");
              a.forEach(function (x) { v = x.previousElementSibling === i ? v + x.textContent : x.textContent + v; });
            }
          }
        }
        if (v) out.push(label + ": " + v);
      });
      if (out.length) lines.push("== " + sec.getAttribute("data-title").toUpperCase() + " ==", out.join("\n"), "");
    });
    return lines.join("\n").trim();
  }

  function phone(p) {
    var d = p.replace(/\D/g, "");
    if (d.length === 10) return "+1" + d;
    if (d.length === 11 && d[0] === "1") return "+" + d;
    return "";
  }

  function fail(msg, el) {
    errEl.textContent = msg;
    errEl.hidden = false;
    if (el) { el.focus(); el.scrollIntoView({ block: "center" }); }
  }

  function check() {
    errEl.hidden = true;
    if (!vals("q").length) return fail("Choose at least one question for the report.", form.querySelector('[name="q"]'));
    var req = form.querySelectorAll("[required]");
    for (var k = 0; k < req.length; k++) {
      var el = req[k];
      if (!visible(el) || el.disabled) continue;
      if (el.type === "radio" ? !vals(el.name).length : el.type === "checkbox" ? !el.checked : !el.value.trim()) {
        var lab = el.closest(".pa-f, .pa-tiers, .pa-consent");
        return fail((lab && lab.getAttribute("data-label") ? lab.getAttribute("data-label") + " is required." : el.type === "checkbox" ? "Please confirm the acknowledgment above to continue." : "Please complete the required fields."), el);
      }
    }
    var em = form.elements.email;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value.trim())) return fail("Enter a valid email address.", em);
    return true;
  }

  async function token() {
    var r = await fetch(API + "/oauth2/token", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ clientId: CLIENT_ID, grantType: "anonymous" }) });
    if (!r.ok) throw new Error("auth");
    return (await r.json()).access_token;
  }

  form.addEventListener("input", function () { apply(); save(); });
  form.addEventListener("change", function () { apply(); save(); });
  form.addEventListener("submit", async function (e) {
    e.preventDefault();
    if (check() !== true) return;
    var tier = val("tier") === "rush" ? "rush" : "standard";
    var qs = Array.prototype.map.call(form.querySelectorAll('[name="q"]:checked'), function (c) { return c.getAttribute("data-text"); });
    var s = {
      first_name_pa: val("first_name"),
      email_pa: val("email"),
      property_address_pa: val("address"),
      turnaround_pa: tier === "rush" ? "Rush: PDF within 1 business day, $149" : "Standard: PDF within 2 business days, $99",
      main_question_pa: qs.join("; ").slice(0, 900),
      intake_details_pa: summary()
    };
    if (val("last_name")) s.last_name_pa = val("last_name");
    var ph = phone(val("phone"));
    if (ph) s.phone_pa = ph;
    submitBtn.disabled = true;
    submitBtn.textContent = "Sending your answers...";
    try {
      var t = await token();
      var r = await fetch(API + "/form-submission-service/v4/submissions", {
        method: "POST", headers: { "Content-Type": "application/json", Authorization: t },
        body: JSON.stringify({ submission: { formId: window.PA.form, submissions: s } })
      });
      if (!r.ok) throw new Error("submit " + r.status);
      try { localStorage.removeItem(DRAFT); } catch (x) {}
      submitBtn.textContent = "Received. Opening secure checkout...";
      window.location.href = window.PA.pay[tier];
    } catch (err) {
      submitBtn.disabled = false;
      apply();
      fail("Your answers could not be sent. Please try again, or email denver@apolloadvising.com and we will take it from there. Your answers are saved in this browser.");
    }
  });

  restore();
  apply();
})();
