const backendUrl = "/predict"; // No need for localhost or port since Flask serves everything

document.getElementById("check-button").addEventListener("click", async () => {
    const emailText = document.getElementById("email-input").value.trim();
    const resultDiv = document.getElementById("result");

    if (!emailText) {
        resultDiv.innerHTML = "<p style='color: red;'>Please enter email text.</p>";
        return;
    }

    try {
        const response = await fetch(backendUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email: emailText })
        });

        const data = await response.json();
        resultDiv.innerHTML = `<p><strong>Result:</strong> ${data.result}</p>`;
    } catch (error) {
        resultDiv.innerHTML = "<p style='color: red;'>Error connecting to the server.</p>";
        console.error("Error:", error);
    }
});
