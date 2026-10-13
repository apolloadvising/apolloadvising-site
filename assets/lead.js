// Apollo Advising free worksheet signup: sends name and email to the Wix lead form
// (which creates or updates the Wix contact and applies the lead label), then opens the download page.
(function () {
  var API = "https://www.wixapis.com";
  var CLIENT_ID = "de8b48ef-b9f8-4f9f-9320-eb82d8403b47";
  var FORM_ID = "d56290bc-8f59-4679-94d4-79cee6a142d7";
  var NEXT = "/free/hold-sell-or-1031-checklist/thanks/";

  async function token() {
    var r = await fetch(API + "/oauth2/token", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ clientId: CLIENT_ID, grantType: "anonymous" }) });
    if (!r.ok) throw new Error("auth");
    return (await r.json()).access_token;
  }

  document.querySelectorAll("form[data-lead]").forEach(function (form) {
    var err = form.querySelector(".lead__err");
    var btn = form.querySelector("button[type=submit]");
    var label = btn.textContent;
    function fail(msg, el) { err.textContent = msg; err.hidden = false; if (el) el.focus(); }

    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      err.hidden = true;
      var first = form.elements.first_name.value.trim();
      var email = form.elements.email.value.trim();
      if (!first) return fail("Enter your first name.", form.elements.first_name);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return fail("Enter a valid email address.", form.elements.email);
      btn.disabled = true;
      btn.textContent = "Sending...";
      try {
        var t = await token();
        var r = await fetch(API + "/form-submission-service/v4/submissions", {
          method: "POST", headers: { "Content-Type": "application/json", Authorization: t },
          body: JSON.stringify({ submission: { formId: FORM_ID, submissions: {
            first_name_lm: first, email_lm: email, subscribe_lm: !!form.elements.optin.checked,
            source_lm: (form.getAttribute("data-source") || location.pathname).slice(0, 200)
          } } })
        });
        if (!r.ok) throw new Error("submit " + r.status);
        window.location.href = NEXT;
      } catch (x) {
        btn.disabled = false;
        btn.textContent = label;
        fail("That did not go through. Please try again, or email denver@apolloadvising.com and we will send it to you.");
      }
    });
  });
})();
