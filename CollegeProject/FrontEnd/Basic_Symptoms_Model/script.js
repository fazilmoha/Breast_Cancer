function redirectToPage() {
    // Change the URL to the desired page
    window.location.href = "../Diagnostic_Value_Model/index.html";
}
document.getElementById('medical-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect form data
    const formData = {
        lump_mass: document.getElementById('lump_mass').value,
        breast_changes: document.getElementById('breast_changes').value,
        skin_changes: document.getElementById('skin_changes').value,
        nipple_changes: document.getElementById('nipple_changes').value,
        breast_pain: document.getElementById('breast_pain').value,
        armpit_swelling: document.getElementById('armpit_swelling').value,
        texture_color_changes: document.getElementById('texture_color_changes').value,
        nipple_discharge: document.getElementById('nipple_discharge').value,
        family_history: document.getElementById('family_history').value,
        age: parseInt(document.getElementById('age').value)
    };

    // Convert form data to JSON
    const jsonData = JSON.stringify(formData);

    // Send JSON data via POST request
    fetch('http://localhost:5000/basic_symptoms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        return response.json();
    })
    .then(data => {
        // Handle response from server
        document.getElementById('response-message').innerHTML = `<p>${data.prediction}</p>`;
    })
    .catch(error => {
        document.getElementById('response-message').innerHTML = `<p>Error: ${error.message}</p>`;
    });

    
});

function getHospitals() {
var city = document.getElementById("cityInput").value;
var url = "http://localhost:5000/hospitals?city=" + encodeURIComponent(city);

fetch(url)
.then(response => response.json())
.then(data => {
var hospitalList = document.getElementById("hospitalList");
hospitalList.innerHTML = ""; // Clear previous results

if (data.error) {
    hospitalList.innerHTML = "<p>" + data.error + "</p>";
} else {
    var hospitals = data.hospitals;
    if (hospitals.length > 0) {
        var html = "<h3>Hospitals in " + city + ":</h3>";
        html += "<ul>";
        hospitals.forEach(function(hospital) {
            html += "<li>" + hospital + "</li>";
        });
        html += "</ul>";
        hospitalList.innerHTML = html;
    } else {
        hospitalList.innerHTML = "<p>No hospitals found in " + city + "</p>";
    }
}
})
.catch(error => {
console.error('Error:', error);
var hospitalList = document.getElementById("hospitalList");
hospitalList.innerHTML = "<p>Failed to fetch hospitals</p>";
});
}