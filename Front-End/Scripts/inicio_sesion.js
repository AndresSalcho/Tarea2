document.getElementById('fromSign').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const cedula = document.getElementById('ced').value;
    const contrasena = document.getElementById('pas1').value;

    fetch(`http://localhost:5000/user/${cedula}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('El usuario ingresado no existe!');
            } else {
                hash = data.contrasena
                fetch('http://localhost:3000/sign', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ contrasena, hash })
                })
                .then(response => response.text())
                .then(data2 => {
                    if(data2){
                        alert('Inicio de Sesion exitoso!');
                        window.history.back(-1);
                    }else{
                        alert(`Correo o contraseña incorrectos!`);
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        }).catch(error => console.error('Error:', error));
});

