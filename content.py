"""All editable site content for Al-Trekking Rinjani lives here.

Edit this file, then run `python3 build.py` to regenerate the site/ folder.
"""

AGENCY = {
    "name": "Al-Trekking Rinjani",
    "tagline": "Local guides. Honest prices. Unforgettable summits.",
    # TODO: replace with your real details
    "whatsapp": "33695817057",  # international format, digits only (country code, no +, no leading 0, no spaces)
    "email": "hello@al-trekkingrinjani.com",
    "address": "Senaru, North Lombok, Indonesia",
    "instagram": "https://instagram.com/",
    "facebook": "https://facebook.com/",
    "tripadvisor": "https://tripadvisor.com/",
}

WHY_US = [
    ("Best Value", "We are a local operator, not a reseller. No middlemen means "
     "fair prices for you and fair wages for our guides and porters."),
    ("Personal Care", "Small groups that move at your pace. Your guide knows your "
     "name, your diet and how you like your coffee at 5,000 steps."),
    ("Local Roots", "Our team was born at the foot of Rinjani. Every trek supports "
     "families in Senaru and Sembalun villages."),
]

INCLUDED = [
    "Hotel pickup and drop-off in Lombok (Senggigi, Kuta, airport, Bangsal)",
    "Licensed English-speaking mountain guide",
    "Porters to carry tents, food and cooking gear",
    "Tents, sleeping bags, mattresses and toilet tent",
    "All meals on the mountain (vegetarian, vegan and gluten-free on request)",
    "Drinking water, tea, coffee and snacks",
    "Rinjani National Park entrance fees",
    "Luggage storage while you trek",
]

EXCLUDED = [
    "Tips for guides and porters",
    "Personal trekking gear (day pack, warm jacket, gloves, headlamp)",
    "Travel insurance",
    "Flights and accommodation outside the program",
]

PACKING = [
    "Sturdy hiking shoes with good grip",
    "Warm jacket, beanie and gloves (summit is near 0°C)",
    "Headlamp with spare batteries",
    "Day pack (20–30 L) and rain cover",
    "Sunscreen, sunglasses and a hat",
    "Personal medication and blister plasters",
    "Swimwear for the hot springs (3–4 day treks)",
    "Cash for tips and drinks in the villages",
]

FAQ = [
    ("How high is Mount Rinjani?",
     "Mount Rinjani rises to 3,726 m, making it the second-highest volcano in "
     "Indonesia and the highest point on Lombok."),
    ("When is the trekking season?",
     "The national park is usually open from April to December. It closes during "
     "the peak of the rainy season (roughly January to March) for safety and "
     "environmental recovery."),
    ("How fit do I need to be?",
     "The crater rim trek suits anyone with regular exercise habits. Summit treks "
     "are demanding: expect long, steep sections on loose volcanic sand. If you can "
     "hike 6–8 hours on consecutive days, you are ready."),
    ("Can I customise my trek?",
     "Yes. Every itinerary can be adjusted: private groups, extra nights at the "
     "lake, transport around Lombok or a pre-trek stay in the village. Message us "
     "and we will build it with you."),
    ("How do I book?",
     "Send us a message on WhatsApp or through the enquiry form with your dates and "
     "group size. We confirm availability, then a small deposit secures your spot; "
     "the balance is paid on arrival."),
]

# Each trek generates its own page at site/treks/<slug>.html
TREKS = [
    {
        "slug": "rinjani-2-days-summit-trek",
        "title": "2 Days Summit Trek",
        "short": "The fastest way to stand on top of Lombok. For fit hikers short on time.",
        "duration": "2D / 1N",
        "days": 2,
        "grade": "Challenging",
        "distance": "26 km",
        "max_alt": "3,726 m",
        "start": "Sembalun (1,156 m)",
        "price_from": "Ask us",  # e.g. "USD 180"
        "image": "assets/img/summit.jpg",
        "overview": [
            "A short, intense ascent from the Sembalun side straight to the summit of "
            "Mount Rinjani. You climb through savanna to the crater rim, camp above "
            "the clouds, and set off in the dark to watch sunrise from 3,726 m.",
            "From the top you can see the whole of Lombok, the turquoise Segara Anak "
            "lake inside the caldera, the smoking Gunung Barujari cone, and on clear "
            "mornings Mount Agung on Bali.",
        ],
        "highlights": [
            "Sunrise from the summit of Rinjani at 3,726 m",
            "Sunset over the caldera from Sembalun crater rim camp",
            "Rolling savanna hills of Sembalun",
            "Views of Segara Anak lake and Barujari volcano",
            "Mount Agung on the horizon on clear days",
        ],
        "itinerary": [
            ("Day 0 — Arrival", "Pickup from your hotel, airport or harbour and transfer "
             "to Sembalun village. Briefing with your guide (optional village stay)."),
            ("Day 1 — Sembalun → Crater Rim (2,639 m)", "Start from the national park gate "
             "and cross the savanna via Pos 1, Pos 2 and Pos 3, where we stop for lunch. "
             "The 'seven hills' climb brings you to the Sembalun crater rim for sunset "
             "and dinner. About 7–8 hours."),
            ("Day 2 — Summit (3,726 m) → Sembalun", "Wake at 02:00 for the 3–4 hour push to "
             "the summit in time for sunrise. Descend to camp for breakfast, then walk "
             "back down to Sembalun. Transfer to your hotel. About 10–11 hours."),
        ],
    },
    {
        "slug": "rinjani-2-days-crater-rim-trek",
        "title": "2 Days Crater Rim Trek",
        "short": "Jungle trails and caldera views without the summit push. Loved by photographers.",
        "duration": "2D / 1N",
        "days": 2,
        "grade": "Moderate",
        "distance": "16 km",
        "max_alt": "2,641 m",
        "start": "Senaru (601 m)",
        "price_from": "Ask us",
        "image": "assets/img/crater-rim.jpg",
        "overview": [
            "Climb from the village of Senaru through dense tropical rainforest, home "
            "to long-tailed macaques and hornbills, up to the Senaru crater rim.",
            "Camp right on the edge of the caldera with a front-row view of Segara Anak "
            "lake and the active Barujari cone. Ideal if you want the drama of Rinjani "
            "at a more relaxed pace.",
        ],
        "highlights": [
            "Rainforest trail full of wildlife",
            "Sunset and sunrise over the caldera",
            "Camp on the rim above the clouds",
            "Optional visit to Sendang Gile and Tiu Kelep waterfalls",
        ],
        "itinerary": [
            ("Day 0 — Arrival", "Pickup and transfer to Senaru. Optional waterfall visit "
             "and overnight in the village."),
            ("Day 1 — Senaru → Crater Rim (2,641 m)", "From the park gate, climb through "
             "the forest via Pos 1, Pos 2 (lunch) and Pos 3, then out above the tree line "
             "to the rim. Sunset, dinner and camp. About 6–7 hours."),
            ("Day 2 — Crater Rim → Senaru", "Sunrise over the lake, breakfast, then descend "
             "the same trail to Senaru. Lunch in the village and transfer to your hotel. "
             "About 4–5 hours."),
        ],
    },
    {
        "slug": "rinjani-3-days-summit-and-lake-trek",
        "title": "3 Days Summit & Lake Trek",
        "short": "Summit, crater lake and hot springs. The classic Rinjani crossing.",
        "duration": "3D / 2N",
        "days": 3,
        "grade": "Challenging",
        "distance": "32 km",
        "max_alt": "3,726 m",
        "start": "Sembalun → Senaru",
        "price_from": "Ask us",
        "image": "assets/img/lake.jpg",
        "overview": [
            "The full traverse of Rinjani. Start in Sembalun, summit at sunrise, drop "
            "into the caldera to soak in natural hot springs beside Segara Anak lake, "
            "then climb out to the Senaru rim and descend through the rainforest.",
            "This route shows you every face of the mountain: savanna, volcanic ridge, "
            "crater lake and jungle.",
        ],
        "highlights": [
            "Summit sunrise at 3,726 m",
            "Swim or fish in Segara Anak crater lake",
            "Natural hot springs inside the caldera",
            "Both crater rims: Sembalun and Senaru",
            "Descent through tropical rainforest",
        ],
        "itinerary": [
            ("Day 0 — Arrival", "Pickup and transfer to Sembalun. Briefing and optional village stay."),
            ("Day 1 — Sembalun → Sembalun Crater Rim", "Cross the savanna via Pos 1–3 and "
             "climb to the rim camp for sunset. About 7–8 hours."),
            ("Day 2 — Summit → Lake → Senaru Crater Rim", "02:00 summit push for sunrise. "
             "Back to camp for breakfast, descend to Segara Anak lake for lunch and the "
             "hot springs, then climb to the Senaru rim for the night. About 11–12 hours."),
            ("Day 3 — Senaru Crater Rim → Senaru", "Sunrise, breakfast and a forest descent "
             "to Senaru. Transfer to your hotel. About 5 hours."),
        ],
    },
    {
        "slug": "rinjani-4-days-full-experience",
        "title": "4 Days Full Experience",
        "short": "The complete traverse with an extra night at the lake. No rushing.",
        "duration": "4D / 3N",
        "days": 4,
        "grade": "Challenging",
        "distance": "32 km",
        "max_alt": "3,726 m",
        "start": "Sembalun → Senaru",
        "price_from": "Ask us",
        "image": "assets/img/full.jpg",
        "overview": [
            "Everything from the 3-day crossing, at a gentler pace. The extra night "
            "camping beside Segara Anak lake gives you time to rest your legs in the "
            "hot springs, explore the caves and watch the stars from inside a volcano.",
        ],
        "highlights": [
            "Summit sunrise at 3,726 m",
            "A full night camping on the shore of Segara Anak",
            "Unhurried time at the hot springs and caves",
            "Both crater rims and the rainforest descent",
        ],
        "itinerary": [
            ("Day 0 — Arrival", "Pickup and transfer to Sembalun. Briefing and optional village stay."),
            ("Day 1 — Sembalun → Sembalun Crater Rim", "Savanna crossing and climb to the rim. About 7–8 hours."),
            ("Day 2 — Summit → Segara Anak Lake", "Summit at sunrise, breakfast at camp, then "
             "descend into the caldera. Afternoon at the hot springs, camp by the lake. "
             "About 9–10 hours."),
            ("Day 3 — Lake → Senaru Crater Rim", "Slow morning at the lake, then climb to the "
             "Senaru rim for sunset. About 3–4 hours."),
            ("Day 4 — Senaru Crater Rim → Senaru", "Sunrise, breakfast and the forest descent "
             "to Senaru. Transfer to your hotel. About 5 hours."),
        ],
    },
]
