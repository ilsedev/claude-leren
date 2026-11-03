// Start het filmpje meteen. Blokkeert de browser dat, dan verschijnt een grote afspeelknop.
(function(){
  var v=document.querySelector('.video video'); if(!v) return;
  var vak=v.parentNode, knop=document.createElement('button');
  knop.className='grote-play'; knop.type='button'; knop.setAttribute('aria-label','Filmpje afspelen');
  knop.hidden=true; vak.appendChild(knop);
  knop.onclick=function(){ knop.hidden=true; v.play(); };
  v.addEventListener('play',function(){ knop.hidden=true; });
  var p=v.play(); if(p&&p.catch) p.catch(function(){ knop.hidden=false; });
})();
