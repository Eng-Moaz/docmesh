async function askAI() {

    const question =
        document.getElementById("question").value

    const response = await fetch(
        "http://localhost:8080/chat",
        {
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                question
            })
        }
    )

    const data = await response.json()

    document.getElementById("answer").innerHTML = `
        <h3>Answer</h3>

        <p>${data.answer}</p>

        <h4>Sources</h4>

        <ul>
            ${data.sources.map(
                s=>`<li>${s}</li>`
            ).join("")}
        </ul>
    `
}
