//CALLBACK: Es una función que recibe como parámetro una función ya definida 

function sum(num1, num2){
    return num1 + num2;
}
 
function calc(num1, num2, callback){
    return callback(num1, num2);
}

console.log(calc(2, 2, sum))//no se le pone los parentesis a la funcion que llamamos como argumento 

//Ejemplo setTimeout

setTimeout(() => {
    console.log("HolaJS")
}, 2000); //le estoy diciendo que se ejecute a los 2 seg 

function greeting (name){
    console.log(`Hola ${name}`)
}

setTimeout(greeting, 2000, "Nathalia");