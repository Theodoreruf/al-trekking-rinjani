"""Generate the static Al-Trekking Rinjani website into site/.

Usage:
    python3 build.py                  # build only
    python3 build.py --serve [PORT]   # build, then serve on the local network
"""
import socket
import sys
from functools import partial
from html import escape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote

from content import AGENCY, EXCLUDED, FAQ, INCLUDED, PACKING, TREKS, WHY_US

OUT = Path(__file__).parent / "site"


def wa_link(text="Hello Al-Trekking Rinjani, I would like to book a trek."):
    return f"https://wa.me/{AGENCY['whatsapp']}?text={quote(text)}"


def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{escape(i)}</li>" for i in items) + "</ul>"


def faq_html():
    return "".join(
        f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in FAQ
    )


def enquiry_form(trek_title=""):
    options = "".join(
        f'<option{" selected" if t["title"] == trek_title else ""}>{escape(t["title"])}</option>'
        for t in TREKS
    )
    return f"""
<form class="enquiry" data-enquiry>
  <div class="grid-2">
    <label>Name<input name="name" required></label>
    <label>Email<input name="email" type="email" required></label>
    <label>Country<input name="country"></label>
    <label>Trek<select name="trek">{options}<option>Custom trip</option></select></label>
    <label>Preferred date<input name="date" type="date"></label>
    <label>Group size<input name="people" type="number" min="1" value="2"></label>
  </div>
  <label>Message<textarea name="message" rows="4" placeholder="Dietary needs, questions, pickup location…"></textarea></label>
  <button class="btn btn-primary" type="submit">Send enquiry via WhatsApp</button>
  <p class="form-note">Prefer email? Write to <a href="mailto:{AGENCY['email']}">{AGENCY['email']}</a></p>
</form>"""


def page(title, body, root="", description=""):
    nav_treks = "".join(
        f'<a href="{root}treks/{t["slug"]}.html">{escape(t["title"])}</a>' for t in TREKS
    )
    desc = escape(description or f"{AGENCY['name']}: {AGENCY['tagline']}")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="{root}assets/img/logo.svg">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="{root}index.html"><img class="logo-mark" src="{root}assets/img/logo.svg" alt="" width="57" height="57"><span>Al-Trekking <b>Rinjani</b></span></a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    <nav class="menu">
      <a href="{root}index.html">Home</a>
      <div class="dropdown">
        <a href="{root}index.html#treks">Treks ▾</a>
        <div class="dropdown-menu">{nav_treks}</div>
      </div>
      <a href="{root}index.html#about">About</a>
      <a href="{root}index.html#faq">FAQ</a>
      <a href="{root}contact.html">Contact</a>
      <a class="btn btn-primary btn-sm" href="{wa_link()}" target="_blank" rel="noopener">Book now</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="logo" href="{root}index.html"><img class="logo-mark" src="{root}assets/img/logo.svg" alt="" width="38" height="38"><span>Al-Trekking <b>Rinjani</b></span></a>
      <p>{escape(AGENCY['tagline'])}</p>
      <p>{escape(AGENCY['address'])}</p>
    </div>
    <div>
      <h4>Treks</h4>
      {nav_treks}
    </div>
    <div>
      <h4>Contact</h4>
      <a href="{wa_link()}" target="_blank" rel="noopener">WhatsApp +{AGENCY['whatsapp']}</a>
      <a href="mailto:{AGENCY['email']}">{AGENCY['email']}</a>
      <a href="{root}contact.html">Enquiry form</a>
    </div>
    <div>
      <h4>Follow us</h4>
      <a href="{AGENCY['instagram']}" target="_blank" rel="noopener">Instagram</a>
      <a href="{AGENCY['facebook']}" target="_blank" rel="noopener">Facebook</a>
      <a href="{AGENCY['tripadvisor']}" target="_blank" rel="noopener">Tripadvisor</a>
    </div>
  </div>
  <div class="container copyright">© <span data-year></span> {AGENCY['name']}. All rights reserved.</div>
</footer>
<a class="wa-float" href="{wa_link()}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3Z"/></svg>
</a>
<script>window.AGENCY_WA = "{AGENCY['whatsapp']}";</script>
<script src="{root}assets/js/main.js"></script>
</body>
</html>"""


def trek_card(t, root=""):
    return f"""
<article class="card">
  <a href="{root}treks/{t['slug']}.html" class="card-img" style="--img:url('{root}{t['image']}')">
    <span class="tag">{t['duration']}</span>
  </a>
  <div class="card-body">
    <h3><a href="{root}treks/{t['slug']}.html">{escape(t['title'])}</a></h3>
    <p>{escape(t['short'])}</p>
    <ul class="meta">
      <li>⛰ {t['max_alt']}</li><li>↔ {t['distance']}</li><li>◆ {t['grade']}</li>
    </ul>
    <div class="card-foot">
      <span class="price"><small>From</small> {escape(t['price_from'])}</span>
      <a class="btn btn-outline btn-sm" href="{root}treks/{t['slug']}.html">View trek</a>
    </div>
  </div>
</article>"""


def build_home():
    why = "".join(
        f'<div class="why-item"><h3>{escape(h)}</h3><p>{escape(p)}</p></div>' for h, p in WHY_US
    )
    cards = "".join(trek_card(t) for t in TREKS)
    body = f"""
<section class="hero" style="--img:url('assets/img/hero.jpg')">
  <div class="container hero-inner">
    <p class="eyebrow">Lombok · Indonesia</p>
    <h1>Mount Rinjani<br><span>3,726 m above Lombok</span></h1>
    <p class="lead">Summit treks, crater lake camps and hot springs, guided by the people who grew up on the mountain.</p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="#treks">Explore treks</a>
      <a class="btn btn-ghost" href="{wa_link()}" target="_blank" rel="noopener">Book your trip</a>
    </div>
  </div>
</section>

<section class="why" id="about">
  <div class="container why-grid">{why}</div>
</section>

<section class="intro container">
  <div>
    <p class="eyebrow">About Al-Trekking Rinjani</p>
    <h2>Trek Indonesia's second-highest volcano with a local team</h2>
    <p>Al-Trekking Rinjani is a family-run trekking agency based in the villages at the foot of Mount Rinjani.
    Our guides and porters are licensed by Rinjani National Park and know every switchback, camp and hidden
    spring on the mountain. We keep groups small, cook fresh meals on the trail and carry out every piece of rubbish we bring in.</p>
  </div>
  <div class="stats">
    <div><b>3,726 m</b><span>Summit height</span></div>
    <div><b>4</b><span>Signature routes</span></div>
    <div><b>100%</b><span>Local guides</span></div>
  </div>
</section>

<section class="treks" id="treks">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Our packages</p>
      <h2>Choose your Rinjani trek</h2>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="custom" style="--img:url('assets/img/custom.jpg')">
  <div class="container custom-inner">
    <p class="eyebrow">Your mountain, your way</p>
    <h2>Need something different?</h2>
    <p>Private groups, extra nights at the lake, waterfall tours, island transport or a stay in the village:
    tell us what you have in mind and we will build the trip around you.</p>
    <a class="btn btn-primary" href="{wa_link('Hello Al-Trekking Rinjani, I would like a custom trip.')}" target="_blank" rel="noopener">Plan a custom trip</a>
  </div>
</section>

<section class="practical container">
  <div>
    <h2>What's included</h2>
    {ul(INCLUDED, "check")}
  </div>
  <div>
    <h2>What to bring</h2>
    {ul(PACKING, "dot")}
  </div>
</section>

<section class="faq container" id="faq">
  <div class="section-head">
    <p class="eyebrow">Good to know</p>
    <h2>Frequently asked questions</h2>
  </div>
  {faq_html()}
</section>

<section class="contact-band" id="contact">
  <div class="container contact-grid">
    <div>
      <p class="eyebrow">Ready to go?</p>
      <h2>Send us your dates</h2>
      <p>We usually reply within a few hours. Tell us when you are in Lombok and how many people are coming.</p>
    </div>
    {enquiry_form()}
  </div>
</section>"""
    return page(f"{AGENCY['name']} | Mount Rinjani Trekking Packages", body)


def build_trek(t):
    root = "../"
    itin = "".join(
        f'<div class="day"><h3>{escape(h)}</h3><p>{escape(p)}</p></div>' for h, p in t["itinerary"]
    )
    overview = "".join(f"<p>{escape(p)}</p>" for p in t["overview"])
    others = "".join(trek_card(o, root) for o in TREKS if o is not t)
    body = f"""
<section class="hero hero-sm" style="--img:url('{root}{t['image']}')">
  <div class="container hero-inner">
    <p class="eyebrow">Mount Rinjani · {t['duration']}</p>
    <h1>{escape(t['title'])}</h1>
    <p class="lead">{escape(t['short'])}</p>
  </div>
</section>

<div class="facts container">
  <div><span>Duration</span><b>{t['duration']}</b></div>
  <div><span>Grade</span><b>{t['grade']}</b></div>
  <div><span>Distance</span><b>{t['distance']}</b></div>
  <div><span>Max altitude</span><b>{t['max_alt']}</b></div>
  <div><span>Start</span><b>{escape(t['start'])}</b></div>
</div>

<nav class="tabs container">
  <a href="#overview">Overview</a><a href="#highlights">Highlights</a><a href="#included">Included</a>
  <a href="#itinerary">Itinerary</a><a href="#faq">FAQ</a><a href="#book">Book</a>
</nav>

<div class="container trek-layout">
  <div class="trek-main">
    <section id="overview"><h2>Overview</h2>{overview}</section>
    <section id="highlights"><h2>Highlights</h2>{ul(t['highlights'], "check")}</section>
    <section id="included" class="two-col">
      <div><h2>Included</h2>{ul(INCLUDED, "check")}</div>
      <div><h2>Not included</h2>{ul(EXCLUDED, "cross")}</div>
    </section>
    <section id="itinerary"><h2>Itinerary</h2><div class="timeline">{itin}</div></section>
    <section id="faq" class="faq"><h2>FAQ</h2>{faq_html()}</section>
    <section id="book"><h2>Enquire about this trek</h2>{enquiry_form(t['title'])}</section>
  </div>
  <aside class="trek-aside">
    <div class="price-box">
      <span>Price from</span>
      <b>{escape(t['price_from'])}</b>
      <small>per person · all-inclusive or trek-only options</small>
      <a class="btn btn-primary" href="{wa_link(f'Hello Al-Trekking Rinjani, I am interested in the {t["title"]}.')}" target="_blank" rel="noopener">Book on WhatsApp</a>
      <a class="btn btn-outline" href="#book">Send enquiry</a>
    </div>
  </aside>
</div>

<section class="treks">
  <div class="container">
    <div class="section-head"><h2>Other treks</h2></div>
    <div class="cards">{others}</div>
  </div>
</section>"""
    return page(f"{t['title']} | {AGENCY['name']}", body, root, t["short"])


def build_contact():
    body = f"""
<section class="hero hero-sm" style="--img:url('assets/img/hero.jpg')">
  <div class="container hero-inner"><h1>Contact us</h1>
  <p class="lead">Questions, custom trips or bookings: we are happy to help.</p></div>
</section>
<section class="container contact-grid page-pad">
  <div class="contact-info">
    <h2>Talk to us directly</h2>
    <p><b>WhatsApp</b><br><a href="{wa_link()}" target="_blank" rel="noopener">+{AGENCY['whatsapp']}</a></p>
    <p><b>Email</b><br><a href="mailto:{AGENCY['email']}">{AGENCY['email']}</a></p>
    <p><b>Base</b><br>{escape(AGENCY['address'])}</p>
  </div>
  {enquiry_form()}
</section>"""
    return page(f"Contact | {AGENCY['name']}", body)


def main():
    (OUT / "treks").mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(build_home(), encoding="utf-8")
    (OUT / "contact.html").write_text(build_contact(), encoding="utf-8")
    for t in TREKS:
        (OUT / "treks" / f"{t['slug']}.html").write_text(build_trek(t), encoding="utf-8")
    print(f"Built {2 + len(TREKS)} pages into {OUT}")


def lan_ip():
    # Connecting a UDP socket sends nothing; it only picks the outgoing interface.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
        except OSError:
            return "127.0.0.1"


def serve(port=8000):
    handler = partial(SimpleHTTPRequestHandler, directory=str(OUT))
    try:
        httpd = ThreadingHTTPServer(("0.0.0.0", port), handler)
    except OSError as e:
        sys.exit(f"Cannot use port {port} ({e.strerror}). Try another: python3 build.py --serve 8005")
    with httpd:
        print(f"Serving site/ on:\n  http://localhost:{port}\n  http://{lan_ip()}:{port}  (other devices on your network)")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
    if "--serve" in sys.argv:
        args = sys.argv[sys.argv.index("--serve") + 1:]
        serve(int(args[0]) if args else 8000)
