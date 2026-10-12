// Apollo Advising: return-on-equity sentence. Type over the figures; the result updates as you type.
(function () {
  function num(s) {
    var n = parseFloat(String(s).replace(/[^0-9.\-]/g, ""));
    return isFinite(n) ? n : 0;
  }
  function money(n) {
    return "$" + Math.round(Math.abs(n)).toLocaleString("en-US");
  }
  var ctx = document.createElement("canvas").getContext("2d");
  function fit(i) {
    var cs = getComputedStyle(i);
    ctx.font = cs.fontWeight + " " + cs.fontSize + " " + cs.fontFamily;
    var ls = parseFloat(cs.letterSpacing) || 0;
    i.style.width = Math.ceil(ctx.measureText(i.value || "0").width + ls * (i.value.length || 1) + 3) + "px";
  }
  document.querySelectorAll("[data-roe]").forEach(function (root) {
    var form = root.querySelector("form");
    var el = form.elements;
    var pct = root.querySelector("[data-out=pct]");
    var say = root.querySelector("[data-out=say]");
    function calc() {
      var v = num(el.mv.value), o = num(el.owed.value), n = num(el.net.value), e = v - o;
      if (e <= 0) {
        pct.textContent = "No equity";
        say.textContent = "When you owe as much as the property is worth, return on equity does not apply yet. Cash flow and risk are the questions to look at.";
        return;
      }
      var r = (n / e) * 100;
      pct.textContent = (Math.abs(r) < 10 ? r.toFixed(1) : Math.round(r)) + "%";
      if (n >= 0) {
        say.textContent = "is what your " + money(e) + " of equity earns each year in cash flow, before appreciation and loan paydown. That is " + money((n / e) * 100000) + " a year for every $100,000 tied up in the property.";
      } else {
        say.textContent = "is the cash return on your " + money(e) + " of equity. The property is costing you " + money(n) + " a year before appreciation and loan paydown.";
      }
    }
    form.addEventListener("submit", function (ev) { ev.preventDefault(); });
    Array.prototype.forEach.call(form.querySelectorAll("input"), function (i) {
      fit(i);
      i.addEventListener("input", function () { fit(i); calc(); });
      i.addEventListener("focus", function () { i.select(); });
      i.addEventListener("blur", function () {
        var n = num(i.value);
        i.value = Math.round(n).toLocaleString("en-US");
        fit(i);
        calc();
      });
    });
    calc();
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () { Array.prototype.forEach.call(form.querySelectorAll("input"), fit); });
    }
  });
})();
