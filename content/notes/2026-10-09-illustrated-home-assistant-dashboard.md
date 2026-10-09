+++
title = "A hand-drawn house becomes a Home Assistant dashboard"
slug = "2026-10-09-illustrated-home-assistant-dashboard"
date = 2026-10-09T19:42:00+05:30
[taxonomies]
tags = ["other"]
[extra]
source_url = "https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my"
source_type = "article"
newsletter_candidate = true
why_it_matters = "An attractive, spatial interface can make smart-home controls usable for the whole household; technically, a layered illustration plus Home Assistant's built-in picture-elements card keeps the implementation simple."
saved_link = "https://antonfrolov.substack.com/p/i-hired-an-illustrator-to-draw-my"
source_title = "I hired an illustrator to draw my house. Now it's my Home Assistant dashboard."
+++
**Logged at IST:** 2026-10-09 19:42 IST

**What it is:** Anton Frolov's account of commissioning an environment artist to draw his house and turning the artwork into an interactive Home Assistant dashboard.

**Gist:** The illustrated floor plan is the interface: Home Assistant's stock `picture-elements` card places device artwork and state labels over a background image. Transparent device layers share one full-size canvas so they align without manual positioning; each can switch between still “off” art and animated WebP “on” art. Conditional elements and a helper toggle day/night versions, with an automation switching at sunrise and sunset. The article also covers the detailed art brief: room photos, floor plans, style references, common canvas dimensions, individual device layers, transparent PNGs, and day/night states. The result gives the family a visual way to control items such as garden lights, air conditioning, and sprinklers.

**Why it matters:** The main effort is not custom dashboard code but commissioning and specifying the right artwork. A familiar, inviting interface can make a technically capable smart home practical for people who would otherwise avoid its app.

**Implementation note:** Keep device layers on a shared canvas and request the animation format directly; the author found aligning separately cropped assets tedious and converted sprite sheets to animated WebP afterward.
