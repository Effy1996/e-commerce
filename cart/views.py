from django.shortcuts import render, get_object_or_404
from .cart import Cart
from fashion.models import Product
from django.http import JsonResponse

# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    totals = cart.total()
    return render(request, "cart/cart.html", {
        'cart_products':cart_products,
        "quantities":quantities,
        "totals":totals
    })

def cart_add(request):
    #Get cart
    cart = Cart(request)
    #Test for POST
    if request.POST.get('action') == 'post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #Save to sessions
        cart.add(product=product, quantity=product_quantity)
        #Get cart quantity
        cart_quantity = cart.__len__()
        #Retun Response
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'quantity': cart_quantity})
        return response
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        return response
        


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #Get stuff
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity')) 

        cart.update(product=product_id, qnty=product_quantity)

        response = JsonResponse({'quantity':product_quantity})
        return response
        
