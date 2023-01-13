
/*VARIABLES*/
/*3. traduce las variables a código*/
let nombre = "Nathalia";
let apellido = "Olivera";
let nombredeUsuario = "Nolivera";
let edad = 28;
let correo = "olivernathalia@gmail.com"
let esMayorDeEdad = edad>18; 
let dineroAhorrado = 8;
let deudas = 10;


/*4. Calcula e imprime las siguientes variables a partir de las variables del ejemplo anterior*/
    /*Nombre completo (nombre y apellido)*/
    console.log(nombre+" "+ apellido);
    /*Dinero real (dinero ahorrado menos deudas)*/
    console.log(dineroAhorrado-deudas)

/*FUNCIONES*/

/*2. Convierte esto a función
            const name = "Juan David";
            const lastname = "Castro Gallego";
            const completeName = name + lastname;
            const nickname = "juandc";

            console.log("Mi nombre es " + completeName + ", pero prefiero que me digas " + nickname + ".");*/

            function mensaje (name, lastname, nickname)
            {
                return "Mi nombre es " + name + " " + lastname +", pero prefiero que me digas " + nickname + ".";
            }

/*CONDICIONES*/
/*2. Replica el comportamiento de este cód usando if elese y else if.

     const tipoDeSuscripcion = "Basic";
        switch (tipoDeSuscripcion) {
               case "Free":
                   console.log("Solo puedes tomar los cursos gratis");
                   break;
               case "Basic":
                   console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
                   break;
               case "Expert":
                   console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
                   break;
               case "ExpertPlus":
                   console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
                   break;
            }*/

let tipoDeSuscripcion = "Basic";


if (tipoDeSuscripcion == "Free") 
    {
    console.log("Solo puedes tomar los cursos gratis");
    } 
    
    else if (tipoDeSuscripcion == "Basic") 
    {
    console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
    }

    else if (tipoDeSuscripcion == "Expert") 
    {
    console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
    }  
    else if (tipoDeSuscripcion == "ExpertPlus") 
    {
    console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
    }
    else
    {
        console.log("error")
    }
/*3. Replica el comportamiento de tu condicional anterior con if, else y else if, pero ahora solo con if (sin else ni else if).*/

    if (tipoDeSuscripcion == "Free") 
        {
        console.log("Solo puedes tomar los cursos gratis");
        } 
        
    if (tipoDeSuscripcion == "Basic") 
        {
        console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
        }

    if (tipoDeSuscripcion == "Expert") 
        {
        console.log("Puedes tomar casi todos los cursos de Platzi durante un año");
        }  
    
    if (tipoDeSuscripcion == "ExpertPlus") 
        {
        console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
        }

/*CICLOS*/
    /*2. Replica el comportamiento de los siguientes ciclos for utilizando ciclos while:
            /*for (let i = 0; i < 5; i++) {
                console.log("El valor de i es: " + i);
            }*/
            let i=0;
            while (i < 5) {
                
                console.log("El valor de i es: " + i);
                i++
            }

            /*for (let i = 10; i >= 2; i--) {
                console.log("El valor de i es: " + i);
            }*/
            i=10;
            while(i>=2){
                console.log("El valor de i es: " + i)
                i--
            }
    /*3. Escribe un código en JavaScript que le pregunte a los usuarios cuánto es 2 + 2. Si responden bien, mostramos un mensaje de felicitaciones, pero si responden mal, volvemos a empezar.*/

            function validar (respuesta){
                respuesta=parseInt(prompt("escribe cuato es 2 + 2") ); 
                if (respuesta==4){
                    return alert("Felicitaciones")
                }
                else{
                    
                    validar()   
                }
            }
            
            //RESPUESTA PROFE
            /*let respuesta;
            while(respuesta != 4) {
                respuesta=parseInt(prompt("escribe cuato es 2 + 2"));
            }/*
            
/*LISTAS*/


        let arr=["a", "b","c","d"];
        console.log(arr[0]);

        //2. Crea una función que pueda recibir cualquier array como parámetro e imprima su primer elemento.

        function primer (x){
            return x[0];
        }

        //3.Crea una función que pueda recibir cualquier array como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el array completo).
        function todo (p){
            for(let i = 0; i < p.length; i++){
            console.log(p[i]);
            }
        }

        //4.Crea una función que pueda recibir cualquier objeto como parámetro e imprima todos sus elementos uno por uno (no se vale imprimir el objeto completo).

        const planeta = {
            nombre: 'Jupiter',
            radio: 71492,
            diametro: 142984 
        }
        
        function imprimir(objeto){
            for(let elemento in objeto){
                console.log(objeto[elemento]);
            }
        }
        
        imprimir(planeta);