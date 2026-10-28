// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const menu = document.querySelector(".menu");
toggle?.addEventListener("click", () => {
  const open = menu.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});
menu?.addEventListener("click", (e) => {
  if (e.target.tagName === "A") menu.classList.remove("open");
});

// Footer year
document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

// Enquiry forms: no backend needed, the form opens WhatsApp with a pre-filled message
document.querySelectorAll("[data-enquiry]").forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    const lines = [
      "Hello Al-Trekking Rinjani, I'd like to enquire about a trek.",
      `Name: ${d.name}`,
      `Email: ${d.email}`,
      d.country && `Country: ${d.country}`,
      `Trek: ${d.trek}`,
      d.date && `Preferred date: ${d.date}`,
      `Group size: ${d.people}`,
      d.message && `Message: ${d.message}`,
    ].filter(Boolean);
    window.open(`https://wa.me/${window.AGENCY_WA}?text=${encodeURIComponent(lines.join("\n"))}`, "_blank");
  });
});

// Highlight the active tab on trek pages
const tabs = document.querySelectorAll(".tabs a");
if (tabs.length) {
  const sections = [...tabs].map((a) => document.querySelector(a.getAttribute("href")));
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        tabs.forEach((a) => a.classList.toggle("active", a.getAttribute("href") === `#${entry.target.id}`));
      });
    },
    { rootMargin: "-40% 0px -55% 0px" }
  );
  sections.forEach((s) => s && observer.observe(s));
}
