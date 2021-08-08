// here we declair all inputs variables
// aqui nos declaramos variaveis de todos inputs
var inputEmail = document.getElementById('input_email');
var inputPass = document.getElementById('input_password');
var send = document.getElementById('login');
// here we setup all actions for validade status
// aqui nos setamos todas ações de validação dos status dos campos
inputEmail.addEventListener("focusout", verifyemail);
inputPass.addEventListener("focusout", verifypass);
// here we declair one array to set the state from inputs
// aqui nós declaramos um array para setar o estado dos inputs
var validate = [false,false];
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
        validate[0] = false;
        inputEmail.style.borderColor="#FF0000";
    }    
}
// function for password
// função para senha
function verifypass(){
    var teste = inputPass.value;
    if(teste.length > 0){
        inputPass.style.borderColor="#00FF00";
        validate[1] = true;
        enable();

    }
    else{
        inputPass.style.borderColor="#FF0000";
        validate[1] = false;
    }    
}
// here we setup the status for the button
// aqui setamos o status para o botão
function enable(){

    for(var i = 0; i < 2; i++){
        if(validate[i] == true){
            if(i==5){
                login.disabled = false;
            }
        }else{
            login.disabled = true;
        }
    }
    
}