---
name: promptstad-publiceren
description: Een nieuw deel (filmpje met stem, artikel, oefeningen en nieuws) toevoegen aan claude-leren.promptstad.nl en live zetten via GitHub Pages. Gebruik bij "zet op PromptStad", "nieuw deel", "publiceer", of een nieuw filmpje voor Claude leren.
---

# Nieuw deel publiceren op claude-leren.promptstad.nl

## Waar staat wat
- Site: **claude-leren.promptstad.nl**, repo `ilsedev/claude-leren` (openbaar). GitHub Pages publiceert `main` automatisch (workflow "pages build and deployment", ongeveer 1 minuut). `CNAME` en `.nojekyll` staan in de root.
- **Let op:** `ilsedev/promptstad-claude` is iets anders: een privé-repo met één HTML-bestand voor de Copilot-training. Die wordt niet gepubliceerd. Nieuwe Claude-lessen horen in `claude-leren`.
- Opbouw: `index.html` (voorpagina, laadt `filmpjes.json`), per deel een map `JJJJ-MM-slug/` met `index.html` en `filmpje.mp4`, thumbnails in `beeld/deelN.svg`, `stijl.css` (huisstijl), `afspelen.js` (autoplay en volgende filmpje), `sitemap/`, `cheat-sheet/`.

## Huisstijl (hele site, sinds 27-11-2026)
Blauw-oranje: hoofdkleur #095CD4, accent #EE6C0A, donker #0B2A5B, lichte tint #D2DCEC, steunkleur #8EA2AF. Alle kleuren staan als variabelen in `stijl.css`. Regels: geen crème; oranje alleen op wit of de lichte tint, of als tekst op donker; op oranje vlakken donkere tekst; oranje nooit als kleine tekst op wit; steunkleur nooit voor tekst. Schrijf Claude als 'hij', 'ja/nee-vragen' in plaats van PASS/FAIL, 'kun je', 'bestanden', 'kerncijfers'.

## Stappen
1. **Inhoud**: schrijf het artikel in gewone, korte zinnen. Controleer beweringen over Claude in de officiële documentatie van Anthropic (code.claude.com/docs, platform.claude.com/docs) en noem bronnen. Ingesproken notities bewaren in de repo.
2. **Dia's** (1920×1080): kopieer `hulpmiddelen/dias-voorbeeld-deel5.html` en vervang de inhoud. Stijl (blauw-oranje, sinds 27-11-2026): lichte tint #D2DCEC of donker #0B2A5B als achtergrond, kleine kop met oranje streepje, grote donkerblauwe titel met een woord in hoofdkleur #095CD4, witte kaarten met dunne donkere rand, oranje nummerblokjes met donkere tekst, motief van afgeronde vierkanten met potloodarcering (oranje #EE6C0A, licht, grijsblauw #8EA2AF) alleen op donkere dia's. Onderaan "Deel N · titel · x/N" en een oranje voortgangsbalk. 8 tot 10 dia's. Bewaar de gesproken tekst als `hulpmiddelen/stemtekst-deelN.md`. Render met `node hulpmiddelen/render.js <aantal dia's>` (vanuit de map met `dias.html`) en bekijk een overzicht.
   - **Bestaand filmpje aanvullen** zonder alles opnieuw in te spreken: zoek de dia-overgangen met `ffmpeg -i filmpje.mp4 -vf "select='gt(scene,0.1)',showinfo" -an -f null -`, knip de oude audio per dia (`-ss`/`-to`, als wav), genereer alleen de nieuwe dia's (met 0,6 s stilte ervoor en 1,0 s erna) en plak alles opnieuw achter de nieuw gerenderde dia's. Deel 5 is zo van 10 naar 12 dia's gegaan voor ongeveer 690 credits.
3. **Stem**: ElevenLabs, stem **Ramon – Warm & Authentic** (`voice_id QkkCTFipKAsDWEnEuFkb`), model `eleven_multilingual_v2`, `generations_count 1`, één generatie per dia, allemaal op één flow (`creative_create_flow` eerst).
   - **Vraag de gebruiker vooraf toestemming voor de credits** en noem de schatting (ongeveer 15 credits per seconde spraak: Deel 5, 3 minuten 24, kostte ongeveer 3.100 credits). Zonder die toestemming weigert het systeem een deel van de generaties.
   - Schrijf uitspraak uit: "Claude punt md", "slash memory", "Opus vijf", "S.O.P.".
   - Downloaden van de mp3's vraagt host `elevenlabsusercontent.com` in de netwerkinstellingen van de omgeving (staat sinds 24-11-2026 in Default). De links verlopen na een paar uur: download meteen.
4. **Filmpje**: `bash hulpmiddelen/maak-mp4.sh <werkmap> <aantal dia's>` → `filmpje.mp4` (1080p, ongeveer 18 MB voor 3,5 minuut). Maak mappen leeg met `: >` of nieuwe mapnamen, niet met `rm -rf` op variabelen (dat wordt geblokkeerd).
5. **Pagina's**: gebruik `hulpmiddelen/bouw-deel5-voorbeeld.py` als voorbeeld. Dat script:
   - maakt `JJJJ-MM-slug/index.html` (video, met daaronder een `article.dagpagina artikel`) en oefenpagina's in submappen;
   - zet een nieuwe regel bovenaan `filmpjes.json` (titel "Deel N · ...", datum, omschrijving);
   - maakt `beeld/deelN.svg` in dezelfde stijl als de andere thumbnails;
   - vervangt het blok `#nieuws` op de voorpagina door het nieuwe nieuws (badge "Nieuw", datum, links);
   - zet oefeningen in de sitemap;
   - verhoogt bij een CSS-wijziging `stijl.css?v=` op de nieuwe pagina's en op `index.html`.
   - **Indeling (sinds 24-11-2026):** de voorpagina toont alleen de delen met de nieuwste `datum` in `filmpjes.json`. Oudere delen verschijnen vanzelf op `eerder/`. Geef een nieuw deel dus een nieuwe datum.
   - **Geen oefeningen meer**, maar een pagina `JJJJ-MM-slug/prompts/` met kant-en-klare prompts (titel, "Wanneer:", prompt met kopieerknop, tip). Zie deel 5 als voorbeeld. Een skill om te downloaden zet je als zip in een eigen map naast de prompts.
6. **Testen**: `python3 -m http.server` in de repo (nodig voor `filmpjes.json`), en screenshots met Playwright op 1280 en 390 breed. Controleer op JavaScript-fouten en horizontaal scrollen. Afgebroken mp4-verzoeken op de voorpagina zijn normaal (de duur wordt uit de metadata gelezen).
7. **Live zetten** (de gebruiker heeft toestemming gegeven om te publiceren): branch → commit → `git -c push.negotiate=true push` → PR naar `main` → mergen. Controleer daarna met `actions_list` (list_workflow_runs) of "pages build and deployment" op `success` staat. De site zelf is vanuit de cloudsessie niet bereikbaar, dus laat de gebruiker hem bekijken.
8. **Afronden**: meld de link (https://claude-leren.promptstad.nl/), wat er nieuw is, en hoeveel ElevenLabs-credits er gebruikt zijn.
