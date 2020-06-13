$(".list-group-item").hover(function(){
    $(this).addClass("active");
  }, function(){
  $(this).removeClass("active");
});

// Animação do Mapa
//$("#mapa-rotulo-jatai").hide();

$("#mapa-mun-jatai").hover(function(){
    $("#mapa-rotulo-chapadao").hide();
    $("#mapa-mun-chapadao-do-ceu").css("fill", "#179999");

    $("#mapa-rotulo-jatai").show();
    $(this).css("fill", "#1a5f5f");
  }, function(){
    $("#mapa-rotulo-jatai").hide()
    $(this).css("fill", "#179999");

    $("#mapa-rotulo-chapadao").show();
    $("#mapa-mun-chapadao-do-ceu").css("fill", "#1a5f5f");
});

$("#mapa-mun-cacu").hover(function(){
  $("#mapa-rotulo-chapadao").hide();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#179999");

  $("#mapa-rotulo-cacu").show();
  $(this).css("fill", "#1a5f5f");
}, function(){
  $("#mapa-rotulo-cacu").hide();
  $(this).css("fill", "#179999");

  $("#mapa-rotulo-chapadao").show();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#1a5f5f");
});

$("#mapa-mun-mineiros").hover(function(){
  $("#mapa-rotulo-chapadao").hide();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#179999");

  $("#mapa-rotulo-mineiros").show();
  $(this).css("fill", "#1a5f5f");
}, function(){
  $("#mapa-rotulo-mineiros").hide();
  $(this).css("fill", "#179999");

  $("#mapa-rotulo-chapadao").show();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#1a5f5f");
});

$("#mapa-mun-rio-verde").hover(function(){
  $("#mapa-rotulo-chapadao").hide();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#179999");

  $("#mapa-rotulo-rio-verde").show();
  $(this).css("fill", "#1a5f5f");
}, function(){
  $("#mapa-rotulo-rio-verde").hide();
  $(this).css("fill", "#179999");

  $("#mapa-rotulo-chapadao").show();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#1a5f5f");
});

$("#mapa-mun-santa-helena").hover(function(){
  $("#mapa-rotulo-chapadao").hide();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#179999");

  $("#mapa-rotulo-santa-helena").show();
  $(this).css("fill", "#1a5f5f");
}, function(){
  $("#mapa-rotulo-santa-helena").hide();
  $(this).css("fill", "#179999");

  $("#mapa-rotulo-chapadao").show();
  $("#mapa-mun-chapadao-do-ceu").css("fill", "#1a5f5f");
});