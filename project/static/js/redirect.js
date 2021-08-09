// here is the funcion to make the redirect when the user make a login
// aqui está a função para fazer o redirecionamento quando o usuário faz login
function load(location){
    setTimeout(function() {
        window.location.href = location;
        parent.location.reload();}
        ,2000);
        
}
