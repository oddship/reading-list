+++
title = "Rumik OSS 1 releases open weights for expressive Indic text-to-speech"
slug = "2026-09-08-rumik-oss-1-indic-voice-model"
date = 2026-09-08T19:46:00+05:30
[taxonomies]
tags = ["ai-infra", "llm-research"]
[extra]
source_url = "https://rumik.ai/research/rumik-oss"
source_type = "x-post"
newsletter_candidate = true
why_it_matters = "Open Indic voice models are moving toward real model cards, weights, eval protocols, and benchmark artifacts, not only product demos."
saved_link = "https://x.com/lets_dig_deeper/status/2097231291079069725"
related_urls = ["https://huggingface.co/rumik-ai/rumik-oss-1", "https://huggingface.co/rumik-ai/rumik-oss-1-base", "https://huggingface.co/spaces/rumik-ai/rumik-oss-1", "https://github.com/ira-rumik/IndicEmo", "https://github.com/ira-rumik/nova-bench"]
retrieval_note = "Tweet extracted via FXTwitter; Rumik research post and Hugging Face model card/API read directly; attached X launch video sampled for visible release and benchmark slides."
+++

**Logged at IST:** 2026-09-08 19:46 IST

**What it is:** Rumik AI's launch of rumik-oss-1, a 3B multilingual text-to-speech model with open weights, focused on expressive Indic and code-switched speech.

**Gist:** Rumik describes rumik-oss-1 as a 24 kHz text-to-speech model trained on fewer than 70,000 hours of speech. It supports 22 languages, four released voices, native-script and code-switched synthesis, description-conditioned delivery, and inline vocalization tags such as `<laugh>`, `<chuckle>`, and `<sigh>`.

The model card says rumik-oss-1 extends tiny aya fire with discrete speech tokens from the Mimi codec. Text conditioning and audio generation share a single autoregressive sequence; the model predicts eight codec tokens per audio frame and the frozen Mimi decoder reconstructs waveform audio. Speaker identity is separate from delivery controls: prompts can combine tone, accent, and pace while choosing one of the released voices.

**Benchmarks:** Rumik introduces IndicEmo for expressive delivery in code-switched speech, with prompts spanning English, Hindi, Telugu, Tamil, Kannada, Bengali, and Punjabi. It reports rumik-oss-1 at 2.92/5 overall and 3.03/5 on emotion categories. NoVA evaluates inline laughter, chuckle, and sigh placement; Rumik reports a 0.884 rendering score. The release also reports WER/CER across selected Indic languages using ASR-based transcription comparisons.

**Caveats:** This is not an unrestricted commercial release. The Hugging Face card lists CC-BY-NC-4.0, inherited from the tiny-aya-derived weights, with an acceptable-use addendum; commercial products and paid synthesis services require separate permission. The technical report, training recipe, and training code are described as forthcoming, and the model card calls out limitations around long-form synthesis and vocalization precision.

**Newsletter angle:** Interesting because it makes an Indic voice-model release inspectable: weights, demos, samples, benchmarks, eval repos, and a fairly detailed training write-up are all public. The caveat is that "open source" here really means research/non-commercial open weights today, with the most important reproducibility artifacts still promised rather than released.

{{ tweet(id="2097231291079069725", url="https://x.com/lets_dig_deeper/status/2097231291079069725") }}
