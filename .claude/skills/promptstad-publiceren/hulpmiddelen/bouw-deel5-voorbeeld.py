import html, json, os, re, shutil

R = '/home/user/claude-leren'
SP = '/tmp/claude-0/-home-user/c49bcf10-0ad2-579a-ac30-5928c5037b16/scratchpad'
SLUG = '2026-11-korter-prompten'
V = '19'
LOGO = '<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><path d="M16.0 12.8L16.0 1.5M17.6 13.2L21.5 6.5M18.8 14.4L28.6 8.7M19.2 16.0L27.0 16.0M18.8 17.6L28.6 23.2M17.6 18.8L21.5 25.5M16.0 19.2L16.0 30.5M14.4 18.8L10.5 25.5M13.2 17.6L3.4 23.3M12.8 16.0L5.0 16.0M13.2 14.4L3.4 8.7M14.4 13.2L10.5 6.5" stroke="#D97757" stroke-width="3" stroke-linecap="round"/></svg>'


def pagina(diepte, titel_tag, band_span, band_titel, intro, inhoud, script=''):
    up = '../' * diepte
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}stijl.css?v={V}">
<title>{titel_tag}</title>
</head>
<body>
<nav><div class="nav-in"><a class="home-logo" href="{up}" aria-label="Home" title="Home">{LOGO}</a><a class="knop actief" href="{up}#filmpjes">Claude Leren</a><a class="knop" href="{up}cheat-sheet/"><span class="slash">/</span>Cheat Sheet</a></div></nav>
<div class="band"><h1><span>{band_span}</span> {band_titel}</h1></div>
<div class="intro"><p>{intro}</p></div>
{inhoud}
<footer class="voet"><a href="{up}sitemap/">Sitemap</a></footer>
{script}</body>
</html>
'''


def pre(t):
    return '<pre class="voorbeeld">' + html.escape(t, quote=False) + '</pre>'


# ---------- CSS ----------
CSS = '''
/* Deel 5: artikel, was/wordt, nieuws, oefeningen */
.artikel{margin-top:1.5rem}
.artikel h2{font-size:1.3rem}
.artikel p+p,.artikel p+ul,.artikel ul+p,.artikel p+ol,.artikel ol+p{margin-top:.8rem}
.artikel blockquote{margin:1rem 0 0;border-left:5px solid var(--accent);background:var(--bg-2);border-radius:7px;padding:.9rem 1.1rem;font-style:italic;color:var(--accent-dim)}
.artikel blockquote cite{display:block;font-style:normal;font-size:.85rem;color:var(--tekst-zacht);margin-top:.4rem}
.kernvraag{background:var(--navy);color:#fff;border-radius:var(--radius);padding:1.3rem 1.5rem;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:1.25rem;line-height:1.35;margin:1rem 0 0}
.kernvraag em{font-style:normal;color:#B9B1F2}
.ww{margin-top:1rem;border:1px solid var(--bg-2);border-radius:10px;overflow:hidden}
.ww-rij{display:grid;grid-template-columns:1fr 1.6rem 1fr;gap:.5rem;padding:.7rem .9rem;border-top:1px solid var(--bg-2);align-items:start;font-size:.95rem;line-height:1.45}
.ww-rij:first-child{border-top:0;background:var(--navy);color:#B9B1F2;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase}
.ww-was{color:#8A8FA3}
.ww-was s{text-decoration-color:#C0141A;text-decoration-thickness:2px}
.ww-pijl{color:var(--accent);font-weight:800;text-align:center}
.ww-wordt b{color:var(--navy)}
.ww-bron{display:block;font-size:.78rem;color:var(--tekst-zacht);margin-top:.2rem}
.tag{display:inline-block;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;padding:.12rem .45rem;border-radius:99px;margin-right:.35rem;vertical-align:1px}
.tag.nieuw{background:#E3F5EC;color:#1A7A55}.tag.anders{background:#FDF0E4;color:#B85A18}.tag.blijft{background:var(--bg-2);color:var(--tekst-zacht)}
@media(max-width:560px){.ww-rij{grid-template-columns:1fr}.ww-pijl{text-align:left}.ww-rij:first-child{display:none}}
.vanaf{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.7rem;margin-top:.8rem}
.vanaf div{background:var(--navy);color:#fff;border-radius:10px;padding:.9rem 1rem;font-size:.92rem;line-height:1.45}
.vanaf b{display:block;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.6rem;color:#B9B1F2;line-height:1;margin-bottom:.35rem}
.knoppen{display:flex;flex-wrap:wrap;gap:.7rem;margin-top:1.2rem}
.knoppen a{font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;text-decoration:none;color:var(--navy);background:var(--accent);border-radius:8px;padding:.65rem 1rem}
.knoppen a.licht{background:var(--bg-2)}
.stap{margin-top:1.6rem;padding-top:1.4rem;border-top:1px solid var(--bg-2)}
.stap:first-of-type{border-top:0;padding-top:0;margin-top:0}
.niveau{display:inline-block;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent-dim);background:var(--bg-2);padding:.15rem .55rem;border-radius:99px;margin-left:.4rem;vertical-align:2px}
.stap pre.voorbeeld{margin-top:.7rem}
.nieuws{background:#fff;border-radius:var(--radius);padding:1.4rem 1.6rem;box-shadow:0 2px 8px rgba(13,27,62,.07);border-left:5px solid #D97757;margin-bottom:1.5rem}
.nieuws .kop{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap}
.nieuws .badge{font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#fff;background:#D97757;padding:.2rem .6rem;border-radius:99px}
.nieuws .datum{font-size:.9rem;color:var(--tekst-zacht)}
.nieuws h2{font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:1.3rem;color:var(--navy);margin:.5rem 0 .3rem}
.nieuws p{margin:0 0 .8rem;color:var(--tekst-zacht);line-height:1.5}
.nieuws ul{list-style:none;margin:0;padding:0;display:grid;gap:.5rem}
.nieuws li a{display:block;text-decoration:none;background:var(--bg-2);border-radius:8px;padding:.6rem .8rem;color:var(--tekst)}
.nieuws li a:hover{background:#DCD8F3}
.nieuws li b{font-family:'Plus Jakarta Sans',sans-serif;color:var(--navy)}
.nieuws li span{display:block;font-size:.88rem;color:var(--tekst-zacht)}
'''


def rij(was, wordt, tag, bron=''):
    t = {'nieuw': 'Nieuw', 'anders': 'Anders', 'blijft': 'Blijft'}[tag]
    b = f'<span class="ww-bron">{bron}</span>' if bron else ''
    return f'<div class="ww-rij"><div class="ww-was">{was}</div><div class="ww-pijl">→</div><div class="ww-wordt"><span class="tag {tag}">{t}</span>{wordt}{b}</div></div>\n'


SCHEMA = '<div class="ww"><div class="ww-rij"><div>Was: tot een paar weken geleden</div><div></div><div>Wordt: vanaf nu</div></div>\n' + \
    rij('<s>"Je bent een adviseur met 20 jaar ervaring op het hoogste niveau…"</s>', '<b>Hooguit één korte zin</b> over de rol, of weglaten als doel en context duidelijk zijn.', 'anders', 'Prompting-gids van Anthropic: "Even a single sentence makes a difference."') + \
    rij('<s>"Check je werk."</s>', '<b>Een pass/fail-lijst</b> die Claude afvinkt vóór het resultaat.', 'nieuw', 'Anthropic: Opus 5 controleert zichzelf al') + \
    rij('<s>ZEER BELANGRIJK, ALTIJD, NOOIT</s>', '<b>Gewone zinnen</b>, met de reden erbij.', 'anders', 'Anthropic: "What you can stop doing"') + \
    rij('<s>"Denk goed na." "Ga door, niet lui zijn."</s>', '<b>Het juiste inspanningsniveau</b> (<code>/effort</code>).', 'anders', 'Anthropic: "What you can stop doing"') + \
    rij('<s>Een lange prompt waarin je alles zelf uitschrijft</s>', '<b>Een korte briefing met een doel</b>, of laat Claude je interviewen.', 'nieuw') + \
    rij('<s>Je vaste werkwijze (SOP) meteen meegeven</s>', '<b>Eerst vragen: "Hoe zou jij het doen?"</b>', 'nieuw') + \
    rij('<s>Zelf nalezen in dezelfde sessie</s>', '<b>Review in een verse sessie.</b>', 'nieuw', 'Anthropic: "A second session is also the easiest independent reviewer you can get."') + \
    rij('<s>Een CLAUDE.md die blijft groeien</s>', '<b>Onder de 200 regels</b>, stijl per doelgroep apart.', 'anders', 'Anthropic: "under 200 lines per CLAUDE.md file"') + \
    rij('<s>Mappen en bestanden uitleggen in CLAUDE.md</s>', '<b>Claude kijkt zelf.</b> Schrijf alleen op wat Claude niet kan zien.', 'anders', 'Anthropic: "Claude reads the repo itself."') + \
    rij('<s>Eén lange sessie voor alles</s>', '<b>Vers beginnen</b> bij een nieuwe deeltaak.', 'anders', 'Anthropic: "/clear between unrelated tasks. It costs nothing."') + \
    rij('Context en echte gegevens meegeven', '<b>Blijft.</b> Geef het echte Excel- of CSV-bestand mee.', 'blijft') + \
    rij('Voorbeelden van goede output', '<b>Blijft.</b> Nu als je kwaliteitsnorm.', 'blijft') + '</div>'

OE1 = 'oefening-briefing'
OE2 = 'oefening-claude-md'

ARTIKEL = f'''<article class="dagpagina artikel">
<h2>De kernvraag</h2>
<p>Claude kan zelf goed bedenken <em>hoe</em> iets moet. Stel jezelf daarom bij elke prompt één vraag:</p>
<div class="kernvraag">Welke informatie kan <em>alleen jij</em> geven, en heeft Claude dus echt van jou nodig?</div>
<p>Dat is de laatste les uit de video waar dit deel op gebaseerd is, en eigenlijk de samenvatting van alles hieronder. Korter prompten betekent niet vager prompten: wat je weglaat aan franje, stop je in een scherp doel en een toetsbare check.</p>

<h2>Was en wordt in één overzicht</h2>
{SCHEMA}
<blockquote>"Every one of these was good advice when it was written. Most were workarounds for something the model couldn't reliably do yet, and the models have since caught up. If a few are still habits, here's why it's safe to drop them."<cite>Anthropic, Claude Code-documentatie: Best practices, "What you can stop doing"</cite></blockquote>

<h2>De rol: hooguit één zin</h2>
<p>Lange rolbeschrijvingen ("je bent een ervaren tekstschrijver en financieel adviseur op het hoogste niveau…") kun je loslaten. Ze kosten tokens en voegen weinig toe. De lijst "What you can stop doing" noemt de rol niet, en de algemene prompting-gids van Anthropic vindt een korte rol nog nuttig. Mijn advies: één zin is genoeg, en als doel en context al duidelijk zijn, laat je hem weg.</p>

<h2>"Check je werk" werkt niet meer</h2>
<p>Claude Opus 5 controleert zijn eigen werk al. Een algemene regel als "check je werk" laat Claude alleen nog een keer doen wat het al deed. Dat kost tokens en het antwoord wordt er niet beter van. Anthropic noemt dat <em>over-verification</em>. Wat wel werkt: een pass/fail-lijst (zie hieronder).</p>

<h2>De briefing: kort, maar niet vaag</h2>
<p>Hoe concreter je doel, hoe gerichter de uitkomst. Een briefing heeft een doel en vijf onderdelen:</p>
<ol><li><b>Wat en waarom</b>, met de echte gegevens, zoals je Excel- of CSV-bestand.</li><li><b>De kwaliteitsnorm</b>: voorbeelden die jij goed vindt, of laat Claude ze zoeken en kies zelf.</li><li><b>Tools</b>: welke Claude moet gebruiken, en of andere ook mogen.</li><li><b>Vrijheid in het plan</b>: mag Claude het plan onderweg aanpassen? Of: "Wil je het plan aanpassen, vraag het me dan eerst."</li><li><b>De check</b>: een lijst met ja/nee-vragen.</li></ol>
<p>Je hoeft dit niet zelf uit te schrijven. Laat Claude je <b>interviewen</b>, één vraag tegelijk. Het interview eindigt weer bij het doel.</p>

<h2>Je vaste werkwijze (SOP): wel of niet meegeven?</h2>
<p>Een SOP is hoe mensen iets vaak al jaren doen. Claude weet het misschien handiger. Drie manieren:</p>
<ul><li>Vraag eerst "Hoe zou jij het doen?", geef daarna je SOP en vraag wat er ontbreekt.</li><li>Geef eerst je SOP en vraag of Claude een efficiëntere manier weet.</li><li>Laat je SOP weg en beoordeel de aanpak van Claude in de planmodus.</li></ul>

<h2>De check: pass of fail</h2>
<p>Niet: "Maak het rapport professioneel." Wel: "Check of elk bedrag uit de CSV in het rapport staat en klopt." Meer voorbeelden:</p>
<ul><li>Is elke gebruikte waarde precies gelijk aan de bron?</li><li>Kloppen alle totalen?</li><li>Voldoet de tekst aan de schrijfstijl van het coalitieakkoord?</li><li>Is de tekst korter dan 200 woorden?</li></ul>
<p>Zet in je prompt: "Markeer elke regel met PASS of FAIL voordat je de output laat zien." Pas als alles PASS is, is het klaar. Lukt dat redelijkerwijs niet, bijvoorbeeld door tegenstrijdige input, dan mag Claude FAIL geven en uitleggen waarom. Tip: laat Claude je helpen de lijst op te stellen.</p>

<h2>Frisse ogen: review in een verse sessie</h2>
<p>Zegt Claude dat het klaar is? Open een nieuwe sessie die niet heeft meegewerkt en laat die de output beoordelen: een code review bij software, een kritische lezing bij een voorstel. Geef dezelfde pass/fail-lijst mee. Die sessie heeft de redeneringen niet gezien en kijkt dus echt fris.</p>

<h2>CLAUDE.md kort en opgeruimd</h2>
<p>Claude leest CLAUDE.md aan het begin van elke sessie. Houd hem onder de 200 regels en bekijk hem bij elke grote opdracht, of wekelijks. Zet stijl per lezer in losse bestanden, zoals <code>werkschrijfstijl.md</code>, <code>gemeenteraadstijl.md</code>, <code>directiestijl.md</code>, <code>huisstijl.md</code> of <code>claude-like-me.md</code>.</p>
<p><b>Let op:</b> een verwijzing met <code>@bestand.md</code> laadt het bestand altijd mee, dus dat bespaart niets. Schrijf liever in gewone woorden wanneer Claude het moet lezen ("Schrijf je voor de gemeenteraad? Lees dan eerst gemeenteraadstijl.md."), of maak er een skill van.</p>

<h2>Memory, skills, inspanning en vers beginnen</h2>
<ul><li><b>Auto-memory</b> staat standaard aan: Claude maakt eigen notities en vertrouwt daarop. Met <code>/memory</code> zie je wat erin staat, en kun je het uitzetten. Een bewuste keuze, want het kan je volgende opdrachten helpen of hinderen.</li>
<li><b>Skills</b>: doe je iets maandelijks of vaker, zeg dan: "Verander wat we zojuist gemaakt hebben in een skill om te bewaren." Ging er later iets mis, vraag Claude dan de skill bij te werken. Een oude skill test je eerst.</li>
<li><b>Inspanning</b> (<code>/effort</code>): laag voor snel vraag en antwoord, gemiddeld voor routinewerk, hoog als je een fout zoekt, max voor complexe problemen. Combineren kan: maken op gemiddeld, testen en controleren op hoog.</li>
<li><b>Vers beginnen</b>: in een lange sessie neemt Claude steeds alles mee. Nieuwe deeltaak? <code>/clear</code> of een nieuwe sessie.</li></ul>

<h2>Vanaf vandaag</h2>
<div class="vanaf"><div><b>1</b>Vraag je af: wat kan <em>alleen ik</em> Claude vertellen?</div><div><b>2</b>Schrap de franje: geen lange rol, geen "check je werk", geen HOOFDLETTERS.</div><div><b>3</b>Voeg een pass/fail-lijst toe en laat een verse sessie reviewen.</div><div><b>4</b>Ruim je CLAUDE.md op: onder 200 regels, stijl apart.</div></div>
<div class="knoppen"><a href="{OE1}/">Oefening: een scherpe briefing →</a><a class="licht" href="{OE2}/">Oefening: CLAUDE.md opschonen →</a></div>

<h2>Bronnen</h2>
<ul><li>Eric Tech, "Give Me 10 Minutes and I'll Make Claude Code 100x Smarter", YouTube, 22 november 2026.</li>
<li><a href="https://code.claude.com/docs/en/best-practices" target="_blank" rel="noopener">Claude Code: Best practices</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5" target="_blank" rel="noopener">Prompting Claude Opus 5</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices" target="_blank" rel="noopener">Prompting best practices</a></li>
<li><a href="https://code.claude.com/docs/en/memory" target="_blank" rel="noopener">CLAUDE.md en memory</a></li></ul>
</article>'''

DEEL = pagina(1, 'Deel 5 · Korter prompten, scherper briefen', 'Deel 5:', 'Korter prompten, scherper briefen',
    'De nieuwste Claude-modellen hebben geen lange prompts meer nodig, wel duidelijke. Wat je kunt loslaten, wat ervoor in de plaats komt, en de kernvraag: welke informatie kan alleen jij geven? Onder het filmpje staan het hele artikel en twee oefeningen.',
    f'<main><div class="inner"><a class="terug" href="../">← Alle filmpjes</a><div class="video"><video src="filmpje.mp4" controls preload="metadata" playsinline></video></div>\n{ARTIKEL}\n</div></main>',
    '<script src="../afspelen.js"></script>\n')


def stap(nr, titel, niveau, uitleg, prompt, tip):
    return f'<section class="stap"><h2>Stap {nr}: {titel}<span class="niveau">{niveau}</span></h2><p>{uitleg}</p>{pre(prompt)}<div class="tip"><b>Tip</b>{tip}</div></section>\n'


import sys
sys.path.insert(0, SP)

OEF1_STAPPEN = [
 ('Van vaag naar toetsbaar', 'Basis', '"Maak het rapport professioneel" is kort, maar vaag. Deze prompt is net zo kort, maar zegt waar het resultaat aan moet voldoen.',
 '''Hieronder staat een fictief overzicht van de inkoopuitgaven per categorie (CSV).
Maak er een kort rapport van voor het MT: per categorie het totaal, de grootste post en één zin duiding.

Checklist (markeer elke regel met PASS of FAIL voordat je het rapport laat zien):
1. Elk bedrag in het rapport staat precies zo in de CSV.
2. Alle totalen kloppen.
3. Het rapport is korter dan 300 woorden.
4. Er staan geen conclusies in die niet uit de cijfers volgen.

Het rapport is pas klaar als alle regels PASS zijn. Lukt dat niet, geef dan FAIL en leg uit waarom.

categorie;leverancier;bedrag
ICT;Leverancier A;48.200
ICT;Leverancier B;12.950
Schoonmaak;Leverancier C;31.400
Catering;Leverancier D;8.700
Catering;Leverancier E;4.150''',
 'Probeer ook de vage variant en vergelijk. "Professioneel" kun je niet afvinken, "elk bedrag staat zo in de CSV" wel.'),
 ('Laat Claude je interviewen', 'Verder', 'Een briefing heeft een doel en vijf onderdelen. Laat Claude ernaar vragen in plaats van ze zelf uit te schrijven.',
 '''Ik wil [wat wil je maken].

Stel me eerst vragen, één voor één, en wacht steeds op mijn antwoord. Vraag naar:
1. Wat en waarom: het doel, en met welke gegevens of bestanden je moet werken.
2. De kwaliteitsnorm: voorbeelden die ik goed vind, of waar je zelf naar moet zoeken.
3. Tools: wat je moet gebruiken en of je ook andere tools mag gebruiken.
4. Vrijheid: mag je het plan onderweg aanpassen, of vraag je het eerst?
5. De check: een korte lijst met ja/nee-vragen waaraan het resultaat moet voldoen.

Vat daarna de briefing samen en sluit af met het doel. Begin pas als ik akkoord geef.''',
 'Het interview eindigt weer bij het doel: wat Claude oplevert, moet daaraan voldoen.'),
 ('Maak samen de pass/fail-lijst', 'Verder', 'Weet je niet welke regels je in de lijst zet? Laat Claude meedenken.',
 '''Ik ga je vragen om [opdracht]. Het doel is: [doel].

Help me eerst een checklist te maken waarmee we toetsen of het resultaat goed is.
- Maximaal 6 regels.
- Elke regel is met ja of nee te beantwoorden.
- Geen vage regels als "is het professioneel?". Wel bijvoorbeeld: "Komt elk bedrag overeen met de bron?"

Ik kies daarna welke regels we gebruiken.''',
 'Zet daarna in je opdracht: "Markeer elke regel met PASS of FAIL voordat je de output laat zien."'),
 ('Je SOP: wel of niet meegeven?', 'Gevorderd', 'Vraag eerst hoe Claude het zou doen, en leg daarna je eigen werkwijze ernaast.',
 '''Ik wil [opdracht]. Het doel is: [doel].
Hoe zou jij dit aanpakken? Geef je aanpak in maximaal 6 stappen. Begin nog niet.

[Na het antwoord van Claude:]
Zo doen wij het nu altijd:
[plak hier je vaste werkwijze]

Vergelijk de twee. Wat ben ik vergeten, en wat ben jij vergeten? Welke aanpak is efficiënter, en waarom?''',
 'Of laat je werkwijze helemaal weg en beoordeel de aanpak van Claude in de planmodus.'),
 ('Review in een verse sessie', 'Gevorderd', 'Zegt Claude dat het klaar is? Plak het resultaat in een nieuwe sessie.',
 '''Hieronder staat [een voorstel / rapport / notitie] voor [doelgroep].
Jij hebt niet meegewerkt aan het maken ervan. Lees het kritisch.

Werk deze checklist af en markeer elke regel met PASS of FAIL:
1. [regel uit je checklist]
2. [regel uit je checklist]
3. [regel uit je checklist]

Noem daarna maximaal 3 verbeterpunten, belangrijkste eerst. Herschrijf niets.

[Plak hier het resultaat]''',
 'Bij software laat je de nieuwe sessie een code review doen. Zeg erbij waar die op moet letten.'),
]

OEF2_STAPPEN = [
 ('Kijk wat Claude elke sessie leest', 'Basis', 'Vaak lezen er meer bestanden mee dan je denkt.',
 '''Welke CLAUDE.md-bestanden en memory-bestanden heb je in deze sessie geladen?
Geef per bestand: waar het staat, hoeveel regels het heeft, en in één zin waar het over gaat.''',
 'Je kunt het ook zelf bekijken met /memory.'),
 ('Laat Claude je CLAUDE.md doorlichten', 'Verder', 'Eerst analyseren, dan pas veranderen. Zo houd jij de regie.',
 '''Lees mijn CLAUDE.md en deel elke regel in bij één van deze groepen:
A. Doet Claude al vanzelf, dus kan weg (zoals "check je werk", "denk goed na").
B. Achterhaald of te zwaar aangezet (lange rolbeschrijvingen, HOOFDLETTERS, ZEER BELANGRIJK, ALTIJD/NOOIT).
C. Alleen nodig bij bepaalde taken of doelgroepen, dus verplaatsen naar een los bestand.
D. Echt nodig voor bijna elke sessie, dus laten staan.

Verander nog niets. Laat een tabel zien met per regel de groep en een korte reden, en doe daarna een voorstel voor een nieuwe CLAUDE.md.

Checklist (markeer elke regel met PASS of FAIL):
1. De nieuwe CLAUDE.md heeft minder dan 200 regels.
2. Er staan geen regels in HOOFDLETTERS of met ZEER BELANGRIJK.
3. Elke regel uit groep D staat er nog in.
4. Elke regel uit groep C heeft een nieuwe plek.''',
 'Twijfel je bij groep D? Haal de regel weg en kijk of je hem mist.'),
 ('Splits stijl per doelgroep af', 'Verder', 'Schrijven voor de gemeenteraad is anders dan voor de directie. Geef elke stijl een eigen bestand.',
 '''Maak voor de regels uit groep C losse, korte bestanden, bijvoorbeeld:
- werkschrijfstijl.md: zakelijke documenten voor mijn werk
- gemeenteraadstijl.md: teksten voor de gemeenteraad
- directiestijl.md: teksten voor de directie
- huisstijl.md: ontwerpen in de huisstijl
- claude-like-me.md: teksten die klinken alsof ik ze zelf schrijf

Zet in CLAUDE.md een kort blok "Wanneer lees je wat", in gewone zinnen en zonder @-verwijzing. Bijvoorbeeld:
"Schrijf je voor de gemeenteraad? Lees dan eerst gemeenteraadstijl.md."

Laat me de nieuwe bestanden zien voordat je ze opslaat.''',
 'Een @-verwijzing laadt het bestand altijd mee. Een gewone zin laat Claude het alleen lezen als het nodig is.'),
 ('Bepaal wat Claude zelf mag onthouden', 'Gevorderd', 'Auto-memory staat standaard aan. Kijk af en toe wat erin staat.',
 '''Laat me zien wat er in je auto-memory staat voor dit project.
Geef per notitie: wat je hebt onthouden, of het nog klopt met mijn CLAUDE.md, en of het botst met een van mijn stijlbestanden.
Stel voor welke notities ik beter kan verwijderen. Verwijder nog niets.''',
 'Wil je niet dat Claude zelf notities maakt? Zet auto-memory uit via /memory.'),
 ('Maak er een vaste gewoonte van', 'Gevorderd', 'Een CLAUDE.md groeit vanzelf weer aan. Een korte wekelijkse check houdt hem scherp.',
 '''Wekelijkse check van mijn CLAUDE.md. Markeer elke regel met PASS of FAIL:
1. CLAUDE.md heeft minder dan 200 regels.
2. Er zijn geen regels bijgekomen die maar bij één soort taak horen.
3. Er staan geen regels in die Claude al vanzelf doet.
4. Elk stijlbestand waar CLAUDE.md naar verwijst, bestaat nog.
5. Auto-memory bevat geen notities die botsen met CLAUDE.md.

Geef bij elke FAIL een voorstel. Verander nog niets.''',
 'Doe je dit wekelijks? Maak er een skill van.'),
]


def oefpagina(titel, intro, stappen, ander, ander_titel):
    body = ''.join(stap(i + 1, *s) for i, s in enumerate(stappen))
    inhoud = f'''<main><div class="inner smal"><a class="terug" href="../">← Deel 5: Korter prompten</a>
<article class="dagpagina">
{body}</article>
<nav class="dagnav"><a class="vorige" href="../">← Artikel en filmpje</a><span></span><a class="volgende" href="../{ander}/">{ander_titel} →</a></nav>
</div></main>'''
    return pagina(2, f'Oefening: {titel} · Deel 5', 'Oefening:', titel, intro, inhoud)


OEF1 = oefpagina('een korte, scherpe briefing', 'Kort, maar niet vaag: in vijf stappen oefen je met een doel, een interview, een pass/fail-lijst, je vaste werkwijze en een review in een verse sessie. Gebruik alleen fictieve gegevens.', OEF1_STAPPEN, OE2, 'CLAUDE.md opschonen')
OEF2 = oefpagina('CLAUDE.md opschonen', 'Claude leest CLAUDE.md bij elke sessie. In vijf stappen maak je hem weer kort, splits je stijl per doelgroep af en bepaal je wat Claude zelf mag onthouden.', OEF2_STAPPEN, OE1, 'Een scherpe briefing')

NIEUWS = f'''<div class="nieuws" id="nieuws"><div class="kop"><span class="badge">Nieuw</span><span class="datum">Toegevoegd op 24 november 2026</span></div>
<h2>Deel 5: Korter prompten, scherper briefen</h2>
<p>Ken je deze site al? Dit is er nieuw: een filmpje, een artikel met was/wordt-schema, en twee oefeningen.</p>
<ul><li><a href="{SLUG}/"><b>Filmpje en artikel</b><span>Wat je kunt loslaten, wat ervoor in de plaats komt, en de kernvraag.</span></a></li>
<li><a href="{SLUG}/{OE1}/"><b>Oefening: een korte, scherpe briefing</b><span>Doel, interview, pass/fail-lijst en een frisse blik.</span></a></li>
<li><a href="{SLUG}/{OE2}/"><b>Oefening: CLAUDE.md opschonen</b><span>Onder de 200 regels, stijl apart en memory bewust aan of uit.</span></a></li></ul></div>
'''

THUMB = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 340"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#13265A"/><stop offset="1" stop-color="#0D1B3E"/></linearGradient><radialGradient id="r" cx=".8" cy=".2" r=".6"><stop offset="0" stop-color="#A89FEF" stop-opacity=".35"/><stop offset="1" stop-color="#A89FEF" stop-opacity="0"/></radialGradient></defs><rect width="600" height="340" fill="url(#g)"/><rect width="600" height="340" fill="url(#r)"/>
<rect x="70" y="80" width="260" height="22" rx="11" fill="#5C6480"/><rect x="70" y="120" width="230" height="22" rx="11" fill="#5C6480"/><rect x="70" y="160" width="250" height="22" rx="11" fill="#5C6480"/><rect x="70" y="200" width="200" height="22" rx="11" fill="#5C6480"/>
<g stroke="#C0141A" stroke-width="5" stroke-linecap="round"><path d="M62 91h276M62 131h246M62 171h266M62 211h216"/></g>
<path d="M352 170h40" stroke="#A89FEF" stroke-width="6" stroke-linecap="round"/><path d="M384 158l14 12-14 12" fill="none" stroke="#A89FEF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="420" y="120" width="120" height="100" rx="16" fill="#ECECF4"/><rect x="438" y="140" width="84" height="16" rx="8" fill="#7A6FD6"/>
<g fill="#107C41"><circle cx="446" cy="186" r="9"/></g><rect x="462" y="180" width="60" height="12" rx="6" fill="#5C6480"/><g fill="#107C41"><circle cx="446" cy="206" r="9"/></g><rect x="462" y="200" width="44" height="12" rx="6" fill="#5C6480"/>
</svg>
'''

# ---------- schrijven ----------
os.makedirs(f'{R}/{SLUG}/{OE1}', exist_ok=True)
os.makedirs(f'{R}/{SLUG}/{OE2}', exist_ok=True)
open(f'{R}/{SLUG}/index.html', 'w').write(DEEL)
open(f'{R}/{SLUG}/{OE1}/index.html', 'w').write(OEF1)
open(f'{R}/{SLUG}/{OE2}/index.html', 'w').write(OEF2)
shutil.copy(f'{SP}/filmpje.mp4', f'{R}/{SLUG}/filmpje.mp4')
open(f'{R}/beeld/deel5.svg', 'w').write(THUMB)

css = open(f'{R}/stijl.css').read()
if 'Deel 5: artikel' not in css:
    open(f'{R}/stijl.css', 'w').write(css.rstrip('\n') + '\n' + CSS.strip() + '\n')

f = json.load(open(f'{R}/filmpjes.json'))
if not any(x['slug'] == SLUG for x in f):
    f.insert(0, {"slug": SLUG, "titel": "Deel 5 · Korter prompten, scherper briefen", "datum": "2026-11-24", "omschrijving": "Wat je kunt loslaten en wat ervoor in de plaats komt: was/wordt-schema, de briefing, pass/fail-lijst, review in een verse sessie, CLAUDE.md kort houden en de kernvraag. Met artikel en twee oefeningen."})
    s = '[\n' + ',\n'.join('  ' + json.dumps(x, ensure_ascii=False) for x in f) + '\n]\n'
    open(f'{R}/filmpjes.json', 'w').write(s)

idx = open(f'{R}/index.html').read()
if 'id="nieuws"' not in idx:
    idx = idx.replace('<main id="filmpjes"><div class="inner">', '<main id="filmpjes"><div class="inner">' + NIEUWS, 1)
    idx = idx.replace('stijl.css?v=18', f'stijl.css?v={V}')
    open(f'{R}/index.html', 'w').write(idx)

sm = open(f'{R}/sitemap/index.html').read()
if OE1 not in sm:
    sm = sm.replace('<h2>Cheat Sheet</h2>', f'<h2>Oefeningen</h2>\n<ul><li><a href="../{SLUG}/{OE1}/">Oefening: een korte, scherpe briefing</a></li>\n<li><a href="../{SLUG}/{OE2}/">Oefening: CLAUDE.md opschonen</a></li></ul>\n<h2>Cheat Sheet</h2>', 1)
    sm = sm.replace('stijl.css?v=18', f'stijl.css?v={V}')
    open(f'{R}/sitemap/index.html', 'w').write(sm)
print('klaar')
