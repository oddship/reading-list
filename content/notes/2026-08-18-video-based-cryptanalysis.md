+++
title = "Video-Based Cryptanalysis"
slug = "2026-08-18-video-based-cryptanalysis"
date = 2026-08-18T14:11:00+05:30
[taxonomies]
tags = ["security", "systems"]
[extra]
source_url = "https://www.nassiben.com/video-based-crypta"
source_type = "research"
newsletter_candidate = true
why_it_matters = "A sharp reminder that physical indicators and observability surfaces can become side channels when they correlate with sensitive computation."
saved_link = "https://x.com/i/status/2089470651505512727"
related_url = "https://x.com/DoingFedTime/status/2089470651505512727"
related_urls = ["https://eprint.iacr.org/2023/923/"]
retrieval_note = "X post extracted via FXTwitter. The linked Ben Nassi research page and IACR ePrint abstract were read directly."
+++
**Logged at IST:** 2026-08-18 14:11 IST

**What it is:** Ben Nassi, Etay Iluz, Ofek Vayner, Or Cohen, Dudi Nassi, Boris Zadov, and Yuval Elovici's 2023 work on recovering cryptographic keys from video footage of a device's power LED.

**Gist:** The paper's useful idea is that a status LED can carry more information than it appears to. Cryptographic work changes a device's power consumption. In many circuits, the power LED's brightness or color shifts with that consumption, so video of the LED can become a side-channel trace.

The researchers show how to turn ordinary video into a higher-rate signal by filling the frame with the LED and exploiting a camera's rolling shutter. In their demonstrations, they recovered a 256-bit ECDSA key from a smart-card reader filmed by a hijacked internet-connected security camera 16 meters away, and a 378-bit SIKE key from a Samsung Galaxy S8 indirectly, through the power LED on connected Logitech USB speakers.

The important caveat is that the LED is the leak path, not the root cryptographic bug. Their FAQ says the demonstrated attacks rely on vulnerable cryptographic libraries, while the LED provides a visual way to exploit the underlying timing side channel.

**Newsletter angle:** Good security/systems example for the theme that operational signals, LEDs, logs, metrics, timing, can become attack surfaces when they correlate with secrets.

## Embedded source

{{< tweet id="2089470651505512727" url="https://x.com/i/status/2089470651505512727" >}}
