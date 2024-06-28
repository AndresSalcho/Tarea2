document.getElementById('ticketForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const Mes = document.getElementById('mes').value;
    var auxMes = "";

    switch (Mes){
        case 'ene': auxMes = "01"; break
        case 'feb': auxMes = "02"; break
        case 'mar': auxMes = "03"; break
        case 'abr': auxMes = "04"; break
        case 'may': auxMes = "05"; break
        case 'jun': auxMes = "06"; break
        case 'jul': auxMes = "07"; break
        case 'ago': auxMes = "08"; break
        case 'set': auxMes = "09"; break
        case 'oct': auxMes = "10"; break
        case 'nov': auxMes = "11"; break
        case 'dic': auxMes = "12"; break
    }

    const Serie = document.getElementById('serie').value;
    const Numero = document.getElementById('num').value;

    if (Serie && Numero) {
        fetch(`http://localhost:5000/ticket/${Serie},${Numero}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('El tiquete ingresado no existe!');
            } else {
                if(!data.ganador){
                    alert('Lo siento, no ha ganado nada!')
                }else{
                    alert(`Felicidades, ha ganado ${data.premio} colones`)
                }
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('No es una info valida');
    }

});

