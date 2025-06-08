function classifyEmail() {
    const email = document.getElementById("emailText").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.result || data.error;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
