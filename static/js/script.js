// Global chart variable
let benchmarkChart = null;

// Cache for use cases (so we don't fetch multiple times)
let useCasesCache = {};

// Toggle use case information display
async function toggleInfo(dataStructure) {
    const infoDiv = document.getElementById(`${dataStructure}-info`);

    // If already visible, just hide it
    if (infoDiv.style.display === 'block') {
        infoDiv.style.display = 'none';
        return;
    }

    // If we haven't fetched the data yet, fetch it
    if (!useCasesCache[dataStructure]) {
        try {
            const res = await fetch(`/api/use-cases?ds=${dataStructure}`);
            const data = await res.json();
            useCasesCache[dataStructure] = data;
        } catch (error) {
            showAlert("Failed to load use case information", "error");
            return;
        }
    }

    // Display the information
    displayUseCases(dataStructure, useCasesCache[dataStructure]);
    infoDiv.style.display = 'block';
}

// Display use case information
function displayUseCases(dataStructure, data) {
    const infoDiv = document.getElementById(`${dataStructure}-info`);

    let html = `
        <h3>💡 ${data.name}</h3>
        
        <h4>✨ Best Used For:</h4>
        <ul>
            ${data.best_for.map(item => `<li>${item}</li>`).join('')}
        </ul>
        
        <h4>🌍 Real-World Examples:</h4>
        <ul>
            ${data.real_world_examples.map(item => `<li>${item}</li>`).join('')}
        </ul>
        
        <h4>✅ Advantages:</h4>
        <ul>
            ${data.advantages.map(item => `<li>${item}</li>`).join('')}
        </ul>
        
        <h4>⚠️ Disadvantages:</h4>
        <ul>
            ${data.disadvantages.map(item => `<li>${item}</li>`).join('')}
        </ul>
        
        <div class="when-to-use">
            <strong>📌 When to Use:</strong> ${data.when_to_use}
        </div>
    `;

    infoDiv.innerHTML = html;
}

// Enhanced complexity display with time and space
async function showDetailedComplexity(ds, op) {
    try {
        const res = await fetch(`/api/complexity/detailed?ds=${ds}&op=${op}`);
        const data = await res.json();

        const elementId = ds === 'linked_list' ? 'll-complexity' : `${ds}-complexity`;
        const complexityDiv = document.getElementById(elementId);

        complexityDiv.innerHTML = `
            <div class="complexity-details">
                <div class="complexity-item">
                    <div class="complexity-label">⏱️ Time Complexity</div>
                    <div class="complexity-value">${data.time}</div>
                    <div class="complexity-explanation">${data.explanation}</div>
                </div>
                <div class="complexity-item">
                    <div class="complexity-label">💾 Space Complexity</div>
                    <div class="complexity-value">${data.space}</div>
                    <div class="complexity-explanation">${data.details}</div>
                </div>
            </div>
        `;
    } catch (error) {
        console.error('Failed to fetch detailed complexity:', error);
        // Fallback to simple complexity display
        showComplexity(ds, op);
    }
}

// Stack Functions
async function pushStack() {
    const value = document.getElementById("stack-input").value;
    if (!value) {
        showAlert("Please enter a value", "warning");
        return;
    }

    const res = await fetch("/api/stack/push", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();
    renderStack(data.state);
    document.getElementById("stack-input").value = "";
    showDetailedComplexity("stack", "insert");
}

async function popStack() {
    const res = await fetch("/api/stack/pop", { method: "POST" });
    const data = await res.json();
    if (data.error) {
        showAlert(data.error, "error");
    } else {
        renderStack(data.state);
        showAlert("Popped: " + data.popped, "success");
    }
    showDetailedComplexity("stack", "delete");
}

async function clearStack() {
    const res = await fetch("/api/stack/clear", { method: "POST" });
    const data = await res.json();
    renderStack(data.state);
    document.getElementById("stack-complexity").textContent = "";
}

async function peekStack() {
    const res = await fetch("/api/stack/peek", { method: "GET" });
    const data = await res.json();
    if (data.error) {
        showAlert(data.error, "error");
    } else {
        showAlert(`Top element: ${data.value}`, "info");
        // Highlight the top element temporarily
        const boxes = document.querySelectorAll("#stack-visual .box");
        if (boxes.length > 0) {
            boxes[0].style.transform = "scale(1.1)";
            boxes[0].style.boxShadow = "0 4px 16px rgba(24, 119, 242, 0.6)";
            setTimeout(() => {
                boxes[0].style.transform = "";
                boxes[0].style.boxShadow = "";
            }, 1000);
        }
    }
}

async function searchStack() {
    const value = document.getElementById("stack-input").value;
    if (!value) {
        showAlert("Please enter a value to search", "warning");
        return;
    }

    const res = await fetch("/api/stack/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();

    if (data.found) {
        showAlert(data.message, "success");
        // Highlight the found element
        const boxes = document.querySelectorAll("#stack-visual .box");
        if (boxes[data.index]) {
            boxes[data.index].style.background = "linear-gradient(135deg, #42b72a 0%, #2d8a1e 100%)";
            setTimeout(() => {
                boxes[data.index].style.background = "";
            }, 2000);
        }
    } else {
        showAlert(data.message, "warning");
    }
    showDetailedComplexity("stack", "search");
}

function renderStack(state) {
    const container = document.getElementById("stack-visual");
    container.innerHTML = "";
    if (state.length === 0) {
        container.classList.add('empty');
        return;
    }
    container.classList.remove('empty');
    [...state].reverse().forEach((val) => {
        const box = document.createElement("div");
        box.className = "box";
        box.textContent = val;
        container.appendChild(box);
    });
}

// Queue Functions
async function enqueueQueue() {
    const value = document.getElementById("queue-input").value;
    if (!value) {
        showAlert("Please enter a value", "warning");
        return;
    }

    const res = await fetch("/api/queue/enqueue", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();
    renderQueue(data.state);
    document.getElementById("queue-input").value = "";
    showDetailedComplexity("queue", "insert");
}

async function dequeueQueue() {
    const res = await fetch("/api/queue/dequeue", { method: "POST" });
    const data = await res.json();
    if (data.error) {
        showAlert(data.error, "error");
    } else {
        renderQueue(data.state);
        showAlert("Dequeued: " + data.dequeued, "success");
    }
    showDetailedComplexity("queue", "delete");
}

async function clearQueue() {
    const res = await fetch("/api/queue/clear", { method: "POST" });
    const data = await res.json();
    renderQueue(data.state);
    document.getElementById("queue-complexity").textContent = "";
}

async function peekQueue() {
    const res = await fetch("/api/queue/peek", { method: "GET" });
    const data = await res.json();
    if (data.error) {
        showAlert(data.error, "error");
    } else {
        showAlert(`Front element: ${data.value}`, "info");
        // Highlight the front element
        const boxes = document.querySelectorAll("#queue-visual .box");
        if (boxes.length > 0) {
            boxes[0].style.transform = "scale(1.1)";
            boxes[0].style.boxShadow = "0 4px 16px rgba(24, 119, 242, 0.6)";
            setTimeout(() => {
                boxes[0].style.transform = "";
                boxes[0].style.boxShadow = "";
            }, 1000);
        }
    }
}

async function searchQueue() {
    const value = document.getElementById("queue-input").value;
    if (!value) {
        showAlert("Please enter a value to search", "warning");
        return;
    }

    const res = await fetch("/api/queue/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();

    if (data.found) {
        showAlert(data.message, "success");
        // Highlight the found element
        const boxes = document.querySelectorAll("#queue-visual .box");
        if (boxes[data.index]) {
            boxes[data.index].style.background = "linear-gradient(135deg, #42b72a 0%, #2d8a1e 100%)";
            setTimeout(() => {
                boxes[data.index].style.background = "";
            }, 2000);
        }
    } else {
        showAlert(data.message, "warning");
    }
    showDetailedComplexity("queue", "search");
}

function renderQueue(state) {
    const container = document.getElementById("queue-visual");
    container.innerHTML = "";
    if (state.length === 0) {
        container.classList.add('empty');
        return;
    }
    container.classList.remove('empty');
    state.forEach((val) => {
        const box = document.createElement("div");
        box.className = "box";
        box.textContent = val;
        container.appendChild(box);
    });
}

// Linked List Functions
async function insertLL() {
    const value = document.getElementById("ll-input").value;
    if (!value) {
        showAlert("Please enter a value", "warning");
        return;
    }

    const res = await fetch("/api/linkedlist/insert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();
    renderLL(data.state);
    document.getElementById("ll-input").value = "";

    // Use detailed complexity display
    showDetailedComplexity("linked_list", "insert");
}

async function deleteLL() {
    const value = document.getElementById("ll-input").value;
    if (!value) {
        showAlert("Please enter a value to delete", "warning");
        return;
    }

    const res = await fetch("/api/linkedlist/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();
    renderLL(data.state);
    document.getElementById("ll-input").value = "";

    // Use detailed complexity display
    showDetailedComplexity("linked_list", "delete");

    if (data.deleted) {
        showAlert("Successfully deleted: " + value, "success");
    } else {
        showAlert("Value not found: " + value, "warning");
    }
}

async function clearLL() {
    const res = await fetch("/api/linkedlist/clear", { method: "POST" });
    const data = await res.json();
    renderLL(data.state);
    document.getElementById("ll-complexity").textContent = "";
}

async function searchLL() {
    const value = document.getElementById("ll-input").value;
    if (!value) {
        showAlert("Please enter a value to search", "warning");
        return;
    }

    const res = await fetch("/api/linkedlist/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ value }),
    });
    const data = await res.json();

    if (data.found) {
        showAlert(data.message, "success");
        // Highlight the found element
        const boxes = document.querySelectorAll("#ll-visual .box");
        if (boxes[data.index]) {
            boxes[data.index].style.background = "linear-gradient(135deg, #42b72a 0%, #2d8a1e 100%)";
            setTimeout(() => {
                boxes[data.index].style.background = "";
            }, 2000);
        }
    } else {
        showAlert(data.message, "warning");
    }
    showDetailedComplexity("linked_list", "search");
}

function renderLL(state) {
    const container = document.getElementById("ll-visual");
    container.innerHTML = "";
    if (state.length === 0) {
        container.classList.add('empty');
        return;
    }
    container.classList.remove('empty');
    state.forEach((val, idx) => {
        const box = document.createElement("div");
        box.className = "box";
        box.textContent = val;
        container.appendChild(box);

        if (idx < state.length - 1) {
            const arrow = document.createElement("span");
            arrow.textContent = " → ";
            container.appendChild(arrow);
        }
    });
}

// Complexity Display
async function showComplexity(ds, op) {
    const res = await fetch(`/api/complexity?ds=${ds}&op=${op}`);
    const data = await res.json();
    const elementId = ds === 'linked_list' ? 'll-complexity' : `${ds}-complexity`;
    document.getElementById(elementId).textContent = `⏱️ Time Complexity: ${data.complexity}`;
}

// Benchmark Functions
async function runBenchmark() {
    const ds = document.getElementById("bench-ds").value;
    const op = document.getElementById("bench-op").value;
    const loadingDiv = document.getElementById("benchmark-loading");
    const outputDiv = document.getElementById("benchmark-output");

    // Show loading
    loadingDiv.style.display = "block";
    outputDiv.innerHTML = "";

    try {
        const res = await fetch(`/api/benchmark?ds=${ds}&op=${op}`);
        const data = await res.json();

        if (data.error) {
            showAlert(data.error, "error");
            return;
        }

        // Hide loading
        loadingDiv.style.display = "none";

        // Display results
        let output = `<h3>📊 Benchmark Results for ${formatDSName(ds)} - ${formatOpName(op)}</h3>`;
        output += `<p><strong>Predicted Complexity:</strong> <span style="color: #1877f2; font-size: 16px;">${data.predicted}</span></p>`;
        output += `<table>
            <thead>
                <tr>
                    <th>Input Size (n)</th>
                    <th>Execution Time (seconds)</th>
                    <th>Operations/Second</th>
                </tr>
            </thead>
            <tbody>`;

        data.sizes.forEach((size, i) => {
            const opsPerSec = (size / data.times[i]).toFixed(0);
            output += `<tr>
                <td>${size.toLocaleString()}</td>
                <td>${data.times[i].toFixed(6)}</td>
                <td>${Number(opsPerSec).toLocaleString()}</td>
            </tr>`;
        });

        output += `</tbody></table>`;
        outputDiv.innerHTML = output;

        // Create or update chart
        createBenchmarkChart(data);

    } catch (error) {
        loadingDiv.style.display = "none";
        showAlert("Error running benchmark: " + error.message, "error");
    }
}

// Create Chart.js visualization
function createBenchmarkChart(data) {
    const ctx = document.getElementById('benchmarkChart');

    // Destroy existing chart if it exists
    if (benchmarkChart) {
        benchmarkChart.destroy();
    }

    benchmarkChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.sizes.map(s => s.toLocaleString()),
            datasets: [{
                label: 'Actual Execution Time (seconds)',
                data: data.times,
                borderColor: '#1877f2',
                backgroundColor: 'rgba(24, 119, 242, 0.1)',
                borderWidth: 3,
                tension: 0.4,
                fill: true,
                pointRadius: 6,
                pointHoverRadius: 8,
                pointBackgroundColor: '#1877f2',
                pointBorderColor: '#fff',
                pointBorderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                title: {
                    display: true,
                    text: `Performance: ${formatDSName(data.data_structure)} - ${formatOpName(data.operation)} - ${data.predicted}`,
                    font: {
                        size: 16,
                        weight: 'bold',
                        family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
                    },
                    color: '#1c1e21',
                    padding: 20
                },
                legend: {
                    display: true,
                    position: 'top',
                    labels: {
                        font: {
                            size: 13,
                            family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif'
                        },
                        color: '#1c1e21',
                        padding: 15
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(28, 30, 33, 0.9)',
                    titleFont: {
                        size: 14,
                        weight: 'bold'
                    },
                    bodyFont: {
                        size: 13
                    },
                    padding: 12,
                    cornerRadius: 6,
                    callbacks: {
                        label: function(context) {
                            return `Time: ${context.parsed.y.toFixed(6)} seconds`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Input Size (n)',
                        font: {
                            size: 14,
                            weight: 'bold'
                        },
                        color: '#1c1e21'
                    },
                    grid: {
                        color: '#e4e6eb'
                    },
                    ticks: {
                        color: '#65676b',
                        font: {
                            size: 12
                        }
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Execution Time (seconds)',
                        font: {
                            size: 14,
                            weight: 'bold'
                        },
                        color: '#1c1e21'
                    },
                    grid: {
                        color: '#e4e6eb'
                    },
                    ticks: {
                        color: '#65676b',
                        font: {
                            size: 12
                        },
                        callback: function(value) {
                            return value.toFixed(4);
                        }
                    },
                    beginAtZero: true
                }
            }
        }
    });
}

// Helper Functions
function formatDSName(ds) {
    const names = {
        'stack': 'Stack',
        'queue': 'Queue',
        'linked_list': 'Linked List'
    };
    return names[ds] || ds;
}

function formatOpName(op) {
    const names = {
        'insert': 'Insert',
        'delete': 'Delete',
        'search': 'Search'
    };
    return names[op] || op;
}

function showAlert(message, type) {
    // Create a simple alert system (could be enhanced with a toast notification library)
    const alertTypes = {
        'success': '✅',
        'error': '❌',
        'warning': '⚠️',
        'info': 'ℹ️'
    };

    alert(`${alertTypes[type] || ''} ${message}`);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('Data Structure Learning Tool Loaded');
});

