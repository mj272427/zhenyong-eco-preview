// 振勇環保 新站 — 共用互動
(function(){
  // 手機選單
  var burger=document.getElementById('burger'),menu=document.getElementById('menu');
  if(burger&&menu){
    burger.addEventListener('click',function(){
      var open=menu.classList.toggle('open');
      burger.setAttribute('aria-expanded',open);
    });
  }
  // 實績分類篩選
  var gal=document.getElementById('gal');
  if(gal){
    document.querySelectorAll('.filters button').forEach(function(btn){
      btn.addEventListener('click',function(){
        document.querySelectorAll('.filters button').forEach(function(b){b.setAttribute('aria-pressed','false');});
        btn.setAttribute('aria-pressed','true');
        var f=btn.dataset.f;
        gal.querySelectorAll('.case').forEach(function(c){
          var show=f==='all'||(' '+c.dataset.cat+' ').indexOf(' '+f+' ')>-1;
          c.style.display=show?'':'none';
        });
      });
    });
  }
})();
