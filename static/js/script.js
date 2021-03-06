const conversation = document.querySelector(".message-container");

function updateConvo() {
    const displayMessage = document.querySelector(".message");
    const displayResponse = document.querySelector(".result");
    const message = conversation.dataset.message;
    const response = conversation.dataset.response;
    sessionStorage.setItem(message, response);
    displayMessage.innerHTML = message;
    setTimeout(function(){
        displayResponse.innerHTML = sessionStorage.getItem(message)}, 1750);
    return
}


document.querySelector(".form-overall").onsubmit = updateConvo();