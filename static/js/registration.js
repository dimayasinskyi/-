document.getElementById('register').addEventListener('submit', function (event) {
        const firstName = document.getElementById('FirstNameInput').value.trim();
        const lastName = document.getElementById('LastNameInput').value.trim();
        const email = document.getElementById('EmailInput').value.trim();
        const password1 = document.getElementById('Password1Input').value.trim();
        const password2 = document.getElementById('Password2Input').value.trim();
    
        if (!firstName || !lastName || !email || !password1 || !password2) {
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
    
        if (password1 !== password2) {
            alert("Паролі не співпадають.");
            event.preventDefault();
            return;
        }
    
        if (password1.length < 4) {
            alert("Пароль має бути не менше 4 символів.");
            event.preventDefault();
            return;
    }});