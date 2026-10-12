// Apollo Advising charts: one shared tooltip for hover and keyboard focus.
(function () {
  var tip = document.createElement("div");
  tip.className = "chart-tip";
  tip.setAttribute("role", "status");
  document.body.appendChild(tip);
  var show = function (el, x, y) {
    tip.textContent = el.getAttribute("data-tip");
    var r = tip.getBoundingClientRect();
    var left = Math.min(Math.max(8, x - r.width / 2), window.innerWidth - r.width - 8);
    var top = y - r.height - 12;
    if (top < 8) top = y + 16;
    tip.style.left = left + "px";
    tip.style.top = top + "px";
    tip.classList.add("on");
  };
  var hide = function () { tip.classList.remove("on"); };
  document.addEventListener("pointermove", function (e) {
    var el = e.target.closest && e.target.closest(".chart [data-tip]");
    if (el) show(el, e.clientX, e.clientY); else hide();
  });
  document.addEventListener("focusin", function (e) {
    var el = e.target.closest && e.target.closest(".chart [data-tip]");
    if (!el) return hide();
    var r = el.getBoundingClientRect();
    show(el, r.left + r.width / 2, r.top);
  });
  document.addEventListener("focusout", hide);
  window.addEventListener("scroll", hide, { passive: true });
})();
