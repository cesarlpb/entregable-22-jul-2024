document.addEventListener('DOMContentLoaded', function() {
    const autores = document.getElementById('id_autor');
    const sagas = document.getElementById('id_saga');
    const libros = document.getElementById('id_libro');

    autores.addEventListener('change', function() {
        const AutorId = this.value;
        if (AutorId) {
            fetch(`/sagas/${AutorId}/`)
                .then(response => response.json())
                .then(data => {
                    sagas.innerHTML = '';
                    data.sagas.forEach(saga => {
                        const option = document.createElement('option');
                        option.value = saga.id;
                        option.textContent = saga.nombre;
                        sagas.appendChild(option);
                    });
                });
        }
        else {
            sagas.innerHTML = '';
        }
    });
});