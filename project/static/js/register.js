// here we declair all inputs variables
// aqui nos declaramos variaveis de todos inputs
var inputEmail = document.getElementById('input_email');
var inputPass = document.getElementById('input_password');
var input_name = document.getElementById('input_name');
var input_birthday = document.getElementById('input_birthday');
var input_identity_number = document.getElementById('input_identity_number');
var input_address_other = document.getElementById('input_addreess_other');
var input_password_repeat = document.getElementById('input_password_repeat');
var send = document.getElementById('send');
// here we setup all actions for validade status
// aqui nos setamos todas ações de validação dos status dos campos
inputEmail.addEventListener("focusout", verifyemail);
inputPass.addEventListener("focusout", verifypass);
input_password_repeat.addEventListener("focusout", verifypass);
input_name.addEventListener("focusout", verifyname);
input_birthday.addEventListener("focusout", verifybirthday);
input_identity_number.addEventListener("focusout", verifyidentify);
input_address_other.addEventListener("focusout", verifyother);
// here we declair one array to set the state from inputs
// aqui nós declaramos um array para setar o estado dos inputs
var validate = [false,false,false,false,false,false];
// here we create the functions for all actions 
// aqui nós criamos as funções para todas as ações
// function for email
// função para email
function verifyemail(){
    var teste = inputEmail.value;
    if(teste.length > 0 && teste.includes("@") && teste.includes(".com")){
        inputEmail.style.borderColor="#00FF00";
        validate[0] = true;
        enable();
    }
    else{
        inputEmail.style.borderColor="#FF0000";
        validate[0] = false;
    }    
}
// function for password
// função para senha
function verifypass(){
    var teste = inputPass.value;
    if(teste.length > 0 && teste === input_password_repeat.value){
        inputPass.style.borderColor="#00FF00";
        input_password_repeat.style.borderColor="#00FF00";
        validate[1] = true;
        enable();
    }
    else{
        inputPass.style.borderColor="#FF0000";
        input_password_repeat.style.borderColor="#FF0000";
        validate[1] = false;
    }    
}
// function for name
// função para nome
function verifyname(){
    var teste = input_name.value;
    if(teste.length > 0){
        input_name.style.borderColor="#00FF00";
        validate[2] = true;
        enable();
    }
    else{
        input_name.style.borderColor="#FF0000";
        validate[2] = false;
    }    
}
// fucntion for birthday
// função para aniversário
function verifybirthday(){
    var teste = input_birthday.value;
    if(teste.length > 0){
        validate[3] = true;
        input_birthday.style.borderColor="#00FF00";
        enable();
    }
    else{
        input_birthday.style.borderColor="#FF0000";
        validate[3] = false;
    }    
}
// function for identity number
// função para numero de identidade
function verifyidentify(){
    var teste = input_identity_number.value;
    if(teste.length > 0){
        input_identity_number.style.borderColor="#00FF00";
        validate[4] = true;
        enable();
    }
    else{
        input_identity_number.style.borderColor="#FF0000";
        validate[4] = false;
    }    
}
// function for other address values
// função para outras informaçoes de endereço
function verifyother(){
    var teste = input_addreess_other.value;
    if(teste.length > 0){
        input_address_other.style.borderColor="#00FF00";
        validate[5] = true;
        enable();
    }
    else{
        input_address_other.style.borderColor="#FF0000";
        validate[5] = false;
    }    
}
// here we setup the status for the button
// aqui setamos o status para o botão
function enable(){
    for(var i = 0; i < 6; i++){
        if(validate[i] == true){
            if(i==5){
                send.disabled = false;
                send.style.backgroundColor="#2B3240"
            }
        }else{
            send.disabled = true;
            send.style.backgroundColor="#a1a1a1e8"
        }
    }
    
}