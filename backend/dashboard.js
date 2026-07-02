// ===============================
// CADMS Dashboard V2
// ===============================

// Statistics Cards
const cameraCount = document.getElementById("cameraCount");
const eventCount = document.getElementById("eventCount");
const intrusionCount = document.getElementById("intrusionCount");
const evidenceCount = document.getElementById("evidenceCount");

// Table
const eventBody = document.getElementById("eventBody");

// Filters
const searchInput = document.getElementById("searchInput");
const cameraFilter = document.getElementById("cameraFilter");
const eventFilter = document.getElementById("eventFilter");

// Store events already displayed
const knownEvents = new Set();

// =========================================
// Remember all events already in the table
// =========================================

document.querySelectorAll("#eventBody tr").forEach(row => {

    if (row.dataset.id) {
        knownEvents.add(row.dataset.id);
    }

});

// =========================================
// Load Statistics
// =========================================

async function loadStats() {

    try {

        const stats = await fetch("/stats").then(r => r.json());

        cameraCount.innerText = stats.cameras;
        eventCount.innerText = stats.events;
        intrusionCount.innerText = stats.intrusions;
        evidenceCount.innerText = stats.evidence;

    }

    catch (err) {

        console.error("Stats Error:", err);

    }

}

// =========================================
// System Status
// =========================================

async function loadSystemStatus() {

    try {

        const data = await fetch("/system").then(r => r.json());

        const status = document.getElementById("systemStatus");

        if (data.status === "ONLINE") {

            status.className = "status online";

            status.innerHTML =
                `🟢 SYSTEM ONLINE<br>${data.connected} / ${data.total} Cameras`;

        }

        else if (data.status === "WARNING") {

            status.className = "status warning";

            status.innerHTML =
                `🟡 SYSTEM WARNING<br>${data.connected} / ${data.total} Cameras`;

        }

        else {

            status.className = "status offline";

            status.innerHTML =
                `🔴 SYSTEM OFFLINE<br>${data.connected} / ${data.total} Cameras`;

        }

    }

    catch (err) {

        console.error("System Status Error:", err);

    }

}

// =========================================
// Load Events
// =========================================

async function loadEvents() {

    try {

        const events = await fetch("/events").then(r => r.json());

        events.forEach(event => {

            const eventId =
                `${event.Date}-${event.Time}-${event.Camera}-${event.Person}`;

            // Skip if already shown
            if (knownEvents.has(eventId))
                return;

            // Remember this event
            knownEvents.add(eventId);

            // Create row
            const row = document.createElement("tr");

            row.dataset.id = eventId;

            row.innerHTML = `
                <td>${event.Date}</td>
                <td>${event.Time}</td>
                <td>${event.Camera}</td>
                <td>${event.Event}</td>
                <td>${event.Person}</td>
                <td>
                    <a href="/evidence?path=${event.Evidence}" target="_blank">
                        View
                    </a>
                </td>
            `;

            // Insert newest event at top
            eventBody.prepend(row);

        });

        // Re-apply filters
        filterTable();

    }

    catch (err) {

        console.error("Events Error:", err);

    }

}

// =========================================
// Search & Filters
// =========================================

function filterTable() {

    const search = searchInput.value.toLowerCase();
    const camera = cameraFilter.value;
    const event = eventFilter.value;

    const rows = eventBody.querySelectorAll("tr");

    rows.forEach(row => {

        const person = row.cells[4].innerText.toLowerCase();
        const cam = row.cells[2].innerText;
        const evt = row.cells[3].innerText;

        let visible = true;

        if (search && !person.includes(search))
            visible = false;

        if (camera && cam !== camera)
            visible = false;

        if (event && evt !== event)
            visible = false;

        row.style.display = visible ? "" : "none";

    });

}

// =========================================
// Event Listeners
// =========================================

searchInput.addEventListener("keyup", filterTable);
cameraFilter.addEventListener("change", filterTable);
eventFilter.addEventListener("change", filterTable);

// =========================================
// Initial Load
// =========================================

loadStats();
loadEvents();
loadSystemStatus();

// =========================================
// Auto Refresh Every 5 Seconds
// =========================================

setInterval(() => {

    loadStats();

    loadEvents();

    loadSystemStatus();

}, 5000);

// =====================================
// Live Date & Time
// =====================================

function updateDateTime() {

    const now = new Date();

    const options = {
        day: "2-digit",
        month: "long",
        year: "numeric"
    };

    document.getElementById("currentDate").innerText =
        now.toLocaleDateString("en-GB", options);

    document.getElementById("currentTime").innerText =
        now.toLocaleTimeString();

}

updateDateTime();

setInterval(updateDateTime, 1000);