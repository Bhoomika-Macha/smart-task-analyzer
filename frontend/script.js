function cleanJSON(text) {
    return text.replace(/[\u200B-\u200F\uFEFF]/g, '').trim();
}

async function analyzeTasks() {
    try {
        const data = JSON.parse(cleanJSON(document.getElementById("taskInput").value));

        const res = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        displayResults(await res.json());
    } catch {
        alert("Invalid JSON Format");
    }
}

async function suggestTasks() {
    try {
        const data = JSON.parse(cleanJSON(document.getElementById("taskInput").value));

        const res = await fetch("http://127.0.0.1:8000/api/tasks/suggest/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        displayResults((await res.json()).suggested_tasks);
    } catch {
        alert("Invalid JSON Format");
    }
}

function displayResults(tasks) {
    document.getElementById("results").innerHTML = "";
    tasks.forEach(t => {
        const c = document.createElement("div");
        c.className = "task-card";
        c.innerHTML = `
            <h3>${t.title}</h3>
            <p><strong>Score:</strong> ${t.score}</p>
            <p><strong>Due:</strong> ${t.due_date}</p>
            <p><strong>Importance:</strong> ${t.importance}</p>
            <p><strong>Hours:</strong> ${t.estimated_hours}</p>
        `;
        document.getElementById("results").appendChild(c);
    });
}
