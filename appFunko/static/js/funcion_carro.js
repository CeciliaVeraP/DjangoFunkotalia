
if (document.readyState == 'loading') {
    document.addEventListener("DOMContentLoaded", ready);
  } else {
    ready();
  }
function ready(){
    //Funcion para el boton agregar al carrito
    var botonesAgregarAlCarrito = document.getElementsByClassName('fa-sharp');
    for(var i = 0; i<botonesAgregarAlCarrito.length; i++){
        var button=botonesAgregarAlCarrito[i];
        button.addEventListener('click', agregarAlCarroClicked);
    }
}

function agregarAlCarroClicked(event){
    Swal.fire({
        title:"bienvenido!"
    });
  /* var button = event.target;
  var product = button.parentElement;
  var categoria = product.getElementsByClassName("product_categoria")[0].innerText;
  var title = product.getElementsByClassName("product__title")[0].innerText;
  var price = product.getElementsByClassName("producto__price")[0].innerText;
  var productImg = product.getElementsByClassName("img-product")[0].src;

  var cartItems = document.getElementsByClassName('container-car')[0];
  var cartItemsNames = cartItems.getElementsByClassName('product__title');

  agregarProductAlCarrito(categoria,title, price, productImg);
  actualizarTotalCarrito(); 
     */
}
/* function agregarProductAlCarrito(titulo, precio, imagenSrc){
    var product = document.createElement('div');
    product.classList.add = 'product';
    var productCarrito = document.getElementsByClassName('carrito')[0];

    productCarrito.append(product);
 }     */