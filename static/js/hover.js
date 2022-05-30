// here we setup the image for hover in menu
// aqui nos setamos a imagem para a transição no menu
function hoverFuncion(value){
    var iditem = "img" + value;
    document.getElementById(iditem).style.backgroundImage = 'url("static/img/dog-hands.png")';
    document.getElementById(iditem).style.backgroundSize = 'auto 100%';
    document.getElementById(iditem).style.backgroundRepeat = 'no-repeat';
}
// here is the function to reset state of item Image
// aqui esta a função para resetar a imgem do botão
function liaveFunction(value){
    var iditem = "img" + value;
    document.getElementById(iditem).style.backgroundImage = 'none';
}
// here is the function to set the image in a selected item
// aqui está a funçãp que seta a imagem para o item selecionado
function clickFunction(value){
    document.getElementById("iframe").src=value;
}
// here redirect page when the user has loged
// aqui redireciona a pagina quando o usuŕio está logado
function redirectIframe(){
    document.getElementById('iframe').src="/profile";
}

