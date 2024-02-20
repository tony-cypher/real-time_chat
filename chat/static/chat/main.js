const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const username = JSON.parse(document.getElementById('json-username').textContent);
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + roomName
    + '/'
);
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    if (data.message) {
        let html = data.username + ': ' + data.message + '<br>'
        document.getElementById('chat-messages').innerHTML += html;
        scroll();
    } else {
        alert('The message is empty');
    };

}
chatSocket.onclose = function (e) {
    console.error('Socket closed unexpectedly');
};


document.getElementById('send').onclick = function (e) {
    e.preventDefault()
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value;

    // sending the message to the consumer.py from chatSocket
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
        'room': roomName
    }));

    messageInput.value = '';
};

// for scroll functionality
function scroll() {
    const mcontainer = document.getElementById('chat-messages');
    mcontainer.scrollTop = m.mcontainer.scrollHeight;
}

scroll();