var inputEmail = document.getElementById('input_email');
var inputPass = document.getElementById('input_password');
inputEmail.addEventListener("focusout", verifyemail);
inputPass.addEventListener("focusout", verifypass);
function verifyemail(){
    var teste = inputEmail.value;
    if(teste.length > 0 && teste.inludes("@") && teste.includes(".com")){
        inputEmail.style.borderColor="#00FF00";
    }
    else{
        inputEmail.style.borderColor="#FF0000";
    }    
}
function verifypass(){
    var teste = inputPass.value;
    if(teste.length > 0){
        inputPass.style.borderColor="#00FF00";
    }
    else{
        inputPass.style.borderColor="#FF0000";
    }    
}