
$(function(){

    //직접입력 인풋박스 기존에는 숨어있다가

$("#selboxDirect").hide();



$("#selbox").change(function() {

      

              //직접입력을 누를 때 나타남

      if($("#selbox").val() == "direct") {

          $("#selboxDirect").show();

      }  else {

          $("#selboxDirect").hide();

      }

      

  }) 

  

});