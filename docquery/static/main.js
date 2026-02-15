document.addEventListener("DOMContentLoaded", function () {
    const modalElement = document.getElementById("welcomeModal");

    if (modalElement) {
        const welcomeModal = new bootstrap.Modal(modalElement);
        welcomeModal.show();
    }
});


// Chatbot logic
// Append message to chat container
function appendMessage(role, text) {
    const chat = document.getElementById("chat-container");

    const msg = document.createElement("div");
    msg.classList.add("chat-message");

    if (role === "user") {
        msg.classList.add("user-message");
    } else {
        msg.classList.add("bot-message");
    }

    msg.innerText = text;
    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;

    return msg;
}


// Handle form submit (THIS replaces your loop)
document.getElementById("messageArea").addEventListener("submit", async function (e) {
    e.preventDefault(); // stop normal form POST

    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (!message) return;

    // Show user message
    appendMessage("user", message);
    input.value = "";

    // Show typing indicator
    const typingBubble = appendMessage("bot", "Typing...");

    try {
        // Send message to backend
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Replace typing with actual response
        typingBubble.innerText = data.answer;

    } catch (err) {
        typingBubble.innerText = "Error occurred. Please try again.";
    }
});
