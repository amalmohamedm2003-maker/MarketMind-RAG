async function runAnalysis() {
  const question = document.getElementById("question").value;

  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("result").classList.add("hidden");

  const response = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await response.json();

  document.getElementById("loading").classList.add("hidden");
  document.getElementById("result").classList.remove("hidden");

  document.getElementById("summary").innerText = data.summary;

  renderList("insights", data.key_insights);
  renderList("recommendations", data.recommendations);

  document.getElementById("metrics").innerText =
    JSON.stringify(data.metrics_impact, null, 2);

  document.getElementById("confidence").innerText = data.confidence_level;
}

function renderList(id, items) {
  const el = document.getElementById(id);
  el.innerHTML = "";

  if (!items || items.length === 0) {
    el.innerHTML = "<li>No data</li>";
    return;
  }

  items.forEach(item => {
    const li = document.createElement("li");
    li.innerText = item;
    el.appendChild(li);
  });
}
