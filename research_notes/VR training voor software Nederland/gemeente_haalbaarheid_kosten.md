# Haalbaarheid, kosten en alternatieven: ~8 VR-headsets voor applicatietraining in een Nederlandse gemeente

_Research notes, opgesteld 6 november 2026. Methodologische kanttekening: in deze sessie konden de meeste vendor-sites niet volledig worden opgehaald (netwerkblokkade voor o.a. aeno.nl, forwork.meta.com, warpvr.com, arborxr.com, softwarecatalogus.nl, uploadvr.com). De bevindingen hieronder komen daarom grotendeels uit zoekresultaat-samenvattingen van die pagina's; bedragen moeten vóór gebruik in een besluit opnieuw worden gecontroleerd bij de bron. Bedragen in USD zijn niet omgerekend tenzij vermeld._

## 1. Wat is "U-Force" (leverancier, gebruikers, e-learning)?

### Takeaway
Er bestaat geen gemeentelijke applicatie die "U-Force" heet. Vrijwel zeker gaat het om **Youforce** (uitgesproken als "joe-fors"). Dat is het HR-/salaris- en medewerkerselfservicepakket van **Visma | Raet**, dat nu onder het merk **Visma | YouServe** valt. Youforce is geen zaaksysteem, CRM of workflowtool voor primaire processen. Het is een HR-cloudplatform: personeels- en salarisadministratie, selfservice voor medewerkers en managers ("Mijn Youforce") en digitaal ondertekenen. Bijna elke gemeentemedewerker gebruikt het dus, maar alleen af en toe (verlof, declaraties, loonstroken).

### Cited Findings
- Zoekopdrachten naar "U-Force" en "UForce" leveren geen Nederlandse gemeentesoftware op. De gevonden matches zijn UFORCE (een Brits/Oekraïens defensietechbedrijf), Upforce (een uitzendbureau) en U-Forward (een innovatieplatform van Utrecht) — [Wikipedia UFORCE](https://en.wikipedia.org/wiki/UFORCE); [IMAP – VE Partners/Upforce](https://imap.com/en/transactions/ve-partners-upforce-opus-people~t)
- Youforce staat in de VNG Softwarecatalogus als HR-pakket voor personeels- en salarisadministratie. De catalogus vermeldt ook hoeveel gemeenten het in productie hebben (het aantal kon niet worden opgehaald). Uit de vendortekst: "Met onze HR cloud software Youforce geeft u managers en medewerkers inzicht in en controle over hun HR-zaken" — [Softwarecatalogus – Youforce](https://www.softwarecatalogus.nl/pakket/youforce)
- Youforce heeft selfservice-workflows en een digitale handtekening. HR bepaalt in HR Core (veld "Youforce gebruiker", P15013) of een medewerker kan inloggen op Mijn Youforce — [Visma community – Digitale Handtekening](https://community.visma.com/xqnef94594/attachments/xqnef94594/nl_ra_digital_signing_knowledge/2/2/infosheet_Digitale_Handtekening.pdf); [Visma community – Handleiding Gebruikersbeheer](https://community.visma.com/xqnef94594/attachments/xqnef94594/nl_ra_YF_Portaal_knowledge/250/1/Handleiding%20Gebruikersbeheer.pdf)
- Gemeenten kopen Youforce aan, soms samen. Voorbeeld: Urk, Dronten en Noordoostpolder wilden samen een overeenkomst sluiten met Visma Raet voor hun HRM-systeem. Een aanbesteding vroeg ten minste 5 jaar aantoonbare ervaring met Youforce-implementaties bij gemeenten — [TenderNed doc](https://www.tenderned.nl/papi/tenderned-rs-tns/v2/publicaties/402862/documenten/13378111/content); [TenderNed doc](https://www.tenderned.nl/papi/tenderned-rs-tns/v2/publicaties/402725/documenten/13372571/content)
- Training en e-learning: de YouServe Academy (presentatie YouInspire 2025) noemt e-learning, waaronder een payroll-e-learning en een aanbod voor gratis e-learningtoegang. Visma heeft ook een Learning API en een koppeling met het LMS mijnLMS (Online Academie). Daarmee kan een LMS medewerkers en de organisatiestructuur uit Youforce lezen en certificaten in het personeelsdossier zetten — [YouInspire Academy pdf](https://www.youserve.nl/hubfs/08%20Infosheets,%20whitepapers,%20onderzoeken,%20webinars,%20events/Events/YouInspire%202025/presentaties/YouInspire%20Academy.pdf); [Visma community – mijnLMS Learning API](https://community.visma.com/t5/Tijdelijke-kennisbank/mijnLMS-Visma-YouServe-Learning-API/ta-p/458566)
- Andere veelgebruikte zaaksystemen bij gemeenten: Rx.Mission (Roxit/Centric), Suite4Gemeenten (Centric), Decos JOIN (zaakgericht werken, archivering, klantcontact) en open standaarden als OpenZaak (ZGW-API's) — [Decos](https://decos.com/); [OpenZaak](https://openzaak.org/); [Corver Development](https://corverdevelopment.nl/welke-software-gebruiken-gemeenten-voor-hun-interne-bedrijfsvoering/); [VNG – Zaakgericht werken](https://vng.nl/projecten/zaakgericht-werken)

### Inferences
- Dat "U-Force" Youforce betekent, is een afleiding (klankovereenkomst, gemeentelijke context, gebruikt door alle medewerkers). Laat de opdrachtgever dit bevestigen.
- Youforce is een webapplicatie met eenvoudige formulieren die medewerkers zelden gebruiken. Dat is het minst geschikte type software om in VR te trainen. Een korte e-learning, een klikinstructie, uitleg in het product zelf (DAP) of de e-learning van Visma | YouServe zijn hier logischer en goedkoper.
- Zaaksystemen (Suite4, Rx.Mission, Decos JOIN, xxllnc Zaken) en KCC-systemen hebben hetzelfde probleem. Het zijn 2D-schermapplicaties: de vaardigheid is klikken, invullen en de procesflow volgen. VR voegt daar weinig toe aan didactische waarde, en lezen in een headset en typen zonder toetsenbord zijn lastig.

### Gaps
- Het aantal gemeenten dat Youforce gebruikt kon niet worden opgehaald (softwarecatalogus.nl was geblokkeerd).
- Onbekend is of Visma | YouServe een aparte oefen-/acceptatieomgeving (sandbox) voor eindgebruikers aanbiedt. Navragen bij de leverancier.
- Trainingsomgevingen voor Centric/PinkRoccade/Decos/xxllnc/iBurgerzaken zijn niet onderzocht. Vanuit kennis vooraf (niet geverifieerd in deze sessie): de meeste leveranciers bieden gemeenten een test- of acceptatieomgeving tegen meerprijs.

## 2. Hardwarekosten 2025-2026 en status van Meta for Business / MDM

### Takeaway
Meta is **per 20 februari 2026 gestopt** met de verkoop van zakelijke Quest-versies en met nieuwe Horizon Managed Services-abonnementen (HMS). Workrooms stopte op 16 februari 2026. Bestaande HMS-klanten houden tot **4 januari 2030** support, en HMS-licenties zijn volgens Meta gratis geworden. Wie nu instapt, krijgt de consumentenversie van de Quest 3/3S plus een externe MDM (ArborXR/ManageXR, circa $4–13 per apparaat per maand), of een Pico 4 Ultra Enterprise (circa €850–1.000 incl. btw). Voor 8 headsets komt de hardware zelf op circa €3.000–8.000, plus MDM, accessoires en een laadkast.

### Cited Findings
- Meta stopt per 20 feb 2026 met de verkoop van commerciële Quest-SKU's, neemt geen nieuwe HMS-klanten meer aan en verlaagt de HMS-prijs voor bestaande klanten naar $0 per maand. Bestaande klanten krijgen support tot 4 januari 2030. Volgens berichtgeving zijn Quest 3 en 3S (consument) nog de enige Meta-headsets en zijn ze HMS-geschikt — [SiliconANGLE 16 jan 2026](https://siliconangle.com/2026/01/16/meta-stop-selling-quest-headsets-businesses-discontinue-multiple-vr-features/); [UploadVR](https://www.uploadvr.com/meta-is-shutting-down-its-quest-for-business-program/); [Meta for Work blog](https://forwork.meta.com/ca/blog/an-update-on-meta-for-work/)
- Bronnen spreken elkaar tegen over de vraag of HMS als gratis product blijft bestaan of helemaal ophoudt. Meta's eigen blog meldt gratis licenties vanaf 20 feb — [Hiverlab](https://hiverlab.com/meta-shuts-down-quest-for-business-program-in-2026/); [Unbound XR (NL)](https://unboundxr.com/blogs/meta-beindigt-het-zakelijke-aanbod-per-20-februari); [heise](https://www.heise.de/en/news/Meta-Quest-Official-VR-office-app-and-B2B-program-discontinued-11144019.html?view=print)
- Horizon Workrooms stopte op 16 februari 2026. Als achtergrond wordt genoemd dat Meta minder investeert in VR en meer in smart glasses — [heise](https://heise.de/-11144019); [Thurrott](https://www.thurrott.com/?p=331731)
- MSP's moeten bij klanten opruimen: dataverwijdering en het bijstellen van verwachtingen — [Business of Tech, 20 jan 2026](https://businessof.tech/2026/01/20/metas-retreat-from-business-vr-leaves-msps-managing-cleanup-data-deletion-and-client-expectations/)
- Meta verhoogde de prijzen van Quest 3 en 3S per 19 april 2026 (de officiële aankondiging is gevonden voor Japan) — [Meta JP blog](https://www.meta.com/ja-jp/blog/update-meta-quest-pricing/)
- Europese winkelprijzen Quest 3S 128GB in 2026: circa €399 bij NL/EU-retailers volgens een (marketing)bron, €429,49 bij een Letse retailer (geldig tot 15-07-2026) en €466 voor een geïmporteerde bundel in België. Geen officiële NL-adviesprijs gevonden — [comGateway](https://www.comgateway.com/blogs/calculating-if-the-meta-quest-3s-us-price-tag-is-realistic-for-netherlands-buyers-after-shipping) (onbetrouwbaar); [aio.lv](https://aio.lv/en/product--meta-0815820025252--11164086.md); [u-buy.be](https://www.u-buy.be/nl/product/MDLXIJN3W-streamer-bundle)
- Unbound XR (NL) heeft nog een "Meta Quest 3S 256GB Enterprise" in de catalogus (restvoorraad of staging-pagina) — [Unbound XR](https://m2staging.unboundxr.com/meta-quest-3s-256gb-yyy1)
- Pico 4 Ultra Enterprise 256GB: €957,85 regulier en €916,53 in de uitverkoop bij Unbound XR (NL); €999 bij Galaxus BE (uitverkocht); €852,78 bij een Italiaanse reseller; $899 in de VS (Knox Labs). Een set van 4 Pico 4 Ultra's met koffer, tablet, router en accessoires kost €4.876,80 (circa €1.219 per headset) — [Unbound XR](https://m2staging.unboundxr.com/pico-4-ultra-yyy1-256-gb); [Galaxus BE](https://www.galaxus.be/en/s1/product/pico-4-ultra-enterprise-256-gb-vr-headsets-53128208); [3digital](https://3digital.tech/en/products/pico-4-enterprise-visore-vr); [Knox Labs](https://www.knoxlabs.com/products/pico4-ultra-enterprise); [vali.bg](https://www.vali.bg/en/product/35326/print)
- ArborXR (MDM): volgens de officiële prijspagina gelden prijzen per apparaat per maand, jaarlijks gefactureerd. Education: Classroom $4, Classroom Pro $6, Ultimate op maat. Oudere of derdenbronnen noemen Starter $7, Essential $10 en Enterprise $13 per apparaat per maand. Unbound XR verkoopt ArborXR als licentie per apparaat per jaar — [ArborXR pricing](https://arborxr.com/pricing); [Fitgap](https://us.fitgap.com/products/027341/arborxr); [TechCrunch 2024](https://techcrunch.com/2024/08/13/arborxr-secures-12m-to-boost-management-platform-for-ar-and-vr-devices); [Unbound XR – ArborXR](https://unboundxr.eu/b2b/arbor-xr)
- ManageXR: instapprijs vanaf $7 per apparaat per maand volgens G2. ArborXR zegt zelf dat beide in dezelfde prijsrange zitten — [G2](https://www.g2.com/compare/arborxr-vs-managexr); [ArborXR vs ManageXR](https://arborxr.com/arborxr-vs-managexr)

### Inferences
- Rekenvoorbeeld (schatting): 8× Quest 3S à circa €400–450 geeft circa €3.200–3.600. 8× Pico 4 Ultra Enterprise à circa €920–1.000 geeft circa €7.400–8.000. MDM voor 8 apparaten à $7–13 per maand komt op circa $670–1.250 per jaar. Accessoires (elite strap/batterijstrap, hygiëne-facemasks en wegwerpcovers, UV-C-reiniger, koffers of een laad-/opbergkast, wifi-accesspoint) komen naar schatting op €1.500–4.000 eenmalig. Dat is een schatting zonder bron in deze sessie: navragen bij Unbound XR of VR Expert.
- Apple Vision Pro (circa €4.000 per stuk, kennis vooraf, niet geverifieerd) en HTC Vive Focus Vision (geen prijs gevonden) zijn voor 8 trainingsheadsets onevenredig duur.
- Strategisch risico: Meta trekt zich terug uit de zakelijke markt. De consumenten-Quest vereist een Meta-account, en het platform kan veranderen. Pico (ByteDance) heeft eigen soevereiniteits- en privacyvragen, omdat het een Chinese moedermaatschappij heeft. Dit weegt voor een overheidsorganisatie zwaar.

### Gaps
- Officiële NL-adviesprijzen voor Quest 3 en 3S na de prijsverhoging van april 2026 zijn niet gevonden. Vanuit kennis vooraf (niet geverifieerd): de introductieprijs in de EU (okt 2024) was €329,99 voor de Quest 3S 128GB en €549,99 voor de Quest 3 512GB.
- Geen prijzen gevonden voor de HTC Vive Focus Vision of voor laadkasten en hygiëneproducten.
- Onduidelijk is of nieuwe klanten na februari 2026 nog HMS kunnen activeren (bronnen spreken elkaar tegen).

## 3. Contentkosten: maatwerk-VR-module vs 360°-video vs streaming van de echte app

### Takeaway
Een maatwerk-VR-training kost volgens (veelal Amerikaanse) branchebronnen **$25k–75k voor 360°-video** en **$60k–200k+ voor real-time 3D (Unity)**. Een platform zoals Warp VR (Rotterdam) kost daarnaast een abonnement van grofweg $360–400 per maand of meer (€50–100 per gepubliceerd scenario per maand). Het enige referentieproject bij gemeenten (Leeuwarden, A&O-gesubsidieerd) leverde 3+1 VR-processimulaties op in een traject van 6–8 maanden. Een goedkopere technische route is de **echte applicatie in VR tonen** via Windows/Windows 365 (Mixed Reality Link, Quest 3/3S). Dat is in feite een virtueel beeldscherm en levert geen didactische meerwaarde ten opzichte van een gewone pc.

### Cited Findings
- VR Vision Group (2025/2026-data): gefilmde 360°-video kost $8.000–15.000 per afgewerkte minuut, een opnamedag $8.000–12.000. Een typisch 360°-VR-trainingsprogramma kost $30.000–75.000 — [VR Vision Group – costs guide](https://vrvisiongroup.com/whitepaper/what-does-vr-training-actually-cost-a-clear-cut-guide-to-your-investment/); [VR Vision pdf 2025](https://vrvisiongroup.com/wp-content/uploads/2025/05/VR-Training-Costs-Guide-2025-VR-Vision.pdf)
- Tekrevol: $25.000–60.000 voor 360°-video-VR en $60.000–200.000+ voor real-time CG-VR. Een pilot start rond $40.000–60.000 — [Tekrevol](https://www.tekrevol.com/blogs/?p=30713); [Roundtable Learning](https://roundtablelearning.com/?p=39626)
- Warp VR (Rotterdam) maakt VR-trainingen met 360°-video en 3D. De prijscalculator vermeldt €100 tot €50 per actief gepubliceerd scenario per maand (lager bij meer scenario's) en een LMS-add-on van €50 per workspace per maand (inbegrepen bij Team en Enterprise). Derden noemen een Start-plan van $360–400 per maand, en G2 een pakket vanaf $9.600 per jaar voor 1 creatorlicentie en 50 learners per maand — [Warp VR calculator](https://www.warpvr.com/pricing/calculator); [Capterra Warp VR](https://www.capterra.com/p/218597/Warp-VR/); [G2 Warp VR pricing](https://www.g2.com/products/warp-vr/pricing); [rotterdam.info](https://www.rotterdam.info/en/invest/warp-vr)
- Serious VR (NL) biedt een platform met een vaste prijs per training per gebruiker, gericht op het mkb — [Emerce](https://www.emerce.nl/wire/serious-vr-industrieel-trainen-vr-nu-bereikbaar-mkb)
- Microsoft: Mixed Reality Link en de Windows App voor Meta Quest zijn sinds 30 okt 2025 algemeen beschikbaar. Je krijgt tot 3 virtuele beeldschermen van een lokale pc of een Windows 365 Cloud PC, alleen op de Quest 3/3S. Een update rond sept 2026 voegt microfoon- en passthrough-input toe — [Windows Experience Blog 30-10-2025](https://blogs.windows.com/windowsexperience/2025/10/30/immersive-productivity-with-windows-and-meta-quest-now-generally-available); [VR.org sept 2026](https://vr.org/articles/mixed-reality-link-meta-avatar-camera-windows-2026); [Tom's Hardware](https://www.tomshardware.com/software/windows/windows-11-mixed-reality-support-revived-for-meta-quest-3-quest-3s-headsets)
- Teams op Quest: de aankondigingen dateren van Meta Connect 2022 (Quest Pro/Quest 2). Er is geen bron uit 2026 gevonden die Teams-support op de huidige Quest bevestigt — [fonearena](https://www.fonearena.com/blog/376375/microsoft-meta-teams-windows-365-xbox-cloud-gaming-quest.html/amp)

### Inferences
- Opties voor software-training in VR, van goedkoop naar duur:
  - (a) De echte oefenomgeving streamen via Mixed Reality Link of Windows 365. De contentkosten zijn dan circa nul, maar er is een Windows-pc of Cloud PC per headset nodig en de didactische meerwaarde is nihil.
  - (b) 360°- of screencast-scenario's in Warp VR of Uptale. Dat kost een platformabonnement plus circa €10k–30k productie per module (schatting).
  - (c) Een gesimuleerde UI in Unity, met naar schatting €40k–150k+ per applicatie. De onderhoudskosten zijn hoog, want elke release van het pakket maakt de simulatie verouderd.
- VR loont vooral bij "zachte" of ruimtelijke scenario's: een balie- of klantgesprek bij het KCC, agressie aan de balie, een huisbezoek of een procesbeleving (zoals Leeuwarden deed). Voor klikinstructies in een applicatie loont het niet.

### Gaps
- Geen openbare europrijzen gevonden van Nederlandse bureaus (VRee, TechRebels, Warp VR-studio's) voor een maatwerkmodule. Offertes nodig.
- Uptale-prijzen zijn niet onderzocht.
- De kosten van Immersed en Virtual Desktop (consumentenapps, circa €20, kennis vooraf) zijn niet geverifieerd. Ze vereisen consumentenaccounts en zijn daardoor ongeschikt binnen de BIO.

## 4. Security en IT: BIO, AVG/DPIA, IBD/SLM Rijk, camera's, M365

### Takeaway
Er is **geen specifiek IBD-, VNG- of SLM Rijk-advies en geen Rijks-DPIA over Meta Quest of VR-headsets** gevonden. De gemeente moet dus zelf een DPIA en een risicoanalyse onder de BIO uitvoeren. Risicofactoren: een verplicht Meta-account bij consumentenapparaten (sinds feb 2026 is er geen nieuwe zakelijke route meer), camera's en sensoren (passthrough, handtracking, eye-tracking op sommige modellen), dataverwerking buiten de EU en bij Pico een Chinese moedermaatschappij.

### Cited Findings
- De IBD (onderdeel van VNG) ondersteunt gemeenten bij informatiebeveiliging en de BIO. Vragen kunnen naar info@IBDgemeenten.nl, privacyvragen naar privacy@VNG.nl — [VNG – IBD](https://vng.nl/projecten/informatieveiligheid); [VNG – normenkaders](https://vng.nl/vragen-en-antwoorden/wat-zijn-de-normenkaders-voor-informatiebeveiliging); [GEMMA – IBD producten](https://www.gemmaonline.nl/wiki/IBD_producten_privacy_en_informatiebeveiliging)
- SLM Rijk (Strategisch Leveranciersmanagement, ministerie van JenV) voert DPIA's uit op grote techleveranciers (Microsoft, Google). Voor Meta is alleen een DPIA bekend over het gebruik van Facebook-pagina's door de overheid, waarvan Meta de conclusies betwistte. Er is geen DPIA over Quest gevonden — [Kamerstuk 26643-1098](https://zoek.officielebekendmakingen.nl/kst-26643-1098.pdf); [kst-32761-297](https://zoek.officielebekendmakingen.nl/dossier/kst-32761-297.odt)
- PIRG: Meta Quest-headsets hebben sensoren, microfoons en camera's die veel dataverzameling mogelijk maken. Common Sense Media gaf de Quest 2 een privacyscore van 55%, de op twee na laagste van de geteste headsets — [PIRG](https://pirg.org/illinois/articles/meta-quest-virtual-reality-headsets-can-put-your-personal-data-at-risk/)
- Het Duitse Bundeskartellamt stond hervatting van de Quest-verkoop pas toe nadat Meta het inlogbeleid had aangepast (eerder was een Facebook-account verplicht) — [Mobile World Live](https://www.mobileworldlive.com/?p=359566)
- Na het einde van Meta for Business moeten MSP's dataverwijdering en de afbouw bij klanten regelen — [Business of Tech](https://businessof.tech/2026/01/20/metas-retreat-from-business-vr-leaves-msps-managing-cleanup-data-deletion-and-client-expectations/)

### Inferences
- Een gedeelde, reserveerbare headset met een consumentenaccount past slecht bij BIO-eisen voor identiteit, toegang en logging. Je hebt dan een MDM met een kiosk- of shared mode nodig (ArborXR of ManageXR kunnen dit, ook voor Pico), geen persoonlijke log-in, en geen toegang tot productiedata of persoonsgegevens (alleen een oefenomgeving met fictieve data).
- Een DPIA is waarschijnlijk verplicht of sterk aan te raden als er camera's of passthrough, eye- of handtracking en een Meta- of Pico-account in het spel zijn. Een DPIA plus advies van de FG kost naar schatting 20–60 uur intern of extern (schatting).
- Een M365-login op een gedeelde headset (Windows 365 / Mixed Reality Link) brengt token- en sessierisico's mee. Gebruik in dat geval aparte oefenaccounts.

### Gaps
- Het ophalen van de IBD-productcatalogus (eventuele factsheets over IoT of consumentenapparaten) is niet gelukt.
- Er is niet geverifieerd of SURF of het Rijk een standpunt heeft ingenomen over Meta- of Pico-headsets (SURF heeft voor het onderwijs XR-verkenningen gedaan, kennis vooraf, niet geverifieerd).

## 5. Goedkopere alternatieven (DAP, klik-simulaties, sandbox, e-learning)

### Takeaway
Voor applicatietraining zijn de gangbare en goedkopere routes:
- authoring tools voor klik-simulaties: Articulate 360 (circa $1.449–1.749 per auteur per jaar) of iSpring Suite ($720–1.290 per auteur per jaar);
- Digital Adoption Platforms (WalkMe, Whatfix, Userlane), die alleen op offerte prijzen geven en vaak in de tienduizenden euro's per jaar zitten (schatting);
- een oefenomgeving van de leverancier;
- e-learning van de leverancier zelf (bijv. YouServe Academy voor Youforce).

### Cited Findings
- Articulate 360: het AI Teams-plan kost $1.749 per gebruiker per jaar (Capterra), het Personal-plan circa $1.449 per jaar. Andere bronnen noemen "vanaf $500 per jaar" (tegenstrijdig) — [Capterra Articulate 360 pricing](https://www.capterra.com/p/156978/Articulate-360/pricing/); [Waybook](https://www.waybook.com/blog/articulate-360-alternatives)
- iSpring Suite kost $970 per auteur per jaar, Suite AI $1.290 en Cloud AI circa $720 (vendorblog en vergelijkingssite) — [iSpring blog](https://ispringsolutions.com/blog/alternative-to-articulate)
- Whatfix werkt met prijzen op maat. WalkMe en Userlane publiceren geen prijzen — [TrustRadius](https://www.trustradius.com/compare-products/articulate-360-vs-whatfix)
- Visma | YouServe biedt e-learning via de YouServe Academy en een LMS-koppeling (mijnLMS) — [YouInspire Academy](https://www.youserve.nl/hubfs/08%20Infosheets,%20whitepapers,%20onderzoeken,%20webinars,%20events/Events/YouInspire%202025/presentaties/YouInspire%20Academy.pdf)

### Inferences
- Een klik-simulatie (Storyline of iSpring "simulation mode") van een zaaksysteem of Youforce kost een interne of externe e-learningontwikkelaar naar schatting 20–60 uur per module (circa €2k–6k extern). Dat is een orde van grootte goedkoper dan VR, werkt op elke pc en is via het LMS te koppelen.
- Een DAP (in-app begeleiding in de echte applicatie) is het meest effectief voor applicaties die zelden worden gebruikt, zoals Youforce, maar is duurder en vergt een eigen DPIA (scriptinjectie in de browser).
- Groepssessies: een gewone trainingsruimte met laptops en een oefenomgeving, of een beamer, is didactisch gelijkwaardig of beter dan 8 headsets voor 2D-software.

### Gaps
- Geen geverifieerde prijzen voor WalkMe, Whatfix of Userlane (offerte nodig). Ook Adobe Captivate, GoodHabitz (gemeentelicenties) en Nederlandse DAP's zijn niet onderzocht.

## 6. Nederlandse gemeenten en overheid met VR-pilots, en financiering (A&O fonds Gemeenten)

### Takeaway
Er zijn concrete voorbeelden. **Gemeente Leeuwarden** ontwikkelde met subsidie van het **A&O fonds Gemeenten** (thema "Leren en ontwikkelen") VR-processimulaties voor een Yellow Belt-training (continu verbeteren), gebaseerd op het vergunningproces voor een buurtfeest. Het A&O fonds maakte daarover een "Receptenboek Virtual Reality" (2023) met een doorlooptijd van 6–8 maanden en 2–6 simulaties. **Amsterdam** liet VR-managementtraining maken (TechRebels), **Zaanstad** experimenteerde met VR voor ambtenaren en **Schiedam** zette VR in voor burgerparticipatie. Geen van deze projecten gaat over training in applicatiegebruik.

### Cited Findings
- Het A&O fonds Gemeenten publiceerde "VRecepten" / het Receptenboek Virtual Reality (17-03-2023). Een van de recepten beschrijft de ontwikkeling van een VR-processimulatie met Leeuwarden als voorbeeld: 6–8 maanden en 2–6 simulaties — [A&O Receptenboek VR](https://aeno.nl/uploads/2023-03-17-Receptenboek-Virtual-Reality.pdf)
- Eindrapportage Leeuwarden (24-03-2023): het project viel onder het thema "Leren en ontwikkelen". Het leverde drie VR-processimulaties op, gebaseerd op het script van een vergunning voor een buurtfeest, plus één introductiesimulatie over continu verbeteren. Het was de eerste VR-simulatie van Leeuwarden, opgeleverd eind oktober 2022, en de ondersteuning en expertise van A&O worden positief beoordeeld — [A&O Eindrapportage VR Leeuwarden](https://www.aeno.nl/uploads/2023-03-24-Eindrapportage-Virtual-Reality-Gem-Lwd.pdf)
- Gemeente Amsterdam: een VR-managementtraining door TechRebels met 6 scenario's (o.a. een conflict met de leidinggevende, MT-overleg) — [TechRebels](https://techrebels.io/work/virtual-reality-training-at-gemeente-amsterdam)
- Zaanstad: "Zaanse ambtenaren enthousiast over virtual reality" (Binnenlands Bestuur). Schiedam zet VR in voor burgerparticipatie — [Binnenlands Bestuur – Zaanstad](https://www.binnenlandsbestuur.nl/bestuur-en-organisatie/informatiehuishouding/zaanse-ambtenaren-enthousiast-over-virtual-reality); [Binnenlands Bestuur – Schiedam](https://www.binnenlandsbestuur.nl/bestuur-en-organisatie/lokale-lasten-ozb/schiedam-zet-virtual-reality-in-voor-burgerparticipatie)
- Politie Eenheid Amsterdam: VR-training als kit (headsets, handleiding, reflectiekaart) met eerst een tutorial, omdat veel collega's nieuw zijn met VR. Uit een evaluatie door TwynstraGudde bleken deelnemers overwegend positief — [VR Owl](https://vrowl.io/nl/recherche-zet-virtual-reality-training-in-bij-strijd-tegen-personeelstekort/)
- A&O fonds-subsidies: de folder uit 2022 beschrijft wisselende subsidiabele thema's per aanvraagperiode (o.a. leren en ontwikkelen, loopbaanontwikkeling), aanvragen via subsidies@aeno.nl, en het onderscheid tussen de Stimuleringsregeling (direct uitbetaald) en de StimuleringsregelingPLUS (uitbetaald na afloop). A&O kan steunen met geld of met expertise — [A&O Subsidie Expertise folder 2022](https://www.aeno.nl/uploads/Subsidie-Expertise-folder-2022.pdf); [A&O Subsidie en Expertise info](https://www.aeno.nl/uploads/AenO-Subsidie-en-Expertise-info-pdf.pdf); [Binnenlands Bestuur – subsidiemogelijkheden A&O](https://www.binnenlandsbestuur.nl/bestuur-en-organisatie/bestuursacademie-nederland/subsidiemogelijkheden-a-o-fonds-gemeenten)
- Regionale LLO-fondsen in 2026 (geen A&O): Ontwikkelfonds Flevoland Leert 2026 (plafond €750.000) en de Subsidieregeling Leven Lang Ontwikkelen – Ontwikkelfonds Regio Zwolle — [prb-2026 (Flevoland)](https://zoek.officielebekendmakingen.nl/prb-2026-1288.pdf); [gmb-2026-278748](https://zoek.officielebekendmakingen.nl/gmb-2026-278748.pdf)

### Inferences
- Het A&O fonds is de logische eerste stop voor financiering of expertise, en het Leeuwarden-traject is een direct bruikbaar sjabloon. Het werkt wel met tijdelijke thema's en aanvraagperiodes, dus de actuele regeling voor 2026/2027 moet worden gecheckt.
- De Leeuwarden-casus laat zien dat VR bij gemeenten vooral wordt ingezet om processen en klantgerichtheid te laten beleven, niet om software te leren gebruiken. Dat ondersteunt een advies om VR (als dat er komt) in te zetten voor KCC- en baliegesprekken of procesbeleving, en applicatietraining via e-learning, een oefenomgeving of een DAP te doen.

### Gaps
- De actuele A&O-subsidievoorwaarden en -bedragen voor 2026 konden niet worden opgehaald (aeno.nl was geblokkeerd in deze sessie). Ook de kosten en subsidiebedragen van het Leeuwarden-project zijn niet gevonden.
- Geen resultaten gevonden van VR-pilots bij Rotterdam, Den Haag, Utrecht, Eindhoven of VNG specifiek voor applicatietraining. Er zijn geen bronnen voor gevonden.
