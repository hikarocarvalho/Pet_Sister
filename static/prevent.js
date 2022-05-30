
let input_name = document.querySelector('#input_name');
let input_email = document.querySelector('#input_email');
let input_message = document.querySelector('#input_message');
let send = document.getElementById("send");
let nomeOk = false;
let emailOk = false;
let msgOk = false;


input_name.addEventListener('keyup', () => {
   if (input_name.value.length < 3) {
      input_name.style.borderColor = 'red';
      nomeOk = false;
   } else {
      input_name.style.borderColor = 'green';
      nomeOk = true;
   }

   if (nomeOk && emailOk && msgOk) {
      send.disabled = false;
   } else {
      send.disabled = true;
   }
})

input_email.addEventListener('keyup', () => {
   if (input_email.value.indexOf('@') == -1 || input_email.value.indexOf('.') == -1) {
        input_email.style.borderColor = 'red';
        emailOk = false;
   } else {
        input_email.style.borderColor = 'green';
        emailOk = true;
   }

   if (nomeOk && emailOk && msgOk) {
        send.disabled = false;
   } else {
        send.disabled = true;
   }
})

input_message.addEventListener('keyup', () => {
   if (input_message.value.length > 500) {
        input_message.style.borderColor = 'red';
        msgOk = false;
   } else {
        input_message.style.borderColor = 'green';
        msgOk = true;
   }

   if (nomeOk && emailOk && msgOk) {
        send.disabled = false;
   } else {
        send.disabled = true;
   }
})

send.addEventListener("click", function(event){
    let load = document.querySelector('#load')
   load.style.display = 'flex'

   /* Esconde o Form */
   let form = document.querySelector('#form')
   form.style.display = 'none'

    
  })
