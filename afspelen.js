// Start het filmpje meteen. Blokkeert de browser dat, dan verschijnt een grote afspeelknop.
// Na afloop gaat de bezoeker na een korte aftelling vanzelf naar het volgende filmpje.
(function(){
  var v=document.querySelector('.video video'); if(!v) return;
  var vak=v.parentNode, knop=document.createElement('button');
  knop.className='grote-play'; knop.type='button'; knop.setAttribute('aria-label','Filmpje afspelen');
  knop.hidden=true; vak.appendChild(knop);
  knop.onclick=function(){ knop.hidden=true; v.play(); };
  v.addEventListener('play',function(){ knop.hidden=true; });
  var p=v.play(); if(p&&p.catch) p.catch(function(){ knop.hidden=false; });

  // Volgend filmpje bepalen uit filmpjes.json, op volgorde van deelnummer.
  var volgende=null;
  var hier=location.pathname.replace(/\/index\.html$/,'').replace(/\/$/,'').split('/').pop();
  fetch('../filmpjes.json',{cache:'no-store'}).then(function(r){return r.json();}).then(function(f){
    var nr=function(x){var m=x.titel.match(/Deel (\d+)/);return m?parseInt(m[1]):99;};
    f.sort(function(a,b){return nr(a)-nr(b);});
    for(var i=0;i<f.length;i++) if(f[i].slug===hier){ volgende=f[i+1]||null; break; }
  }).catch(function(){});

  var SEC=8, paneel=null, timer=null;
  function stop(){ clearInterval(timer); timer=null; if(paneel){ paneel.remove(); paneel=null; } }
  function ga(){ location.href='../'+volgende.slug+'/'; }
  v.addEventListener('play',stop);
  v.addEventListener('ended',function(){
    if(!volgende) return;
    var titel=volgende.titel.replace(/^Deel (\d+) · /,'Deel $1: ');
    paneel=document.createElement('div'); paneel.className='volgende-paneel';
    paneel.innerHTML='<div class="vp-label">Volgend filmpje over <span class="vp-tel">'+SEC+'</span> seconden</div>'
      +'<div class="vp-titel"></div>'
      +'<div class="vp-knoppen"><button type="button" class="vp-nu">Nu afspelen</button><button type="button" class="vp-stop">Annuleren</button></div>';
    paneel.querySelector('.vp-titel').textContent=titel;
    vak.appendChild(paneel);
    paneel.querySelector('.vp-nu').onclick=ga;
    paneel.querySelector('.vp-stop').onclick=stop;
    var rest=SEC, tel=paneel.querySelector('.vp-tel');
    timer=setInterval(function(){ rest--; if(rest<=0){ clearInterval(timer); ga(); } else tel.textContent=rest; },1000);
  });
})();
