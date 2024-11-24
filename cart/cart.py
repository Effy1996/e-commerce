from fashion.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        #Get request
        self.request = request
        #Get current session key
        cart = self.session.get("session_key")

        #If the user is new, they don't have a session, create one!
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        #Cart is avaiable in all pages
        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)} 
            self.cart[product_id] = int(product_quantity) 

        self.session.modified = True  

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            conv_cart = str(self.cart)
            conv_cart = conv_cart.replace("\'", "\"")

            #Save conv_cart to Profile model
            current_user.update(old_cart=str(conv_cart))

    def add(self, product, quantity):
        product_id = str(product.id)
        product_quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)} 
            self.cart[product_id] = int(product_quantity) 

        self.session.modified = True  

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            conv_cart = str(self.cart)
            conv_cart = conv_cart.replace("\'", "\"")

            #Save conv_cart to Profile model
            current_user.update(old_cart=str(conv_cart))

    def __len__(self):
        return len(self.cart) 
    
    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quantities(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, qnty):
        product_id = str(product)
        product_quantity = int(qnty) 

        mycart = self.cart
        mycart[product_id] = product_quantity

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            conv_cart = str(self.cart)
            conv_cart = conv_cart.replace("\'", "\"")

            #Save conv_cart to Profile model
            current_user.update(old_cart=str(conv_cart))

        item = self.cart
        return item
    
    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
        
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)

            conv_cart = str(self.cart)
            conv_cart = conv_cart.replace("\'", "\"")

            #Save conv_cart to Profile model
            current_user.update(old_cart=str(conv_cart))

    def total(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        stuff = self.cart

        total = 0
        for key, value in stuff.items(): 
            key = int(key)

            for product in products:
                if product.id == key:
                    total = total + (product.price * value)
        return total


        