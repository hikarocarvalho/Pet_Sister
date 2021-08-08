var inputEmail = document.getElementById('input_email');
var inputPass = document.getElementById('input_password');
var input_name = document.getElementById('input_name');
var input_birthday = document.getElementById('input_birthday');
var input_identity_number = document.getElementById('input_identity_number');
var input_address_other = document.getElementById('input_addreess_other');
var input_password_repeat = document.getElementById('input_password_repeat');
var send = document.getElementById('send');


inputEmail.addEventListener("focusout", verifyemail);
inputPass.addEventListener("focusout", verifypass);
input_name.addEventListener("focusout", verifyname);
input_birthday.addEventListener("focusout", verifybirthday);
input_identity_number.addEventListener("focusout", verifyidentify);
input_address_other.addEventListener("focusout", verifyother);

emailTrue = (inputEmail.style.borderColor=="#00FF00");
passTrue = inputPass.style.borderColor=="#00FF00";
nameTrue = input_name.style.borderColor=="#00FF00";
birthayTrue = input_birthday.style.borderColor=="#00FF00";
numberTrue = input_identity_number.style.borderColor=="#00FF00";
addressTrue = input_address_other.style.borderColor=="#00FF00";

function verifyemail(){
    var teste = inputEmail.value;
    if(teste.length > 0 ){
        if(teste.includes("@")){
            if(teste.includes(".com")){
                inputEmail.style.borderColor="#00FF00";
                enable();
            }
        }
    }
    else{
        inputEmail.style.borderColor="#FF0000";
    }    
}
function verifypass(){
    var teste = inputPass.value;
    if(teste.length > 0 && teste === input_password_repeat.value){
        inputPass.style.borderColor="#00FF00";
        input_password_repeat.style.borderColor="#00FF00";
        enable();
    }
    else{
        inputPass.style.borderColor="#FF0000";
        input_password_repeat.style.borderColor="#FF0000";
    }    
}
function verifyname(){
    var teste = input_name.value;
    if(teste.length > 0){
        input_name.style.borderColor="#00FF00";
        enable();
    }
    else{
        input_name.style.borderColor="#FF0000";
    }    
}
function verifybirthday(){
    var teste = input_birthday.value;
    if(teste.length > 0){
        input_birthday.style.borderColor="#00FF00";
        enable();
    }
    else{
        input_birthday.style.borderColor="#FF0000";
    }    
}
function verifyidentify(){
    var teste = input_identity_number.value;
    if(teste.length > 0){
        input_identity_number.style.borderColor="#00FF00";
        enable();
    }
    else{
        input_identity_number.style.borderColor="#FF0000";
    }    
}
function verifyother(){
    var teste = input_addreess_other.value;
    if(teste.length > 0){
        input_address_other.style.borderColor="#00FF00";
        enable();
    }
    else{
        input_address_other.style.borderColor="#FF0000";
    }    
}
function enable(){

    if (emailTrue == true){
        if(passTrue  == true){
            if(nameTrue == true){
                if(birthayTrue == true){
                    if(numberTrue == true){
                        if(addressTrue == true){
                            send.disabled = false;
                        }
                    }
                }
            }
        }
    }
}