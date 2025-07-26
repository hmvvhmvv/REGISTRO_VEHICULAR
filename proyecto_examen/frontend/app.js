const API_URL = "http://localhost:8000/estudiantes";
const btn_guardar = document.getElementById("btn_guardar");
const btn_borrar_todo = document.getElementById("btn_borrar_todo");

// Función para mostrar los datos en la tabla
async function mostrarVehiculos() {
    const response = await fetch(API_URL);
    if (response.ok) {
        const data = await response.json();
        tabla.innerHTML = "";
        data.details.forEach(vehiculo => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${vehiculo.modelo}</td>
                <td>${vehiculo.numero_vin}</td>
                <td>${vehiculo.año}</td>
                <td>${vehiculo.tipo}</td>
                <td>${vehiculo.nombre}</td>
                <td>${vehiculo.telefono}</td>
            `;
            tabla.appendChild(fila);
        });
    }
}

async function cargarVehiculos() {
    const res = await fetch('http://localhost:3000/api/vehiculos');
    const datos = await res.json();
    const tabla = document.getElementById('tabla_estudiantes');
    tabla.innerHTML = '';
    datos.forEach(v => {
        const fila = document.createElement('tr');
        fila.innerHTML = `
            <td>${v.matricula}</td>
            <td>${v.nombre}</td>
            <td>${v.apellidos}</td>
            <td>${v.genero}</td>
            <td>${v.direccion}</td>
            <td>${v.telefono}</td>
        `;
        tabla.appendChild(fila);
    });
    // Mostrar último registro
    if (datos.length > 0) {
        const ultimo = datos[datos.length - 1];
        document.getElementById('datos_ultimo_registro').innerHTML = `
            <li><strong>Modelo:</strong> ${ultimo.matricula}</li>
            <li><strong>Número VIM:</strong> ${ultimo.nombre}</li>
            <li><strong>Año de Fabricación:</strong> ${ultimo.apellidos}</li>
            <li><strong>Tipo:</strong> ${ultimo.genero}</li>
            <li><strong>Nombre Propietario:</strong> ${ultimo.direccion}</li>
            <li><strong>Teléfono:</strong> ${ultimo.telefono}</li>
        `;
        document.getElementById('ultimo_registro').style.display = 'block';
    }
}

// Evento para guardar y actualizar la tabla
btn_guardar.onclick = async (event) => {
    event.preventDefault();

    // Borra todos los registros anteriores
    await fetch(API_URL, { method: "DELETE" });

    // Guarda el nuevo registro
    const estudiante = {
        modelo: document.getElementById("modelo").value,
        numero_vin: document.getElementById("numero_vin").value,
        anio: document.getElementById("anio").value,
        tipo: document.getElementById("tipo").value,
        nombre: document.getElementById("nombre").value,
        telefono: document.getElementById("telefono").value
    };
    await fetch(API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(estudiante)
    });

    formulario.reset();
    mostrarVehiculos(); // Solo se mostrará el registro recién ingresado
}

// Evento para borrar todos los registros
btn_borrar_todo.onclick = async () => {
    await fetch(API_URL, { method: "DELETE" });
    mostrarVehiculos();
};

// Al cargar la página, muestra los datos existentes
window.onload = mostrarVehiculos;

document.addEventListener('DOMContentLoaded', () => {
    const formulario = document.getElementById('formulario');
    const tabla = document.getElementById('tabla_estudiantes');
    const ultimoRegistro = document.getElementById('ultimo_registro');
    const datosUltimoRegistro = document.getElementById('datos_ultimo_registro');

    // Mostrar vehículos al cargar
    fetch('http://localhost:3000/api/vehiculos')
        .then(res => res.json())
        .then(data => {
            tabla.innerHTML = '';
            data.forEach(v => {
                const fila = document.createElement('tr');
                fila.innerHTML = `
                    <td>${v.modelo}</td>
                    <td>${v.vim}</td>
                    <td>${v.año}</td>
                    <td>${v.tipo}</td>
                    <td>${v.propietario}</td>
                    <td>${v.telefono}</td>
                `;
                tabla.appendChild(fila);
            });
        });

    formulario.addEventListener('submit', function(e) {
        e.preventDefault(); // Evita el envío por defecto

        // Obtén los valores de los campos
        const modelo = document.getElementById('modelo').value;
        const numero_vin = document.getElementById('numero_vin').value;
        const anio = document.getElementById('año').value;
        const tipo = document.getElementById('tipo').value;
        const nombre = document.getElementById('nombre').value;
        const telefono = document.getElementById('telefono').value;

        // Agrega una fila a la tabla
        const tabla = document.getElementById('tabla_estudiantes');
        const fila = document.createElement('tr');
        fila.innerHTML = `
            <td>${modelo}</td>
            <td>${numero_vin}</td>
            <td>${año}</td>
            <td>${tipo}</td>
            <td>${nombre}</td>
            <td>${telefono}</td>
        `;
        tabla.appendChild(fila);

        // Muestra el último registro
        document.getElementById('ultimo_registro').style.display = 'block';
        document.getElementById('datos_ultimo_registro').innerHTML = `
            <li>Modelo: ${modelo}</li>
            <li>Número VIM: ${numero_vin}</li>
            <li>Año: ${año}</li>
            <li>Tipo: ${tipo}</li>
            <li>Propietario: ${nombre}</li>
            <li>Teléfono: ${telefono}</li>
        `;

        // Opcional: limpiar el formulario
        e.target.reset();
    });

    document.getElementById('btn_cancelar').addEventListener('click', () => {
        formulario.reset();
    });
});