document.getElementById("signup-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let username = document.getElementById("signup-username").value;
    let email = document.getElementById("signup-email").value;
    let password = document.getElementById("signup-password").value;

    // You can perform signup/authentication logic here
    console.log("Signup:", username, email, password);

    fetch('http://localhost:5000/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, email, password }),
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Signup failed');
      }
    })
    .then(data => {
      // Handle successful signup
      console.log('Signup successful:', data);
      // Redirect to login page or perform any other action
      window.location.href = '../Login/index.html';
    })
    .catch(error => {
      // Handle signup failure
      console.error('Signup error:', error.message);
      // Display error message to user or perform any other action
    });
  });