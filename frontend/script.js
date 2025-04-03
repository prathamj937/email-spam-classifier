async function classifyEmail() {
    const emailText = document.getElementById("emailText").value;
    const resultElement = document.getElementById("result");

    if (!emailText.trim()) {
        resultElement.innerHTML = "⚠️ Please enter email text.";
        resultElement.style.color = "red";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: emailText })
        });

        const data = await response.json();
        resultElement.innerHTML = `📝 Result: <strong>${data.result}</strong>`;
        resultElement.style.color = data.result === "Spam" ? "red" : "green";
    } catch (error) {
        resultElement.innerHTML = "❌ Error: Unable to connect to server.";
        resultElement.style.color = "red";
    }
}