// Apollo Advising tools: 1031 deadline calculator and rental strategy comparison.
(function () {
  function num(s) {
    var n = parseFloat(String(s).replace(/[^0-9.\-]/g, ""));
    return isFinite(n) ? n : 0;
  }
  function money(n) {
    return (n < 0 ? "-$" : "$") + Math.round(Math.abs(n)).toLocaleString("en-US");
  }

  /* 1031 exchange deadlines */
  var dl = document.querySelector("[data-1031]");
  if (dl) {
    var inp = dl.querySelector("input[type=date]");
    var o = function (k) { return dl.querySelector("[data-o=" + k + "]"); };
    var warn = o("warn");
    var calBtn = dl.querySelector("[data-cal]");
    var parse = function (v) { var p = v.split("-"); return new Date(+p[0], p[1] - 1, +p[2]); };
    var add = function (d, n) { var x = new Date(d.getTime()); x.setDate(x.getDate() + n); return x; };
    var fmt = function (d) { return d.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", year: "numeric" }); };
    var ymd = function (d) { return d.getFullYear() + String(d.getMonth() + 1).padStart(2, "0") + String(d.getDate()).padStart(2, "0"); };
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var rel = function (d) {
      var n = Math.round((d - today) / 864e5);
      if (n === 0) return "That is today.";
      return n > 0 ? n + (n === 1 ? " day" : " days") + " from today." : "That date passed " + -n + (n === -1 ? " day" : " days") + " ago.";
    };
    var last = null;
    var update = function () {
      if (!inp.value) return;
      var c = parse(inp.value), a = add(c, 45), b = add(c, 180), due = new Date(c.getFullYear() + 1, 3, 15);
      o("d45").textContent = fmt(a);
      o("d180").textContent = fmt(b);
      o("r45").textContent = rel(a);
      o("r180").textContent = rel(b);
      if (b > due) {
        warn.hidden = false;
        o("due").textContent = due.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" });
      } else {
        warn.hidden = true;
      }
      last = { c: c, a: a, b: b };
      var tl = document.querySelector("[data-timeline]");
      if (tl) {
        var q = function (k) { return tl.querySelector("[data-o=" + k + "]"); };
        var short = function (d) { return d.toLocaleDateString("en-US", { month: "short", day: "numeric" }); };
        q("tl-close").textContent = c.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" });
        q("tl-d0").textContent = short(c);
        q("tl-d45").textContent = short(a);
        q("tl-d180").textContent = short(b);
        var dueDays = Math.round((due - c) / 864e5), dueEl = q("tl-due"), risk = q("tl-risk");
        if (dueDays < 180) {
          dueEl.hidden = false; risk.hidden = false; if (q("tl-risk-leg")) q("tl-risk-leg").hidden = false;
          dueEl.style.left = (dueDays / 190 * 100) + "%";
          risk.style.left = (dueDays / 190 * 100) + "%";
          risk.style.width = ((180 - dueDays) / 190 * 100) + "%";
          q("tl-due-d").textContent = short(due);
        } else {
          dueEl.hidden = true; risk.hidden = true; if (q("tl-risk-leg")) q("tl-risk-leg").hidden = true;
        }
      }
    };
    inp.addEventListener("input", update);
    inp.addEventListener("change", update);
    if (calBtn) {
      calBtn.addEventListener("click", function () {
        if (!last) return;
        var ev = function (d, title, desc) {
          return ["BEGIN:VEVENT", "UID:" + ymd(d) + "-" + title.length + "@apolloadvising.com", "DTSTAMP:" + ymd(new Date()) + "T000000Z",
            "DTSTART;VALUE=DATE:" + ymd(d), "DTEND;VALUE=DATE:" + ymd(add(d, 1)), "SUMMARY:" + title, "DESCRIPTION:" + desc,
            "BEGIN:VALARM", "TRIGGER:-P7D", "ACTION:DISPLAY", "DESCRIPTION:" + title, "END:VALARM", "END:VEVENT"].join("\r\n");
        };
        var ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Apollo Advising//1031 deadlines//EN",
          ev(last.a, "1031 exchange: identify replacement property (day 45)", "Signed written identification must reach your qualified intermediary by the end of this day. Confirm with your intermediary and CPA."),
          ev(last.b, "1031 exchange: close on replacement property (day 180)", "Last day of the exchange period, unless your tax return is due earlier. Confirm with your intermediary and CPA."),
          "END:VCALENDAR"].join("\r\n");
        var a = document.createElement("a");
        a.href = URL.createObjectURL(new Blob([ics], { type: "text/calendar" }));
        a.download = "1031-exchange-deadlines.ics";
        document.body.appendChild(a);
        a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
      });
    }
    update();
  }

  /* Rental strategy comparison */
  var sc = document.querySelector("[data-strategy]");
  if (sc) {
    var f = sc.elements;
    var put = function (k, v) { var el = sc.querySelector("[data-o=" + k + "]"); if (el) el.textContent = v; };
    var names = { str: "Short-term", mtr: "Medium-term", ltr: "Long-term" };
    var calc = function () {
      var v = function (n) { return num(f[n].value); };
      var g = {
        str: v("str_rate") * 365 * v("str_occ") / 100,
        mtr: v("mtr_rent") * v("mtr_months"),
        ltr: v("ltr_rent") * v("ltr_months")
      };
      var pct = function (k, n) { return g[k] * v(n) / 100; };
      var hot = g.str * v("str_hot") / 100, hotOwner = f.str_hotmode.value === "owner";
      var hotNote = sc.querySelector("[data-o=str_hotnote]");
      if (hotNote) hotNote.textContent = hotOwner ? money(hot) + " a year comes out of your rate." : "Guests pay about " + money(hot) + " a year on top. Not counted as your cost.";
      var cost = {
        str: v("str_clean") + v("str_fees") + v("str_util") + v("str_monthly") * 12 + v("str_furn") + pct("str", "str_mgmt") + pct("str", "str_maint") + pct("str", "str_capex") + (hotOwner ? hot : 0),
        mtr: v("mtr_clean") + v("mtr_fees") + v("mtr_util") + v("mtr_monthly") * 12 + v("mtr_furn") + pct("mtr", "mtr_mgmt") + pct("mtr", "mtr_maint") + pct("mtr", "mtr_capex"),
        ltr: v("ltr_turn") + v("ltr_monthly") * 12 + pct("ltr", "ltr_mgmt") + pct("ltr", "ltr_maint") + pct("ltr", "ltr_capex")
      };
      var net = {};
      ["str", "mtr", "ltr"].forEach(function (k) {
        net[k] = g[k] - cost[k];
        put(k + "_gross", money(g[k]));
        put(k + "_cost", money(cost[k]));
        put(k + "_net", money(net[k]));
      });
      var order = ["str", "mtr", "ltr"].sort(function (a, b) { return net[b] - net[a]; });
      sc.querySelectorAll("[data-col]").forEach(function (col) { col.classList.toggle("is-top", col.getAttribute("data-col") === order[0]); });
      var chart = document.querySelector("[data-live-strategy]");
      if (chart) {
        var mx = Math.max(g.str, g.mtr, g.ltr, 1);
        ["str", "mtr", "ltr"].forEach(function (k) {
          var row = chart.querySelector("[data-k=" + k + "]");
          var total = Math.max(g[k], 0), keep = Math.max(Math.min(net[k], total), 0), spent = Math.max(total - keep, 0);
          row.querySelector(".sb__bar").style.width = (total / mx * 100) + "%";
          var nEl = row.querySelector(".sb__net"), cEl = row.querySelector(".sb__cost");
          nEl.style.flexBasis = (total ? keep / total * 100 : 0) + "%";
          cEl.style.flexBasis = (total ? spent / total * 100 : 0) + "%";
          row.querySelector(".sb__lab").textContent = money(net[k]);
          row.querySelector(".sb__gross").textContent = money(g[k]);
          nEl.setAttribute("data-tip", names[k] + ": " + money(net[k]) + " left after operating costs");
          cEl.setAttribute("data-tip", names[k] + ": " + money(cost[k]) + " in operating costs");
        });
        var gs = [g.str, g.mtr, g.ltr], ns = [net.str, net.mtr, net.ltr];
        chart.querySelector("figcaption strong").textContent = "Gross rent varies by " + money(Math.max.apply(null, gs) - Math.min.apply(null, gs)) + ". What is left varies by " + money(Math.max.apply(null, ns) - Math.min.apply(null, ns)) + ".";
      }
      put("sum", names[order[0]] + " keeps the most: " + money(net[order[0]]) + " a year, " + money(net[order[0]] - net[order[1]]) + " more than " + names[order[1]].toLowerCase() + " and " + money(net[order[0]] - net[order[2]]) + " more than " + names[order[2]].toLowerCase() + ". Gross rent differs by " + money(Math.max(g.str, g.mtr, g.ltr) - Math.min(g.str, g.mtr, g.ltr)) + ".");
    };
    sc.addEventListener("input", calc);
    sc.addEventListener("change", calc);
    sc.addEventListener("submit", function (e) { e.preventDefault(); });
    calc();
  }
})();
