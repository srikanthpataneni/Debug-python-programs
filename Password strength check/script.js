function checkPasswordStrength() {
    const password = document.getElementById("password").value;
    const strengthIndicator = document.getElementById("strength");

    let strength = 0;

    // Check for length
    if (password.length > 8) {
        strength += 1;
    } else if (password.length > 6) {
        strength += 0.5;
    }

    // Check for uppercase letters
    if (/[A-Z]/.test(password)) {
        strength += 1;
    }

    // Check for lowercase letters
    if (/[a-z]/.test(password)) {
        strength += 1;
    }

    // Check for digits
    if (/\d/.test(password)) {
        strength += 1;
    }

    // Check for special characters
    if (/[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]/.test(password)) {
        strength += 1;
    }

    // Display strength
    if (strength >= 4) {
        strengthIndicator.innerText = "Strong";
        strengthIndicator.style.color = "green";
    } else if (strength >= 2) {
        strengthIndicator.innerText = "Medium";
        strengthIndicator.style.color = "orange";
    } else {
        strengthIndicator.innerText = "Weak";
        strengthIndicator.style.color = "red";
    }
}
