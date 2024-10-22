const signupModal = document.getElementById("signup");
const signinModal = document.getElementById("signin");
const closeButtons = document.querySelectorAll(".close-button");

document.querySelectorAll('.nav-button').forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        const target = event.target.getAttribute('href');
        if (target === "#signup") {
            signupModal.style.display = "block";
        } else if (target === "#signin") {
            signinModal.style.display = "block";
        }
    });
});

closeButtons.forEach(button => {
    button.addEventListener('click', () => {
        signupModal.style.display = "none";
        signinModal.style.display = "none";
    });
});

window.addEventListener('click', (event) => {
    if (event.target === signupModal || event.target === signinModal) {
        signupModal.style.display = "none";
        signinModal.style.display = "none";
    }
});

// Validate Signup Form
document.getElementById("signup-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    // Basic validation
    if (username === "") {
        alert("Username is required.");
        return;
    }
    
    if (!validateEmail(email)) {
        alert("Please enter a valid email.");
        return;
    }

    if (!validatePassword(password)) {
        alert("Password must contain at least one uppercase letter, one lowercase letter, one number, and be at least 6 characters long.");
        return;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    // Simulate successful signup
    alert("Signup successful!");
    signupModal.style.display = "none";
});

// Password validation function
function validatePassword(password) {
    const hasUppercase = /[A-Z]/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);
    const isLongEnough = password.length >= 6;

    return hasUppercase && hasLowercase && hasNumber && isLongEnough;
}

// Email validation function
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

// Show password requirements on focus
document.getElementById("password").addEventListener("focus", function() {
    const requirements = document.getElementById("password-requirements");
    requirements.innerHTML = "Password must include:<br>- At least one uppercase letter<br>- At least one lowercase letter<br>- At least one number<br>- At least 6 characters long";
});
``
