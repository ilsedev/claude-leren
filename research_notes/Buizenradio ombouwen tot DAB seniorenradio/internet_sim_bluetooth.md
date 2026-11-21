# SIM/4G internet radio + Bluetooth option (NL, state as of Nov 2026)

Method note: all "Cited Findings" come from web search results gathered on 2026-11-21. Almost none of the pages could be opened in full: the two direct fetches attempted (simbase.com, elecrow.com) were blocked by the session network, so figures are taken from search-result summaries and should be re-checked on the live page before they go into a BOM or business case. Anything under "Inferences" is calculation or engineering judgement, not a sourced fact. Prices in USD are left in USD where the source quoted USD.

## 1. Cellular modules: which are cheap and suitable for 64-128 kbps streaming

### Takeaway
An LTE Cat-1 module of the SIMCom A7670E family costs about USD 9-10 per piece at LCSC, and a ready ESP32+A7670E dev board (LilyGO T-A7670E) about USD 33, so the modem itself is not the cost problem. 2G is not a viable basis in NL: Odido has no 2G, KPN stops 1 December 2027, Vodafone "between end 2026 and 2030".

### Cited Findings
- A7670E-FASE (LCSC C7435296): reference price from USD 9.80, 325 in stock, SMD 24x24 mm, LTE Cat 1, trays of 20 — [LCSC](https://www.lcsc.com/product-detail/C7435296.html)
- A7670E-LASE (LCSC C5362211): USD 9.39 at 1+, USD 9.21 at 10+ — [LCSC](https://www.lcsc.com/product-detail/C5362211.html); an older LCSC datasheet snapshot showed USD 8.30 at 1+ (date unclear) — [LCSC datasheet](https://datasheet.lcsc.com/lcsc/2308241748_SIMCom-Wireless-Solutions-A7670E-LASE_C5362211.pdf)
- A7672E-FASE is in the JLCPCB assembly parts library (C5370391), i.e. it can be placed by JLCPCB; no price was visible — [JLCPCB](https://jlcpcb.com/partdetail/A7672E-FASE/C5370391)
- LilyGO T-A7670E/G/SA R2 (ESP32-WROVER-E, 4 MB flash, 8 MB PSRAM + A7670 module): regular price USD 32.89 in LilyGO's own shop; the page carries a customer comment "This version of the board is not stable" — [LilyGO shop](https://lilygo.cc/products/t-sim-a7670e), [LilyGO wiki](https://wiki.lilygo.cc/products/t-sim-series/t-a7670/t-a7670e/)
- Third-party resale of the same board: about USD 49.65 (approx. EUR 42.72) without GPS antenna, USD 56.90 with — [eBay.de](https://www.ebay.de/itm/316848212710), [eBay](https://www.ebay.com/itm/355018611624)
- LilyGO also sells an ESP32-S3 variant (T-A7670E-S3) and a T-Call A7670 board — [Tindie S3](https://www.tindie.com/products/lilygo/t-a7670esa-s3-standard-development-board/), [Tindie T-Call](https://www.tindie.com/products/lilygo/lilygo-t-call-a7670-4g-2g-esp32-development-board/)
- A7670E bands according to a third-party component page: LTE B1/B3/B5/B7/B8/B20/B28 plus GSM 900/1800; certifications listed as CE, FCC, RoHS. Bands vary per variant (FASE/LASE/LABE) — [Cirkit Designer](https://docs.cirkitdesigner.com/component/e31a11e7-26fb-4517-893f-ee70f324a393/a7670e-ltegnss-cat-1-module)
- LilyGO lists its T-A7670 board as RoHS/CE(RED)/FCC certified (board-level listing, not the module's Declaration of Conformity) — [LilyGO wiki](https://wiki.lilygo.cc/get_started/en/SIM/T-A7670/T-A7670G/T-A7670G.html)
- Waveshare ESP32-S3-A7670E-4G: the on-board speaker and mic are wired to the A7670E for calls only, not to the ESP32, so an external I2S DAC is needed for radio audio — [Waveshare FAQ](https://docs.waveshare.com/ESP32-S3-A7670E-4G/FAQ)
- Some LilyGO SIM boards (SIM7000/7080 class) support only LTE-M/NB-IoT/2G and not regular Cat-1/Cat-4 4G; the SIM and carrier must then support LTE-M/NB-IoT — [Random Nerd Tutorials](https://randomnerdtutorials.com/lilygo-ttgo-t-a7670g-a7670e-a7670sa-esp32)
- On UART-connected modems (SIM7600 boards) the MCU gets roughly 14 KB/s at 115,200 baud up to about 115 KB/s at 921,600 baud (forum estimate) — [Arduino forum](https://forum.arduino.cc/t/getting-downloaded-4g-lte-data-from-sim7600-to-mcu/1276759)
- For a comparable Cat-1bis module (Quectel EG915U-EU) a forum thread cites 1 A peak on VBAT_BB and 2.5 A on VBAT_RF — [Quectel forum](https://forums.quectel.com/t/eg915u-eu-clarification-on-lte-current-peaks-and-burst-duration/46610)
- 2G/3G in NL: KPN switched off 3G on 31 March 2022 and stops 2G definitively on 1 December 2027 (moved from 1 December 2025) — [KPN](https://www.kpn.com/zakelijk/mobiel/van-3g-naar-4g-verbinding.htm), [KPN community](https://community.kpn.com/mobiel-15/hoe-lang-kan-ik-mijn-toestel-nog-gebruiken-wanneer-stopt-kpn-met-2g-643050)
- Vodafone stopped 3G in 2020; 2G stays "at least until end 2026", switch-off somewhere between end 2026 and 2030 — [ID.nl](https://id.nl/huis-en-entertainment/mobiel/smartphone-en-tablet/ook-vodafoneziggo-stopt-met-aanbieden-van-2g-netwerk), [Bright](https://www.bright.nl/plusplus/2098913/kan-jouw-oma-straks-nog-wel-bellen-2g-gaat-eruit-dus-check-deze-alternatieven.html), [Emerce](https://www.emerce.nl/nieuws/acm-informeer-gebruikers-tijdig-afschakelen-2g-3g)
- Odido switched off 2G in June 2023 and promised 3G until at least 1 August 2026, with the final date to be announced 6 months ahead — [Odido business blog](https://www.odido.nl/business-blog/connectiviteit/2g-3g-iot-verdwijnen/), [iCulture](https://www.iculture.nl/nieuws/odido-stopt-3g/), [ACM](https://www.acm.nl/nl/publicaties/gevolgen-van-de-afschakeling-van-2g-en-3g)

### Inferences
- A 128 kbps stream needs 16 KB/s net. At 115,200 baud (about 11.5 KB/s with 10 bits per byte) the UART link is too slow; the modem UART must run at 460,800-921,600 baud with hardware flow control, or the modem must be attached over USB (ESP32-S3 USB host). This is the single most likely cause of stutter in a naive design.
- Cat-1 / Cat-1bis (A7670E, A7672E, EC200U, EG800K, Air780E class) is the right category: downlink of several Mbps is far above the 64-192 kbps needed. NB-IoT (tens of kbps) is too slow; LTE-M is marginal at best for 128 kbps and is sold with tiny data budgets. These data-rate statements are general background knowledge, not verified this session.
- 2G/GPRS modules (SIM800, the old LilyGO T-Call SIM800) should be ruled out: too slow for 128 kbps and the networks are being closed (Odido gone, KPN December 2027).
- PSU: budget for 2 A (or more) bursts on the modem supply, with a dedicated buck converter around 3.8-4.0 V and large low-ESR bulk capacitance close to the module, separate from the class-D amplifier supply. The exact A7670E peak figure was not confirmed (see Gaps); the 2.5 A Quectel figure above is for a different module.
- Antenna: inside a wooden vintage cabinet an adhesive FPC or external LTE antenna on a u.FL/SMA pigtail is the practical choice; keep it away from the speaker magnet, mains transformer and metal chassis. The B20 (800 MHz) and B28 (700 MHz) low bands matter for indoor coverage and need a physically larger antenna. Engineering judgement, unsourced.
- TDMA-like burst noise from the modem can couple into the audio path; layout separation and a digital-input (I2S) class-D amp reduce this. Engineering judgement, unsourced.

### Gaps
- No price found this session for Quectel EC200U-EU, EC800, EG800K-EU, Air780E, or SIM7600E, and no Mouser or AliExpress listings were returned.
- The official SIMCom A7670 hardware design guide (VBAT range, peak current, capacitor recommendations) could not be opened: www.elecrow.com is outside the session's allowed network domains. The "2 A burst" figure in the brief is therefore unconfirmed for the A7670E specifically.
- The module-level RED Declaration of Conformity for the A7670E was not retrieved; only third-party statements that it is CE certified.
- Whether Odido actually switched off 3G after 1 August 2026, and Vodafone's definitive 2G date, could not be confirmed. Irrelevant for an LTE-only design, but relevant if a module falls back to 2G.

## 2. Software: ESP32 audio streaming over PPP/cellular

### Takeaway
No project was found that runs an ESP32 internet radio (ESP32-audioI2S, yoRadio, KaRadio32, MiniWebRadio) over an LTE modem; the building blocks exist (esp_modem PPP, working A7670 bring-up) but the combination would be the maker's own integration and soak-testing work.

### Cited Findings
- esp_modem is Espressif's managed ESP-IDF component for GSM/LTE modems that support AT commands and PPP; it provides a PPP network interface — [Espressif docs](https://docs.espressif.com/projects/esp-protocols/esp_modem/docs/latest/README.html)
- Espressif's docs note the A7670 does not exit CMUX mode correctly and supply patches for the entry/exit sequence — [Espressif docs](https://docs.espressif.com/projects/esp-protocols/esp_modem/docs/latest/README.html)
- A community gist shows an A7670 bring-up reaching a PPP connection with an IP address — [GitHub gist](https://gist.github.com/diplfranzhoepfinger/44aa433829e36bc7266f11f1e7fc5ab2)
- Waveshare's A7670E example is built with ESP-IDF; using Arduino IDE requires porting work (TinyUSB, PPP packet processing) — [Waveshare FAQ](https://docs.waveshare.com/ESP32-S3-A7670E-4G/FAQ)
- ESP32-audioI2S handles the Icecast HTTP protocol and decodes to PCM; its examples use WiFi — [DigiKey maker.io](https://www.digikey.com/es/maker/projects/esp32-audio-project-part-i-internet-radio-with-is-dac/b8378782c8524ab78bc1335a2ddb57cb)
- ESP32-audioI2S issue #1013: choppy audio on HLS (.m3u8) stations when built under ESP-IDF with "better WiFi speed" sdkconfig, fine under plain Arduino — [issue index](https://issues.ecosyste.ms/hosts/GitHub/repositories/schreibfaul1%2FESP32-audioI2S/issues)
- In an arduino-audio-tools discussion a user partly cured MP3 stream stutter with a heavily oversized output-side buffer — [GitHub discussion](https://github.com/pschatzmann/arduino-audio-tools/discussions/1930)
- yoRadio is a widely used ESP32 WiFi radio firmware with deployment instructions for many hardware platforms — [DigiKey maker.io](https://www.digikey.com/en/maker/projects/how-to-make-simplest-and-cheapest-compact-internet-radio-yoradio/e2ea59e092e744efac23dde7c30fe711)

### Inferences
- Because PPP via esp_modem yields a normal lwIP network interface, any ESP-IDF-based HTTP/Icecast client should in principle work unchanged over it; WiFi-specific firmware (yoRadio, KaRadio32) would need its WiFi connection manager and web UI replaced. Plausible, but untested in any source found.
- Firmware must handle: modem power-on sequencing and hard reset via the PWRKEY/RESET pin, PPP drop detection, automatic redial, stream reconnect with back-off, and a hardware watchdog. For an unattended device at an elderly user's home, "pull the plug and put it back" must always recover.
- A PSRAM-backed buffer of several seconds (ESP32-WROVER or S3 with PSRAM) is advisable for cellular jitter and cell handovers.
- Avoid HLS-only stations where possible; plain Icecast MP3/AAC streams are simpler and are what these libraries handle best.

### Gaps
- No stability, reconnect or long-run reports for ESP32 audio streaming over LTE were found. This is a real signal: the 4G route has no proven reference design in the hobby ecosystem.
- KaRadio32 and ESP32-MiniWebRadio were not individually checked for cellular support.

## 3. Data usage

### Takeaway
At 128 kbps a radio uses about 58 MB per hour, so 4/8/16 hours per day means roughly 7/14/28 GB per month; choosing 48-64 kbps AAC streams cuts that by half or more.

### Cited Findings
- NPO streams are served from icecast.omroep.nl with URLs of the form `http://icecast.omroep.nl/radio4-bb-aac` — [Roon community](https://community.roonlabs.com/t/dutch-public-radio-url/10194)
- A stream directory lists NPO Radio 1 at 32 kbps AAC, an NPO themed channel with MP3 192 kbps plus AAC 32 and 64 kbps variants, NPO Blend at 192 kbps MP3, and NPO Radio 5 as audio/mpeg — [radio.dubbeh.net NPO Radio 1](https://radio.dubbeh.net/stations/npo-radio-1-59), [NPO Soul & Jazz](https://radio.dubbeh.net/stations/npo-radio-2-soul-jazz-922), [NPO Blend](https://radio.dubbeh.net/stations/npo-blend-2230), [NPO Radio 5](https://radio.dubbeh.net/stations/npo-radio-5-127) (unofficial directory)

### Inferences
Calculated: MB/h = kbps x 3600 / 8 / 1000; month = 30 days; add about 3-5% for TCP/HTTP/PPP overhead.

| Stream bitrate | MB per hour | 4 h/day | 8 h/day | 16 h/day |
|---|---|---|---|---|
| 32 kbps AAC | 14.4 | 1.7 GB | 3.5 GB | 6.9 GB |
| 48 kbps AAC | 21.6 | 2.6 GB | 5.2 GB | 10.4 GB |
| 64 kbps AAC | 28.8 | 3.5 GB | 6.9 GB | 13.8 GB |
| 96 kbps AAC | 43.2 | 5.2 GB | 10.4 GB | 20.7 GB |
| 128 kbps MP3 | 57.6 | 6.9 GB | 13.8 GB | 27.6 GB |
| 192 kbps MP3 | 86.4 | 10.4 GB | 20.7 GB | 41.5 GB |

- Elderly users often leave a radio on all day, so the 8-16 h/day columns are the realistic design case. The firmware should prefer the lowest acceptable AAC variant and could auto-stop after N hours without a button press to cap data use.

### Gaps
- Actual current bitrates for Radio 10, Sky Radio, 100% NL and regional stations were not verified; the NPO figures come from an unofficial directory.

## 4. Recurring cost in NL/EU

### Takeaway
Realistic connectivity cost is roughly EUR 5-10 per month per radio (EUR 60-120 per year, EUR 300-600 over 5 years), which exceeds the hardware cost many times over; the cheapest figures are consumer SIM-only promotions that are tied to a person and a contract term.

### Cited Findings
- Simbase advertises a EUR 10 for 10 GB per month EU IoT plan with extra data at EUR 1 per GB and states no overage fees; pay-as-you-go Europe rate USD 0.005 per MB (= USD 5 per GB) — [Simbase EU plan](https://www.simbase.com/10gb-for-10/eu), [Simbase pricing](https://simbase.com/pricing?data=10000)
- 1NCE high-data option (EU price list, 2026): EUR 1.00 activation, EUR 0.50 per month, pay-per-use EUR 2.60/GB (zone 1), EUR 5.00/GB (zone 2), EUR 10.00/GB (zone 3); the classic 10-year flat is 500 MB for EUR 12 — [1NCE price list](https://a.storyblok.com/f/335000/x/23bb62a8c3/1nce_gmbh_price_list_01_2026.pdf), [1NCE pricing](https://www.1nce.com/en-eu/1nce-connect/pricing)
- emnify pricing is quote-based — [European Purpose directory](https://europeanpurpose.com/category/iot-connectivity-providers)
- Consumer SIM-only, regular price: Youfone 10 GB for EUR 8.50 per month (1-year contract); Simyo and Lyca Mobile 6 GB for EUR 7.50 and EUR 8.50 (overview October 2026) — [Keuze.nl](https://www.keuze.nl/sim-only)
- Consumer SIM-only, promotions: Youfone 10 GB at EUR 1.94 per month and 50+ Mobiel 5 GB at EUR 3.75 (10 November 2026, temporary); Lycamobile 10 GB EUR 4.50 and Simpel 10 GB EUR 5.00 per month on 2-year terms (July 2026) — [Androidworld](https://androidworld.nl/aanbiedingen/sim-only-overzicht/), [Androidplanet](https://www.androidplanet.nl/sim-only-aanbiedingen/)
- Consumentenbond comparison (May 2026): providers without their own network often cost under EUR 10 per month for 10 GB — [BNNVARA Kassa](https://www.bnnvara.nl/kassa/artikelen/goedkoop-mobiel-internet-budgetproviders-veel-voordeliger-dan-kpn-odido-en-vodafone)
- Lebara prepaid (KPN network) data bundles are valid 30 days and then stop automatically; listed prices (updated 26 July 2026): 500 MB EUR 5, 1 GB EUR 10, 20 GB EUR 30, 30 GB EUR 40, 50 GB EUR 50. The same table lists 3 GB at EUR 30, which looks inconsistent — [Selectra](https://selectra.nl/telecom/telecomaanbieder/lebara/prepaid)
- Lebara prepaid credit stays valid only if the SIM is used or topped up at least once per 90 days; otherwise services are blocked and the number lapses after a further 30 days — [Dundle](https://dundle.com/nl/lebara)
- Ubigi sells a Netherlands eSIM data plan of 10 GB for 30 days (travel eSIM type) — [Ubigi](https://cellulardata.ubigi.com/nl/rates-and-coverage/netherlands-esim-gegevensplan/nederland-10-gb-30-dagen/?wmc-currency=EUR)

### Inferences
- Cost scenarios (estimates built from the prices above):
  - 8 h/day at 64 kbps (about 7 GB): Simbase 10 GB plan EUR 10/month = EUR 120/year = EUR 600 per 5 years. Consumer SIM-only 10 GB at regular price EUR 8.50/month = EUR 102/year = EUR 510 per 5 years; at a held 2-year promo of EUR 4.50-5.00, about EUR 54-60/year.
  - 1NCE high data at 7 GB: EUR 0.50 + 7 x 2.60 = about EUR 18.70/month, more expensive than a bundle at this volume; 1NCE only wins for very light listening (under about 3 GB per month). Whether the Netherlands is in 1NCE zone 1 was not verified.
  - 16 h/day at 128 kbps (about 28 GB): Simbase 10 + 18 = about EUR 28/month; a consumer 30 GB or unlimited plan is the only sensible route.
- Who holds the subscription is the real business question. An IoT SIM (Simbase/1NCE) lets the seller hold all SIMs in one account, pool data, monitor usage and suspend remotely, but the seller then needs a monthly subscription fee from each customer plus billing and debt handling. A consumer SIM-only is cheaper but is a personal contract (ID, IBAN, 1-2 year term) and consumer terms normally assume use in a phone; the family would have to arrange it.
- Prepaid is a poor fit: bundles expire every 30 days and must be renewed by someone, and an unused SIM lapses. A radio that silently stops after 30 days is exactly the failure an elderly user cannot fix.
- IoT SIM providers typically also offer industrial and solderable MFF2 (and eSIM/eUICC) form factors; for 50 units a normal nano-SIM holder is simpler and allows a provider swap. Unverified per provider.

### Gaps
- www.simbase.com could not be fetched (outside the session's allowed domains), so the EUR 10 / 10 GB terms (minimum term, SIM cost, networks used in NL) are from the search snippet only.
- No pricing found for Onomondo, Things Mobile or Hologram; nothing found on KPN, Vodafone or Odido own-brand prepaid data SIMs or 50plus mobiel regular prices.
- Unlimited-data SIM pricing was not retrieved, nor fair-use/terms clauses on using consumer SIMs in non-phone devices.

## 5. Long-term stability of Dutch radio streams; remote update

### Takeaway
Stream URLs do change and break in practice (several user reports for Radio 10 and other Talpa stations), so a product with fixed presets needs a remotely updatable station list; no official NPO or Talpa stream policy was found.

### Cited Findings
- KPN community (early 2025): the Radio 10 stream on an internet radio played a different station than Radio 10 — [KPN community](https://community.kpn.com/internet-9/internetradio-hapert-628102?postid=2079828)
- Homey forum: Radio 10 stopped working for several days while other stations worked — [Homey community](https://community.homey.app/t/app-pro-onlineradio/88230?page=4)
- Volumio forum: Radio 10 and its themed channels do not work — [Volumio community](https://community.volumio.com/t/some-radio-links-dont-work/10321)
- In Apple's Music app/Siri, only themed variants of Radio 538, Sky Radio and Radio 10 play rather than the main channels — [iCulture](https://www.iculture.nl/nieuws/siri-muziek-geen-nederlandse-radiozenders/)
- A Roon user reported NPO URLs failing in Roon, with TuneIn URLs suggested as workaround (undated thread) — [Roon community](https://community.roonlabs.com/t/dutch-public-radio-url/10194)

### Inferences
- Design the firmware to fetch a small station list (JSON) from a server the seller controls at boot and daily, over the same cellular link, with the last good list cached in flash; this costs a few kB. Full firmware OTA over cellular is also feasible (1-2 MB per update) but adds to the RED cybersecurity obligations (signed updates).
- Commercial stations may insert pre-roll audio adverts on connect and may redirect through ad/analytics hosts; the HTTP client must follow redirects and HTTPS. Not verified per station this session.
- This is a structural advantage of DAB+: no URLs, no server, no account, nothing to maintain remotely.

### Gaps
- No official NPO stream policy, no statement on geo-blocking, and no confirmed current stream URLs for Radio 10, Sky Radio, 100% NL or regional stations were found.

## 6. Regulatory extras with a built-in cellular module

### Takeaway
A pre-certified module does not make the finished radio compliant; the maker must do a final-product RED assessment, and since 1 August 2025 that includes the cybersecurity requirements (EN 18031) for internet-connected radio equipment.

### Cited Findings
- Delegated Regulation (EU) 2022/30 activates RED Articles 3.3(d), (e), (f) and applies from 1 August 2025 — [SGS](https://www.sgs.com/en/news/2025/02/safeguards-02625-eu-harmonizes-en-18031-standards)
- EN 18031-1/-2/-3:2024 are the harmonised standards (Implementing Decision (EU) 2025/1385), harmonised with restrictions; where a restriction applies, a RED Notified Body is required — [SGS](https://www.sgs.com/en/news/2025/02/safeguards-02625-eu-harmonizes-en-18031-standards), [BSI](https://www.bsigroup.com/en-US/products-and-services/assessment-and-certification/product-testing-certification/radio-equipment-directive-cybersecurity-testing-for-radio-products/)
- If EN 18031 is applied in full with no restricted clauses, self-declaration under Module A is possible; otherwise Module B+C or H with a notified body — [Spanish government EN 18031 guide](https://digital.gob.es/content/dam/portal-mtdfp/avance-digital/telecomunicacion-e-infraestructuras-digitales/areas_interes/equipos-telecomunicacion/documents/Guia-aplicacion-EN-18031.pdf)
- A certified radio module does not make the product compliant: the requirements apply to the finished product, and most of the work is in firmware and the update process; module certificates are supporting evidence only — [CEL](https://www.cel.com/blog/red-article-3-3-compliance-guide-oems/)
- Cyber Resilience Act: reporting obligations from 11 September 2026, most other requirements from 11 December 2027 — [CEL](https://www.cel.com/blog/red-article-3-3-compliance-guide-oems/)

### Inferences
- A DAB+-only receiver (receive-only, no internet connection) falls outside the EN 18031 scope; a WiFi or 4G radio falls inside it. For a 50-unit series this paperwork/testing difference is a significant hidden cost of options (b) and (c). Scope reading is my interpretation, not confirmed by a source.
- Using a module with a CE/RED DoC and following its integration conditions (antenna gain, 20 cm separation distance) normally lets the maker rely on the module's radio test reports and handle RF exposure by a simple distance-based assessment rather than SAR measurement, since a table radio is not body-worn. Common practice, not verified this session.
- If an ESP32 with WiFi/BT is combined with a cellular module, the combination of co-located transmitters must be covered in the final-product assessment. Common practice, not verified.

### Gaps
- No source spelled out how a cellular module's certification maps onto the OEM's obligations, and no cost figure for EN 18031 testing or notified-body involvement was found.

## 7. Bluetooth

### Takeaway
Bluetooth Classic A2DP sink works only on the original ESP32 (WROOM/WROVER); the ESP32-S3 is BLE-only, so the choice of MCU decides whether Bluetooth is a free software add-on or needs a separate module costing a few euros.

### Cited Findings
- Espressif: ESP32-S3 supports Bluetooth LE only, not Classic Bluetooth or LE Audio; the original ESP32 is recommended for A2DP/AVRCP/HFP — [Espressif ESP-ADF docs](https://docs.espressif.com/projects/esp-adf/en/latest/solution-center/bluetooth-audio.html)
- pschatzmann ESP32-A2DP refuses to compile on unsupported platforms (error in BluetoothA2DPCommon.h, reported on an ESP32-S3 board) — [issue #745](https://github.com/pschatzmann/ESP32-A2DP/issues/745), [library](https://github.com/pschatzmann/ESP32-A2DP)
- The library maintainer: the S3 "is missing the relevant hardware support" — [arduino-audio-tools discussion](https://github.com/pschatzmann/arduino-audio-tools/discussions/1697); one GitHub issue claims the opposite without showing a working build — [issue #420](https://github.com/pschatzmann/ESP32-A2DP/issues/420)
- A Hackaday.io project combines internet radio with Bluetooth audio streaming on ESP32 — [Hackaday.io](https://hackaday.io/project/195189-internet-radio-with-bluetooth-audio-streaming)
- Dedicated module prices (wholesale listings, not AliExpress retail): BK3266 Bluetooth 5.0 module USD 3.30-4.40; generic Bluetooth 5.0 receiver boards from USD 0.52-0.65 up to about USD 6; a QCC3008-based BTM308 module USD 36.99 — [Alibaba](https://electronics.alibaba.com/product/stereo-bluetooth-audio-module), [eBay](https://ebay.com/itm/255005037978), [Newegg](https://www.newegg.com/p/2S7-07JP-0TMZ4)

### Inferences
- With an original ESP32 (e.g. the WROVER on the LilyGO T-A7670E), A2DP sink is a software feature at zero BOM cost. In a 4G design the ESP32's WiFi is unused, so the usual WiFi/Bluetooth coexistence problem (one shared 2.4 GHz radio, audio drop-outs when both are busy) does not arise: cellular data runs on the separate modem.
- In a WiFi design, running the stream and A2DP at the same time is the weak spot; the practical pattern is mode switching (radio or Bluetooth, not both), which also saves RAM. Based on general experience, no source found this session.
- A separate Jieli/BK3266-class module with analog or I2S output is the route if an ESP32-S3 is chosen; it then needs an audio mux or mixing into the amp and a mode line. Such modules usually announce themselves with loud Chinese/English voice prompts, which is undesirable for elderly users and often cannot be disabled.
- Usability: pairing should never be asked of the elderly user. Make Bluetooth a family feature: always-discoverable or enabled by a hidden/long-press button, fixed device name, volume still capped by the device's software limiter, automatic return to the last radio preset when the phone disconnects.
- Bluetooth adds a transmitter, so it brings the product under RED even if the base product is a receive-only DAB+ radio; without internet connectivity the EN 18031 burden should be lighter, but that needs checking.

### Gaps
- No prices found for MH-M18/MH-M28, CSR8645 or Jieli AC69xx finished modules; no source on WiFi/A2DP coexistence performance.

## 8. Existing products and DIY projects

### Takeaway
No commercial radio with a built-in SIM/4G for elderly or dementia care was found, and no documented DIY 4G internet radio either; the nearest commercial analogues are 4G desk phones for seniors.

### Cited Findings
- Search for a SIM-based internet radio for elderly/dementia users returned only senior phones and trackers, e.g. the Doro 4100H 4G desk phone with SIM — [MediaMarkt](https://www.mediamarkt.nl/nl/product/_doro-4100h-4g-bureautelefoon-met-simfunctie-zwart-seniorentelefoon-137447240.html)
- A KPN community answer to a no-WiFi radio question points to DAB+ models as the way to receive radio without internet — [KPN community](https://community.kpn.com/thuisnetwerk-72/wifi-483860)
- ESP32 + SIM7600 4G LTE hobby project exists as hardware bring-up, not as a radio — [Hackaday.io](https://hackaday.io/project/186843-esp32-sim7600-4g-lte)

### Inferences
- The absence of products suggests the recurring SIM cost and subscription administration make the concept unattractive when DAB+ covers the mainstream stations for free. The common workaround in practice is a WiFi radio behind a 4G MiFi router, which moves the same subscription problem into a second box.

### Gaps
- Absence of evidence only: two searches, Dutch and English. Dementia-specific radios (simple one-button music players) were not surveyed.

## 9. Bottom line comparison and FM/DAB+ context

### Takeaway
Hardware for a 4G radio is in the same range as the DAB+ design, but the 5-year cost is dominated by EUR 300-600 of data plus compliance and remote maintenance, so 4G only makes sense for users who need stations that are not on DAB+. FM is guaranteed in NL until at least 2035.

### Cited Findings
- Nine national commercial stations hold FM/DAB+ licences from 1 September 2023 through 2035; mandatory FM phase-out will not happen before 2035 — [Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2023/07/07/negen-commerciele-radiostations-gaan-na-veiling-tot-2035-landelijk-uitzenden)
- Ten parties won regional commercial FM+DAB licences from 1 September 2025 through 2035 — [Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2025/05/26/tien-partijen-verkrijgen-regionale-commerciele-radiovergunningen-bij-veiling)
- Listening share by platform, Audify monthly report July 2023 (NMO data): FM 35.4%, IP 25.4%, DAB+ 13%, cable 10.7% — [Audify/Broadcast Magazine](https://www.broadcastmagazine.nl/wp-content/uploads/2023/08/Audify-Audiomaandrapport-Juli2023.pdf)
- Older NLO figure (undated, pre-NMO): FM/cable 64%, internet 20%, DAB+ 8% — [Emerce](https://www.emerce.nl/?p=2311465)
- Flanders dropped its 2031 FM switch-off date; now 2035 at the earliest — [Belga](https://www.belganewsagency.eu/flemish-government-postpones-fm-radio-switch-off-dropping-2031-end-date)
- An Audify Audiojaarrapport 2025 and an NMO AudioMonitor 2026 exist but their platform split was not retrieved — [Audify 2025](https://www.voicebooking.com/app/uploads/Audify-Audiojaarrapport-2025.pdf)

### Inferences
All figures below are estimates, excluding cabinet, speaker, adapter, labour, and compliance testing. DAB+ hardware figure is the one given in the brief. USD list prices were read as roughly equal EUR amounts before VAT and import costs.

| Option | Prototype hardware | 50-unit series hardware | Recurring per year | 5-year total per unit | Main risk |
|---|---|---|---|---|---|
| (a) DAB+ Si4684 + MCU | EUR 40-60 | EUR 25-40 (brief) | EUR 0 | EUR 25-40 | Indoor DAB+ reception; station must be on DAB+ |
| (b) WiFi internet radio (ESP32 + I2S amp) | EUR 15-25 | EUR 10-20 | EUR 0 | EUR 10-20 | Target users have no WiFi; URL maintenance; EN 18031 |
| (c) 4G SIM radio (ESP32 + A7670E + SIM holder + antenna + modem PSU + I2S amp) | EUR 45-60 (LilyGO T-A7670E about USD 33 plus amp, antenna) | EUR 25-40 (module about USD 9.50 plus about EUR 15-25 rest) | EUR 60-120 | EUR 325-640 | Subscription administration; unproven software stack; EN 18031; URL maintenance |
| (d) Bluetooth add-on | EUR 0 (original ESP32) or EUR 1-5 (module) | same | EUR 0 | EUR 0-5 | Pairing usability; makes a receive-only DAB+ product a RED radio product |

- The 4G option costs roughly 10 to 20 times the DAB+ option over 5 years, almost entirely in data.
- A hybrid is possible (DAB+ as the base, Bluetooth as family add-on); it gives phone-sourced audio without any subscription and covers the "station not on DAB+" case when family visits.
- FM remains available until at least 2035, so an FM+DAB+ tuner chip (the Si4684 does both) keeps a fallback at no extra cost.

### Gaps
- No 2025/2026 Dutch platform-share figures (FM vs DAB+ vs online) were retrieved; the latest sourced split is July 2023. The trend claim "DAB+ growing in NL" is therefore unsourced here.
- The hardware estimates for (b), (c) and (d) are not backed by a priced BOM; only the modem module and dev-board prices are sourced.
- Hosts that must be allowed in the session's network settings for verification: www.simbase.com and www.elecrow.com.
