const N=+(process.argv[2]||10);const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.cwd()+'/dias.html');await p.waitForTimeout(1500);
for(let i=0;i<N;i++){await p.evaluate(i=>toon(i),i);await p.waitForTimeout(100);await p.screenshot({path:`dia${String(i+1).padStart(2,'0')}.png`});}
await b.close();})();
