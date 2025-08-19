<?php
$archivo = "visitas.txt";
$clave = "secreta123"; // Cambia esto por tu clave personal

// Leer el número actual de visitas
if (!file_exists($archivo)) {
    file_put_contents($archivo, "0");
}
$visitas = (int) file_get_contents($archivo);
$visitas++;

// Guardar la nueva cantidad
file_put_contents($archivo, $visitas);

// Si se pasa la clave por GET, mostrar el conteo
if (isset($_GET['clave']) && $_GET['clave'] === $clave) {
    echo "Visitas totales: $visitas";
} else {
    // No mostrar nada (modo oculto)
}
?>
