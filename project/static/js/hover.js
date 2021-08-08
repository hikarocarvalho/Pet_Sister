function hoverFuncion(value){
    var iditem = "img" + value;
    document.getElementById(iditem).style.backgroundImage = 'url("static/img/dog-hands.png")';
    document.getElementById(iditem).style.backgroundSize = 'auto 100%';
    document.getElementById(iditem).style.backgroundRepeat = 'no-repeat';
}
function liaveFunction(value){
    var iditem = "img" + value;
    document.getElementById(iditem).style.backgroundImage = 'none';
}
function clickFunction(value){
    document.getElementById("internalPage").src=value;
}