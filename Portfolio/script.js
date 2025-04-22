// script.js
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;

    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-theme');
        const icon = themeToggle.querySelector('i');
        if (body.classList.contains('dark-theme')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    });

    const toggleSkillsButton = document.getElementById('toggleSkills');
    const skillsList = document.getElementById('skillsList');

    toggleSkillsButton.addEventListener('click', function() {
        skillsList.classList.toggle('visible');
        if (skillsList.classList.contains('visible')) {
            toggleSkillsButton.textContent = 'Hide Skills';
        } else {
            toggleSkillsButton.textContent = 'Show Skills';
        }
    });

    const contactForm = document.getElementById('contactForm');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const messageInput = document.getElementById('message');
    const nameError = document.getElementById('nameError');
    const emailError = document.getElementById('emailError');
    const messageError = document.getElementById('messageError');

    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        // Reset error messages
        nameError.textContent = '';
        emailError.textContent = '';
        messageError.textContent = '';
        nameError.classList.remove('visible');
        emailError.classList.remove('visible');
        messageError.classList.remove('visible');

        let isValid = true;

        // Validate Name
        if (nameInput.value.trim() === '') {
            nameError.textContent = 'Name is required';
            nameError.classList.add('visible');
            isValid = false;
        }

        // Validate Email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (emailInput.value.trim() === '') {
            emailError.textContent = 'Email is required';
            emailError.classList.add('visible');
            isValid = false;
        } else if (!emailPattern.test(emailInput.value.trim())) {
            emailError.textContent = 'Invalid email address';
            emailError.classList.add('visible');
            isValid = false;
        }

        // Validate Message
        if (messageInput.value.trim() === '') {
            messageError.textContent = 'Message is required';
            messageError.classList.add('visible');
            isValid = false;
        }

        // If all fields are valid, submit the form
        if (isValid) {
            alert('Thank you for your message!');
            contactForm.reset();
        }
    });
});