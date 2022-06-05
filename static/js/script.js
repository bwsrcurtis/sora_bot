function updateConvo(message) {
    
    const response = conversation.dataset.response;
    sessionStorage.setItem(message, response);
    console.log(sessionStorage.getItem(message))
    console.log(sessionStorage.key(response))
    return
}

const conversation = document.querySelector(".message-container");
const message = conversation.dataset.message;
document.querySelector(".form-overall").onsubmit = updateConvo(message);