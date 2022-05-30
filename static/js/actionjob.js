var cadpet = document.getElementById('link1');
var card = document.getElementById('box-cad-job');
var close = document.getElementById('close');
close.addEventListener("click",closeCadJob);
cadpet.addEventListener("click", openCadJob);
function openCadJob(){
    card.style.display = "flex";    
}
function closeCadJob(){
    card.style.display = "none";
}