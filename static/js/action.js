var cadpet = document.getElementById('newpet');
var card = document.getElementById('box-cad-pet');
var close = document.getElementById('close');
close.addEventListener("click",closeCadPet);
cadpet.addEventListener("click", openCadPet);
function openCadPet(){
    card.style.display = "flex";    
}
function closeCadPet(){
    card.style.display = "none";
}
