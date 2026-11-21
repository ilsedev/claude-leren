# Rules for selling converted vintage tube radios (DAB+ "senior radios") in NL/EU — state of law late 2026

> **Verification note (read first).** Informational research, not legal advice. The session's network blocked direct fetching of `eur-lex.europa.eu`, `belastingdienst.nl`, `stichting-open.org`, `via-la.com` (and probably other official sites). No primary legal text could be opened. Each finding is therefore tagged:
> - **[S]** = confirmed by web-search results in this session (secondary summaries or search snippets of the cited page).
> - **[K]** = stated from the researcher's own knowledge of the legal text; the URL points to where the official text lives but was NOT opened in this session. Article numbers and wording should be checked against the source before being relied on.
> Dates: today is 21 Nov 2026. Items marked **UPCOMING** change soon.

---

## 1. When is a converted second-hand radio a "new product" and the converter the "manufacturer"?

### Takeaway
A tube radio whose mains-powered valve chassis is replaced by a DAB+/ESP32/class-D design is, under every available test (Blue Guide 2022 §2.1, RED art. 14, GPSR art. 13), a new product and the converter is its manufacturer; the old radio was never CE-marked and its performance, purpose and type are all changed. The only real escape routes are (a) not acting commercially (genuinely occasional hobby supply) or (b) converting the customer's own radio for the customer's own use.

### Cited Findings
- [S] Blue Guide 2022 §2.1: a product counts as "new" when its original performance, purpose or type is modified without this being foreseen in the initial risk assessment, and the nature of the hazard has changed or the level of risk has increased; the person making the change then has the same duties as an original manufacturer (technical documentation, DoC, CE). Repairs that do not change performance/purpose/type do not create a new product. — [White & Case summary](https://www.whitecase.com/insight-alert/revised-eu-blue-guide-product-rules-zooms-e-commerce-modificationsrepairs-assembling); [getreadycompliance](https://getreadycompliance.eu/substantial-modification-ce-marking/); official text (not opened): [Blue Guide 2022/C 247/01](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52022XC0629(04))
- [K] Blue Guide 2022 §2.2 says "making available" requires a commercial activity, judged case by case (regularity of supplies, product characteristics, supplier's intentions), and that "in principle, occasional supplies by charities or hobbyists should not be considered as taking place in a business related context". — [Blue Guide 2022/C 247/01](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52022XC0629(04))
- [K] RED art. 14: an importer or distributor who places radio equipment on the market under his own name/trade mark, or modifies equipment already on the market in a way that may affect compliance, is considered a manufacturer with art. 10 obligations. — [Directive 2014/53/EU](https://eur-lex.europa.eu/eli/dir/2014/53/oj)
- [S] GPSR applies to products "whether new, used, repaired or reconditioned", and applies to products placed on the market from 13 Dec 2024. — [Regulation (EU) 2023/988](https://eur-lex.europa.eu/eli/reg/2023/988/oj) (search snippet); [Commission GPSR Q&A](https://webgate.ec.europa.eu/safety/consumers/consumers_safety_gate/obligationsForBusinesses/documents/Q&A.pdf)
- [S] GPSR art. 13(3): a physical or digital modification is substantial where it affects the safety of the product and (a) it was not foreseen in the initial risk assessment, (b) the nature of the hazard changed, a new hazard was created or the risk level increased, and (c) it was not made by the consumer for own use. The modifier is manufacturer for the modified part, or for the whole product if safety of the whole is affected. One source calls the criteria cumulative. — [EDANA GPSR guidelines](https://www.edana.org/hubfs/Docs/default-source/regulatory-affairs/edana_gpsr_guidelines_final_a3.pdf?hsLang=en); [Linklaters](https://www.linklaters.com/insights/blogs/productliabilitylinks/2024/december/changes-through-the-new-product-safety-regulation); [Baker McKenzie](https://www.bakermckenzie.com/en/insight/publications/resources/product-risk-radar-articles/general-product-safety-regulation)
- [K] The exact wording of art. 13(3)(c) is, to the researcher's recollection, "made by the consumers themselves **or on their behalf** for their own use" — which matters for the conversion-service framing (section 4). Not verified in session. — [Regulation (EU) 2023/988 art. 13](https://eur-lex.europa.eu/eli/reg/2023/988/oj)
- [K] GPSR art. 2(2)/(3): the regulation does not apply to antiques, nor to products "to be repaired or reconditioned prior to being used" when clearly marked as such. So an unconverted, non-working tube radio sold explicitly "for restoration / not for use" is outside GPSR; a converted, ready-to-use radio is not. — [Regulation (EU) 2023/988 art. 2](https://eur-lex.europa.eu/eli/reg/2023/988/oj)
- [K] GPSR art. 2(1): for products covered by harmonisation legislation (here RED), the GPSR is a safety net for risks not covered there; the manufacturer-duty section (Ch. III s. 1) does not apply for risks RED covers, but art. 19 (information in distance-sale offers) and art. 20 (accident reporting via Safety Business Gateway) remain relevant. — [Regulation (EU) 2023/988](https://eur-lex.europa.eu/eli/reg/2023/988/oj)
- [S] The Commission published GPSR guidelines for businesses (C/2025/6233, Nov 2025). — [C/2025/6233](https://eur-lex.europa.eu/eli/C/2025/6233/oj/eng); [Taylor Wessing](https://www.taylorwessing.com/de/insights-and-events/insights/2025/11/new-guidance-on-the-general-product-safety-regulation)

### Inferences
- Settled in practice: replacing the complete electronics is not "repair/refurbishment"; nothing of the original risk assessment (if one ever existed, pre-CE) survives. Treat each radio type as a new product you manufacture.
- Because RED is the specific harmonisation act, the manufacturer duties come from RED art. 10, not GPSR art. 9; GPSR adds the web-shop information duty and covers residual risks of the old cabinet (sharp edges, glass, chemical/asbestos residues, stability).
- "Type" can sensibly be defined as the electronics kit (PCB, modules, firmware, adapter, antenna) — one technical file and DoC for the kit, with a short per-cabinet annex. This is an interpretation, not something a source confirms.

### Gaps
- Exact wording of GPSR art. 13(3) and art. 2(3) not verified against EUR-Lex (blocked).
- No source found that discusses vintage-radio or "restomod" conversions specifically under RED/GPSR.
- Where the line lies between "occasional hobbyist supply" and commercial activity is undefined (no number of units or turnover in any source).

---

## 2. Which CE and environmental rules apply to an adapter-powered broadcast receiver?

### Takeaway
One CE regime dominates: the Radio Equipment Directive (it replaces LVD and EMC Directive for any receiver), plus RoHS and ecodesign standby limits under the same CE mark; WEEE registration has no small-producer exemption. Leaving WiFi/Bluetooth disabled removes the cybersecurity delegated act, EN 300 328, RF-exposure and (from Dec 2027) most Cyber Resilience Act exposure; leaving out batteries removes the Batteries Regulation.

### Cited Findings
**RED scope and essential requirements**
- [K] RED art. 2(1)(1) covers equipment that intentionally emits *and/or receives* radio waves, so a receive-only DAB+/FM radio is radio equipment. Art. 1(4): LVD does not apply to it; safety is covered through art. 3(1)(a), which imports LVD safety objectives "with no voltage limit applying" — so a 5 V/12 V device still needs a safety assessment. Art. 3(1)(b) EMC; art. 3(2) efficient spectrum use (for receivers: receiver performance). — [Directive 2014/53/EU](https://eur-lex.europa.eu/eli/dir/2014/53/oj); [Commission RED page](https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en)
- [S] RDI supervises these rules in NL under the Telecommunicatiewet (art. 15.1), covering both technical requirements and administrative ones (documentation, CE marking). — [OM Aanwijzing handhaving Telecommunicatiewet](https://www.om.nl/onderwerpen/b/beleidsregels/aanwijzingen/specialistisch/aanwijzing-handhaving-telecommunicatiewet-2024a004)

**Cybersecurity (only if WiFi/Bluetooth is enabled)**
- [S] Delegated Regulation (EU) 2022/30 (RED art. 3(3)(d)(e)(f)) applies to products placed on the market from 1 Aug 2025; EN 18031-1/-2/-3:2024 were cited as harmonised standards by Implementing Decision (EU) 2025/138 with restrictions. — [SGS](https://www.sgs.com/en/news/2025/02/safeguards-02625-eu-harmonizes-en-18031-standards); [Impl. Decision 2025/138](https://eur-lex.europa.eu/eli/dec_impl/2025/138/oj/eng)
- [S] Espressif's own guide: responsibility for RED-DA compliance lies with the manufacturer of the final product; a certified module alone is not sufficient; the end product must be evaluated as a whole against EN 18031. — [Espressif RED-DA guide](https://developer.espressif.com/blog/2025/04/esp32-red-da-en18031-compliance-guide/)
- [K] Art. 3(3)(d) applies to "internet-connected radio equipment" (able to communicate over the internet directly or via other equipment); (e) additionally when personal data are processed. A radio that only receives DAB+/FM and has the ESP32 radios disabled in firmware is not internet-connected. The restrictions on EN 18031 mean that if the device lets the user run without a password, presumption of conformity is lost and a notified body is needed. — [Delegated Regulation (EU) 2022/30](https://eur-lex.europa.eu/eli/reg_del/2022/30/oj)
- [S] NL government page announcing stricter security rules for smart devices. — [Ondernemersplein](https://ondernemersplein.overheid.nl/wetswijzigingen/slimme-apparaten-moeten-veiliger/)
- [K] **UPCOMING** Cyber Resilience Act (EU) 2024/2847: vulnerability/incident reporting duties from 11 Sep 2026, full application 11 Dec 2027 for "products with digital elements" with a data connection; it will replace the RED delegated act. — [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)

**RoHS**
- [K] RoHS 2011/65/EU art. 4(1) + Annex II limit Pb, Hg, Cr(VI), PBB, PBDE and four phthalates to 0.1 % and Cd to 0.01 % per homogeneous material in EEE placed on the market; art. 7 requires the manufacturer's technical documentation, DoC and CE marking (EN IEC 63000). The spare-part exemptions of art. 4(4)/(5) are for repairing old equipment, not for building a new product. — [Directive 2011/65/EU](https://eur-lex.europa.eu/eli/dir/2011/65/oj)

**WEEE / batteries / packaging (NL)**
- [S] Once registered with Stichting OPEN (portal myOPEN) a producer is entered in the Nationaal (W)EEE Register and reports yearly the appliances placed on the market; fees are set annually and include a fixed contribution per producer plus product tariffs; "anyone who puts devices, lamps and batteries on the market" is covered, including web sellers. — [Stichting OPEN](https://stichting-open.org/en); [fee page](https://www.stichting-open.org/en/producers-importers/waste-management-fee-why-and-how-much); [Ondernemersplein EEA rules](https://ondernemersplein.overheid.nl/wetten-en-regels/regels-voor-elektrische-en-elektronische-apparatuur/)
- [S] The generally-binding declaration (AVV) for e-waste was granted to Stichting OPEN for 2026–2031; 2026 tariff list published 23 Oct 2025 (e.g. mobile phones €0.096/kg). — [Stichting OPEN tariff list 2026](https://www.stichting-open.org/wp-content/uploads/2025/10/23-10-2025-Tarieven-EEA-2026-NL.pdf); [Staatscourant 2026, 77](https://zoek.officielebekendmakingen.nl/stcrt-2026-77.pdf)
- [K] WEEE Directive 2012/19/EU has no de minimis threshold; product must carry the crossed-out wheelie-bin symbol (art. 14(4), EN 50419). — [Directive 2012/19/EU](https://eur-lex.europa.eu/eli/dir/2012/19/oj)
- [K] Batteries Regulation (EU) 2023/1542 applies only if a battery is supplied (even an RTC coin cell): producer registration, and from 18 Feb 2027 user-removability (art. 11). — [Regulation (EU) 2023/1542](https://eur-lex.europa.eu/eli/reg/2023/1542/oj)
- [S] Packaging: a 50,000 kg/year threshold still exempts small firms from Verpact's fee; from 12 Aug 2026 Verpact uses the PPWR producer definition; the threshold disappears when the PPWR producer register opens (Verpact expects 2029; other sources say 2027/2028). Below threshold "nothing to do for now" but be able to show it. — [Verpact PPWR micro-enterprises](https://www.verpact.nl/sites/default/files/2026-09/vrp_ppwr_micro_ondernemingen_03.pdf); [Ondernemersplein](https://ondernemersplein.overheid.nl/wetten-en-regels/afvalbeheersbijdrage-verpakkingen-betalen/); [KVK PPWR](https://www.kvk.nl/wetten-en-regels/ppwr-dit-betekent-de-europese-verpakkingswet-voor-je-bedrijf/)

**Ecodesign standby**
- [S] Regulation (EU) 2023/826 applies from 9 May 2025 (repealing 1275/2008): off mode ≤0.5 W (0.3 W from 2027), standby ≤0.5 W, standby with information/status display ≤0.8 W; networked standby 2 W for non-HiNA equipment (secondary sources quote 2–8 W by product type). The Commission says the regulation also covers products using a low-voltage external power supply. — [Commission product page](https://energy-efficient-products.ec.europa.eu/product-list/standby-networked-standby-and-mode_en); [UL](https://www.ul.com/news/eu-regulation-2023826-new-energy-efficiency-requirements); [business.gov.nl](https://business.gov.nl/amendments/stricter-requirements-standby-energy-consumption-applicances/); [Regulation (EU) 2023/826](https://eur-lex.europa.eu/eli/reg/2023/826/oj/eng)
- [K] The adapter itself falls under the external-power-supply ecodesign regulation (EU) 2019/1782, which is the adapter manufacturer's responsibility. — [Regulation (EU) 2019/1782](https://eur-lex.europa.eu/eli/reg/2019/1782/oj)

**Common charger / DAB+ mandate**
- [K] Common-charger rules (Directive (EU) 2022/2380, RED art. 3(4) + Annex Ia) cover listed categories of *rechargeable* radio equipment (phones, tablets, cameras, headphones, portable speakers, e-readers, etc.; laptops from 28 Apr 2026). A mains-adapter radio without rechargeable battery is not listed. — [Directive (EU) 2022/2380](https://eur-lex.europa.eu/eli/dir/2022/2380/oj)
- [K] EECC (Directive (EU) 2018/1972) art. 113 + Annex XI obliges digital-radio capability only for car radios in new M-category vehicles; Member States *may* extend to other consumer receivers. — [Directive (EU) 2018/1972](https://eur-lex.europa.eu/eli/dir/2018/1972/oj)

### Inferences
- Design effect: no mains inside → safety assessment reduces to low-voltage hazards (fire from fault currents, heat, mechanical); bought adapter → mains-side safety/EMC/ecodesign evidence is the adapter maker's, provided you buy from an EU-based supplier and keep its DoC. If you import adapters yourself from outside the EU you become their importer with importer duties.
- Supplying the adapter in the box makes it part of what you place on the market; choose a branded one with a traceable EU manufacturer/importer and file its DoC and test reports.
- Keeping old electrical parts (leaded-solder wiring, cadmium-plated chassis, old speaker, dial lamps) inside a "new" product is the main RoHS weak spot. Legally cleanest: retain only non-electrical cabinet parts (wood, glass dial, knobs, grille cloth) and new RoHS-compliant electronics. Whether the antique cabinet parts themselves must meet RoHS limits is genuinely ambiguous (RoHS applies to the whole EEE, but no source addresses antique enclosures).
- Standby: an always-powered ESP32 + DAB module + amplifier must be designed to ≤0.5 W in standby/off (≤0.8 W with clock display); a hard on/off switch that cuts the supply is the simplest route, but the adapter's no-load draw is then the adapter maker's matter.
- With WiFi/BT off: no RED art. 3(3) cyber, no EN 300 328, no EN 62311 exposure assessment; "networked standby" limits irrelevant.

### Gaps
- Stichting OPEN's actual fixed annual contribution and per-unit/kg tariff for a radio, and whether a reduced small-producer rate exists: not found (site blocked; search snippets silent).
- No source found for any Dutch DAB+ requirement for non-automotive consumer radios; I found no evidence one exists, but could not confirm from the Telecommunicatiewet.
- Networked-standby limit applicable to a WiFi-enabled radio (2 W vs higher) is inconsistent across secondary sources; check Annex of 2023/826.
- Which Dutch authority enforces ecodesign/RoHS/WEEE for this product (ILT vs NVWA) not confirmed in session.

---

## 3. What does RED self-declaration involve for a micro-producer?

### Takeaway
Self-declaration (Module A, no notified body) is legally available, but it means the maker personally holds a technical file with a risk assessment and test evidence for the *finished* radio; pre-certified modules shorten the radio-spectrum part but do not remove EMC and safety evidence for the assembled product. Realistic lab cost for a type test is roughly €1,500–4,000; a receive-only design sits at the low end.

### Cited Findings
- [K] Conformity assessment (RED art. 17): for art. 3(1)(a)/(b) the manufacturer may always use internal production control (Annex II, Module A). For art. 3(2) and 3(3) Module A is allowed only if harmonised standards cited in the OJ are applied in full; otherwise a notified body (Annex III/IV) is required. — [Directive 2014/53/EU art. 17](https://eur-lex.europa.eu/eli/dir/2014/53/oj)
- [K] Manufacturer duties (RED art. 10): technical documentation per art. 21/Annex V (description, schematics, standards applied, risk analysis, test reports), kept 10 years; type/batch/serial number; name, trade name and postal address on the equipment (or packaging/document if too small); instructions and safety information in a language determined by the Member State (Dutch in NL); a copy of the EU DoC or the simplified DoC (Annex VII) with a web address with every unit; CE marking on the product and on the packaging (art. 19–20). — [Directive 2014/53/EU](https://eur-lex.europa.eu/eli/dir/2014/53/oj)
- [S] Dutch government guidance: the manufacturer must draw up and sign an EU declaration of conformity, declaring the product meets EU requirements and that he is responsible. — [Ondernemersplein](https://ondernemersplein.overheid.nl/wetswijzigingen/slimme-apparaten-moeten-veiliger/)
- [S] Belgian regulator (same directive): technical documentation and DoC must be kept 10 years after placing on the market. — [BIPT](https://www.bipt.be/index.php/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/f711f28ac3393a80a2af4d97b4ac4fa220d30d97/ctr-equp-doc-2019-07-02-nl.pdf)
- [K] Relevant standards: ETSI EN 303 345-1 (+ -3 FM, -4 DAB) for broadcast sound receivers under art. 3(2); EN 55032 (emissions) / EN 55035 (immunity) for multimedia equipment and ETSI EN 301 489-1/-17 for EMC of equipment with WiFi/BT; ETSI EN 300 328 for 2.4 GHz transmitters; EN 62368-1 for safety; EN 62311/EN 62479 for RF exposure of transmitters; EN 18031-1/-2 for cyber. Which editions are currently cited in the OJ under RED was not checked. — [Commission RED harmonised standards](https://single-market-economy.ec.europa.eu/single-market/european-standards/harmonised-standards/radio-equipment_en)
- [K] The Commission's RED Guide treats a product that incorporates a radio module as radio equipment as a whole; the integrator is the manufacturer and must assess the combination (ETSI EG 203 367 gives the method for combined equipment). — [RED Guide (Commission docsroom 33162)](https://ec.europa.eu/docsroom/documents/33162/attachments/1/translations/en/renditions/pdf)
- [S] "A collection of component test reports can therefore not substitute a product-specific lab test report." — [Compliance Gate](https://compliancegate.com/electronic-product-lab-testing-european-union)
- [S] Cost indications: wireless (RED) products about $1,500–3,000+ or €1,500–4,000; multi-radio devices $2,000–4,000 testing alone; simple self-certified electronics $400–1,500; no fee for the CE mark itself. — [Compliance Gate cost](https://www.compliancegate.com/ce-marking-cost/); [ecocomply](https://ecocomply.ai/blog/what-does-ce-marking-cost-for-your-product); [getreadycompliance](https://getreadycompliance.eu/ce-marking-cost/)
- [S] RDI has a published fine policy (2025) with category-based fines and a turnover-related component; for natural persons a 5 % factor applies to the calculated amount. — [RDI boetebeleid](https://rdi.nl/binaries/rdi/documenten/besluiten/2025/01/30/boetebeleid/RDI+boetebeleid.pdf)

### Inferences
- What pre-certified modules buy you: if the ESP32 module and the DAB module each have their own RED DoC and test reports and are used exactly as the module maker specifies (same antenna type, supply, layout notes), their art. 3(2) radio reports can be referenced in your file instead of repeating those tests. What they do not buy: radiated/conducted emissions and immunity of your whole assembly (class-D amplifier and wiring harness in a wooden, unshielded cabinet are typical emission sources), receiver performance with your antenna, and safety of your construction.
- Proportionate route for a micro-producer: (1) freeze one electronics design; (2) write the risk assessment and a clause-by-clause safety rationale (extra-low voltage from a certified adapter, input fuse/PTC, current-limited rails, temperature check, no accessible hot parts, strain relief, flammability of materials near electronics); (3) buy a pre-compliance EMC scan of the finished radio at a lab and fix findings; (4) decide whether to pay for a formal EN 55032/55035 (and EN 303 345) report — strongly advisable before selling in any volume; (5) file module and adapter DoCs/reports; (6) issue DoC, label, Dutch manual. Legally the DoC signature asserts conformity whether or not a lab was used; without measurements the risk assessment has little evidential value in an inspection or liability case.
- Label content: brand/trade name, type designation, serial number, postal address, CE mark, WEEE bin symbol, rated input (e.g. 5 V ⎓ 2 A), plus e-mail/web address for GPSR purposes. Manual in Dutch with safety instructions (use only the supplied adapter, indoor use, ventilation, cleaning, disposal).
- Enforcement practice appears to be risk- and complaint-driven; I found no published RDI or NVWA cases against one-person makers, so "low probability, real consequence" is an inference rather than a documented pattern. The practical trigger is usually an interference complaint, an incident, a competitor report, or marketplace checks.

### Gaps
- No Dutch source found on how RDI treats very small series or one-offs; no exemption exists in the directive, and none was found in search results.
- Hourly/pre-compliance lab rates in NL not sourced.
- Whether common hobby DAB+ modules (e.g. Si468x-based boards) ship with a usable RED DoC and EN 303 345 report is unknown and must be checked per supplier — this largely determines test cost.
- Accepted language of the DoC in NL (Dutch vs English) not confirmed.

---

## 4. Does framing as "second-hand/vintage, modified", "DIY kit" or "conversion service" change obligations?

### Takeaway
Labelling the product "second-hand, modified" changes consumer expectations but not CE duties. A DIY kit is still radio equipment placed on the market by the kit seller. A conversion service on the customer's own radio is the framing with the most legal effect, but its limits are untested.

### Cited Findings
- [S] If a modified product is "new", the modifier carries the full manufacturer duties regardless of the base product's age. — [White & Case on Blue Guide 2022](https://www.whitecase.com/insight-alert/revised-eu-blue-guide-product-rules-zooms-e-commerce-modificationsrepairs-assembling)
- [S] GPSR art. 13(3) excludes modifications made by the consumer for own use from "substantial modification". — [EDANA GPSR guidelines](https://www.edana.org/hubfs/Docs/default-source/regulatory-affairs/edana_gpsr_guidelines_final_a3.pdf?hsLang=en)
- [K] RED Annex I exempts only kits "for assembly and use by radio amateurs" and custom evaluation kits for R&D professionals; there is no general consumer-kit exemption. — [Directive 2014/53/EU Annex I](https://eur-lex.europa.eu/eli/dir/2014/53/oj)
- [K] BW 6:230p contains exceptions to the 14-day withdrawal right, including goods made to the consumer's specifications and services fully performed with prior express consent. — [BW Boek 6, afd. 6.5.2B](https://wetten.overheid.nl/BWBR0005289/)

### Inferences
| Framing | Pros | Cons / what stays |
|---|---|---|
| Finished radio, sold honestly as "new electronics in original vintage cabinet" | Clear; one type file; matches reality | Full manufacturer duties (RED, RoHS, WEEE, ecodesign), full consumer rights |
| "Second-hand / vintage, modified" | Lowers expectations on cosmetic condition (BW 7:17); may support margin scheme argument (weak, see s. 7) | No effect on CE status; if used to suggest "no CE needed" it is misleading |
| DIY kit | Buyer assembling for own use is not a manufacturer | Kit seller still needs CE/RED file for the kit as intended to be assembled; unsuitable for the senior target group; WEEE still applies |
| Conversion service on customer's own radio | No sale of a finished product; old cabinet (asbestos/RoHS/trade mark issues) remains the customer's property; possible GPSR 13(3)(c) carve-out; withdrawal-right exceptions may apply; no margin-scheme question (service at 21 % VAT) | The electronics set you supply and install is arguably still radio equipment made available (needs its own RED compliance); you owe a duty of care for the work (BW 6:74/7:750 ff.) and product liability for parts you supply; if you routinely source the cabinet for the customer it is a disguised sale |
| Occasional hobby sale (not a business) | Blue Guide: occasional hobbyist supplies are "in principle" not commercial | Fragile: advertising, repeat sales or a web shop make it commercial; civil liability (BW 6:162) remains in any case |

### Gaps
- No authority or case found on whether fitting a self-built radio assembly into a customer-owned cabinet counts as "placing on the market" under RED. This is the central ambiguity; a written question to RDI would be the proportionate way to settle it.

---

## 5. Consumer law, product liability, insurance

### Takeaway
Selling to consumers as a business brings the full conformity regime (no fixed term, one-year reversed burden of proof), 14-day withdrawal for distance sales and strict product liability as "producer"; the new Product Liability Directive applies to products placed on the market after 9 Dec 2026 and expressly treats substantial modifiers as manufacturers. Liability insurance is cheap relative to the exposure, but product liability for self-made electronics must be explicitly included.

### Cited Findings
- [K] BW 7:17 (goods must conform; expectations depend on the nature of the item and seller's statements); BW 7:18 lid 2: defects appearing within one year of delivery are presumed present at delivery (extended from six months on 27 Apr 2022, implementing Directive (EU) 2019/771); BW 7:18 also contains update duties for goods with digital elements (relevant to ESP32 firmware); BW 7:21–7:22 remedies (repair/replacement, then price reduction/rescission); BW 7:23 complaint within reasonable time, two months always timely; BW 7:6 mandatory in consumer sales. — [BW Boek 7](https://wetten.overheid.nl/BWBR0005290/); [ConsuWijzer garantie](https://www.consuwijzer.nl/garantie)
- [K] Distance selling: information duties BW 6:230m; 14-day withdrawal BW 6:230o; refund incl. standard delivery costs within 14 days BW 6:230r; exceptions BW 6:230p. — [BW Boek 6](https://wetten.overheid.nl/BWBR0005289/)
- [K] Product liability now: BW 6:185–6:193 (producer strictly liable for damage by a defective product; property damage only to private goods above a €500 franchise; 3-year limitation, 10-year long-stop; anyone presenting himself as producer by name/mark counts as producer). — [BW Boek 6, afd. 6.3.3](https://wetten.overheid.nl/BWBR0005289/)
- [S] New PLD (EU) 2024/2853 entered into force 8 Dec 2024, transposition deadline 9 Dec 2026; NL implements via bill 36 906 amending BW Books 6 and 7 (explanatory memorandum Feb 2026; Eerste Kamer documents through Sept 2026); NL keeps the development-risk defence and implements minimally. — [Eerste Kamer 36 906](https://www.eerstekamer.nl/nonav/wetsvoorstel/36906_implementatiewet_richtlijn); [CMS](https://cms.law/en/nld/legal-updates/transposition-time-netherlands-finland-and-sweden-update-on-the-eu-member-states-adoption-of-the-new-product-liability-directive); [HLC](https://www.hlc.com/en/publications/implementing-the-new-eu-product-liability-directive-in-the-netherlands)
- [K] PLD 2024/2853: applies to products placed on the market after 9 Dec 2026 (art. 2); a person who substantially modifies a product outside the original manufacturer's control and then makes it available is treated as manufacturer (art. 8(2)); the €500 threshold disappears; software and data loss are covered; courts can order evidence disclosure and presume defect when mandatory safety rules were not met (arts. 9–10). — [Directive (EU) 2024/2853](https://eur-lex.europa.eu/eli/dir/2024/2853/oj)
- [S] AVB (business liability) is not legally mandatory; example premiums from about €8/month for web-shop owners and small retail (insured sum typically €2.5 million per claim); product damage is covered only "mits meeverzekerd". — [mijnzzp.nl](https://www.mijnzzp.nl/Beroep/1295-Webshophouder/Bedrijfsaansprakelijkheidsverzekering); [ondernemenmetpersoneel.nl](https://ondernemenmetpersoneel.nl/mijn-branche/detailhandel/bedrijfsaansprakelijkheid-de-detailhandel); [overstappen.nl](https://www.overstappen.nl/verzekeringen/zakelijk/aansprakelijkheidsverzekering/); [Ondernemersplein](https://ondernemersplein.overheid.nl/bedrijfsvoering/verzekeringen/verzekering-bedrijfsaansprakelijkheid/)
- [K] **UPCOMING/RECENT**: Directive (EU) 2023/2673 (online withdrawal function, from 19 Jun 2026) and Directive (EU) 2024/825 (ban on vague environmental claims, harmonised guarantee notice, from 27 Sep 2026) affect web-shop design and "sustainable/upcycled" claims. Dutch transposition status not checked. — [Directive (EU) 2023/2673](https://eur-lex.europa.eu/eli/dir/2023/2673/oj); [Directive (EU) 2024/825](https://eur-lex.europa.eu/eli/dir/2024/825/oj)

### Inferences
- The converted radio is new electronics, so a buyer may expect a normal lifespan for the electronics (several years); "second-hand" only tempers expectations for the cabinet. State this split explicitly in the listing.
- Under the new PLD, missing CE documentation becomes directly relevant in civil claims (presumption of defectiveness when safety requirements are not shown to be met), which raises the value of a real technical file.
- Premiums for a self-declared electronics *manufacturer* are likely higher than the €8/month retail examples and some insurers exclude products without demonstrable CE conformity; a quote naming the activity honestly is needed (inference, no source).

### Gaps
- Whether bill 36 906 has been enacted and in force by 9 Dec 2026: not confirmed.
- No premium quote for "small-series electronics manufacturer" found.
- Article/paragraph numbers within BW 7:18 for digital-element updates not verified.

---

## 6. Marketing claims and the medical-device boundary (MDR 2017/745)

### Takeaway
Qualification depends on the manufacturer's stated intended purpose. A radio sold as easy to operate for older people is a consumer product; one advertised as treating, alleviating or monitoring dementia symptoms risks being a class I medical device with its own regime.

### Cited Findings
- [S] A product can be a medical device if the manufacturer states a medical purpose; check manual and promotional claims. — [VU MDR stappenplan](https://assets.vu.nl/d8b6f1f5-816c-005b-1dc1-e363dd7ce9a5/1b7e6560-1ffc-40a8-bf91-44ff59919776/Be%CC%80ta%20MDR%20Stappenplan%20NL.pdf)
- [S] Intended use by the manufacturer is decisive; the same function (e.g. heart-rate tracking) is or is not a medical device depending on the claimed use. — [Hogeschool Leiden MDR document](https://www.hsleiden.nl/binaries/content/assets/hsl/lectoraten/eigen-regie/2023-medical-device-regulations-erfb-f-lotters-vs3.pdf)
- [S] VWS/IGJ acknowledge that the boundary between consumer product and medical device is hard to draw for consumer-friendly products. — [Kamerstuk bijlage blg-881608](https://zoek.officielebekendmakingen.nl/blg-881608.pdf)
- [K] MDR art. 2(1): medical purposes include "diagnosis, prevention, monitoring, prediction, prognosis, treatment or alleviation of disease" and "alleviation of, or compensation for, an injury or disability"; art. 2(12): intended purpose is taken from label, instructions, promotional or sales materials. — [Regulation (EU) 2017/745](https://eur-lex.europa.eu/eli/reg/2017/745/oj)

### Inferences
- Safe wording: "eenvoudige radio met één knop", "vertrouwd uiterlijk", "geschikt voor ouderen / mensen die moderne apparaten lastig vinden". Risky wording: "vermindert onrust bij dementie", "therapeutisch", "muziektherapie", "hulpmiddel bij dementie", "bewezen effect op geheugen". "Compensation for a disability" is the grey zone: describing ease of use is fine; presenting the radio as an aid that compensates cognitive impairment moves toward MDR.
- Health-effect claims without evidence are also a consumer-law problem (misleading commercial practice), independent of MDR.

### Gaps
- No IGJ or MDCG borderline decision on dementia radios/music players found; commercial "dementia radios" exist on the market but their regulatory status was not researched.

---

## 7. Business basics: KVK, VAT margin scheme, KOR

### Takeaway
There is no turnover threshold for KVK registration — it turns on acting as an entrepreneur; the KOR removes VAT up to €20,000 turnover; the margin scheme very probably does not apply to a radio rebuilt with all-new electronics.

### Cited Findings
- [S] KVK registration is required if three entrepreneur criteria are met; there is no general amount below which an activity automatically stays a hobby, and what you call it is irrelevant; borderline cases can register by answering four extra questions. KVK and Belastingdienst apply different tests. — [KVK](https://kvk.nl/starten/moet-ik-mijn-bedrijf-inschrijven-bij-kvk/); [Ondernemersplein](https://ondernemersplein.overheid.nl/wanneer-bent-u-ondernemer/)
- [S] KOR: available if turnover excl. VAT is at most €20,000 in the calendar year and the previous one; a separate €2,200 turnover figure applies for those who cannot register at KVK; income can still be taxed as "overig werk" without KVK registration. — [KVK KOR](https://www.kvk.nl/starten/starter-zo-werkt-de-kleineondernemersregeling-kor/); [KVK](https://kvk.nl/geldzaken/kleineondernemersregeling-gebruiken/)
- [S] Margin scheme (Wet OB art. 28b ff.): VAT on the margin instead of turnover for used goods bought without VAT; refurbishment costs may not be deducted from the margin. A 2007 policy letter states that when a reseller manufactures a new good out of used goods, the scheme does not apply. — [Belastingdienst margeregeling](https://belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/bijzondere_regelingen/margeregeling); [Staatscourant 2007, 133](https://zoek.officielebekendmakingen.nl/stcrt-2007-133-p18-SC81270.pdf); [Ondernemersplein](https://ondernemersplein.overheid.nl/margeregeling-voor-de-btw)

### Inferences
- A cabinet bought from a private person and fitted with completely new electronics is most likely a "newly manufactured good" for VAT → 21 % on the full price, input VAT on parts deductible. This also mirrors the product-law conclusion; arguing "used good" for VAT and "new product" for CE would be inconsistent. Under the KOR the question is moot.
- KOR participants charge no VAT and deduct none; with material-heavy builds and low volume this is usually the simplest.

### Gaps
- Current Belastingdienst wording on "new good from used goods" not verified (site blocked; 2007 source only).
- The three KVK criteria were not retrieved verbatim.

---

## 8. Hazards of old cabinets relevant to liability

### Takeaway
The legal exposure from the old cabinet is mostly about prohibited substances (asbestos, PCBs) and residual fire load; removing all old electrical parts and documenting inspection and cleaning per unit is the proportionate control.

### Cited Findings
- [S] Hobbyist reports describe asbestos sheets (about 20 × 20 cm, near the mains transformer) in old Philips valve equipment; paper-in-oil capacitors may contain PCBs (forum opinion divided); tar-sealed capacitors commonly leak; valve sets carry up to 300 V DC and AC/DC sets may have a live chassis. These are forum sources, not authoritative. — [Circuits Online forum](https://www.circuitsonline.net/forum/view/170290); [Circuits Online forum](https://www.circuitsonline.net/forum/view/123554/2); [radiomuseum.org caveat](https://radiomuseum.org/forum/a_caveat_for_younger_members.html)
- [K] Placing articles containing asbestos on the market is prohibited (REACH Annex XVII entry 6; in NL additionally national asbestos product rules); PCBs are prohibited under the POPs Regulation (EU) 2019/1021 and are hazardous waste. — [REACH Regulation (EC) 1907/2006](https://eur-lex.europa.eu/eli/reg/2006/1907/oj); [Regulation (EU) 2019/1021](https://eur-lex.europa.eu/eli/reg/2019/1021/oj); [Rijksoverheid asbest](https://www.rijksoverheid.nl/onderwerpen/asbest)

### Inferences
- Per-unit checklist worth keeping in the file: photos before/after; all original electrical parts removed (transformer, capacitors, wiring, valves, selenium rectifier, dial lamps) and disposed of as e-waste/hazardous waste; inspection for heat-shield boards — if suspected asbestos, do not process the cabinet yourself and do not sell it; cabinet vacuumed/cleaned; flaking old paint sealed or removed (possible lead); new electronics mounted on non-combustible or flame-retardant carrier with clearance from wood and cloth; input fuse; temperature check after one hour at full volume.
- Do not reuse the original mains cord, mains switch or voltage selector even as decoration connected to anything; dummy controls must be electrically dead.
- Selling a cabinet that still contains asbestos is the one hazard that is flatly unlawful rather than a matter of risk assessment.

### Gaps
- No authoritative list of which radio models/years contain asbestos or PCB capacitors was found; identification is per unit.
- Dutch national asbestos product rules were not opened; exact provision not cited.

---

## 9. Licences and IP: HE-AAC/DAB+ patents, brand names

### Takeaway
Via LA's position is that the maker of the end-user product needs the AAC licence and that buying a component does not confer it; for a micro-producer this is a real but commercially small and rarely enforced exposure. Keeping a "Philips" badge on a radio with replaced internals is the riskiest trade-mark configuration; referential, clearly disclaimed use is far safer.

### Cited Findings
- [S] Via LA AAC programme: a licence is needed by manufacturers/developers of end-user encoder/decoder products; components or implementations that are not end-user products are not covered, so the party incorporating a component must obtain a licence; standard rate $0.98 per unit for the first 500,000 units per year. — [Via LA AAC](https://www.via-la.com/licensing-2/aac/); [Via LA AAC fees](https://www.via-la.com/aac-license-fees-structures/)
- [S] Trade-mark exhaustion is not absolute: the proprietor may oppose further commercialisation for "legitimate reasons", notably where the condition of the goods has been changed or impaired; mere refurbishment is generally not enough, but serious damage to reputation or an impression of a commercial link is; academic comment calls refurbishing trade "a risky business" with "a thin and blurry line". — [Osborne Clarke](https://www.osborneclarke.com/insights/how-can-sustainability-and-ip-rightsholders-interests-be-reconciled-second-hand-goods); [Tilburg University paper](https://research.tilburguniversity.edu/en/publications/trading-repaired-and-refurbished-goods-how-sustainable-is-eu-exha/); [GRUR Int. article](https://academic.oup.com/grurint/article/73/4/287/7490836)
- [K] Legal basis: EUTMR (EU) 2017/1001 art. 15 (exhaustion and legitimate reasons) and art. 14(1)(c) (referential use in accordance with honest practices); Benelux Convention (BVIE) art. 2.23. CJEU: BMW/Deenik C-63/97 (reseller/repairer may use the mark to inform, unless it suggests a commercial connection), Portakabin C-558/08, Viking Gas C-46/10, Soda-Club C-197/21 (refilled/relabelled goods judged by the impression given to consumers). — [Regulation (EU) 2017/1001](https://eur-lex.europa.eu/eli/reg/2017/1001/oj); [CJEU C-63/97](https://curia.europa.eu/juris/liste.jsf?num=C-63/97); [CJEU C-197/21](https://curia.europa.eu/juris/liste.jsf?num=C-197/21)

### Inferences
- Lower-risk branding: sell under your own brand and type name; describe as "gebouwd in een originele Philips-kast uit 195x; binnenwerk volledig nieuw, niet door of namens Philips"; do not use the Philips logo in advertising headers; the original badge on the cabinet is tolerable only alongside your own clear manufacturer label. Your own name must be on the product anyway under RED art. 10(7).
- Patent position: unlicensed sale of a DAB+ decoder product is technically infringing as long as relevant HE-AAC patents are in force; the pool's fee structure is built for volume makers. Whether the module vendor's chipset arrangements exhaust patent rights is fact-specific. This is an unresolved risk to disclose, not something design choices remove.
- If Bluetooth is enabled and the Bluetooth name/logo is used, Bluetooth SIG membership and a product declaration (with a fee) are required even with a pre-qualified module — a further reason to leave Bluetooth off. Not verified in session. — [Bluetooth SIG qualification fees](https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-listing-fees/)

### Gaps
- Via LA initial/administrative fee and any small-entity terms not found; remaining life of HE-AAC patents not researched.
- No CJEU ruling found on "upcycled" goods retaining the original mark.
- Conditions for using the DAB+ logo (WorldDAB) not researched.
