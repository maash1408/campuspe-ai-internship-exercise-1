/* ELEMENTS */
const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");
const historyDiv = document.getElementById("chat-history");
const welcome = document.getElementById("welcome");

/* STATE */
let chats = JSON.parse(localStorage.getItem("chats")) || [];
let currentChat = [];

/* INIT */
renderHistory();

/* SEND BUTTON */
sendBtn.onclick = sendMessage;

/* ENTER KEY */
input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

/* AUTO RESIZE TEXTAREA */
input.addEventListener("input", () => {
    input.style.height = "auto";
    input.style.height = input.scrollHeight + "px";
});

/* SEND MESSAGE */
function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    // Hide welcome screen
    if (welcome) welcome.style.display = "none";

    // Add user message
    addMessage(text, "user");
    currentChat.push({ sender: "user", text });

    input.value = "";
    input.style.height = "auto";

    // Show typing animation
    const typing = showTyping();

    setTimeout(() => {
        typing.remove();

        const reply = generateReply(text);

        addMessage(reply, "bot");
        currentChat.push({ sender: "bot", text: reply });

        saveChat();
        scrollDown();
    }, 800);
}

/* BOT RESPONSE */
function generateReply(text) {
    const replies = [
        "Interesting! Tell me more 😊",
        "I understand 👍 Let me think...",
        "Good question! Here's something useful 🚀",
        "Nice! You're doing great 👏",
        "That's a smart thought 💡"
    ];

    return replies[Math.floor(Math.random() * replies.length)];
}

/* ADD MESSAGE */
function addMessage(text, sender) {
    const row = document.createElement("div");
    row.className = `message ${sender}`;

    const inner = document.createElement("div");
    inner.className = "message-inner";

    inner.innerHTML = marked.parse(text);

    row.appendChild(inner);
    chatBox.appendChild(row);

    scrollDown();
}

/* TYPING INDICATOR */
function showTyping() {
    const row = document.createElement("div");
    row.className = "message bot";

    const inner = document.createElement("div");
    inner.className = "message-inner";

    inner.innerHTML = `
        <div class="dots">
            <span></span><span></span><span></span>
        </div>
    `;

    row.appendChild(inner);
    chatBox.appendChild(row);

    scrollDown();

    return row;
}

/* SCROLL */
function scrollDown() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

/* SAVE CHAT */
function saveChat() {
    if (currentChat.length === 0) return;

    // Add title if not exists
    if (!currentChat.title) {
        currentChat.title = currentChat[0]?.text.substring(0, 20);
    }

    // Avoid duplicate push
    if (!chats.includes(currentChat)) {
        chats.push(currentChat);
    }

    localStorage.setItem("chats", JSON.stringify(chats));
    renderHistory();
}

/* LOAD CHAT */
function loadChat(index) {
    chatBox.innerHTML = "";
    currentChat = chats[index];

    if (welcome) welcome.style.display = "none";

    currentChat.forEach(msg => {
        addMessage(msg.text, msg.sender);
    });
}

/* RENDER HISTORY */
function renderHistory() {
    historyDiv.innerHTML = "";

    chats.forEach((chat, i) => {
        const btn = document.createElement("button");

        btn.innerText = chat.title || chat[0]?.text.substring(0, 20) || "New Chat";

        btn.onclick = () => loadChat(i);

        historyDiv.appendChild(btn);
    });
}

/* NEW CHAT BUTTON */
document.getElementById("new-chat").onclick = () => {
    currentChat = [];
    chatBox.innerHTML = "";

    if (welcome) welcome.style.display = "flex";
};

/* SUGGESTIONS CLICK */
document.querySelectorAll(".card").forEach(card => {
    card.onclick = () => {
        input.value = card.innerText;
        sendMessage();
    };
});

/* AUTO FOCUS */
window.onload = () => {
    input.focus();
};