# VR-training voor software in het Nederlandse bedrijfsleven en de industrie

> Methode: ongeveer 16 web-searches (NL en EN). Het ophalen van volledige pagina's (chemelot.nl, sitech.nl, varjo.com) werd geblokkeerd door de netwerkinstellingen van de sessie. De bevindingen steunen dus op de samenvattingen in de zoekresultaten, niet op volledig gelezen artikelen. Laat chemelot.nl, sitech.nl en varjo.com toe en controleer ze opnieuw als de details belangrijk zijn. Bij veel cases gaat het om leveranciersmateriaal (marketing); dat staat er steeds bij.

## Welke Nederlandse bedrijven trainen software- of systeemgebruik in VR, en hoe wordt de software getoond (gesimuleerde interface, digital twin, gespiegeld scherm)?

### Takeaway
Ik vond **geen enkele aantoonbare Nederlandse case** waarin medewerkers ERP (SAP/AFAS/Exact), CRM, WMS-software, bank- of verzekeringssystemen of klantenservicetools in een VR-headset leren bedienen. Het Nederlandse bewijs voor "software/systeembediening in VR" zit bijna helemaal in **industriële bediening**:
- bedieningspanelen en cabines (Tata Steel, kraansimulator)
- storingsprocedures op basis van digital twins (Chemelot/Sitech, OCI Nitrogen)

Echte HMI/SCADA-training (tunnels bij RWS, bruggen in Noord-Holland, DCS bij Dow) loopt meestal via **desktop- of webgebaseerde simulatoren met digital twin**, niet via een headset. Het grootste deel van de Nederlandse VR-training gaat over veiligheid, procedures, onderhoud of soft skills.

### Cited Findings

**Industrie: echte bediening van besturing/panelen (deels VR)**
- **Tata Steel IJmuiden (kraanbediening):**
  - Wat: een VR-kraancabinesimulator, gebouwd met Steel Sim VR en Varjo-headsets. Hij emuleert de echte kraancabine. Er zijn aparte trajecten voor nieuwkomers en ervaren operators.
  - Scenario's: ook noodsituaties zoals **automatiseringsstoringen** en breakouts.
  - Claims: Hans Pronk (Tata Steel) noemt het "an exact copy of what happens in real life". Training zou "multiple times more cost-effective" zijn.
  - Bewijs: leverancierscase, geen jaartal gevonden. — [Varjo case study](https://varjo.com/case-studies/shaping-the-future-of-steel-production-training-tata-steels-pioneering-use-of-vr-with-steel-sim-vr-and-varjo)
- **Steel Sim VR** (contact in Haarlem): bouwt fysieke cabine-replica's met echte bedieningsknoppen, pulpits en een industriële kraanstoel, gecombineerd met VR of met displays zonder headset. Er is een dashboard dat sessies bijhoudt. Kraantrainers in IJmuiden zouden nieuwe modules hebben getest. Bewijs: LinkedIn-claims van het bedrijf zelf. — [LinkedIn Jan Luc Zandjans](https://nl.linkedin.com/in/janluczandjans)
- **Controllab (Enschede) en BLUF:**
  - Bouwden een VR-simulator voor de kraanmachinistenopleiding van Tata Steel in Port Talbot (VK). Daarmee werd getraind op een nieuwe chargeerkraan nog vóór die geïnstalleerd was, dus training vóór de echte installatie.
  - De instructeur beheert scenario's via een dashboard.
  - Let op: dit project is Brits, de leverancier Nederlands. — [Controllab – Tata Steel](https://www.controllab.nl/?p=2359); [Controllab Training Simulators factsheet](https://www.controllab.nl/factsheets/Training_Simulators.pdf); [Steel Sim VR Simulator (Controllab)](https://controllab.nl/?p=6565)
- **OCI Nitrogen / OMF, Chemelot (Geleen):**
  - Wat: een VR-pilot voor nieuwe en ervaren operators van een salpeterzuurfabriek.
  - Scenario: de aandrijfmotor van de compressortrein valt uit en start niet op tijd op. Dat gebeurt ongeveer eens per drie jaar, en dan moeten operators snel specifieke handelingen uitvoeren om stilstand van de fabriek te voorkomen.
  - Herkomst: het idee kwam uit de Chemcubator van Sitech. Doel was te testen of VR-instructies het meester-gezelprincipe kunnen vervangen.
  - Het artikel is ongeveer 7 jaar oud (circa 2018-2019). Ik vond geen resultaten van de pilot en geen leverancier.
  - Onduidelijk is of de DCS-schermen in VR werden nagebootst of alleen de veldhandelingen. — [Chemelot nieuws](https://www.chemelot.nl/nieuws/omf-traint-operators-met-behulp-van-virtual-reality)
- **Sitech Safety Skills Center (Chemelot):** Sitech zegt dat zijn VR-trainingen voor operators gebouwd zijn op **digital twins van fabrieken op Chemelot**. Dit gaat vooral om onboarding en veiligheid. — [Sitech](https://www.sitech.nl/safety-skills-center-verbetert-veiligheid-bij-onboarding-chemelot-1/)
- **Dow (locatie niet bevestigd):**
  - Dow gebruikt een "Virtual Development/Simulation/Training system": een digital twin met Siemens SIMIT en operatorschermen.
  - Daarmee kunnen operators wijzigingen in de besturingscode overal trainen, ook in de controlekamer.
  - Dit gebeurt op **schermen, niet in VR**, en het artikel noemt Terneuzen niet. — [Automation World](https://www.automationworld.com/home/article/13318988/how-a-digital-twin-eases-dcs-installation-and-operator-training)

**Infrastructuur: SCADA/HMI-training (vooral desktop/web, geen VR)**
- **Rijkswaterstaat (tunnels):**
  - Covalent bouwt in opdracht van A4all een **webgebaseerde trainer die de bediening van alle tunnelinstallaties nabootst**, voor wegverkeersleiders. RWS wil hem hergebruiken voor latere tunnelprojecten.
  - Sinds 2022 verzorgt ICT Improve de OTO-trainingen (opleiden, trainen, oefenen) voor RWS-tunneloperators. De nieuwste tunnels gebruiken een simulatieomgeving "zoals een vliegsimulator".
  - Croonwolter&dros bouwde een simulator voor de TuBeS-besturingslaag van tunnels (op Siemens SCADA), met een trainingslocatie in de Sluiskiltunnel.
  - Schaal: RWS bedient 24 tunnels vanuit 5 verkeerscentrales, met ongeveer 214 verkeersleiders. — [Computable](https://www.computable.nl/?p=245633); [ICT Improve](https://www.ict.eu/en/projects/ict-improve-supports-rijkswaterstaat-tunnel-operator-training)
- **Witteveen+Bos, Piet Heintunnel (Amsterdam):** een digital twin waarin "met één muisklik de tunnel vol rook" staat, voor training van operators. — [Witteveen+Bos](https://www.witteveenbos.com/news/digital-twin-piet-hein-tunnel)
- **Movares/ENGIE (bruggen Noord-Holland):** een opleidingssimulator met 3D-modellen om de bediening op afstand van 44 bruggen en sluizen virtueel te testen. Later is hij mogelijk ook bruikbaar om nieuwe brugbedieners te trainen. — [Movares Magazine 2019](https://magazine.movares.nl/movares-magazine-editie-2-2019/virtueel-testen)
- **ProRail:** geen bewijs gevonden van VR-training voor treindienstleiders. Wel werd in 2020 een vakopleiding aanbesteed, zonder VR-vermelding. De opleiding duurt ongeveer 9 maanden. — [TenderNed](https://www.tenderned.nl/papi/tenderned-rs-tns/v2/publicaties/200640/documenten/5670029/content); [NOS](https://nos.nl/artikel/2404048-personeelstekort-prorail-verstoort-treinverkeer-in-midden-van-het-land)

**Haven en logistiek**
- **Haven Rotterdam:**
  - Kraansimulatoren met originele bedieningselementen: een CM Labs Vortex-demoruimte in Rotterdam, en de case van ZHD Stevedores (leverancierscase, PDF 2026).
  - Een Sennebogen-simulator voor havenmachines, gepresenteerd op Breakbulk Europe in Rotterdam (juni 2026).
  - Het Havenbedrijf gebruikt VSTEP-simulatoren voor de commandanten van zijn schepen.
  - Dit zijn simulatoren voor **machinebediening**, geen VR-software-UI. — [CM Labs](https://cm-labs.com/en/news/new-rotterdam-demo-room-opens-showcasing-a-vortex-simulator-for-port-equipment/); [ZHD case](https://cm-labs.com/wp-content/uploads/2026/02/ZHD-Stevedores-Case-Study.pdf); [Sennebogen](https://www.sennebogen.com/en/news/news-press/sennebogen-presents-new-simulator-for-port-machines); [Port Technology](https://www.porttechnology.org/news/port-of-rotterdam-looks-to-simulators-to-train-vessel-officers/)
- **Vopak, Shell Pernis:** geen VR-operator- of HMI-training gevonden (zie Gaps).
- **Magazijn/WMS:**
  - Serious VR / VR Training Academy (Enschede) verkoopt een VR-training orderpicken in een digitaal magazijn, voor onboarding én selectie. Prijs: € 20 excl. btw, exclusief headset. Er worden geen klanten genoemd.
  - Er is geen koppeling met een echt WMS of een gesimuleerde scanner-UI aangetoond. — [VR Training Academy orderpicken](https://vrta.netlify.app/en/products/orderpicken-vr-training); [Emerce – Serious VR](https://www.emerce.nl/wire/serious-vr-industrieel-trainen-vr-nu-bereikbaar-mkb)
  - Belgische vergelijking: VIL-project met 8 bedrijven, logistieke VR/AR-training, "tot 6x efficiënter" (persbericht). — [VIL](https://vil.be/wp-content/uploads/2018/11/101220-VIL-persbericht-Logistieke-opleidingen-met-behulp-van-Virtual-Augmented-Reality-veel-efficienter-dan-klassieke-trainingen.pdf)
- **SAP:** er is geen Nederlandse VR-training voor SAP-transacties gevonden. Wel bestaan er LMS-koppelingen: Immerse, Talespin en SAP SuccessFactors starten VR-sessies vanuit het leersysteem. Dat is integratie, geen SAP-bedieningstraining. — [Training Industry – Immerse/SuccessFactors](https://trainingindustry.com/press-release/learning-technologies/by-integrating-with-sap-successfactors-the-immerse-virtual-enterprise-platform-delivers-virtual-reality-training-to-customers-at-scale/); [SAP – Talespin](https://www.sap.com/poland/products/hcm/partners/talespin-reality-labs-inc-copilot-vr-content-library.html)

**Luchtvaart en spoor**
- **KLM:**
  - Het XR Center of Excellence bouwde de VR Cockpit Trainer voor KLM Cityhopper (Embraer E175/E190) in Unity, met een team van 16 mensen, onder wie 7 gecertificeerde Unity-ontwikkelaars. Hierin oefenen piloten de bediening van **cockpitsystemen/-procedures**. Dit komt het dichtst bij "systeembediening in VR" bij een groot Nederlands bedrijf. Deze VR-training is nog niet erkend door EASA.
  - Overige toepassingen: HoloLens (mixed reality) voor vrachtmedewerkers van KLM Cargo, VR-evacuatie voor ongeveer 300 monteurs (2017) en leiderschapstraining met Warp VR. — [Unity – KLM](https://unity.com/resources/klm); [Skift 2021](https://skift.com/2021/03/12/klm-is-ramping-up-virtual-reality-to-train-workers-since-pandemics-start); [casestudies.com – KLM HoloLens](https://www.casestudies.com/company/microsoft-corporation/case-study/packing-with-mixed-reality-klm-uses-microsoft-hololens-to-redefine-its-cargo-training-experience-with-mixed-reality); [MT Sprout](https://mtsprout.nl/management-leiderschap/hoe-klm-vr-inzet-tijdens-trainen-onderhoudsmonteurs)
- **NS:**
  - Warp VR-case: VR voor onderhouds- en reparatieprocedures. Besparing doordat treinen langer in dienst blijven. Er zijn plannen voor machinisten.
  - Sogeti-factsheets (2026): VR/XR-training voor conducteurs in plaats van oudere fysieke simulatoren op één locatie. Eerste proof point binnen 6 maanden.
  - Dit gaat om procedures en onderhoud, geen software-UI. Er zijn geen bedragen genoemd. — [Warp VR – NS](https://www.warpvr.com/customer-stories/how-dutch-railways-realizes-huge-cost-savings-each-year-with-vr-training); [Sogeti NS factsheet](https://www.sogeti.com/wp-content/uploads/sites/3/2026/05/NederlandseSpoorwegen-VRXRTraining-SnapshotClientStory.pdf)

**Bank en verzekeringen, klantenservice**
- **ABN AMRO (2018):** een virtuele leeromgeving waarin medewerkers van het hoofdkantoor de klantbeleving ervaren. 500 medewerkers getraind, betere NPS-vaardigheid. Dit is **empathie- en klantbelevingstraining, geen systeemtraining**. — [Euroforum / Next Learning ABN AMRO](https://blog.euroforum.nl/wp-content/uploads/sites/11/2018/05/Next_learning_ABNAMRO_VR_Experience.pdf)
- **ING, Rabobank, Nederlandse verzekeraars:** geen VR-trainingscases gevonden. Internationale voorbeelden zijn soft skills en geen systeemtraining: Bank of America (circa 50.000 medewerkers, 2021), TD, Erste (Warp VR, overvalscenario's). — [Warp VR banking](https://www.warpvr.com/blog/5-key-trends-in-banking-and-vr-training); [Finextra BofA](https://finextra.com/newsarticle/38980/bofa-preps-massive-vr-training-programme)

### Inferences
- Hoe de software wordt getoond, valt in Nederland in drie modellen uiteen:
  1. **Fysieke replica plus VR** (Steel Sim VR, Controllab): echte knoppen en panelen, de omgeving in VR.
  2. **Digital twin met de originele HMI op een scherm** (Dow/SIMIT, RWS-tunneltrainers, Witteveen+Bos): de operator werkt met dezelfde SCADA/DCS-schermen, maar niet in een headset.
  3. **Volledig virtuele procedure en omgeving** (OCI/Sitech, NS, KLM-cockpit): de interface wordt in 3D nagebouwd.
- Ik vond geen voorbeeld van een gespiegeld echt scherm (bijvoorbeeld een SAP-sessie in een virtual desktop) dat als trainingsvorm wordt gebruikt.
- Waarschijnlijke verklaring: kantoorsoftware leer je het makkelijkst gewoon op een 2D-scherm, met sandboxen en digital adoption platforms. VR loont vooral waar de software vastzit aan fysieke handelingen, gevaar of zelden voorkomende storingen.

### Gaps
- Geen bron voor VR-training in SAP, AFAS, Exact, CRM of WMS bij een Nederlands bedrijf. Dit is mogelijk echt afwezig, en niet alleen niet gevonden.
- Vopak, Shell Pernis, Schiphol en Port of Rotterdam (controlekamer): niets gevonden over VR-HMI-training.
- Chemelot/OCI: of de DCS-schermen in VR zaten, wie de leverancier was en wat de resultaten waren, is onbekend. De pagina kon niet volledig gelezen worden.
- Jaartal en uitrolomvang van de Tata Steel IJmuiden-case zijn onbekend.

## Welke leveranciers en platforms zijn er, en wat zijn de resultaten en kosten?

### Takeaway
Nederlandse VR-leveranciers richten zich vooral op scenario- en proceduretraining. Een paar industriële specialisten (Controllab, Steel Sim VR, VSTEP, Serious VR) leveren bedieningssimulatoren. Ik vond geen Nederlandse leverancier met een product specifiek voor ERP- of CRM-training in VR. Resultaten zijn bijna altijd claims van leveranciers. Kosten zijn schaars.

### Cited Findings
- **Warp VR** (Rotterdam, Van Nelle Fabriek):
  - Een platform om 360°-video en 3D-scenario's te maken.
  - Klanten: NS, KLM (leiderschap), Hotelschool The Hague, Yulius, Meliora VR, Erste, Raiffeisen.
  - Gerichte op scenario's en soft skills, geen software-UI. Warp claimt bedrijfsbreed "40% minder trainingstijd" (algemeen, niet NS-specifiek). — [Rotterdam.info](https://www.rotterdam.info/en/invest/warp-vr); [casestudies.com Warp VR](https://www.casestudies.com/company/warp-vr); [Warp VR – NS](https://www.warpvr.com/customer-stories/how-dutch-railways-realizes-huge-cost-savings-each-year-with-vr-training)
- **Controllab** (Enschede): bedieningssimulatoren voor de staalindustrie (Tata Steel), met een instructeursdashboard. — [Controllab](https://www.controllab.nl/factsheets/Training_Simulators.pdf)
- **Steel Sim VR**: kraan- en pulpitsimulatoren met echte bediening, Varjo-headsets. Klanten volgens eigen claims: Tata Steel IJmuiden, ArcelorMittal Eisenhüttenstadt. — [Varjo case](https://varjo.com/case-studies/shaping-the-future-of-steel-production-training-tata-steels-pioneering-use-of-vr-with-steel-sim-vr-and-varjo)
- **Serious VR / VR Training Academy** (Enschede):
  - Online VR Training Academy voor het industriële mkb. Nodig per persoon: een vrije ruimte van minstens 2,5 × 2,5 m, een headset en een pc.
  - Module orderpicken: € 20 excl. btw. — [Emerce](https://www.emerce.nl/wire/serious-vr-industrieel-trainen-vr-nu-bereikbaar-mkb); [VRTA](https://vrta.netlify.app/en/products/orderpicken-vr-training)
- **VSTEP** (Rotterdam): RescueSim en maritieme simulatoren (Havenbedrijf Rotterdam, Gezamenlijke Brandweer, Den Haag tunnels). — [Port Technology](https://www.porttechnology.org/news/port-of-rotterdam-looks-to-simulators-to-train-vessel-officers/)
- **Covalent, ICT Improve, Croonwolter&dros, Witteveen+Bos, Movares**: simulatoren en digital twins voor tunnel-, brug- en SCADA-bediening, niet in VR. — [Computable](https://www.computable.nl/?p=245633); [ICT](https://www.ict.eu/en/projects/ict-improve-supports-rijkswaterstaat-tunnel-operator-training)
- **Sogeti** (Capgemini): XR-training voor NS (2026). — [Sogeti](https://www.sogeti.com/wp-content/uploads/sites/3/2026/05/NederlandseSpoorwegen-VRXRTraining-SnapshotClientStory.pdf)
- **Changefied**: immersive-learning-platform op Meta Quest, gelanceerd in maart 2025, gerelateerd aan OV/onderwijs. — [XR Today](https://www.xrtoday.com/?p=57441)
- **The Simulation Crew** (Radboud Science Park, sinds 2024): soft skills, zorg. — [Radboud Universiteit](https://www.ru.nl/over-ons/nieuws/vaardigheden-trainen-met-virtual-reality-the-simulation-crew)
- **Kostenindicatie:** VR-Innovations noemt maatwerk-VR-training "vanaf € 7.500", met een pilot van één scenario in ongeveer 2 weken (marketing). — [VR-Innovations](https://vr-innovations.nl/vr-training/)
- **Resultaten (alle afkomstig van leveranciers):**
  - Tata Steel: "meerdere keren kosteneffectiever".
  - ZHD Stevedores: "vrijwel direct efficiëntere training".
  - NS: "aanzienlijke besparing", zonder bedragen.
  - ABN AMRO: 500 getraind. — bronnen hierboven.

### Inferences
- Voor software- en HMI-training is de Nederlandse markt verdeeld:
  - VR-contentbureaus (Warp, VR-Innovations, Changefied) richten zich op procedures en gedrag.
  - Industriële simulatorbouwers (Controllab, VSTEP, Covalent) richten zich op getrouwe bediening, vaak zonder headset.

### Gaps
- Uptale is Frans. Xsens is een bewegingssensorbedrijf, geen trainingsleverancier. Over Fectar, Enversed, VRee, Pixel Pro, Virtual Play, TwinLab, Holomoves en "Immersive Learning" vond ik **geen** Nederlandse case met softwaretraining. De zoekopdrachten leverden niets op, dus hun aanbod is niet geverifieerd.
- Er zijn geen onafhankelijke evaluaties (TNO, fieldlabs) van ROI voor software- of HMI-training in VR gevonden.

## Trends: Apple Vision Pro / Meta Quest 3 mixed reality voor softwaretraining, AI-avatars

### Takeaway
In Nederland draaien zakelijke uitrols vooral op Meta Quest 3/Pro. Apple Vision Pro komt alleen voor als optie in het aanbod van leveranciers. Ik vond geen geverifieerde Nederlandse werkgever die Vision Pro voor training gebruikt. Mixed reality wordt gepositioneerd voor procedures in de echte ruimte. Concrete Nederlandse cases met AI-avatars voor softwaretraining vond ik niet.

### Cited Findings
- Een VR-bureau met een vestiging in Amsterdam: "Most enterprise rollouts run on Meta Quest 3 and Quest Pro for cost and ease of deployment." Referenties: Nationale Politie, RWE. — [VROwl](https://vrowl.io/)
- Quest 3 Enterprise heeft geen pc en geen externe sensoren nodig, wat de uitrol op meerdere locaties makkelijker maakt. Mixed reality wordt ingezet voor veiligheid en procedures. — [Unbound XR](https://unboundxr.com/meta-quest-3-512gb-business-bundle)
- Vision Pro: alleen "custom builds" bij leveranciers (Frame Sixty). Er is geen Nederlandse praktijkcase. — [Frame Sixty](https://framesixty.com/vr-training-with-apple-vision-pro/)
- KLM gebruikte al eerder mixed reality (HoloLens) voor vrachttraining. — [casestudies.com](https://www.casestudies.com/company/microsoft-corporation/case-study/packing-with-mixed-reality-klm-uses-microsoft-hololens-to-redefine-its-cargo-training-experience-with-mixed-reality)
- Hoogwaardige VR voor industriële simulatie gebruikt Varjo-headsets (Tata Steel). — [Varjo](https://varjo.com/case-studies/shaping-the-future-of-steel-production-training-tata-steels-pioneering-use-of-vr-with-steel-sim-vr-and-varjo)
- Onderzoekstrend: een "conversational agent-assistant" voor training van tunneloperators (academisch, geen Nederlandse implementatie bevestigd). — [Tunnel Operator Training with a Conversational Agent](https://katalog.lib.cas.cz/KNAV/EdsRecord/edsair,edsair.doi...........0d8c76ace1f87d3042d1067fa128a712)
- Technische trend: koppeling van een echte PLC (Siemens S7-1500) aan een Unity-VR-omgeving met HMI-bewaking, met een latentie onder 15 ms (academisch). Siemens Run MyVirtual Machine biedt training met de originele SINUMERIK-HMI op een virtuele machine. — [PubMed](https://pubmed.ncbi.nlm.nih.gov/41977808/); [Siemens](https://www.siemens.com/en-us/products/sinumerik/run-my-virtual-machine/)

### Inferences
- De meest waarschijnlijke route voor softwaretraining in VR in Nederland is **een digital twin met een echte PLC/DCS en de originele HMI, in VR gebracht** (procesindustrie, Chemelot). ERP of CRM in VR ligt minder voor de hand. Mixed reality op Quest 3 maakt het mogelijk de echte HMI-schermen te blijven zien terwijl je virtuele instructies krijgt. Dit is een afleiding, geen gevonden case.

### Gaps
- Er zijn geen Nederlandse cijfers over adoptie van Vision Pro of Quest 3 in 2025-2026.
- Er zijn geen Nederlandse cases met AI-avatars (bijvoorbeeld een LLM-gestuurde trainer) voor software- of systeemtraining gevonden.
- Er zijn geen Nederlandse cases met "virtual desktop" of productiviteitssoftware in VR (zoals Immersed of de Vision Pro Mac Virtual Display) als trainingsvorm gevonden.
