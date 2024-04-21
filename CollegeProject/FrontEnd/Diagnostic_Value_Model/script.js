document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    // Create a JSON object with form data
    const formData = {
        texture_mean: document.getElementById('texture_mean').value,
        smoothness_mean: document.getElementById('smoothness_mean').value,
        compactness_mean: document.getElementById('compactness_mean').value,
        concave_points_mean: document.getElementById('concave_points_mean').value,
        symmetry_mean: document.getElementById('symmetry_mean').value,
        fractal_dimension_mean: document.getElementById('fractal_dimension_mean').value,
        texture_se: document.getElementById('texture_se').value,
        area_se: document.getElementById('area_se').value,
        smoothness_se: document.getElementById('smoothness_se').value,
        compactness_se: document.getElementById('compactness_se').value,
        concavity_se: document.getElementById('concavity_se').value,
        concave_points_se: document.getElementById('concave_points_se').value,
        symmetry_se: document.getElementById('symmetry_se').value,
        fractal_dimension_se: document.getElementById('fractal_dimension_se').value,
        texture_worst: document.getElementById('texture_worst').value,
        area_worst: document.getElementById('area_worst').value,
        smoothness_worst: document.getElementById('smoothness_worst').value,
        compactness_worst: document.getElementById('compactness_worst').value,
        concavity_worst: document.getElementById('concavity_worst').value,
        concave_points_worst: document.getElementById('concave_points_worst').value,
        symmetry_worst: document.getElementById('symmetry_worst').value,
        fractal_dimension_worst: document.getElementById('fractal_dimension_worst').value
    };

    // Send the JSON data to your Flask API using fetch
    fetch('http://127.0.0.1:5000/diagnostic_value', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle response from server
        document.getElementById('response-message').innerHTML = `<p>${data.Result}</p>`;
        console.log(data.Result);
    })
    .catch(error => {
        document.getElementById('response-message').innerHTML = `<p>Error: ${error.message}</p>`;
    });
});
