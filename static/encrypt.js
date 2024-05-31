document.addEventListener('DOMContentLoaded', function() {
    const textoInput = document.getElementById('texto');
    const botonEncrypt = document.querySelector('.btn-encrypt');
    const botonGenerateKey = document.querySelector('.btn-generate-key');
    const claveInput = document.getElementById('clave');
    const sizeInput = document.getElementById('size');
    const textoEncriptadoOutput = document.getElementById('texto_encriptado');
    const botonDecrypt = document.querySelector('.btn-decrypt');
    const textoDesencriptadoOutput = document.getElementById('texto_desencriptado');

    botonEncrypt.disabled = true;
    botonDecrypt.disabled = true;

    function encriptarTexto(texto, clave) {
        fetch('/encrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                texto: texto,
                key: clave
            })
        })
        .then(response => response.json())
        .then(data => {
            textoEncriptadoOutput.value = data.texto_encriptado;
            botonDecrypt.disabled = false;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ha ocurrido un error al encriptar el texto.');
        });
    }

    function decryptText() {
        const textoEncriptado = textoEncriptadoOutput.value.trim();
        const clave = JSON.parse(claveInput.value.trim());
        if (textoEncriptado !== '' && clave) {
            fetch('/decrypt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    texto: textoEncriptado,
                    key: clave
                })
            })
            .then(response => response.json())
            .then(data => {
                textoDesencriptadoOutput.value = data.texto_desencriptado;
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Ha ocurrido un error al desencriptar el texto.');
            });
        } else {
            alert('Por favor, encripta un texto antes de intentar desencriptarlo.');
        }
    }

    function generarClave() {
        const size = sizeInput.value;
        if(size < 2 || size > 10){
            alert('El tamaño de la clave es inválido.')
            return;
        }
        fetch(`/generate_key?size=${size}`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => {
            claveInput.value = JSON.stringify(data.key);
            botonEncrypt.disabled = false;
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ha ocurrido un error al generar la clave.');
        });
    }

    function onClickEncrypt() {
        if (claveInput.value.length == 0) {
            alert('Por favor genera una clave antes de encriptar.');
        } else {
            const texto = textoInput.value.trim();
            const clave = JSON.parse(claveInput.value.trim());
            if (texto !== '') {
                encriptarTexto(texto, clave);
            } else {
                alert('Por favor ingresa un texto antes de encriptar.');
            }
        }
    }

    botonEncrypt.addEventListener('click', onClickEncrypt);
    botonGenerateKey.addEventListener('click', generarClave);
    botonDecrypt.addEventListener('click', decryptText);
});
