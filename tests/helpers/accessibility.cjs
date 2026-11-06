function collectionAudit(){
  function rgba(s){var a=(s.match(/[\d.]+/g)||[]).map(Number);return a.length>=3?[a[0],a[1],a[2],a.length>3?a[3]:1]:[0,0,0,0];}
  function blend(a,b){return [0,1,2].map(i=>a[i]*a[3]+b[i]*(1-a[3])).concat(1);}
  function background(e){var chain=[];for(var p=e;p;p=p.parentElement)chain.unshift(rgba(getComputedStyle(p).backgroundColor));return chain.reduce((b,a)=>blend(a,b),[255,255,255,1]);}
  function lum(c){var a=c.slice(0,3).map(v=>{v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2];}
  function visible(e){var s=getComputedStyle(e),r=e.getBoundingClientRect();return r.width>1&&r.height>1&&s.visibility!=='hidden'&&s.display!=='none'&&!e.closest('[hidden],.cl-sr-only,.cl-skip');}
  var contrast=[],unnamed=[],seen=new Set(),walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
  while(walker.nextNode()){
    var node=walker.currentNode,e=node.parentElement;if(!node.textContent.trim()||!e||!visible(e)||e.closest('script,style,svg'))continue;
    var style=getComputedStyle(e),fg=rgba(style.color),bg=background(e),opacity=1;for(var p=e;p;p=p.parentElement)opacity*=Number(getComputedStyle(p).opacity);fg[3]*=opacity;fg=blend(fg,bg);var a=lum(fg),b=lum(bg),ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05),large=parseFloat(style.fontSize)>=24||(parseFloat(style.fontSize)>=18.66&&Number(style.fontWeight)>=700),minimum=large?3:4.5;
    if(ratio+.02<minimum){var key=style.color+'|'+bg.join(',')+'|'+e.className;if(!seen.has(key)){seen.add(key);contrast.push({text:node.textContent.trim().slice(0,70),selector:e.tagName+'.'+String(e.className).split(' ').join('.'),ratio:Number(ratio.toFixed(2)),minimum,color:style.color,background:bg.slice(0,3)});}}
  }
  document.querySelectorAll('a,button,input:not([type=hidden]),select,textarea').forEach(e=>{if(!visible(e))return;var name=e.getAttribute('aria-label')||e.getAttribute('title')||Array.from(e.labels||[]).map(x=>x.textContent).join(' ')||e.textContent.trim()||Array.from(e.querySelectorAll('img')).map(i=>i.alt).join(' ');if(!name.trim())unnamed.push(e.outerHTML.slice(0,180));});
  return {contrast,unnamed};
}

module.exports=collectionAudit;
