// Apollo Advising booking: reads live availability from the Apollo Wix site as a visitor,
// then hands the chosen time to Wix's hosted checkout (booking form and payment).
const API = "https://www.wixapis.com";
const CLIENT_ID = "de8b48ef-b9f8-4f9f-9320-eb82d8403b47";
const TZ = "America/Chicago";
const KEY = "apollo-visitor-" + CLIENT_ID;
const SERVICES = {
  strategy: { id: "c4f0da76-bfae-4601-bf9d-070ae9de6519", name: "Strategy Session" },
  intro: { id: "cc815296-149c-433d-8e57-0796c8bd26b9", name: "Free intro call" }
};
const PLAN_ID = "f72f4929-db1b-4ec0-b4d3-a0ab9b8d1a94";

let mem = null;
function load() {
  if (mem) return mem;
  try { mem = JSON.parse(localStorage.getItem(KEY) || "null"); } catch (e) { mem = null; }
  return mem;
}
function save(t) { mem = t; try { localStorage.setItem(KEY, JSON.stringify(t)); } catch (e) {} }
async function mint(body) {
  const r = await fetch(API + "/oauth2/token", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ clientId: CLIENT_ID, ...body }) });
  if (!r.ok) throw new Error("auth");
  const d = await r.json();
  return { accessToken: d.access_token, refreshToken: d.refresh_token, expiresAt: Date.now() + d.expires_in * 1000 };
}
async function token() {
  const t = load();
  if (t && t.expiresAt - 60000 > Date.now()) return t.accessToken;
  let f = null;
  if (t && t.refreshToken) { try { f = await mint({ grantType: "refresh_token", refreshToken: t.refreshToken }); } catch (e) {} }
  if (!f) f = await mint({ grantType: "anonymous" });
  save(f);
  return f.accessToken;
}
async function post(path, body) {
  const r = await fetch(API + path, { method: "POST", headers: { "Content-Type": "application/json", Authorization: await token() }, body: JSON.stringify(body) });
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(d.message || "Request failed (" + r.status + ")");
  return d;
}

const pad = (n) => String(n).padStart(2, "0");
const ymd = (d) => d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate());
function chicagoToday() {
  const p = new Intl.DateTimeFormat("en-US", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" }).formatToParts(new Date());
  const g = (t) => Number(p.find((x) => x.type === t).value);
  return new Date(g("year"), g("month") - 1, g("day"));
}
function fmtTime(local) {
  const [h, m] = local.slice(11, 16).split(":").map(Number);
  const ap = h >= 12 ? "PM" : "AM";
  return ((h % 12) || 12) + ":" + pad(m) + " " + ap;
}

const els = {
  choice: document.querySelectorAll("[data-service]"),
  days: document.getElementById("days"),
  times: document.getElementById("times"),
  status: document.getElementById("status"),
  plan: document.getElementById("buy-block")
};
let current = new URLSearchParams(location.search).get("s") === "intro" ? "intro" : "strategy";
let currentDay = null;

function setStatus(msg, err) { els.status.textContent = msg || ""; els.status.classList.toggle("err", !!err); }

function renderChoice() {
  els.choice.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.service === current)));
}

const DAYS = 28;
let byDay = {};
let loadSeq = 0;

function renderDays() {
  els.days.innerHTML = "";
  const start = chicagoToday();
  for (let i = 0; i < DAYS; i++) {
    const d = new Date(start); d.setDate(start.getDate() + i);
    const key = ymd(d);
    const open = (byDay[key] || []).length;
    const b = document.createElement("button");
    b.type = "button";
    b.dataset.day = key;
    b.disabled = !open;
    b.setAttribute("aria-pressed", String(key === currentDay));
    b.setAttribute("aria-label", d.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" }) + (open ? ", " + open + " open times" : ", no open times"));
    b.innerHTML = "<small>" + d.toLocaleDateString("en-US", { weekday: "short" }) + "</small><b>" + d.getDate() + "</b><small>" + d.toLocaleDateString("en-US", { month: "short" }) + "</small>" + (open ? '<span class="dot"></span>' : "");
    b.addEventListener("click", () => pickDay(key));
    els.days.appendChild(b);
  }
}

async function loadAvailability() {
  const seq = ++loadSeq;
  byDay = {}; currentDay = null;
  els.times.innerHTML = "";
  renderDays();
  setStatus("Checking open times...");
  const start = chicagoToday();
  const end = new Date(start); end.setDate(start.getDate() + DAYS);
  try {
    let cursor = null, slots = [];
    do {
      const body = { serviceId: SERVICES[current].id, fromLocalDate: ymd(start) + "T00:00:00", toLocalDate: ymd(end) + "T00:00:00", timeZone: TZ, bookable: true, cursorPaging: cursor ? { limit: 100, cursor } : { limit: 100 } };
      const res = await post("/service-availability/v2/time-slots", body);
      slots = slots.concat(res.timeSlots || []);
      cursor = res.cursorPagingMetadata && res.cursorPagingMetadata.cursors && res.cursorPagingMetadata.cursors.next;
    } while (cursor && slots.length < 1000);
    if (seq !== loadSeq) return;
    slots.filter((s) => s.bookable !== false).forEach((s) => { const k = s.localStartDate.slice(0, 10); (byDay[k] = byDay[k] || []).push(s); });
    const first = Object.keys(byDay).sort()[0];
    if (!first) { renderDays(); setStatus("No open times in the next four weeks. Email denver@apolloadvising.com and we will find one."); return; }
    pickDay(first);
  } catch (e) {
    if (seq !== loadSeq) return;
    setStatus("Open times could not load. Refresh the page or email denver@apolloadvising.com.", true);
  }
}

function pickDay(day) {
  currentDay = day;
  renderDays();
  els.times.innerHTML = "";
  const slots = byDay[day] || [];
  if (!slots.length) { setStatus("No open times this day. Try another date."); return; }
  const d = new Date(day + "T00:00:00");
  setStatus(d.toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric" }) + ". Times shown in Central Time.");
  slots.forEach((s) => {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = fmtTime(s.localStartDate);
    b.addEventListener("click", () => checkout(s, b));
    els.times.appendChild(b);
  });
}

async function checkout(slot, btn) {
  els.times.querySelectorAll("button").forEach((b) => (b.disabled = true));
  btn.textContent = "Opening...";
  setStatus("Taking you to the secure booking form...");
  try {
    const res = await post("/_api/redirects-api/v1/redirect-session", {
      bookingsCheckout: {
        timezone: TZ,
        slotAvailability: {
          slot: { serviceId: slot.serviceId, scheduleId: slot.scheduleId, startDate: slot.localStartDate, endDate: slot.localEndDate, timezone: TZ },
          bookable: true
        }
      },
      callbacks: { postFlowUrl: location.origin + "/book/", thankYouPageUrl: location.origin + "/thanks/" }
    });
    location.href = res.redirectSession.fullUrl;
  } catch (e) {
    setStatus("That time could not be held. Pick another time.", true);
    loadAvailability();
  }
}

async function buyBlock() {
  els.plan.disabled = true;
  els.plan.textContent = "Opening checkout...";
  try {
    const res = await post("/_api/redirects-api/v1/redirect-session", {
      paidPlansCheckout: { planId: PLAN_ID },
      callbacks: { postFlowUrl: location.origin + "/book/", thankYouPageUrl: location.origin + "/thanks/" }
    });
    location.href = res.redirectSession.fullUrl;
  } catch (e) {
    els.plan.disabled = false;
    els.plan.textContent = "Buy the 3-hour block";
    setStatus("Checkout could not start. Try again or email denver@apolloadvising.com.", true);
  }
}

els.choice.forEach((b) => b.addEventListener("click", () => {
  current = b.dataset.service;
  renderChoice();
  loadAvailability();
}));
if (els.plan) els.plan.addEventListener("click", buyBlock);
renderChoice();
loadAvailability();
