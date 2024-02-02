
//ABRIR Y CERRAR LOS MENUS DESPLEGABLES DE LA BARRA DE NAVEGACIÓN
const menuEmail = document.querySelector(".navbar-email");
const desktopMenu = document.querySelector(".desktop-menu");

const burgerMenuIcon = document.querySelector(".burgerMenuIcon");
const mobileMenu = document.querySelector(".mobile-menu");

const shoppingcar = document.querySelector(".navbar-shopping-cart");
const myorderlist = document.querySelector(".product-detail");

menuEmail.addEventListener("click", toggleDesktopMenu);
burgerMenuIcon.addEventListener("click", toggleMobileMenu);
shoppingcar.addEventListener("click", toggleorderList);

function toggleDesktopMenu(){
 desktopMenu.classList.toggle("inactive");
 myorderlist.classList.add("inactive");
}

function toggleMobileMenu(){
mobileMenu.classList.toggle("inactive");
myorderlist.classList.add("inactive");
}

function toggleorderList(){
    myorderlist.classList.toggle("inactive");
    mobileMenu.classList.add("inactive");
    desktopMenu.classList.add("inactive");
}

//CREACIÓN ARRAY DE PRODUCTOS
const productList = [];

productList.push({
    name:"Bike", 
    price: 120,
    image: "./Products/Bike.jpg"
});

productList.push({
    name:"Shelf", 
    price: 30,
    image: "./Products/shelf.jpg"
});

productList.push({
    name:"Chair", 
    price: 20,
    image: "./Products/chair.jpg"
});

productList.push({
    name:"Unicorn", 
    price: 5,
    image: "./Products/unicorn.jpg"
});

//Creamos todos los elementos de lo que teniamos como "product card" en html desde JS

    /*<div class="product-card">
        <img src="./Products/Bike.jpg" alt="Bike">
        <div class="product-info">
            
            <div>
            <p>$120.00</p>
            <p>Bike</p>
            </div>
            
            <figure>
                <img src="./icons/bt_add_to_cart.svg" alt="">
            </figure>
        </div>
    </div> */


//creamos la variable cards container seleccionado la clase .cards-container que ya existe en el html para "pegarle" todo lo que definimos aca abajo
    const cardsContainer = document.querySelector(".cards-container");


for(product of productList) {
    const productCard = document.createElement("div"); //creo el elemento div
    productCard.classList.add("product-card"); //le agrego la clase
   

        //product ={name, price, image}
        const productImg = document.createElement("img");
        productImg.setAttribute("src", product.image);//Defino que en la parte del html img debe ir el componente del array product image 
        

        const productInfo = document.createElement("div");
        productInfo.classList.add("product-info");
        

            const productInfoDiv = document.createElement("div");
            

                const productPrice = document.createElement("p");
                productPrice.innerText = "$" + product.price;

                const productName = document.createElement("p");
                productName.innerText = product.name;

                productInfoDiv.append(productPrice, productName);
                

            const productInfoFigure = document.createElement("figure");
            
                const productImgCart = document.createElement("img");
                productImgCart.setAttribute("src", "./icons/bt_add_to_cart.svg");
                
                productInfoFigure.appendChild(productImgCart);

            productInfo.append(productInfoDiv, productInfoFigure);

        productCard.append(productImg, productInfo);
                
    cardsContainer.appendChild(productCard);

        
        
}