const saltRounds = 10;
document.getElementById('fromReg').addEventListener('submit', function(event) {
    event.preventDefault();

    const cedula = document.getElementById('ced').value;
    const nombres = document.getElementById('nom').value;
    const apellidos = document.getElementById('ape').value;
    const email = document.getElementById('em').value;
    const pass = document.getElementById('pas1').value;
    const pass2 = document.getElementById('pas2').value;
    const telefono = document.getElementById('tel').value;
    const residencia = document.getElementById('res').value;

    if (pass !== pass2) {
        alert("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.");
        document.getElementById('pas1').value = "";
        document.getElementById('pas2').value = "";
        document.getElementById('pas1').setAttribute('class','highlight')
        document.getElementById('pas2').setAttribute('class','highlight')
        return false;
    }else{
        fetch('http://localhost:3000/hash', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ pass })
        })
        .then(response => response.text())
        .then(data => {
            const contrasena = data;
            fetch('http://localhost:5000/user/submitUser', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ cedula, nombres, apellidos, email, contrasena, telefono, residencia })
            })
            .then(response => {
                if (response.ok) {
                    alert(`Usuario registrado con Exito!`);
                    window.history.back(-1);
                } else {
                    alert('Error al registrar usuario');
                }
            })
            .catch(error => console.error('Error:', error));
        })
        .catch(error => console.error('Error:', error));
    }
})    