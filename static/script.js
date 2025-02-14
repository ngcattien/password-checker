document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.querySelector('input[name="password"]');
    const feedbackContainer = document.createElement('div');
    passwordInput.parentNode.insertBefore(feedbackContainer, passwordInput.nextSibling);

    // Add client-side validation for password length
    document.querySelector('form').onsubmit = function() {
        if (passwordInput.value.length < 6) {
            alert('Password too short. Must be at least 6 characters.');
            return false; // Prevent form submission if password is too short
        }
    };

    // Real-time password strength feedback
    passwordInput.addEventListener('input', function() {
        const value = passwordInput.value;
        let strength = 'Weak';
        let color = 'red';
        if (value.length > 5 && /\d/.test(value) && /[a-zA-Z]/.test(value)) {
            strength = 'Moderate';
            color = 'orange';
        }
        if (value.length > 8 && /\d/.test(value) && /[a-zA-Z]/.test(value) && /[^a-zA-Z\d]/.test(value)) {
            strength = 'Strong';
            color = 'green';
        }
        if (value.length === 0) {
            feedbackContainer.textContent = '';
        } else {
            feedbackContainer.textContent = `Strength: ${strength}`;
            feedbackContainer.style.color = color;
        }
    });
});