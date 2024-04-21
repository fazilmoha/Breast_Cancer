document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    let username = document.getElementById("login-username").value;
    let password = document.getElementById("login-password").value;

    // You can perform login/authentication logic here
    console.log("Login:", username, password);

    fetch('http://localhost:5000/login',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Login failed');
      }
    })
    .then(data => {
      // Handle successful login
      console.log('Login successful:', data);
      // Redirect to dashboard or perform any other action
      window.location.href = '../Basic_Symptoms_Model/index.html';
    })
    .catch(error => {
      // Handle login failure
      console.error('Login error:', error.message);
      // Display error message to user or perform any other action
    });
  });