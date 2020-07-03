$(".list-group-item").hover(function(){
    $(this).addClass("active");
  }, function(){
  $(this).removeClass("active");
});

// Animação do Mapa
//$("#mapa-rotulo-jatai").hide();

var cidade_out = ["jatai", "cacu", "mineiros", "montividiu", "rio-verde", "santa-helena"];
var cidade_in = "chapadao-do-ceu";
var cor_ativa = "#1a5f5f";
var cor_inativa = "#179999";

for(var i in cidade_out){

  (function(){
    var mapa_mun_cid_out = "#mapa-mun-" + cidade_out[i];
    var mapa_rot_cid_out = "#mapa-rotulo-" + cidade_out[i];

    var mapa_mun_cid_in = "#mapa-mun-" + cidade_in;
    var mapa_rot_cid_in = "#mapa-rotulo-" + cidade_in;

    $(mapa_mun_cid_out).hover(function(){
        
        $(mapa_rot_cid_in).hide();
        $(mapa_mun_cid_in).css("fill", cor_inativa);

        $(mapa_rot_cid_out).show();
        $(this).css("fill", cor_ativa);

      }, function(){
        
        $(mapa_rot_cid_out).hide()
        $(this).css("fill", cor_inativa);

        $(mapa_rot_cid_in).show();
        $(mapa_mun_cid_in).css("fill", cor_ativa);

    });
  })();

}