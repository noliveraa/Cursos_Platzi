//DE HTML a JS (Obtenemos los valores que estan o que el usuario aportal al html en JS)
const h1 = document.querySelector("h1");
const p = document.querySelector("p");
const clase1 = document.querySelector(".clase1");
const pid = document.querySelector("#pid");
const input = document.querySelector("input");

console.log({h1,p,clase1,pid,input})



//DE JS a HTML  
    //- Modificamos los valores dados al html desde JS
    h1.innerHTML="Hola"
    //- Modificamos los atributos dados a un elemento de html
    h1.setAttribute("class", "rojo") //le di el atributo clase rojo al elemento h1
    input.value = "456"// le di un valor al input
    //- Crear un elemento y adicionarlo a otro 
            //Pongamos una imagen
            //1. crear una variable en js que contenga la imagen
            const img = document.createElement("img");
            //2. crearle el atributo src
            img.setAttribute("src","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx1AgIRs01lUk6d-mmU6Tn4D4PBfwY5lh2jQ&usqp=CAU")
            //3. Pegarlo a un elemento que ya exista en el html
            pid.appendChild(img)

    //hacer esto con interacción del usuario

        //crear las variables para los inputs
        const input1 = document.querySelector("#calculo1");
        const input2 = document.querySelector("#calculo2");
        const input3 = document.querySelector("#calculo3");
        const input4 = document.querySelector("#calculo4");
        const btn = document.querySelector("#btnCalcular");
        const btn2 = document.querySelector("#btn2Calcular");
        const resultado = document.querySelector("#resultado")
        const pResult = document.querySelector("#pResult")

        //describir que hacer en una función 
        function btnOnClick(){
            console.log("hizo click");
            console.log(parseInt(input1.value) +parseInt(input2.value));
            let respuesta = parseInt(input1.value) +parseInt(input2.value);
            resultado.innerText = "El resultado de esa suma es " + respuesta;
            }
    
    //EventListener
        btn2.addEventListener("click", btn2OnClick)
        function btn2OnClick(){
            const sumaInputs = input3.value + input4.value;
            pResult.innerText = "El resultado de esta concatenación es  " + sumaInputs
        }

        /*OTROS Eventos que podemos identificar 
        blur: Cuando el elemento pierde el foco.
        click: El usuario hace clic sobre el elemento.
        dblclick: El usuario hace doble clic sobre el elemento.
        focus: El elemento gana el foco.
        keydown: El usuario presiona una tecla.
        keypress: El usuario presiona una tecla y la mantiene pulsada.
        keyup: El usuario libera la tecla.
        load: El documento termina su carga.
        mousedown: El usuario presiona el botón del ratón en un elemento.
        mousemove: El usuario mueve el puntero del ratón sobre un elemento.
        mouseout: El usuario mueve el puntero fuera de un elemento.
        mouseover: El usuario mantiene el puntero sobre un elemento.
        mouseup: El usuario libera el botón pulsado del ratón sobre un elemento.
        unload: El documento se descarga, bien porque se cierra la ventana, bien porque se navega a otra página.
        copy: el texto fue copiado*/

