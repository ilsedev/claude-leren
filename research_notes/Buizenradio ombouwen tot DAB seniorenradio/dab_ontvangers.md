# Cheapest reliable DAB+ receiver hardware for a headless MCU-controlled radio (NL buyer, state Nov 2026)

**Read this first (method limits).** The session's network blocked almost every shop, distributor and manufacturer domain (digikey.nl, lcsc.com, monkeyboard.org, dabshield.com, fmdx.org, cnx-software.com, elektormagazine.com, worlddab.org, james.cridland.net all failed to resolve). Only github.com could be fetched directly. Everything else below comes from search-result snippets, which can be stale or truncated. AliExpress, Amazon.nl, bol.com, Action, Lidl, Kruidvat, Tweakers Pricewatch and Mouser returned no usable price data at all. Prices marked "snippet" were not confirmed on the live page. Items marked **[UNVERIFIED RECOLLECTION]** come from the researcher's background knowledge, have no source found in this session, and must be checked before being used in a report.

---

## 1. Which DAB+ receiver chips/modules exist and what do they cost?

### Takeaway
The Skyworks (ex-Silicon Labs) Si4684 is the only DAB+ chip confirmed purchasable in single quantities from a mainstream distributor: about EUR 11 each in small quantities and about USD 8.70 at ~1,000 pieces at DigiKey, with stock in the thousands. Ready-made modules found were all far more expensive (MonkeyBoard/Keystone T4B board EUR 90-99, Raspiaudio Si4689 HAT EUR 59.90); no price could be confirmed for the AVIT DABShield, the PE5PVB receiver (not sold as a product), a bare Keystone T4B module, or a "uGreen DAB board".

### Cited Findings
**Si4684 chip (Skyworks, formerly Silicon Labs)**
- DigiKey lists SI4684-A10-GM (tray, 48-QFN 7x7): 1,270 in stock, USD 12.90 for 1 piece and USD 8.67 each at 1,040 pieces (USD figures from the Brazil regional page); GBP 9.90 for 1 piece on the UK page (snippet) — [DigiKey BR](https://www.digikey.com.br/en/products/detail/skyworks-solutions-inc/SI4684-A10-GM/4069328), [DigiKey UK](https://www.digikey.co.uk/en/products/detail/skyworks-solutions-inc/SI4684-A10-GM/4069328)
- DigiKey lists SI4684-A10-GMR (tape and reel): about 10,800 in stock on several regional pages, around EUR 11 per unit in small quantities; the Ireland page shows a manufacturer standard lead time of 16 weeks (snippet) — [DigiKey NL](https://www.digikey.nl/en/products/detail/skyworks-solutions-inc/SI4684-A10-GMR/4069329), [DigiKey IE](https://www.digikey.ie/en/products/detail/skyworks-solutions-inc/SI4684-A10-GMR/4069329)
- LCSC has a listing for SI4684-A10-GM (part C1526088); no price or stock was visible in the snippet and the page could not be fetched — [LCSC](https://www.lcsc.com/product-detail/C1526088.html)
- The Si4684-A10 datasheet states its characteristics apply to firmware "FM 2.0.10" and "DAB 1.0.6" and refers to a "Si468x Data Sheet Addendum" for later firmware, i.e. the chip is a firmware-loaded device — [Richardson RFPD datasheet copy](https://shop.richardsonrfpd.com/docs/rfpd/si4684.pdf)
- Silicon Labs' AN649 programming guide (2014 revision) tracks separate bootloader "Full Patch" and "Mini-Patch" versions and DAB radio firmware versions per release — [AN649 copy on mikrocontroller.net](https://www.mikrocontroller.net/attachment/412698/SI4684_Prog.pdf)
- In one open-source ESP32 + Si4684 design, the Si4684 DAB and FM images are kept in an external SPI flash on the receiver board ("NVSPI flash") and loaded from addresses 0x086000 (DAB) and 0x106000 (FM); the repository does not say where the images come from — [bales0/FMDABRadio](https://github.com/bales0/FMDABRadio)

**PE5PVB ESP32 + Si4684 receiver**
- Repository PE5PVB/SI4684-DAB-Receiver is licensed GPL-3.0 and contains Gerbers, KiCad files, schematics and STL enclosure files; no BOM or price is listed, the only purchase-like link is a donation ("Buy me a coffee") — [GitHub PE5PVB](https://github.com/PE5PVB/SI4684-DAB-Receiver)
- The design uses an ESP32 board, an ILI9341 colour TFT (TFT_eSPI), two rotary encoders and three buttons; the README warns the repository head is ongoing development that "could and will contain bugs" and points to releases for tested firmware — [GitHub PE5PVB](https://github.com/PE5PVB/SI4684-DAB-Receiver)
- It pairs an ESP32 DevKit v1 with a Si4684 loaded with DAB+ firmware at startup, was created for the 60th VRZA Radio Camp Week 2024, firmware v1.00 is current and betas are distributed via the FMDX Discord (search snippet) — [FMDX.org project page](https://fmdx.org/projects/esp32-dab.php)
- CNX Software (9 Apr 2026) describes it as fully open source and says building it means ordering PCBs and parts and soldering yourself; the "about USD 40 on AliExpress" figure in that article refers to PE5PVB's different TEF6686 FM project, and the DAB radio is not listed there (snippet) — [CNX Software](https://www.cnx-software.com/2026/04/09/open-source-hardware-dab-receiver-combines-esp32-soc-with-skyworks-si4684-chip/)
- Fork/derivative projects exist: bales0/SI4684-FMDAB-Receiver and bales0/FMDABRadio (GPL-3.0, ESP32-WROOM-32D, credits Elektor and dirb.me, has "optional serial control") — [bales0/FMDABRadio](https://github.com/bales0/FMDABRadio), [bales0/SI4684-FMDAB-Receiver](https://github.com/bales0/SI4684-FMDAB-Receiver)

**AVIT Research DABShield**
- The DAB Shield is made by AVIT Research Ltd and carries a Si4684, an audio amplifier and an SMA antenna connector; no price was visible in any snippet — [dabshield.com](https://www.dabshield.com/)
- The DABShield Arduino library supports AVR, SAMD, SAM and ESP32, offers scan, tune, service selection and volume control, and is at version 2.1.3 (June 2026), so it is actively maintained; its licence is listed as "Unknown" — [Arduino Libraries](https://www.arduinolibraries.info/libraries/dab-shield), [arduino.cc reference](https://arduino.cc/reference/en/libraries/dabshield)
- Elektor Labs has projects built on the AVIT DAB Shield, including one with an ESP32 DevKitC — [Elektor Labs "Radio DAB+"](https://www.elektormagazine.com/labs/radio-dab), [Elektor Labs "DAB+ FM Digital Radio with SlideShow"](https://www.elektormagazine.com/labs/dab-fm-digital-radio-with-slideshow)

**Keystone modules / MonkeyBoard**
- MonkeyBoard "DAB DAB+ FM Digital Radio Development Board Pro2.5 with SlideShow" (Keystone T4B module + PIC18F14K50, USB 5 V): EUR 89.95 incl. 19 % German VAT plus shipping at CarTFT (DE); EUR 98.95 incl. VAT on an eBay.de listing (both snippets) — [CarTFT](https://cartft.com/catalog/il/1618), [eBay.de](https://www.ebay.de/itm/403024011826)
- The Keystone T4B has a UART serial control interface and I2S digital audio output — [CarTFT Pro2 PDF](https://www.cartft.com/catalog/PDF/1618/MonkeyBoard%20DAB%20DAB+%20FM%20Digital%20Radio%20Development%20Board%20Pro2%20mit%20SlideShow.pdf)
- Keystone publishes a "slave mode" command protocol (frames start with 0xFE; command type, command ID, serial number, length, data) usable over UART, I2C or SPI — [Keystone SlavemodeSPEC](https://www.mikrocontroller.net/attachment/204713/SlavemodeSPEC_eng.pdf)
- The older Keystone T2_L4A_8650C module's UART pins are on a 1.8 V supply (level shifting needed for 3.3 V MCUs) — [T2_L4A_8650C datasheet](https://www.mikrocontroller.net/attachment/195928/T2_L4A_8650C.pdf)
- Little Bird (AU) lists a MonkeyBoard at 175.72 (AUD), out of stock; CarTFT's older "Pro" board page shows a placeholder 999.00 EUR — both indicate the older variants are effectively unavailable — [Little Bird](https://littlebirdelectronics.com.au/products/monkey-board), [CarTFT old Pro](https://cartft.com/catalog/il/409)

**Other chip-based boards**
- Raspiaudio "Digital Radio V1" HAT for Raspberry Pi (Si4689-A10: AM/FM, DAB/DAB+, HD Radio; I2S audio; open-source Python software; kit with telescopic antenna): EUR 59.90 from the maker's store, buy or pre-order (CNX Software, 10 Apr 2026, snippet) — [CNX Software](https://www.cnx-software.com/2026/04/10/raspberry-pi-sbc-gets-digital-radio-hat-with-am-fm-dab-dab-hd-radio/)
- DABDUINO: an Arduino DAB/DAB+/FM shield with 32-bit DAC and Toslink; no price or current availability found — [Hackaday.io](https://hackaday.io/project/20759-dabduino-dabdabfm-arduino-shield), [GitHub turbyho/dabduino](https://github.com/turbyho/dabduino)
- teknoid/dabpi and c64emulator/dabpi_ctl are open-source Raspberry Pi control tools for Si468x boards — [teknoid/dabpi](https://github.com/teknoid/dabpi), [dabpi_ctl](https://github.com/c64emulator/dabpi_ctl)
- A hobbyist schematic for a self-made Si4684 DAB module exists on mikrocontroller.net — [DAB_Modul_SI4684 schematic](https://www.mikrocontroller.net/attachment/585418/DAB_Modul_SI4684_sch.pdf)

### Inferences
- Module-level options ranked by confirmed price: Raspiaudio HAT EUR 59.90 (needs a Pi or an MCU driving the Si4689 yourself) < MonkeyBoard Pro2.5 EUR 90-99. Neither is cheap enough for a 20-100 series; they are prototype tools only.
- The Si4684 chip at roughly EUR 11 (qty 1) to about EUR 8 (qty ~1,000; price at 20-100 pieces lies in between, not confirmed) is the only verified route to a low per-unit receiver cost, but it requires your own PCB plus a firmware image.
- The PE5PVB receiver cannot be bought; as designed it is a display-centric DX receiver (TFT, two encoders, three buttons). Headless use with preset buttons is not a documented feature. Because firmware is GPL-3.0, it can be modified, but a derived product's firmware must then be released under GPL-3.0. The DABShield library (plain scan/tune/select-service/volume API, ESP32 supported) looks like the easier base for a headless preset radio, but its licence is unclear.
- DigiKey stock of roughly 1,270 trays + 10,800 on reel and no end-of-life signal in any snippet suggests the Si4684 is still an active part; the 16-week factory lead time means a series should be bought from stock in one go.

### Gaps
- **DABShield price and stock**: dabshield.com unreachable. **[UNVERIFIED RECOLLECTION]** historically around GBP 35-40 plus shipping and (post-Brexit) import VAT/handling into NL; the Si468x firmware is pre-loaded in the shield's SPI flash.
- **Bare Keystone T4B/T3B module price** (AliExpress/eBay): not found. **[UNVERIFIED RECOLLECTION]** T4B modules have been sold loose on AliExpress/eBay for roughly EUR 25-40.
- **uGreen DAB board**: no search hit at all; existence in 2026 unconfirmed. **[UNVERIFIED RECOLLECTION]** it was a Si4688 Raspberry Pi board from a small German maker, around EUR 60-70, and may be discontinued.
- **Si4684 price at Mouser, LCSC, Farnell** and exact EUR price breaks at 25/100 pieces: pages unreachable.
- **Si468x firmware licensing**: no source found stating the terms under which the DAB firmware image/patch may be obtained or redistributed. **[UNVERIFIED RECOLLECTION]** Skyworks/SiLabs distributes it to customers (historically under NDA / via the evaluation software), and hobby projects ship it bundled or pre-flashed; the legal status of redistributing it in a sold product needs to be asked of Skyworks or a distributor FAE.
- **Flash size requirement**: only confirmed that images sit at 0x086000 and 0x106000 in an external SPI flash (so at least 2 MB is implied; inference, not stated). Alternatively the host MCU can upload the image over SPI at every boot (documented in AN649, detail not verified here).
- **Other chips** (NXP, Airoha, Quintic, Frontier Smart Venice/Verona/Kino, FCI FC8080, Raontech): no pricing or small-quantity availability found. Frontier/Keystone-class modules are normally sold B2B with minimum order quantities (not verified this session).
- PE5PVB BOM cost, flash chip and DAC used: not stated on the repo page; KiCad files were not inspected.

---

## 2. Cheap ready-made DAB+ receiver boards / dongles (AliExpress, Amazon, eBay) and MCU control

### Takeaway
No bare "DAB+ receiver module board" with a documented UART/I2C interface was found in the search results; what the marketplaces sell cheaply are DAB+ USB dongles/boxes for Android head units at roughly USD 22-45 (one reviewer paid under GBP 20 shipped). Their control protocols are proprietary; the one documented reverse-engineering effort (AP8224 + FC8080 dongle) is early-stage and shows a file-based mass-storage interface that is impractical for a microcontroller.

### Cited Findings
- DAB+ USB dongles/boxes for Android car head units are listed around USD 22.54 to USD 44.73 (Newegg/eBay marketplace listings; snippets, date unknown) — [Newegg example](https://www.newegg.com/p/1W7-00WA-03AS7), [eBay.de example](https://www.ebay.de/itm/254330262439), [eBay.de example 2](https://www.ebay.de/itm/392380764968)
- James Cridland (2026 review) bought a "DAB-PC1" unit from AliExpress for around AUD 35 (under GBP 20) including shipping (snippet; page not fetched) — [james.cridland.net](https://james.cridland.net/blog/2026/review-dabplus-radio/)
- A cheap Chinese "DAB/DAB+ USB-Dongle" sold on eBay/Amazon/AliExpress contains an MVSilicon AP8224C2 MCU/DSP and an FCI FC8080 tuner/demodulator; it enumerates as a USB mass-storage drive ("MP3DAB"), is controlled by opening `.CTL` files (e.g. `DAB_SCAN.CTL`), exposes audio as station-named MP3 files and DLS text as `DAB_DLS.TXT`; reverse engineering is described as early and incomplete, no chip documentation is available — [AlbrechtL/ap8224-dab-dongle](https://github.com/AlbrechtL/ap8224-dab-dongle)
- A Hackster write-up on a cheap serial-controlled FM receiver board reports that its serial interface did not work for the author — [Hackster](https://www.hackster.io/ingo-lohs/fm-radio-48bc05)
- Professional modular DAB+/FM tuner Audac DMP42: EUR 174.49 (irrelevant for cost, shows the price level of "integration-ready" tuners) — [aio.lv](https://aio.lv/en/product--audac-dmp42--12381751)

### Inferences
- The AP8224-type dongle is meant to be plugged into a car stereo's USB port, which then "plays MP3 files"; that explains the odd interface. It needs a USB mass-storage host that reads files, which rules out a simple ESP32/AVR and makes it fragile.
- Android head-unit DAB dongles need a USB host and a vendor Android app; using them from an MCU would need a USB host stack plus a reverse-engineered protocol. Not a low-risk route for a series.
- Therefore, among cheap marketplace items, only modules with a published protocol (Keystone T3B/T4B slave mode over UART) or a bare Si468x are realistically MCU-controllable.

### Gaps
- No AliExpress listing could be opened or even surfaced; actual current AliExpress prices for "DAB+ module", Keystone T4B, Si4684 breakout boards and car DAB boxes are unknown.
- **[UNVERIFIED RECOLLECTION]** Some Android DAB+ USB sticks (Raontech/"DAB-Z"-compatible) are supported by the open-source IRT "omri-usb" Android library; no source was found this session and no MCU/Linux-embedded driver is known.
- Car "DAB+ to FM transmitter" boxes and DAB+ tuner boxes with IR remote/buttons (which could be driven by simulating key presses): not researched; no data.

---

## 3. Cheapest complete retail DAB+ radios in NL/DE to gut for their receiver board

### Takeaway
The cheapest retail DAB+ radios surfaced were about EUR 27-37 (Sangean at MediaMarkt BE EUR 26.99, TechniSat TechniRadio RDR EUR 30.64 at Proshop.nl, Denver DAB-57 EUR 34.71, generic Denver from about EUR 36 on bol.com); nothing under EUR 25 and nothing from Action, Lidl or Kruidvat was found. No source documented power-loss behaviour, numbered preset buttons or line-out for these models.

### Cited Findings
- TechniSat TechniRadio RDR (portable DAB/DAB+/FM, mono): EUR 30.64 incl. VAT (EUR 25.32 excl.) at Proshop.nl (snippet) — [Proshop.nl](https://www.proshop.nl/DAB-Wekkerradio/TechniSat-TechniRadio-RDR-DAB-portable-radio-DABDABFM-Mono/2804080)
- A Sangean DAB+ radio is listed at EUR 26.99 at MediaMarkt Belgium (model not identified in snippet) — [MediaMarkt BE](https://www.mediamarkt.be/nl/v/radio-fm-sangean)
- Denver DAB-57 clock radio (40 station presets): EUR 34.71 at MediaMarkt BE (snippet) — [MediaMarkt BE](https://www.mediamarkt.be/nl/product/_denver-dab57-dab-radio-zwart-147488420.html)
- Denver DAB-18: 20 presets (10 DAB+, 10 FM); price not in snippet — [MediaMarkt NL](https://www.mediamarkt.nl/en/product/_dab18-137642040.html)
- A consumer comparison site names a Denver as "best cheap DAB+ radio", with bol.com prices between EUR 36 and EUR 59.99 on the same page — [debeterewereld.nl](https://www.debeterewereld.nl/wonen-leven/dab-radio/)
- Another names the Denver DAB-46 (mains and battery) as its cheapest pick; no price given — [volgensconsument.nl](https://www.volgensconsument.nl/beste-dab-plu-radio/)
- Netzwelt's 2026 DAB+ test names the Medion DRE-1 as its price tip at about EUR 40 — [netzwelt.de](https://www.netzwelt.de/vergleich/dab-plus-radio-test-2026-besten-modelle-100-euro-preis-leistungs-sieger.html)
- A DAB+ clock radio is shown at EUR 34.99 on MediaMarkt BE's DAB category page — [MediaMarkt BE](https://www.mediamarkt.be/nl/category/dab-radio-0056.html?page=6)
- A senior-oriented retail model exists: Kenwood CR-M70DAB-W "DAB+ radio voor senioren" at BCC (price not in snippet) — [BCC](https://www.bcc.nl/product/kenwood-cr-m70dab-w-dab-radio-voor-senioren-wit)

### Inferences
- A gutted EUR 27-37 retail radio is price-competitive with every confirmed module (EUR 60-99) and brings antenna, PSU, amplifier and paid codec licences with it. Its drawback is control: the receiver is normally a single-board SoC radio driven by its own keypad/display, so an MCU can only "press buttons" (optocouplers/analog switches on the key matrix) without feedback.
- For a 20-100 series this depends on one retail model staying available with unchanged internals, which budget brands (Denver, Medion, Lidl/Action house brands) do not guarantee.
- Many cheap portables use tact-switch presets held in flash and resume the last station on power-up, but this is a general expectation, not a verified property of any model listed here; it must be tested per model.

### Gaps
- Action, Lidl (Silvercrest), Kruidvat, Amazon.nl, bol.com listings and Tweakers Pricewatch/idealo minimum prices: no data retrieved. **[UNVERIFIED RECOLLECTION]** Lidl/Silvercrest and Amazon no-name DAB+ pocket radios have appeared at EUR 15-25 during promotions.
- For every model: numbered preset buttons (count), headphone/line-out, behaviour after mains loss (returns to last station and on-state vs standby), internal chipset (Frontier Kino/Verona, Keystone, Si468x, Airoha, etc.): not found.
- Prices are snippet values with unknown date; MediaMarkt snippets appeared to date from around July 2026.

---

## 4. Software-defined route: RTL-SDR + Raspberry Pi Zero 2 W (welle-cli or similar)

### Takeaway
Technically feasible but neither the cheapest nor the most robust: a Pi Zero 2 W costs about EUR 16-20 incl. VAT and was out of stock at several EU resellers, a genuine RTL-SDR Blog V4 runs USD 35 from the maker and EUR 38-83 at EU resellers, and DAB+ decoding takes roughly half of the Zero 2 W's CPU. Add SD card, DAC/amp and PSU and the unit cost lands well above a Si4684 design, with slow boot and SD-card corruption risk on power cuts.

### Cited Findings
- Raspberry Pi Zero 2 W: EUR 13.99 excl. VAT at Kiwi Electronics (NL), shown out of stock; EUR 16.99 excl. VAT with header, out of stock; EUR 13.20 excl. VAT at Farnell NL; EUR 14.95 at Pimoroni (out of stock); EUR 19.95 incl. VAT at Elektor (out of stock) — snippets — [Kiwi Electronics](https://www.kiwi-electronics.com/nl/raspberry-pi-zero-2-w-10770), [Farnell NL](https://nl.farnell.com/raspberry-pi/rpi-zero-w-v2/raspberry-pi-kit-64bit-arm-cortex/dp/3838499), [Pimoroni](https://shop.pimoroni.com/en-eu/products/raspberry-pi-zero-2-w), [Elektor](https://elektor.com/products/raspberry-pi-zero-2-w)
- RTL-SDR Blog V4: USD 34.95 dongle-only / USD 44.95 with antennas in the maker's eBay store; EU listings EUR 37.67 to EUR 82.90 (eBay.de), EUR 87.31 incl. VAT for the SparkFun-branded kit at DigiKey DE (snippets) — [RTL-SDR Blog eBay store](https://www.ebay.com/str/rtlsdrblog/Computers-Tablets-Networking/_i.html), [eBay.de](https://www.ebay.de/itm/336285786250), [DigiKey DE](https://www.digikey.de/en/products/detail/sparkfun-electronics/WRL-27543/26769969)
- The V4 is a limited edition said to remain in production until the end of 2026; a cheaper R828S-based "V4L" variant is available (snippet) — [rtl-sdr.com](https://rtl-sdr.com/rtl-sdr-blog-v4l-lite-now-available-for-purchase)
- dab-cmdline fork (foonerd) reports DAB+ decoding CPU load: Pi Zero 2 W 45-50 % (65 % before optimisation), Pi 3 B+ 25-28 %, Pi 4 12-14 %, Pi 5 8-10 %; self-reported, test method not described; needs custom RTL-SDR library builds; V3 and V4 dongles supported (V4 needs a PLL-lock fix for DAB frequencies); AGC disabled, PPM correction manual; repository is archived, development moved to foonerd/rtlsdr-radio — [foonerd/dab-cmdline](https://github.com/foonerd/dab-cmdline)
- A welle-cli user reports 85-100 % of one core on a Raspberry Pi 4B serving a single stream (with an SDRplay RSP1A, not an RTL-SDR) — [alexdekker.uk](https://alexdekker.uk/ALEX/?p=141)
- welle-cli has a `-T` option to disable TII decoding to reduce CPU usage — [Debian man page](https://manpages.debian.org/unstable/welle.io/welle-cli.1)
- An RTL-SDR at 2.048 MS/s loaded a Pi Zero 2 W to about 90-110 % CPU in a SatNOGS setup (not DAB) — [Libre Space community](https://community.libre.space/t/raspberry-pi-zero-2w/8575)
- A Volumio FM/DAB plugin based on RTL-SDR exists (ready-made software stack on Pi) — [Volumio community](https://community.volumio.com/t/plugin-fm-dab-radio-rtl-sdr/74311)

### Inferences
- Estimated unit cost (estimate, parts not all price-verified): Pi Zero 2 W ~EUR 17-20 incl. VAT + RTL-SDR ~EUR 12 (generic, unverified) to ~EUR 40 (genuine V4) + microSD ~EUR 5 + I2S DAC/amp ~EUR 3-8 + USB OTG adapter + 5 V/2.5 A supply = roughly EUR 45-80 per unit. Not cheaper than gutting a retail radio and likely 2x a custom Si4684 board.
- CPU is feasible on the Zero 2 W (about half the quad-core budget per the fork's own numbers), but thermal headroom inside a closed valve-radio cabinet and USB power draw of the dongle (roughly 250-300 mA, typical figure, not sourced) need attention.
- Robustness to abrupt power loss requires a read-only root filesystem (overlayfs); Linux boot plus DAB sync means time-to-audio well above a chip receiver. No measured boot time was found.
- Supply risk in 2026: Pi Zero 2 W out of stock at three of five resellers seen; V4 dongle end-of-production announced.

### Gaps
- No direct measurement of welle-cli on Pi Zero 2 W with RTL-SDR found.
- No boot-time or power-cut robustness data found.
- Price of generic RTL2832U/R820T2 sticks and the V4L in EUR: not found. **[UNVERIFIED RECOLLECTION]** generic sticks cost about EUR 10-15 on AliExpress, with worse frequency stability (may need PPM calibration for DAB).

---

## 5. Own PCB route: ESP32 + Si4684 (JLCPCB/PCBWay), RF front-end, availability risk, licences

### Takeaway
An own board is the only route with a verified low core cost: Si4684 about EUR 11 (qty 1) falling toward about USD 8.70 (qty ~1,000) at DigiKey, in stock by the thousands. Open hardware to copy exists (PE5PVB KiCad/Gerbers, GPL-3.0 firmware; bales0 fork; Elektor/dirb.me design). The unresolved risks are the Si468x firmware image (source/licence not documented publicly) and the HE-AAC v2 patent licence, which WorldDAB says is payable to Via Licensing per end product unless the technology supplier includes it.

### Cited Findings
- Si4684-A10 price and stock: see section 1 (DigiKey: USD 12.90 @1, USD 8.67 @1,040; about EUR 11 @1; about 1,270 + 10,800 in stock; 16 weeks factory lead time on reel) — [DigiKey NL](https://www.digikey.nl/en/products/detail/skyworks-solutions-inc/SI4684-A10-GMR/4069329), [DigiKey BR](https://www.digikey.com.br/en/products/detail/skyworks-solutions-inc/SI4684-A10-GM/4069328)
- Package is 48-QFN 7x7 mm (machine-assemblable, not hand-solder friendly) — [DigiKey CA](https://www.digikey.ca/en/products/detail/skyworks-solutions-inc/SI4684-A10-GM/4069328)
- Complete open reference designs: PE5PVB (KiCad, Gerbers, schematics, STL; firmware GPL-3.0) and bales0/FMDABRadio (ESP32-WROOM-32D + Si4684 + external SPI flash holding DAB image at 0x086000 and FM image at 0x106000; GPL-3.0) — [PE5PVB](https://github.com/PE5PVB/SI4684-DAB-Receiver), [bales0/FMDABRadio](https://github.com/bales0/FMDABRadio)
- The Si468x family is described as single-chip digital radio receivers for consumer electronics (launch coverage) — [eeNews Europe](https://www.eenewseurope.com/en/single-chip-digital-radio-receivers-for-consumer-electronics/)
- WorldDAB patent information: the original DAB patents expired in 2013; DAB+ audio uses HE-AAC v2, whose licence is payable to Via Licensing; the royalty applies per product (a product with DAB+ and internet streaming needs one AAC licence); some suppliers of decoding modules include the AAC licence in their offer; applicability depends on country of manufacture and of sale, and for products made in China the effective expiry is given as 2036 (snippet; page not fetched) — [WorldDAB DAB+ patent information](https://worlddab.org/resources/dab-plus-patent-information)
- Historical Via AAC pool rates (2016 table, treat as outdated): tiered per-unit fees from USD 0.78 down to USD 0.35 at higher volumes, inclusive of underlying AAC patents — [Radio World](https://www.radioworld.com/industry/via-licensing-sets-up-extended-high-efficiency-aac-patent-pool)
- For comparison, the DRM consortium states its royalty (about USD 1.10 per device) is paid once per final device, not per chip or module — [DRM.org](https://www.drm.org/drm-technology-and-logo-intellectual-property-rights-ipr/)

### Inferences
- Rough BOM estimate per unit at 20-100 pieces (ESTIMATE, only the Si4684 price is sourced): Si4684 ~EUR 9-11; ESP32 module ~EUR 2.5-4; SPI flash 2-4 MB ~EUR 0.3; crystal, LDOs, passives, RF matching, antenna connector ~EUR 2-3; I2S DAC/class-D amp (if the Si4684 analogue output is not used) ~EUR 1-3; 4-layer or 2-layer PCB + SMT assembly at JLCPCB ~EUR 4-8 at these volumes (Si4684 probably a consigned/global-sourced part with extended-part fees). Total in the order of EUR 20-30 per unit, plus one-off setup/shipping/import VAT. Not verified by quotation.
- The Si4684 has analogue stereo line outputs and I2S (per the family's general design; pin-level detail not verified in this session), so "software volume" can be done with the chip's own volume command (the DABShield library exposes volume control).
- RF front-end: reference designs use a simple VHF band-III input with matching network and an SMA/F connector for a telescopic or wire antenna (DABShield has SMA). Layout of the tuner inductors and keeping ESP32/switching noise out of 174-240 MHz is the main engineering risk; copying a proven layout (PE5PVB, AVIT) is advisable. Detailed front-end requirements (AN650-type guidance) were not retrieved.
- Licence position for a 20-100 unit maker: per WorldDAB the HE-AAC licence attaches to the end product; whether Skyworks' chip price includes it is unconfirmed. At historical rates the fee itself would be under USD 1 per unit, but Via/Via-LA pools typically also involve a licence agreement and reporting, which is the real burden for a micro-producer.
- GPL-3.0 firmware (PE5PVB/bales0) may be used commercially but obliges source release of the modified firmware to recipients.

### Gaps
- Whether the Si4684 purchase price includes the HE-AAC v2 decoder licence: not found; ask Skyworks/distributor.
- Current Via Licensing (now Via LA) AAC fee schedule, minimums and any small-volume exemption: not found (2016 data only).
- WorldDAB logo / "Digital Radio tick mark" conditions and costs for small producers: not found.
- Si468x firmware image: download location, licence, and right to ship it in sold units: not found (see section 1 gaps).
- Any PCN/NRND/EOL notice for Si468x at Skyworks: not found (no negative signal, but skyworksinc.com product page was not retrieved).
- Real JLCPCB/PCBWay quotes; whether JLCPCB's parts library stocks SI4684-A10-GM (LCSC C1526088 exists but stock unknown).
- CE/RED conformity obligations for a receiver sold in the EU (EN 303 345 for broadcast receivers, EMC, LVD for a mains-powered valve-radio conversion): not researched, but relevant for any "product" beyond gifts.

---

## 6. Comparison only: FM module and ESP32 internet radio route

### Takeaway
No prices could be retrieved for FM modules or ESP32 internet-radio parts in this session; everything here is unverified background knowledge. Directionally, both are an order of magnitude cheaper than any DAB+ route.

### Cited Findings
- A TEA5767-based "complete DIY FM stereo receiver board" and an Icstation FM DIY board at about USD 27.99 turned up in marketplace results (snippet; kit boards with amplifier, not bare modules) — [Newegg listing](https://www.newegg.com/p/0NY-05B6-00080)
- Si4703 FM tuner evaluation boards are sold by Pimoroni (price not in snippet) — [Pimoroni](https://shop.pimoroni.com/en-ca/products/si4703-fm-tuner-evaluation-board)
- Adafruit documents an I2C FM radio board (ScoutMakes, RDA5807-class) — [Adafruit Learn](https://learn.adafruit.com/scoutmakes-fm-radio-board-stemma-i2c.md?view=all)

### Inferences
- **[UNVERIFIED RECOLLECTION]** RDA5807M modules cost roughly EUR 0.50-2, TEA5767 modules EUR 1-3, Si4703 breakouts EUR 3-8 on AliExpress (cheaper in tens); all are I2C-controlled with mature Arduino libraries, so an FM-only headless preset radio has a receiver cost under EUR 2.
- **[UNVERIFIED RECOLLECTION]** An ESP32 internet radio needs only an ESP32 board (~EUR 3-5) plus an I2S DAC/amp such as MAX98357A or PCM5102 (~EUR 1.5-4), about EUR 6-10 in total, using open firmware (e.g. ESP32-audioI2S based projects); it depends on Wi-Fi at the user's home and on stream URLs staying valid, which is a maintenance burden for a seniors' radio.
- A hybrid is possible at near-zero extra cost: an ESP32 + Si4684 board already has Wi-Fi for internet-radio fallback, and the Si4684 itself also receives FM.

### Gaps
- No verified 2026 prices for RDA5807M, TEA5767, Si4703, MAX98357A, PCM5102, VS1053 or ESP32 dev boards (AliExpress and NL web shops unreachable).

---

## 7. Status and future of DAB+ and FM in the Netherlands

### Takeaway
There is no FM switch-off date in the Netherlands: the national commercial FM licences auctioned in 2023 run until 2035 and the ministry has said FM will not be phased out before then, with FM expected to remain dominant for several more years. DAB+ is being expanded (simulcast obligations, local DAB+ licences from January 2026, second local channel from June 2026), so both FM and DAB+ are safe choices for roughly the next decade; DAB+ is the more future-proof of the two.

### Cited Findings
- Nine national commercial FM licences were auctioned in 2023, valid from 1 September 2023 through 2035; the auction raised EUR 152.8 million in total — [NOS](https://nos.nl/l/2464150)
- The Ministry of Economic Affairs committed that FM will not be phased out and fully replaced by DAB+ before 2035 (search-snippet summary of the government file "Staat van FM in Nederland", March 2023) — [Rijksoverheid](https://www.rijksoverheid.nl/documenten/2023/03/29/staat-van-fm-in-nederland)
- A study for the ministry concluded that a switch-off before roughly 2027-2032 would have mainly negative effects (snippet) — [officielebekendmakingen blg-827616](https://zoek.officielebekendmakingen.nl/blg-827616.pdf)
- Ministerial letter to parliament (September 2025): the FM-to-DAB+ transition is gradual and FM is expected to remain the dominant distribution channel for several more years; the minister will support the transition with legislation (snippet) — [Eerste Kamer document](https://www.eerstekamer.nl/nonav/behandeling/20250923/brief_regering_diverse_radio/document3/f=/vmrdlh7qqizi.pdf)
- The Postma/Idsinga motion (adopted 1 July 2025) asks the government to pursue full DAB+ coverage for regional public broadcasters in their provinces, noting commercial operators do not invest in less profitable areas such as the Wadden (snippet) — [Eerste Kamer document](https://www.eerstekamer.nl/nonav/behandeling/20250923/brief_regering_diverse_radio/document3/f=/vmrdlh7qqizi.pdf)
- 27 non-national FM licences were bundled with DAB licences in 2023 with a simulcast obligation (FM programme must be carried unchanged and simultaneously on DAB+) (snippet) — [Staatscourant 2025-44300](https://zoek.officielebekendmakingen.nl/stcrt-2025-44300.odt)
- The RDI began allocating local DAB+ licences on 15 January 2026 — [WorldDAB news](https://www.worlddab.org/newsroom/17243/netherlands:-distribution-of-local-dab+-licences-will-commence-on-15-january)
- Since 9 June 2026 local public broadcasters may use two licences in the same DAB+ area (first channel must simulcast the FM programme) — [WorldDAB news](https://www.worlddab.org/newsroom/18182/research:-second-dab+-channel-offers-local-broadcasters-new-opportunities)
- The Dutch minister was reported to be examining a DAB+ model (WorldDAB news item; content not retrieved) — [WorldDAB news](https://www.worlddab.org/newsroom/17639/netherlands-minister-examines-dab+-model)
- Neighbouring context: Flanders dropped its 2031 FM end date, with switch-off now "2035 at the earliest"; Switzerland's National Council voted to abandon the full FM switch-off planned for end of 2026 — [Belga](https://www.belganewsagency.eu/flemish-government-postpones-fm-radio-switch-off-dropping-2031-end-date), [heise](https://heise.de/-10639622)

### Inferences
- A radio built in 2026-2027 on FM alone would work until at least 2035 for the national commercial stations; public-broadcaster FM (NPO) is governed separately and was not specifically confirmed here.
- The European trend in 2025-2026 is toward postponing FM switch-offs, which lowers the urgency of DAB+ but does not reverse the direction; DAB+ additionally offers stations not on FM and noise-free reception, which matters for seniors, while regional gaps (e.g. Wadden) show DAB+ coverage is not yet uniformly complete for regional services.
- A Si4684-based design covers both (DAB+ and FM in one chip), hedging either way.

### Gaps
- Current DAB+ population/indoor coverage percentages for the national multiplexes (NPO mux 12C, commercial mux 11C) and household penetration: not retrieved (worlddab.org country page blocked). **[UNVERIFIED RECOLLECTION]** national multiplexes are generally cited at 95 %+ outdoor/mobile coverage; indoor reception in valve-radio locations (living rooms, steel/concrete buildings) can be weaker and needs a decent antenna.
- Any Dutch government decision taken during 2026 on a post-2035 FM policy: none found; latest government source located is September 2025.
- NPO FM licence end dates: not found.
