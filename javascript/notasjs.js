//BASICO DE JS

    //VARAIBLES

        var a; //declaramos
        var b = 4; //declaramos y asignamos o inicializamos 
        b = 6; //reasignación
        var a = "aa"//redeclaración

        //Ejemplos en los que Boolean devuelve Falso:
        Boolean(0); //false
        Boolean(null); //false
        Boolean(NaN); //false
        Boolean(undefined); //false
        Boolean(false); //false
        Boolean(""); //false

        //Ejemplos en los que Boolean devuelve verdadero:
        Boolean(1); //true para 1 o cualquier número diferente de cero (0)
        Boolean("a"); //true para cualquier caracter o espacio en blanco en el string
        Boolean([]); //true aunque el array esté vacío
        Boolean({}); //true aunque el objeto esté vacío
        Boolean(function(){}); //Cualquier función es verdadera también

        //arrays

            var nombres = ["Andres", "Ramiro", "Silvia"]

            nombres[0] // "Andres"
            nombres[1] // "Ramiro"
            nombres[2] // "Silvia"
            nombres[3] // undefined


            var array = [1,2,3]
            array.push(4,5) //adiciona elementos al aray al final 
            console.log(array) // [ 1, 2, 3, 4, 5 ]

            var array = [3,4,5]
            array.unshift(1,2) //adiciona elementos al aray al principio
            console.log(array) // [ 1, 2, 3, 4, 5 ]

            var array = [1,2,3,4]
            var lastElement = array.pop() //quita el ultimo 
            console.log(lastElement) // 4
            console.log(array) // [ 1, 2, 3 ]

            var array = [1,2,3,4]
            var index = array.indexOf(2) //muestra la posicion en la que esta ese elemento en el array (cuando no encuentra muestra -1)
            console.log(index) // 1

    //OPERADORES
            //Operadores binarios:
                3 + 2 //Suma
                50 - 10 // Resta
                10 * 20 //Multiplicación
                20 / 2 //División

                 "Diego " + "De Granda" //concatenación de strings

            //Operadores unitarios:
                !false //negación de la negación = true

            //Operadores de asignación:
                 var a = 1; //Asignamos un valor a la variable

            //Operadores para comparar:
                3 == "3"; //Compara los valores y devuelve "true" en este caso

                3 === "3"; //Compara y valida los tipos y valores. Devuelve "falso" en este caso

                5 < 3 //Compara y valida si el 5 es menor a 3
                5 > 3 //Compara y valida si el 5 es mayor a 3
                5 <= 6 //Compara y valida si el 5 es menor o igual al 6
                5 >= 6 //Compara y valida si el 5 es mayor o igual al 6

                a && b //Valida si ambas variables son verdaderas para que se cumpla la condición
                a || b //Aquí se cumple la condición si alguna de las dos variables es verdadera

                var edad = 40
                edad++ //Incrementa el valor en 1

                edad += 2 //Incrementa el valor por 2

    //Global Scope
    var fruit = "Apple"; //variable global

    function bestfruit() {
        console.log(fruit)
    }


    //nota: cuando 

    //FUNCIONES
        //declarativas
        function miFuncion (){
            return 3;
        }

        //Expresion
        var c = function (a,b){
            return a + b;
        }

    //scope
    //hoisting
    //coerción: es la forma en la que podemos cambiar un tipo de valor a otro, existen dos tipos de coerción:
        //Coerción implícita = es cuando el lenguaje nos ayuda a cambiar el tipo de valor.
        //Coerción explicita = es cuando obligamos a que cambie el tipo de valor.

    //CONDICIONALES
        //IF
            if (edad >= 18){
                console.log("Puedes conducir")
            }

        //IF ELESE
            if (edad >= 18){
                console.log("Puedes conducir")
            } else {
                console.log("No puedes conducir")
            }

            if (condicion1){
                // Bloque 1
            } else if (condicion2){
                // Bloque 2
            } else if (condicion3){
                // Bloque 3
            } else {
                // Bloque else
            }


            function esPar(numero){
                return numero % 2 === 0 ? "Es par" : "No es par"
            }
            
            esPar(2) // "Es par"
            esPar(3) // "No es par"

        //SWITCH
        function semaforo(color) {
            switch (color) {
              case "verde": {
                console.log("¡Sigue!")
                break
              }
              case "amarillo": {
                console.log("¡Detente!")
                break
              }
              case "rojo": {
                console.log("¡No puedes avanzar!")
                break
              }
              default: {
                console.log("¡No reconozco ese color! :(")
              }
            }
          }
          
          semaforo("verde") //'¡Sigue!'

          // condition ? true : false

    //CICLO O LOOPS

        //FOR
        for (var num = 1; num <= 10; num++) {
            console.log(i)
          }

        var nombres = ["Andres", "Diego", "Platzi", "Ramiro", "Silvia"]

          for(var i = 0; i < nombres.length; i++){
              console.log( nombres[i] )
          }

        var array = [5, 4, 3, 2, 1]

          for (var elemento of array) {
            console.log(elemento) // 5 4 3 2 1
          }

          //Nota: El ciclo for ... of solo accede al valor de cada uno de los elementos del array. Por consiguiente, si quieres cambiar el array original, no podrás, porque necesitas su índice para acceder y cambiar su valor.

        //WHILE

        var numero = 1

        while ( numero <= 10 ){
            console.log(numero)
            numero++
        }

    //OBJETOS
        var miAuto = {
            brand: "Toyota",
            model: "Corolla",
            year: 2020,
            detalledelauto : function () { 
                console.log(this.brand);
            },
        }

        miAuto.brand // "Toyota"
        miAuto.model // "Corolla"
        miAuto.year // 2020
        
        //Función contructora: voy a crear un array de objetos con las mismas caracteristicas
        var car_list = [];

        class Car {
            constructor(brand, model, year) {
                this.brand = brand;
                this.model = model;
                this.year = year
            }
        }

        //Manejo de arrays de objetos
        var articulos = [
            { nombre: "Bici", costo: 3000 },
            { nombre: "TV", costo: 2500 },
            { nombre: "Libro", costo: 320 },
            { nombre: "Celular", costo: 10000 },
            { nombre: "Laptop", costo: 20000 },
            { nombre: "Teclado", costo: 500 },
            { nombre: "Audifonos", costo: 1700 },
          ]

                //Filtrar elementos de un array de objetos usando una de sus características
                var articulos_filtrados = articulos.filter(function(articulo){
                        return articulo.costo <= 500;
                });

                //generar un array con solo una de las caracteristicas de los objetos en el array de objetos

                var nombredelosarticulos = articulos.map(function(articulo){
                    return articulo.nombre;
                });

                //Encontrar objeto a partir de sus caracteristicas. Regresa el primero que encuentra con esa caracteristica.
                var articuloencontrado = articulos.find(function(articulo){
                    return articulo.nombre === "TV";
                });

                // Ejecuta lo que le definamos una vez por cada elemento de nuestro array
                articulos.forEach(function(articulo){
                    return articulo.nombre;
                })

                //Comprueba si al menos un elemento del array cumple con la condición que le damos es una validación de verdadero o falso
                var articulosbaratos = articulos.some(function(articulo){
                    return articulo.costo <= 500;
                }); //En este caso regresaria true pues si hay por lo menos un articulo de menos de 500 pesos 



     