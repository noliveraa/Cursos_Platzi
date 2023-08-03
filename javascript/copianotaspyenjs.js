// VARIABLES
let variable = "Hola"; // string
let numero = 6; // entero
let decimal = 10.2;
let age = 17; // especificar el tipo de dato
let verdadero = true; // booleano
let falso = false;
console.log(typeof variable); // muestra el tipo de dato

// CONCATENAR
let name = "Nathalia";
let last_name = "Olivera";
let full_name = name + " " + last_name;
console.log(full_name);
let template = `Hola, mi nombre es ${name} y mi apellido es ${last_name}`;
console.log(template);
console.log(`Hola, esta es otra forma de insertar ${name} y ${last_name}`);

// MÉTODOS
let texto = "Hola Mundo";
console.log(texto);
console.log(texto.toUpperCase()); // convertir a mayúsculas
console.log(texto.toLowerCase()); // convertir a minúsculas
console.log(texto.indexOf("M")); // encontrar la posición de "M" en el texto
console.log(texto.replace("Mundo", "Chanchito feliz")); // reemplazar "Mundo" por "Chanchito feliz"
let nuevoTexto = texto.replace("Mundo", "Chanchito feliz");
console.log(texto, nuevoTexto);
console.log(texto.includes("Mundo")); // buscar "Mundo" en el texto

// OPERACIONES ARITMÉTICAS
console.log(5 + 14);
console.log(5 - 14);
console.log(5 * 14);
console.log(5 / 14);
console.log(5 ** 2); // elevado
console.log(10 % 3); // módulo: resto de la división de dos números
numero -= 1; // forma abreviada de numero = numero - 1
console.log(numero);
let vector = [3, 4, 5];

// OPERADORES DE COMPARACIÓN
let n1 = 10;
let n2 = 15;
console.log(n1 > n2);
console.log(n1 <= n2);
console.log(n1 === n2);

// OBTENER DATOS DE USUARIO
let edad = parseInt(prompt('Ingresa tu edad:')); // convertir a número entero
console.log(edad);
// convertir a otros tipos de datos
String(220);
parseFloat("22.3");
Boolean(); // evalúa si es verdadero o falso; por lo general, será verdadero, solo será falso si se pone false, 0, "", null

// OPERADORES LÓGICOS
console.log(edad > 18 && edad < 30); // evalúa si es mayor de 18 y menor de 30; si es menor de 18, no evalúa si es 30, automáticamente es falso
console.log(edad > 18 || edad < 30); // uno u otro es verdadero
console.log(!(edad > 18)); // niega la expresión, devuelve el resultado opuesto

// LISTAS
let lenguajes = ["python", "Ruby", "PHP", "js", "java"];
console.log(lenguajes[1]);
lenguajes[1] = "Go"; // reemplazar el segundo elemento
console.log(lenguajes[lenguajes.length - 1]); // último elemento
console.log(lenguajes.slice(1, 3)); // seleccionar un rango, desde el índice 1 hasta el índice 2
console.log(lenguajes.slice(0, 3)); // asume que es desde el primer elemento si omito el 0; [1:] asume que es hasta el último

lenguajes.unshift("C"); // añadir "C" al inicio antes de "python"
lenguajes.splice(lenguajes.indexOf("PHP"), 1); // eliminar "PHP"
console.log(lenguajes.length); // longitud del array

// IF
let puntaje = 97;
if (puntaje >= 95) {
  console.log("Aprobado con honores");
} else if (puntaje >= 50) {
  console.log("Alumno aprobado");
} else {
  console.log("Reprobado");
}

// Ejercicio T en F a C
let temperaturaIn = parseFloat(prompt('Ingresa la temperatura a convertir:'));
let unidad = prompt("¿Está en F o C?");
let temperaturaOut;
if (unidad === "F") {
  temperaturaOut = (temperaturaIn - 32) * (5 / 9);
} else if (unidad === "C") {
  temperaturaOut = (temperaturaIn * 9 / 5) + 32;
} else {
  console.log("Valor ingresado no válido");
}
console.log(temperaturaOut);

// WHILE
let i = 1;
while (i <= 5) {
  console.log("hola ".repeat(i));
  i++;
}

i = 0;
while (i < lenguajes.length) {
  console.log(lenguajes[i]);
  i++;
}

// FOR
for (let lenguaje of lenguajes) {
  console.log(lenguaje);
}
