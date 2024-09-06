document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');
    const scrollDownButton = document.getElementById('scroll-down');
    const backButton = document.getElementById('back-button');

    function addMessage(message, fromUser = true) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${fromUser ? 'user-message' : 'bot-message'}`;

        const profilePic = document.createElement('img');
        profilePic.src = fromUser ? 'user.png' : 'bot.png'; 
        profilePic.alt = fromUser ? 'User Profile' : 'Bot Profile';

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.textContent = message;

        if (fromUser) {
            messageDiv.appendChild(messageContent);
            messageDiv.appendChild(profilePic); 
        } else {
            messageDiv.appendChild(profilePic); 
            messageDiv.appendChild(messageContent);
        }

        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function handleSendMessage() {
        const message = chatInput.value.trim();
        if (message) {
            addMessage(message, true); 
            chatInput.value = '';
            
            setTimeout(() => addMessage('This is a response from the bot.', false), 1000);
        }
    }

    sendButton.addEventListener('click', handleSendMessage);
    chatInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            handleSendMessage();
        }
    });

    scrollDownButton.addEventListener('click', () => {
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    backButton.addEventListener('click', () => {
        
        alert('Back button clicked. Implement your exit logic.');
    });
});

