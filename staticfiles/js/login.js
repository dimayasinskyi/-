document.getElementById('login').addEventListener('submit', function (event) {
    const email = document.getElementById('EmailInput').value.trim();
    const password1 = document.getElementById('PasswordInput').value.trim();

    if (!email || !password1) {
        alert("Будь ласка, заповніть всі поля.");
        event.preventDefault();
        return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Введіть коректний email.");
        event.preventDefault();
        return;
    }

    if (password1) {
        alert("Невірний пароль");
        event.preventDefault();
        return;
}});