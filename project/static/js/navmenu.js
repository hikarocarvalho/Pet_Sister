// make the menu change when the page change
// faz o menu mudar quando a pagina muda

function changeMenu(){
    var instant = document.getElementById('iframe').getAttribute("src");
    console.log(instant);
    if(instant.includes("home") || instant.includes("registeruser")){
        document.getElementById('img1').style.display="none";
        document.getElementById('link1').style.display="none";
        document.getElementById('img2').style.display="none";
        document.getElementById('link2').style.display="none";
        document.getElementById('img3').style.display="flex";
        document.getElementById('link3').style.display="flex";
        document.getElementById('img4').style.display="none";
        document.getElementById('link4').style.display="none";
        document.getElementById('2').style.display="none";
        document.getElementById('3').style.display="none";
        document.getElementById('4').style.display="none";
        console.log('enter here');
    }
    if(!instant.includes("home") && !instant.includes("registeruser")){
        document.getElementById('img1').style.display="flex";
        document.getElementById('link1').style.display="flex";
        document.getElementById('img2').style.display="flex";
        document.getElementById('link2').style.display="flex";
        document.getElementById('img3').style.display="none";
        document.getElementById('link3').style.display="none";
        document.getElementById('img4').style.display="flex";
        document.getElementById('link4').style.display="flex";
        document.getElementById('2').style.display="flex";
        document.getElementById('3').style.display="none";
        document.getElementById('4').style.display="flex";
        console.log("entersecondhere");
    }
}
var logo = document.getElementById('logo');
logo.addEventListener("click", returnToHome);
function returnToHome(){
    parent.location.reload();
}