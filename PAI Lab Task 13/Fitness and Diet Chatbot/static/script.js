async function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value;
    if (!message) return;
    
    addMessage("You", message, "user-msg");
    userInput.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    });
    const data = await response.json();
    addMessage("Bot", data.response, "bot-msg");
}

function addMessage(sender, message, cssClass) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = cssClass;
    msg.textContent = `${sender}: ${message}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function loadQuestions() {
    const res = await fetch("/static/qa_data.json");
    const data = await res.json();
    const list = document.getElementById("question-list");
    Object.keys(data).forEach(q => {
        const li = document.createElement("li");
        li.textContent = q;
        li.onclick = () => {
            document.getElementById("user-input").value = q;
        };
        list.appendChild(li);
    });
}

function filterQuestions() {
    const filter = document.getElementById("search").value.toLowerCase();
    const items = document.querySelectorAll("#question-list li");
    items.forEach(item => {
        item.style.display = item.textContent.toLowerCase().includes(filter) ? "" : "none";
    });
}

window.onload = loadQuestions;
