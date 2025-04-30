document.getElementById('order').addEventListener('submit', function (event) {
    event.preventDefault();

    const nameCar = document.getElementById('nameCarInput').value.trim();
    const termTime = document.getElementById('termTimeInput').value.trim();
    const price = document.getElementById('priceTimeInput').value.trim();
    const sum = document.getElementById('sumInput').value.trim();


    if (!price) {
        alert("Щось пішло не так");
        event.preventDefault();
        return;
    };

    if (!nameCar) {
        alert("Щось пішло не так");
        event.preventDefault();
        return;
    };

    if (!sum) {
        alert("Щось пішло не так");
        event.preventDefault();
        return;
    };

    if ((!termTime)) {
        alert("Будь ласка, заповніть поле 'Темірн'.");
        event.preventDefault();
        return;
    } else {
        alert("Помилка 500");
    }

});

const termInput = document.getElementById('termTimeInput');
const priceInput = document.getElementById('priceTimeInput');
const sumInput = document.getElementById('sumInput');


function updateTotal() {
    const term = parseInt(termInput.value) || 0;
    const pricePerMonth = parseInt(priceInput.value) || 0; 

    const totalPrice = term * pricePerMonth; 
    sumInput.value = totalPrice; 
}

termInput.addEventListener('input', updateTotal);
priceInput.addEventListener('input', updateTotal);

window.addEventListener('load', updateTotal);