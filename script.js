const toggleButton = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

toggleButton.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});