$(".info").hide()
console.log($(".info"))
$(".j").hover(function () {
    var a = $(this).attr('src');
    a = a.replace(" ","");
    console.log($("#"+a))
   // $("#" + ).show()
},function () {

});