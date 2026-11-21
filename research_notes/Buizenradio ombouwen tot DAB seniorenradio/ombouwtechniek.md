# Ombouwtechniek: converting a vintage tube radio to a low-voltage modern radio while reusing original keys, volume pot, switch, dial lamp and speaker

> **Read this first — reliability of these notes**
> - **No page could be fetched in this session.** Every WebFetch failed with a DNS/allow-list error (hackaday.com, hackaday.io, designing-electronics.com, vintage-radio.com, radio-bastler.de, circuitsonline.net, media.elv.com). All "Cited Findings" below therefore rest on **web-search result summaries/snippets only**, not on a full read of the page. Wording may be out of context; verify before quoting. These hosts must be allowed in the session's network settings to do a proper read.
> - Each section separates **Cited Findings** (a URL exists, snippet-level) from **Inferences** (my own engineering reasoning/arithmetic, *not* sourced, marked "ESTIMATE" or "UNSOURCED") and **Gaps**.
> - **Prices**: only a handful of prices were actually seen in search results (Visaton FR 10, eBay kit, Catawiki). All other module prices could not be verified and are listed under Gaps.

---

## 1. Original push-button ("piano key" / druktoetsen / Tastensatz) band switches: construction, tapping contacts for a microcontroller, documented projects

### Takeaway
No documented project was found that does exactly "original interlocked tube-radio piano keys → microcontroller GPIO → station presets"; the closest hits reuse original front buttons through an I2C port expander or reassign existing channel buttons to web stations. Forum practice on the key assemblies themselves is all about mechanical/contact trouble: sticking sliders, oxide on contact springs, and damage from oily contact sprays.

### Cited Findings
- Search for Dutch ("buizenradio ombouwen internetradio ESP32 druktoetsen voorkeuzezenders") and German ("Röhrenradio Umbau Internetradio ESP32 Tastensatz Originaltasten") returned **no** tube-radio project using the original key bank as presets; only generic ESP32 radio projects — [Edzelf/ESP32-radio](https://github.com/Edzelf/ESP32-radio), [AZ-Delivery internet radio with ESP32 + MAX98357A](https://az-delivery.de/en/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/internetradio-mit-esp32-und-max-98357a)
- Ed Smallenburg's ESP32-radio lets buttons/touch inputs be bound to commands such as `uppreset=1` on a GPIO (i.e. a GPIO-to-preset mapping already exists in common firmware) — [Edzelf/ESP32-radio](https://github.com/Edzelf/ESP32-radio)
- A hi-fi/receiver conversion based on that firmware handles the **original front-panel buttons and LEDs through an I2C extender module**; "most of the original front buttons are still available and used for changing modes" — [yellobyte/ESP32-Webradio-PlusDLNA](https://www.github.com/yellobyte/ESP32-Webradio-PlusDLNA)
- One retrofit (search snippet; exact source among the hits is uncertain, most likely the Hackster/Hackaday 1970s-radio projects) states the set's "existing 10 channel buttons can continue to serve their original purpose, only this time with web radio stations assigned" — [Hackster: RetroRadio WiFi Pilot](https://www.hackster.io/pnjorge/retroradio-wifi-pilot-05b075); [Hackaday: Simple Internet Radio Transplant](https://hackaday.com/2022/09/22/simple-internet-radio-transplant)
- An ESP32 tube-radio build wired the **original on/off switch to a digital input and the original volume pot to an analog input**; the ESP32 stays in standby and acts as Bluetooth speaker — [designing-electronics.com: An ESP32 powered tube radio](https://www.designing-electronics.com/an-esp32-powered-tube-radio)
- A Hackaday article dated 7 Oct 2026, "Keep That Old Radio Alive With An ESP32", exists but could not be read (title only) — [Hackaday](https://hackaday.com/2026/10/07/keep-that-old-radio-alive-with-an-esp32/)
- An older Hackaday.io project (Wilcox-Gay A46 internet radio) reads tuning, band and volume **potentiometers through an ADC**, mapping knob angle to voltage — [hackaday.io/project/3030](https://hackaday.io/project/3030-wilcox-gay-a46-internet-radio)
- Mechanical state of old key sets: an Arduino-forum user reports original preset buttons unreliable — "some won't move, others don't return" — with contact cleaner suggested — [Arduino forum](https://forum.arduino.cc/t/play-mp3-files-on-my-vintage-radio/697056)
- Restoration practice (German forums): do **not** spray oily contact spray on the wave-band switch ("Kein öliges Kontaktspray ... auf den Wellenschalter") — [radiomuseum.org forum: Kontaktspray verseucht](https://www.radiomuseum.org/forum/kontaktspray_verseucht.html)
- Telefunken Gavotte 201: slider contacts and the contact tongues in the switch housing were cleaned with a soaked cotton swab — [radiomuseum.org forum](https://www.radiomuseum.org/forum/telefunken_201_gavotte.html)
- Grundig 6099: a stuck slider required removal and full disassembly of the complete key assembly ("das komplette Tastenaggregat ausgebaut") — [radiomuseum.org forum](https://www.radiomuseum.org/forum/reparatur_6099.html)
- Oxide on contact springs is removed with a stiff brush plus contact spray — [radiomuseum.org forum: ITT Kontaktprobleme](https://www.radiomuseum.org/forum/itt_kontakprobleme.html)
- Kontakt Chemie Tuner 600 is sold as a cleaner for switches and potentiometers — [RS Online](https://de.rs-online.com/web/p/elektronik-reiniger/1316183)
- A thread exists specifically on washing an oil-soaked tube-radio Tastensatz — [mikrocontroller.net topic 571986](https://www.mikrocontroller.net/topic/571986)
- ELV's restoration series (part 6, Bluetooth add-on) notes that in its set the volume pot is switched through when the **LW and KW keys are pressed simultaneously** — i.e. key combinations are an established trick to create an extra "input" position without modifying the front — [ELV Radio-Restaurierung Teil 6 (PDF)](https://media.elv.com/file/252591_radio_restaurierung_teil_6.pdf)
- General wetting-current rule (relevant to reading old silver contacts at logic level, see section 2): contacts need a minimum current to break through surface film; below that the switch may read "open" when pressed — [Wikipedia: Wetting current](https://en.wikipedia.org/wiki/Wetting_current)

### Inferences (UNSOURCED engineering reasoning — verify on the bench)
- Construction (general knowledge, not confirmed by a fetched source): the key bank of 1950s–60s Philips/Grundig/Telefunken/Nordmende sets is a row of parallel **multi-pole slide switches**, one slider per key, each carrying several changeover contact sets, with a common spring-loaded **latch bar** that holds the pressed key down and releases the previously pressed one (mutual release). Often one key ("Aus/Uit") is non-latching or operates the mains switch, and tone keys (Bass/Sprache/Jazz) may be independent push-push sliders.
- Because the bank is interlocked, it is a **state** selector (exactly one key down), not momentary buttons. Firmware should read *level*, not edges: "preset = index of the key that is down", sampled every 10–20 ms, accepted after ~50–100 ms of stability, and it must tolerate the transient states "no key down" and "two keys down" during travel. Bonus: the selected station survives power-off mechanically, which suits a seniors' radio.
- Simplest tap: per key choose **one** make-contact pair, **desolder every original wire/coil from the contacts used** (the bank is otherwise still connected to coils and the old chassis), tie one side of all to GND, other side to a GPIO each. For 5–7 keys this costs 5–7 GPIOs; alternatives are an MCP23017/PCF8574 I2C expander (as in the yellobyte project) or a **resistor ladder into one ADC pin** (one pin, but more sensitive to contact resistance).
- Contact resistance: use **external pull-ups of ~1–4.7 kΩ to 3.3 V** (≈0.7–3 mA) rather than the ESP32's weak internal pull-ups (tens of kΩ → ~70 µA), plus 100 nF from pin to GND so each closure gives a small cleaning discharge and RF pickup is suppressed. With digital reading, even several hundred ohms of contact resistance still reads as a clean "low"; a resistor ladder does not have that margin.
- Clean with a non-oily, residue-free cleaner (see cited warning) and exercise the keys; lubricate only the mechanical latch, not the contacts.
- Standardisable: a small "key adapter" header (N inputs, pull-ups, RC, ESD series resistors ~1 kΩ) on the kit PCB; the radio-specific part is only *which* contacts to free — worth documenting once per model.

### Gaps
- No verified source describing the internal construction/latch mechanism of specific Philips or Grundig key banks (service manuals not reachable).
- No documented tube-radio project that reuses the interlocked keys as presets was found; the idea appears technically routine but is not evidenced. Hackaday 2026/10/07 article, radio-bastler.de threads [tid=9274](https://www.radio-bastler.de/forum/showthread.php?tid=9274) and [tid=8669](https://www.radio-bastler.de/forum/showthread.php?tid=8669) (DAB+/internet-radio conversions of tube sets) are the most promising unread sources.
- No measured contact-resistance figures for aged key contacts.

---

## 2. Reading the old 500 k–1 M log volume pot (loudness tap, integrated mains switch) with an MCU ADC; is the mains switch reliable at low voltage?

### Takeaway
Reading a high-value pot with an ESP32 ADC is workable if a ~100 nF capacitor sits at the ADC pin (charge reservoir for the sampling cap) and software averages; ESP32 ADC is noisy and non-linear near the rails. The mains-rated switch is at risk in "dry circuit" logic-level use — give it real current or a discharge capacitor.

### Cited Findings
- Tube-radio precedent: original volume pot to an ESP32 analog input, original on/off switch to a digital input — [designing-electronics.com](https://www.designing-electronics.com/an-esp32-powered-tube-radio)
- High source resistance problem: if divider resistance is too high the ADC's internal sample capacitor does not charge in time; a worked ESP32-S3 example with a **1 MΩ divider** recommends **0.1 µF between ADC pin and ground** as a local charge reservoir — [teachmemicro: ESP32-S3 analog input leakage current](https://www.teachmemicro.com/esp32-s3-analog-input-leakage-current/)
- Espressif docs: a 0.1 µF capacitor on the ADC pad reduces noise, and multisampling further mitigates it; with 11 dB attenuation the recommended measurement range is about **150–2450 mV** (ESP32) — [ESP-IDF ADC docs](https://docs.espressif.com/projects/esp-idf/en/v4.4.6/esp32/api-reference/peripherals/adc.html); [older release](https://docs.espressif.com/projects/esp-idf/en/release-v3.1/api-reference/peripherals/adc.html)
- Some ADC2 pins are strapping pins (GPIO 0, 2, 15) and cannot be used freely — [ESP-IDF ADC docs](https://docs.espressif.com/projects/esp-idf/en/release-v3.1/api-reference/peripherals/adc.html)
- Averaging reduces random noise but does not fix ESP32 ADC non-linearity; a 100 nF ceramic at the pin filters HF noise — [SunFounder ESP32 ADC guide](https://www.sunfounder.com/blogs/news/esp32-adc-calibration-noise-reduction-improve-analog-reading-accuracy); [Waveshare analog input tutorial](https://docs.waveshare.com/ESP32-Arduino-Tutorials/Analog-Input)
- Wetting current: minimum current needed to break through contact surface film; without it a switch may stay electrically open due to oxidation. Ordinary silver/copper-alloy power contacts are not reliable in such low-current ("dry circuit") service; gold-plated contacts are the standard remedy — [Wikipedia: Wetting current](https://en.wikipedia.org/wiki/Wetting_current); [All About Circuits: switch contact design](https://www.allaboutcircuits.com/textbook/digital/chpt-4/switch-contact-design/); [Omron: micro loads](https://components.omron.com/web/en/microloads)
- A small capacitor across the contacts can supply a current pulse on closure to help wetting, provided inrush stays within the switch rating — [DigiKey forum: Wetting current](https://forum.digikey.com/t/wetting-current-designing-reliable-industrial-inputs/71789)
- Practitioner rule of thumb (forum-level, not universal): 10–20 mA is a typical target in low-voltage circuits — [diyAudio: switch contact wetting](https://www.diyaudio.com/community/threads/switch-contact-wetting.386269/)

### Inferences (UNSOURCED / arithmetic)
- Wiring: pot track end → 3.3 V (same rail as ADC reference, so supply variation cancels), other end → GND, wiper → ADC1 pin with 100 nF to GND; leave the **loudness tap unconnected** (remove the old RC network on it). ESTIMATE: 1 MΩ pot → worst-case Thevenin source 250 kΩ at mid-travel; with 100 nF, τ ≈ 25 ms → fine for a volume knob; sample at 20–50 Hz.
- Use an **ADC1** pin (GPIO 32–39 on classic ESP32). Widely reported (not confirmed in my search results) that ADC2 is unusable while Wi-Fi is active.
- Software: average 16–64 samples, then exponential smoothing plus **hysteresis/dead-band** (change volume only if the reading moves more than ~1–2 % of full scale) so a crackly track or ADC noise does not cause volume jitter; clamp the dead zones near 0 V and near 3.3 V (ADC non-linear there).
- Log taper: the wiper voltage ratio of a logarithmic pot *is* the attenuation the original radio applied. So using `gain = Vwiper/Vref` directly as a **linear amplitude multiplier** reproduces the original feel. Only if the firmware/DAB module expects "volume steps" (already dB-like), the reading must be linearised first (e.g. a measured 8–10-point lookup table per pot type; typical "log" pots are two-segment approximations, ~10–20 % resistance at mid-rotation — unverified).
- Crackle: when read by ADC, a scratchy track produces brief wrong *values* rather than audible crackle; median filtering removes them. This is an advantage over passing audio through a 60-year-old pot.
- Why not keep the pot in the analog audio path: 500 k–1 M is far too high an impedance for a class-D module input (typically tens of kΩ) → loading, hum pickup. ADC reading is the cleaner option. Alternative for failed pots: replace with a 10 k linear pot or rotary encoder on the original shaft/knob (shaft diameters: commonly 6 mm, some older sets 4 mm or flatted — verify per set).
- Switch: best use is **not** as a logic input but to switch the **entire low-voltage DC supply** (0.5–2 A at 5/12 V): that current wets the contacts, and DC arcing at ≤12 V is negligible for a contact rated for 250 V AC. If used as a logic input (soft standby), use ≥10 mA pull-up current (e.g. 330 Ω to 3.3 V) and/or 100 nF–1 µF across the contact, and debounce ≥50 ms. Many of these switches are double-pole: one pole can switch power, the other can signal the MCU.

### Gaps
- No source measured actual reliability of vintage pot-mounted mains switches at low voltage; the wetting-current concern is from general switch literature, not tube-radio-specific.
- No verified data on the taper law of specific Philips/Preh/Ruwido log pots with loudness tap.
- Official Espressif statement on maximum recommended source impedance not found in results.

---

## 3. Dial lamps: bulb types, running from 5 V, LED replacements

### Takeaway
The standard dial lamp in these radios is the 6.3 V / 0.3 A E10 bulb fed from the heater winding; warm-white LEDs (around 2000 K) are an accepted replacement in the collector community but are more directional and can be too bright at nominal current.

### Cited Findings
- "6,3 V 0,3 A E10 are the dial lamps that were standard for radios for decades" (forum statement) — [forum.electronicwerkstatt.de](https://forum.electronicwerkstatt.de/phpBB/topic120500_f6_bxtopic_timexDESC_by1_bz0_bs0.html)
- Conrad sells a Barthelme 6.3 V 300 mA E10 dial lamp (listed as 1.9 W) — [Conrad](https://www.conrad.de/de/skalenlampe-63-v-19-w-sockel-e10-klar-00266392-barthelme-1-st-549269.html)
- radiomuseum.org forum thread "LEDs in (Röhren-)Radios": a warm-tone LED of about 2000 K worked very well as a dial lamp with an authentic look behind a celluloid dial; data given 2.65 V forward voltage, 20 mA nominal; LEDs at nominal current may be **too bright** and should be run at reduced current; series resistor sets the current — [radiomuseum.org forum](https://www.radiomuseum.org/forum/leds_in_roehren_radios.html)
- Forum opinions: modern warm-white LEDs are good enough that the difference is hardly noticed; LEDs radiate much more directionally than filament bulbs (matters for even dial illumination); LEDs must not be run on AC with only a series resistor / reverse voltage can damage them — [forum.electronicwerkstatt.de: LED statt Skalenlämpchen?](https://forum.electronicwerkstatt.de/phpBB/topic87110_f47_bxtopic_timexDESC_by1_bz0_bs0.html)
- Ready-made warm-white E10 screw-base LED "bulbs" for 6 V / 6.3 V are sold on eBay (quality/voltage tolerance not evident from listings) — [eBay.de listing](https://www.ebay.de/itm/157179088445); [eBay.de listing](https://www.ebay.de/itm/114548788248)

### Inferences (UNSOURCED / arithmetic)
- A 6.3 V 0.3 A bulb = 1.9 W; two bulbs ≈ 0.6 A ≈ 3.8 W — on a 5 V USB-class supply that is more than the entire radio electronics and a noticeable heat source. ESTIMATE: on 5 V the same bulb draws roughly 0.26–0.27 A (filament resistance drops with temperature), gives clearly less and yellower light (about 40–50 % output) but lasts far longer. Cold-filament inrush is several times nominal current — can brown-out an ESP32 if lamp and MCU share a weak 5 V rail; switch the lamp via a MOSFET with soft-start (PWM ramp) or give it its own feed.
- "7 V 0.3 A" Philips types (e.g. 8045D) were in the task brief but were **not** confirmed by any search result; verify against the set's service sheet or the marking on the bulb.
- Recommended for a kit: E10 warm-white LED insert or a short 5 V warm-white (2200–2700 K) LED strip/diffused LEDs, 20–60 mA total, PWM-dimmable from a GPIO via MOSFET; this also lets the dial lamp double as a status indicator (e.g. slow fade while tuning/no signal). Diffuse (sand the LED dome or use the original reflector) to counter directionality.
- LED PWM for dimming should be ≥ a few kHz with slow edges or use DC current setting; hard PWM wiring running along the dial is another potential noise radiator near the DAB antenna.

### Gaps
- No verified table of bulb types per brand/model (Philips 8045D/7 V types, Grundig 7 V 0.3 A, 18 V series lamps in AC/DC sets).
- No measured brightness comparison incandescent at 5 V vs LED.
- NL retail prices for E10 LEDs not verified.

---

## 4. Loudspeakers: impedances, Philips 800 Ω high-impedance (OTL) speakers, keep or replace, replacement drivers

### Takeaway
Most sets have a ~4–5 Ω speaker behind an output transformer and can be driven directly by a small class-D amp, but many Philips sets from the OTL era use ~800 Ω speakers (range mid-600 Ω to ~1.2 kΩ) that cannot be driven usefully from 5–12 V and need replacing or a matching transformer. A new Visaton FR 10 4 Ω full-range driver costs about €11–13 in NL.

### Cited Findings
- Philips made high-impedance speakers ranging from mid-600 Ω to around 1.2 kΩ, **800 Ω being the most common** — [vintage-radio.com: Philips High Impedance Speakers](https://vintage-radio.com/repair-restore-information/valve_philips-speakers.html)
- "A Philips (tube) radio often has 800 Ω speakers" (Dutch forum statement); 800 Ω types AD3700AM / AD3800AM are mentioned by name — [Circuits Online forum 163888](https://www.circuitsonline.net/forum/view/163888); [Circuits Online forum 133624](https://www.circuitsonline.net/forum/view/133624)
- Rationale: Philips wanted to eliminate output transformers (lossy and expensive); low-Ri valves drive the 800 Ω speaker directly; the EL86 was developed/intended for these OTL radios; UL84 is a close relative — [diyAudio: EL86 and speakers 800 Ohm](https://www.diyaudio.com/community/threads/el86-and-speakers-800-ohm.61690/latest); [Circuits Online](https://www.circuitsonline.net/forum/view/133624)
- Identification hint (forum): Philips type codes for 800 Ω speakers have an "A" after the number — [diyAudio thread](https://www.diyaudio.com/community/threads/el86-and-speakers-800-ohm.61690/latest)
- Specific sets named in results as using this technique: Philips **B7X14A** "Reverbeo"; also B2G25U and a low-cost UCL82 design are mentioned — [vintage-radio.com](https://vintage-radio.com/repair-restore-information/valve_philips-speakers.html); [diyAudio](https://www.diyaudio.com/community/threads/el86-and-speakers-800-ohm.61690/latest)
- To connect 4/8 Ω equipment to 800 Ω speakers (or vice versa) an impedance-matching transformer is required; a forum user mentions a 12.5 W transformer that is "exactly 800 Ω" — [Circuits Online 163888](https://www.circuitsonline.net/forum/view/163888/1)
- Thread on exactly this use case, connecting speakers of a dead tube radio to a 3.5 mm line/phone output — [Circuits Online 163888/3](https://www.circuitsonline.net/forum/view/163888/3)
- A Marktplaats seller converting antique radios to Bluetooth states he only converts radios whose amplifier is defective **and whose speakers are still good** — [Marktplaats listing](https://www.marktplaats.nl/v/antiek-en-kunst/antiek-tv-s-en-audio/m2391162204-antieke-aetherkruiser-radio-omgebouwd-naar-bluetooth)
- Replacement driver prices (NL): Visaton **FR 10 F 4 Ω** (10 cm full-range, 20 W RMS / 30 W peak) **€10.80 incl. VAT** at Bax Music; €13.00 incl. VAT at RS; FR 10 HM 4 Ω €21.67 incl. VAT; FR 10 HMP 4 Ω €18.96 incl. VAT (prices as shown in search results; date of listing unknown) — [Bax Music](https://www.bax-shop.nl/5-inch-luidsprekers/visaton-fr-10-f-4-ohm-inbouwluidspreker); [RS NL](https://nl.rs-online.com/web/p/speaker-drivers/1976433); [RS NL FR 10 HM](https://nl.rs-online.com/web/p/speaker-drivers/7560149)

### Inferences (UNSOURCED / arithmetic)
- How to identify: measure DC resistance across the voice-coil terminals with the speaker disconnected. ~3–5 Ω → conventional speaker (nominal 4–5 Ω) fed by an output transformer; several hundred ohms (ESTIMATE ~600–900 Ω DC) → Philips high-impedance type. Other tells: no output transformer on the chassis, EL86/UL84 pairs in the valve line-up, impedance stamped on the magnet/frame.
- Why 800 Ω is a show-stopper at low voltage: a bridged 5 V amp delivers at most ~3.5 V RMS → P = 3.5²/800 ≈ **15 mW**; a 12 V bridged amp ≈ 8.5 V RMS → ≈ **90 mW**; a 24 V TPA311x ≈ 17 V RMS → ≈ 0.36 W. Options: (a) replace the driver, (b) step-up transformer (e.g. a 100 V-line PA transformer used in reverse; turns ratio ≈ √(800/4) ≈ 14:1), (c) accept ~0.3 W from a 24 V amp. For a low-cost kit, (a) is simplest.
- Which Philips series: generally the mid/late-1950s to 1960s B-series sets (e.g. B3X…/B4X…/B5X…/B6X…/B7X…) with EL86/UL84 OTL stages — **not confirmed per model** by any source read; always measure.
- Conventional speakers: old radio speakers are efficient (large paper cones, ESTIMATE ~90 dB/W/m or more) and were driven by 2–6 W valve stages, so the 2.5–3 W of a 5 V class-D chip at the same impedance gives comparable room loudness. Keep the original if the cone is intact and the coil does not rub (push the cone gently; listen with a 50–100 Hz tone); it preserves the "warm" tone that the target audience expects. Disconnect the speaker fully from the output transformer secondary before connecting the new amp (or remove the transformer).
- Speaker protection: an old 2–3 W speaker on a 15–30 W TPA311x can be destroyed by a firmware volume bug; limit gain/PLIMIT or choose a ≤3 W amp.
- Sets with several speakers (oval main + electrostatic/small tweeters, "3D-Klang"): drive only the main dynamic speaker; electrostatic tweeters need HT polarisation and must be left disconnected.

### Gaps
- vintage-radio.com page (best single source on Philips 800 Ω speakers and affected models) could not be read; no verified model list.
- No verified sensitivity/power-handling data for original Philips/Grundig drivers (AD3700/AD3800 etc.).
- Prices for other candidate drivers (Visaton FRS 8, FR 13, Monacor) not retrieved; oval replacement drivers (e.g. 4×6", 6×9") not researched.

---

## 5. Cheap class-D amplifier choice (MAX98357A, PAM8403, PAM8302, PAM8610, TPA3110/3116/3118) and EMI versus DAB/FM reception

### Takeaway
For one old 4–8 Ω speaker on 5 V, MAX98357A (I2S in, 3.2 W/4 Ω, filterless spread-spectrum with edge-rate control, low output noise) and PAM8302A (analog in, 2.5 W/4 Ω) are the obvious low-cost fits; PAM8403 is "not recommended for new designs". Class-D amplifiers radiating into a tuner in the same enclosure is a documented problem (including one DAB case) that is fixed by grounding, output filtering, ferrites and distance — no source quantified it for DAB band III.

### Cited Findings
- **MAX98357A**: I2S-input mono class D, 2.5–5.5 V supply, **3.2 W into 4 Ω at 5 V**, filterless spread-spectrum modulation, "sophisticated edge rate control enables filterless class D outputs", active emissions limiting; 2.4 mA quiescent current; **22.8 µV RMS output noise** (AV = 15 dB; an older datasheet revision says 25 µV), 77 dB PSRR at 1 kHz — [Analog Devices MAX98357A product page](https://www.analog.com/en/products/max98357a.html); [datasheet copy](https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/kinetis/62892/1/MAX98357A-MAX98357B.pdf)
- Analog Devices' product page recommends the **MAX98360** for improved performance/lower power; MAX98360A is also 3.2 W/4 Ω/5 V, filterless, low EMI — [Analog Devices MAX98360A](https://www.analog.com/en/products/max98360a.html)
- **PAM8403**: 3 W stereo class D, 3 W at 10 % THD into 4 Ω at 5 V; listed by Diodes Inc. as **NRND** (not recommended for new designs) — [Diodes Inc. PAM8403](https://www.diodes.com/products/analog/audio/part/PAM8403)
- **PAM8302A**: 2.5 W mono class D, 2.5 W at 10 % THD into 4 Ω at 5 V, efficiency up to 88 %, supply 2–5.5 V — [Diodes Inc. PAM8302A](https://diodes.com/part/view/PAM8302A)
- **TPA3110D2**: 15 W class-D stereo BTL amplifier (TI datasheet SLOS528; has PLIMIT power-limit function) — [TI TPA3110D2](https://www.ti.com/product/TPA3110D2)
- AZ-Delivery publishes a complete ESP32 + MAX98357A internet radio wiring/software tutorial — [AZ-Delivery](https://az-delivery.de/en/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/internetradio-mit-esp32-und-max-98357a)
- EMI mechanism: class-D stages switch at roughly 300–600 kHz with square edges rich in high-frequency harmonics; typical designs switch at 400–500 kHz, putting harmonics in the AM band; "some type of EMI avoidance scheme must be implemented" — [TI tech note SSZTAK1](https://ti.com/lit/pdf/ssztak1); [diyAudio: RF interferences](https://www.diyaudio.com/community/threads/rf-interferences.61901)
- DAB-specific anecdote: a builder had a class-D amp interfering with a **DAB radio in the same enclosure**; after a better solid ground and reworking the output filter, reception improved and more stations were received — [diyAudio post](https://www.diyaudio.com/community/goto/post?id=5371001) (attribution to this exact post is from the search summary; verify)
- FM anecdote: a class-D amp caused a lot of interference in the FM range near an Si4731 tuner; fixed with ferrite beads on the amp output and power input — [SparkFun community](https://community.sparkfun.com/t/am-fm-tuner-si4731/35780)
- Hypex application note on class-D and EMI exists (not read) — [Hypex: UcD and EMI](https://www.hypex.nl/media/89/13/75/1778574946/Application%20Note%20UcD%20and%20EMI.pdf)
- In the radiomuseum forum a collector objects in principle to putting such a "Rechteckgenerator" (square-wave generator, i.e. switching module) into a radio — [radiomuseum.org: Bluetooth Modul Einbau in ein Allstromradio](https://www.radiomuseum.org/forum/bluetooth_modul_einbau_in_ein_allstromradio.html)

### Inferences (UNSOURCED)
- Selection logic: if the tuner/SoC outputs **I2S** (ESP32 internet radio, or a DAB module with I2S out) → MAX98357A (or MAX98360A) is the natural single-chip DAC+amp on 5 V; volume is then done digitally in firmware from the pot ADC value. If the DAB module only has **analog line out** → PAM8302A (mono, 5 V) with stereo summed via two resistors; or route analog through an ESP32 ADC only if needed.
- 3 W into an efficient vintage 4–5 Ω driver is enough for a living room; a 12 V TPA3110/3118 board only makes sense for large cabinets or if a 12 V rail is needed anyway, and it adds idle power, bigger inductors and a higher risk to the old speaker.
- Hiss: old high-efficiency speakers reveal amplifier noise floor in a quiet room. MAX98357A's ~23 µV noise is favourable; common complaints about hiss with PAM8403 boards are forum lore (not verified here). With MAX98357A set the lowest sufficient gain (GAIN pin strapping) rather than max gain plus digital attenuation.
- EMI measures to design into a kit PCB: keep speaker leads **short and twisted**, ferrite bead + ~220 pF–1 nF to ground on each amp output at the board edge when leads exceed ~10–20 cm, LC/π filter on the amp's supply, single ground reference bonded to the (retained) steel chassis, amplifier and buck converter at the opposite end of the cabinet from the antenna feed, antenna feed in coax up to the element. The steel chassis of the old radio can serve as a ground plane/shield between electronics and antenna.
- ESP32 itself (Wi-Fi/Bluetooth bursts, 40 MHz crystal harmonics at 200 and 240 MHz fall **inside** band III — arithmetic) and the DAB module's own digital section are additional noise sources; test reception with amp on/off and Wi-Fi on/off on the weakest multiplex before finalising layout.

### Gaps
- No source measured class-D harmonics at 174–240 MHz or compared these chips for DAB desensitisation — the "known problem" is supported only by anecdotes.
- Switching frequencies (MAX98357A ~300 kHz class, PAM8403 ~260 kHz), PAM8610, TPA3116/TPA3118 mono figures and all **module prices** (typically quoted from AliExpress/Kiwi/TinyTronics) were not verified in this session.
- No independent hiss comparison found.

---

## 6. Power supply: external CE adapter + buck converter, ground loops/noise, standby

### Takeaway
No tube-radio-specific source on low-voltage PSU design was retrieved; the only cited data points are that one retro build ran from a 6 V supply and that weak supplies cause ESP32/display trouble. The recommendations below are engineering inference.

### Cited Findings
- A 1970s-radio ESP32 retrofit found enough room in the cabinet for the board and a 6 V supply — [Hackster: RetroRadio WiFi Pilot](https://www.hackster.io/pnjorge/retroradio-wifi-pilot-05b075)
- An ESP32 radio build notes that a marginal supply (iPod dock connector) delivered less power than display + ESP32 may need — [Hoogkamer/WIFI-Radio-ESP32-V2](https://github.com/Hoogkamer/WIFI-Radio-ESP32-V2)
- mikrocontroller.net discussion lists the prerequisites for such a conversion as: adequate power supply, Wi-Fi in range, space in the housing; ESP8266 too weak for software codecs → ESP32 or Pi Zero — [mikrocontroller.net topic 475796](https://www.mikrocontroller.net/topic/475796)
- MAX98357A PSRR 77 dB at 1 kHz (helps against supply ripple) — [Analog Devices](https://www.analog.com/en/products/max98357a.html)

### Inferences (UNSOURCED)
- Architecture for "no mains in the cabinet": one external CE-marked plug-in adapter, DC barrel jack on the rear panel (reuse an existing hole, e.g. the old mains-cord grommet or the PU/tape socket cut-out), reverse-polarity protection (P-MOSFET or Schottky) and a polyfuse on the kit PCB.
- **5 V-only** variant (simplest, cheapest, least EMI): 5 V / 2–3 A adapter → MAX98357A/PAM8302 directly on 5 V, 3.3 V LDO for MCU/tuner; no buck converter in the cabinet at all (one fewer switching source near the antenna). Budget ESTIMATE: ESP32 with Wi-Fi 0.1–0.25 A peaks 0.5 A; amp up to ~0.8 A at full power; LED dial light 0.05 A; incandescent lamps +0.3 A each.
- **12 V** variant only if a TPA311x amp or 12 V lamps are wanted: 12 V adapter → buck to 5 V. Pick a buck with ≥500 kHz–2 MHz switching, shielded inductor, input/output LC filtering, placed far from the antenna.
- The external adapter is itself a switch-mode supply whose noise travels up the DC lead, which then acts as an antenna: put a common-mode choke/clip-on ferrite on the DC lead at the jack plus 100 nF + bulk capacitance at entry. Cheap no-name adapters are the commonest cause of DAB/FM desense — choose a branded, properly certified adapter and test reception with a battery/power bank as a reference.
- Ground loops: with a single floating adapter and no other galvanic connections there is no loop; a loop appears only if an aux/line input or external antenna shield is connected to earthed equipment — handle with a series RC/transformer on aux input if offered.
- Standby: if the original pot switch cuts DC power, standby is only the adapter's no-load draw (EU ecodesign limits external supplies to roughly 0.1 W no-load — figure from memory, verify). Soft standby (MCU alive for instant-on) costs more; for seniors a hard switch with <5 s boot is the more predictable behaviour.

### Gaps
- No sources retrieved on adapter noise vs DAB reception, buck-converter choices, or measured standby power of such builds.
- Legal/CE implications of selling a converted radio with an external adapter were not researched here (likely another researcher's scope).

---

## 7. DAB antenna inside a wooden cabinet

### Takeaway
No source addressed band-III reception inside a wooden tube-radio cabinet. The few data points: a 727 mm wire dipole was resonant on channels 9A–9C, antenna position matters more than exact length, and commercial DAB antennas are specified for 174–240 MHz.

### Cited Findings
- A forum user found a wire dipole of **727 mm total length** resonant for DAB+ channels 9A–9C; with about 1 m of wire vertical in the best position signal strength was 90–100, dropping off rapidly elsewhere — [StereoNET forum: DAB antenna](https://www.stereonet.com/forums/topic/217831-dab-antenna-sydney/)
- Commercial DAB antennas are specified for band III 174–240 MHz (some 174–230 MHz); telescopic DAB/FM rod antennas and passive dipoles are standard catalogue items — [TechniSat DAB/FM telescopic antenna](https://www.technisat.de/en/DAB-FM-telescopic-rod-antenna/0000-6027); [Hama DAB+/FM dipole](https://support.hama.com/00205283/hama-dab-fm-dipole-antenna); [Delock 12411 datasheet](https://www.tme.eu/Document/32ae0e847a98d3a9a82e35926da352d5/DELOCK-12411_EN.pdf)
- Silicon Chip published a DIY 5-element band-III antenna for marginal DAB+ areas — [Silicon Chip Nov 2015](https://www.siliconchip.com.au/Issue/SC/2015/November/A+5-Element+Antenna+For+Better+DAB%2B+Reception)

### Inferences (UNSOURCED / arithmetic)
- Wavelength at 200 MHz = 1.5 m → quarter-wave ≈ 37 cm, half-wave dipole ≈ 70–72 cm total (consistent with the 727 mm report). European DAB is vertically polarised (general knowledge) → mount the element **vertically**, e.g. a 35–40 cm wire up the inside rear corner of the cabinet, or a vertical dipole along the side wall, as far as possible from amp/PSU/MCU, fed with thin 50/75 Ω coax.
- Dry wood and the hardboard back panel attenuate VHF little; the **steel chassis, speaker magnet/basket and any foil** inside do detune and shadow — keep the element several cm away from metal, or deliberately use the chassis as the counterpoise of a quarter-wave monopole.
- Reusing the original FM antenna: many German/Dutch sets have an internal **foil or wire FM dipole** glued inside the cabinet (cut for ~95 MHz, ~1.5 m total, 240/300 Ω, usually *horizontal*). Used on band III it is roughly a full-wave element with awkward impedance and wrong polarisation: it will often work in strong-signal areas, but a purpose-cut vertical wire is the better default. The original 240 Ω banana sockets on the rear panel can be reused as the entry for an external antenna.
- Always fit an **external antenna connector** (F or IEC on the back, or SMA pigtail to a rear-mounted telescopic rod) switchable/pluggable against the internal wire: care homes and concrete/foil-insulated flats can have poor indoor band-III levels, and it gives a service fallback without redesign.
- Commissioning step for each conversion: run the tuner's signal-quality/RSSI readout across all local multiplexes with amp at high volume and lamp on; adjust wire position before closing the back.

### Gaps
- No verified information on Dutch DAB+ multiplex channels/field strengths (not researched here).
- No measurement of wood-cabinet attenuation or of original foil dipoles on band III.
- No source comparing internal wire vs telescopic vs active antenna in such builds.

---

## 8. Safety when partly dismantling; what to remove, what can stay

### Takeaway
Sourced material confirms the main electrical hazards (transformerless sets with chassis at mains potential, up to ~300 V DC inside, old electrolytics/paper capacitors failing violently); nothing reliable was found on asbestos, PCB-containing capacitors or selenium rectifiers, so those points below are unsourced cautions that need verification.

### Cited Findings
- In sets without a mains transformer (AC/DC, "universeel"/Allstrom) the chassis is normally at full mains potential; all metal parts can be live; forum members insist on an isolation transformer when working on them — [Circuits Online forum 118004](https://www.circuitsonline.net/forum/view/118004); [Circuits Online forum 134557](https://www.circuitsonline.net/forum/view/134557)
- Tube radios contain voltages up to about 300 V DC — [Circuits Online forum 165752](https://www.circuitsonline.net/forum/view/165752)
- Old electrolytic and paper capacitors fail after long storage; one user reports a capacitor that started smoking and squirted liquid; restorers replace all old capacitors first, or leave old cans in place for looks and fit modern parts underneath; first power-up via series 60 W bulb or variac — [Circuits Online forum 170290](https://www.circuitsonline.net/forum/view/170290); [PA2OHH: verwaarloosde oude buizenradio](https://www.qsl.net/pa2ohh/19vornl.htm)
- A Dutch forum post mentions asbestos only as a small sheet inside a wooden cabinet (i.e. such heat shields do occur) — [Circuits Online forum 145505](https://www.circuitsonline.net/forum/view/145505) (attribution to this thread from the search summary is uncertain)
- A radiomuseum thread deals specifically with fitting a Bluetooth module into an Allstrom (live-chassis) radio — [radiomuseum.org forum](https://www.radiomuseum.org/forum/bluetooth_modul_einbau_in_ein_allstromradio.html)

### Inferences (UNSOURCED — standard practice, verify)
- For a low-voltage-only conversion the radio should **never be plugged into the mains at all** during the work (no "let's see if it still plays"). Before touching: unplug, short the reservoir/filter electrolytics through a ~1–10 kΩ 5 W resistor and confirm <5 V with a meter — charge can persist in sets that were recently powered.
- Remove completely: mains cord and plug, voltage selector wiring, fuse holder wiring, **mains transformer** (also saves 1.5–3 kg), **selenium rectifier** (failed selenium stacks release toxic, foul-smelling selenium compounds — do not power them), multi-section electrolytic can(s) (may leak), wax/paper and "tar" capacitors (leaky; some period oil/paper capacitors may contain PCBs — more typical of large motor/ballast capacitors than radio parts, but treat oily leakage as hazardous waste), and the mains interference capacitor. Dispose via the municipal KCA/e-waste route.
- With the cord removed, the live-chassis problem of AC/DC ("U"-series valves, e.g. Philips …U models) disappears, which makes cheap AC/DC sets *suitable* donors: they are the least desirable to collectors and the most dangerous to keep original.
- Asbestos: thin grey/white fibre boards or paper under/above hot valves, rectifier or dropper resistors, or stapled inside the cabinet top, may be asbestos in pre-1960s sets. Do not sand, drill or vacuum; either leave undisturbed and seal (lacquer/PVA) or reject that donor. For a small business, a written donor-acceptance checklist ("suspected asbestos → do not convert") is prudent.
- Other period hazards: lead solder and cadmium-plated chassis (white/yellow powdery corrosion — don't wire-brush dry), mould/mouse droppings in cabinets, very brittle rubber wiring.
- Can stay as decoration: valves in their sockets (unpowered; optionally lit from below by an amber LED at 2–5 mA for the "glow"), IF cans, tuning capacitor and dial drive (pointer still moves — or the tuning cap/a pot on its shaft can be read by the MCU), magic eye (dead without HT; LED imitation possible), output transformer (unconnected), dial glass and back panel (update or cover the mains rating label; add a new rating label "5 V ⎓ 2 A").
- The retained steel chassis should be bonded to DC ground (shielding) and must have **no** remaining conductor leading outside the cabinet except DC jack and antenna.

### Gaps
- No authoritative source (RIVM, NVHR, radiomuseum articles) retrieved on asbestos, PCB capacitors or selenium rectifier toxicity in domestic radios; treat the unsourced list as a to-verify checklist.
- NVHR/NFOR (nvhr.nl) and buizenradioclub.nl produced no hits in the searches run.

---

## 9. Existing documented conversions, commercial examples, collector opinion, sacrificial models

### Takeaway
Bluetooth conversions of tube radios are common and commercially offered (kits ~€67–113 on eBay; a converted Philips B4X61A fetched €108 on Catawiki); ESP32 internet-radio transplants are well documented for various old sets; DAB+ conversions of tube radios are discussed on radio-bastler.de and mikrocontroller.net but could not be read. Collector opinion is split: purists object, others accept conversion of sets that are defective, and at least one seller converts only radios with a dead amplifier.

### Cited Findings
- Commercial kit: "B.E.A.R Bluetooth Lautsprecher Umbausatz für Antik/Vintage/Retro Röhrenradios", **€67.41–€113.12**, marketed for Grundig, Telefunken, Philips, Nordmende, Loewe Opta sets — [eBay.de shop retroradioshop](https://www.ebay.de/str/retroradioshop)
- Alternative non-destructive approach sold commercially: an AM transmitter kit with Bluetooth that feeds a working tube radio over the air — [eBay.de listing](https://www.ebay.de/itm/145598309820)
- Auction result: "Philips B4X61A Bluetooth buizenradio" sold for **€108** on Catawiki (described as Bluetooth tube amplifier, i.e. valves retained) — [Catawiki lot 101192691](https://www.catawiki.com/nl/l/101192691-philips-b4x61a-bluetooth-buizenradio)
- Marktplaats: antique "Aetherkruiser" radio converted to Bluetooth; seller converts only radios whose amplifier is defective and speakers good — [Marktplaats](https://www.marktplaats.nl/v/antiek-en-kunst/antiek-tv-s-en-audio/m2391162204-antieke-aetherkruiser-radio-omgebouwd-naar-bluetooth)
- Documented ESP32/Pi transplants: EKCO radio with ESP32, OLED and VS1053 + small amp — [hackaday.io project 186284](https://hackaday.io/project/186284-new-life-for-an-old-radio-esp32-in-ekco); Ralph Musto's 1950s Ekco Stroller III refresh — [Hackster news](https://www.hackster.io/news/ralph-musto-s-1950s-ecko-stroller-iii-radio-gets-a-major-refresh-courtesy-of-an-espressif-esp32-400197268dbf); mid-century radio streamer — [Hackster news](https://www.hackster.io/news/stream-in-style-with-this-mid-century-radio-5a421eca6b4f); Raspberry Pi transplant that kept original volume knob and speaker — [Hackaday 2022](https://hackaday.com/2022/09/22/simple-internet-radio-transplant); antique internet radio — [Hackaday 2013](https://hackaday.com/2013/07/14/simple-looking-antique-internet-radio-has-a-lot-under-the-hood); Bluetooth radio keeping a tube amp — [Hackaday 2013](https://hackaday.com/2013/09/22/trash-to-treasure-bluetooth-radio-and-tube-amp-build); Elektor "multimedia valve radio station" — [Elektor Labs](https://www.elektormagazine.com/labs/a-multimedia-valve-radio-station); latest — [Hackaday 7 Oct 2026](https://hackaday.com/2026/10/07/keep-that-old-radio-alive-with-an-esp32/)
- DAB-specific building blocks: "A Minimalistic DAB+ Digital Radio (not only) for the Visually Impaired" using a DAB shield on an ESP32 D1 R32 board — directly relevant to a simple seniors' UI — [Instructables](https://www.instructables.com/A-Minimalistic-DAB-Digital-Radio-not-Only-for-Visu); DAB+ with Arduino UNO — [Hackster](https://www.hackster.io/VGEST/dab-with-arduino-uno-and-large-screen-730f1e); DAB Eigenbau thread — [mikrocontroller.net topic 476785](https://www.mikrocontroller.net/topic/476785); kitchen-radio conversion thread that links a video of a DAB + internet radio conversion — [mikrocontroller.net topic 475796](https://www.mikrocontroller.net/topic/475796)
- German tube-radio forum threads on DAB+/internet/SDR retrofits (unread) — [radio-bastler.de tid=9274](https://www.radio-bastler.de/forum/showthread.php?tid=9274); [tid=8669](https://www.radio-bastler.de/forum/showthread.php?tid=8669)
- ELV Journal series on tube-radio restoration includes a Bluetooth add-on and a reader competition on tube-radio projects — [ELV Teil 6 PDF](https://media.elv.com/file/252591_radio_restaurierung_teil_6.pdf); [ELV Leserwettbewerb PDF](https://media.elv.com/file/2017_04_10_leserwettbewerb_roehrenradio.pdf)
- Opinions (forum-level, not representative):
  - "Many tube radios have been scrapped or converted, so the value [of the rest] keeps increasing" — [Circuits Online 146154](https://www.circuitsonline.net/forum/view/146154)
  - Preferred alternative among enthusiasts: repair the set and feed Bluetooth into the PU/gramophone input — "then you have a real tube amplifier" — [Circuits Online 133995](https://www.circuitsonline.net/forum/view/133995)
  - "What is Bluetooth doing in a tube radio?" / objection in principle to installing a switching module — [mikrocontroller.net topic 383413](https://www.mikrocontroller.net/topic/383413); [radiomuseum.org forum](https://www.radiomuseum.org/forum/bluetooth_modul_einbau_in_ein_allstromradio.html)
  - Collectors do pay notable sums for well-preserved sets; eBay/Kleinanzeigen indicate achievable prices — [mikrocontroller.net: Sind Röhrenradios noch etwas wert?](https://www.mikrocontroller.net/topic/441528)
  - A hobbyist abandoned a tube-radio-to-Bluetooth-box project because it cost too much time — [mikrocontroller.net topic 484415](https://www.mikrocontroller.net/topic/484415)
  - There is "a small market outside collectors" for converted radios — [Circuits Online 133995/2](https://www.circuitsonline.net/forum/view/133995/2)

### Inferences (UNSOURCED)
- The market evidence (kits €67–113; converted set €108) suggests end prices for simple Bluetooth conversions sit around €100–150; a DAB+/preset "seniors' radio" with reused controls is a more elaborate product for which no direct comparable was found.
- Ethical/acceptance line that would be defensible to collectors: convert only sets that are (a) common late-1950s/1960s mass-market models, (b) electrically defective or unsafe (AC/DC live-chassis, burnt transformer), with (c) good cabinet, dial and keys; keep removed parts (valves, transformer, knobs) for donation to restorers; make the conversion reversible where possible (no new holes in the front, original chassis retained).
- Likely cheap/common donors in NL (general market knowledge, **not verified by sources**): 1958–1965 Philips B2/B3/B4-series table sets (e.g. B3X…, B4X…) and their Philetta-class small sets, Erres/Aristona/Siera badge-engineered Philips chassis, mid-range Grundig (Type 80–97, 2xxx/3xxx), Nordmende (Elektra/Carmen/Fidelio), Telefunken (Jubilate/Gavotte), Graetz, Saba small sets — typically €10–40 on Marktplaats/thrift shops. Avoid: pre-war sets, Bakelite design icons, top-of-line models (Saba Freiburg, Grundig 5xxx, Philips Capella-class), anything working and complete in rare condition. Beware Philips sets with 800 Ω speakers (section 4) — budget a replacement driver.

### Gaps
- NVHR/NFOR, buizenradioclub.nl and YouTube builds produced no usable hits; Dutch collector opinion is therefore represented only by Circuits Online posts.
- No commercial provider of DAB+ conversions of tube radios was identified.
- Donor-model list and price levels are unverified.

---

## 10. Labour time per conversion and what can be standardised into a "conversion kit" PCB

### Takeaway
No source gave labour hours for such a conversion; the only signal is negative (a hobbyist abandoned a conversion as too time-consuming, and key banks can require full removal and disassembly). The estimate and kit partitioning below are my own.

### Cited Findings
- A hobbyist gave up converting a defective tube radio into a Bluetooth box because of the time required — [mikrocontroller.net topic 484415](https://www.mikrocontroller.net/topic/484415)
- Freeing a stuck key slider on a Grundig required removing and fully dismantling the key assembly — an example of unpredictable, model-specific labour — [radiomuseum.org forum: Reparatur 6099](https://www.radiomuseum.org/forum/reparatur_6099.html)
- Reusable firmware exists with GPIO-to-preset commands and web-configurable station lists (ESP32-radio; AZ-Delivery project), which removes per-unit software work — [Edzelf/ESP32-radio](https://github.com/Edzelf/ESP32-radio); [AZ-Delivery](https://az-delivery.de/en/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/internet-radio-mit-dem-esp32)
- Commercial precedent for a universal kit approach (Bluetooth only), €67–113 — [eBay.de retroradioshop](https://www.ebay.de/str/retroradioshop)

### Inferences (ESTIMATES, unsourced)
- Per-unit labour for a practised converter with a ready kit (ESTIMATE; first unit of a new model will take 2–3× longer):
  | Step | Hours |
  |---|---|
  | Intake, safety check (asbestos/odd parts), photos, discharge | 0.25–0.5 |
  | Remove chassis, strip mains/HT parts (transformer, rectifier, caps, cord) | 1–1.5 |
  | Clean cabinet, dial glass, chassis; minor cosmetic repair | 1–3 (most variable) |
  | Key bank: clean, free contacts, wire to header, test | 1–2 |
  | Volume pot + switch: clean, rewire, test | 0.5 |
  | Speaker check / replacement (+adapter baffle) | 0.25–1 |
  | Dial lighting (LED) | 0.25–0.5 |
  | Mount kit PCB, DC jack, antenna; wiring | 1 |
  | Programme presets, calibrate pot, reception/EMI test, burn-in | 0.75–1 |
  | **Total** | **≈ 6–11 h** (cosmetic restoration dominates the spread) |
- What can be standardised on one PCB ("ombouwkit"): DC jack input with polarity/over-current protection and filtering; 3.3 V regulation; MCU (ESP32) + DAB/FM tuner module header + I2S class-D amp (MAX98357A/98360A) with output ferrites; screw/JST terminals for **8 key inputs** (pull-ups + RC + series resistors), **volume pot** (3-pin, 100 nF at ADC), **power-switch sense**, **lamp output** (PWM MOSFET, 5 V, soft-start; jumper for LED vs bulb), **speaker**, **antenna** (SMA/U.FL to coax), optional tuning-knob input (second ADC) and aux/BT; a calibration routine in firmware (learn key mapping by pressing each key once; learn pot min/max) so no per-radio code changes are needed.
- What stays model-specific: mechanical mounting (a universal bracket bolted to old valve-socket or transformer holes), choice of key contacts to free, speaker impedance check, antenna routing, cosmetic work. A per-model one-page worksheet (which lugs, which lamp, speaker type) built up over time turns this into repeatable work.

### Gaps
- No documented time studies or small-business accounts of conversion throughput; estimates need validation on 2–3 pilot units.
- Kit BOM cost not verified (module prices not retrievable this session).
