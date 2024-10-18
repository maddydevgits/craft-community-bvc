from flask import Flask,request,render_template,session,redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

cluster=MongoClient("127.0.0.1:27017")
db=cluster['bvc']
customers=db['customers']
uses=db['uses']
products=db['products']
carts=db['cart']
orders1=db['orders']

app=Flask(__name__)
app.secret_key="1234"

@app.route("/")
def home():
    return render_template("sample1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bamboo-baskets")
def bamboobaskets():
    return render_template("bamboo-baskets.html")

@app.route("/bamboo-containers")
def bamboocontainers():
    return render_template("bamboo-containers.html")

@app.route("/bamboo-crafts")
def bamboocrafts():
    return render_template("bamboo-crafts.html")

@app.route("/bamboo-furniture")
def bamboofurniture():
    return render_template("bamboo-furniture.html")

@app.route("/bamboo-matting")
def bamboomatting():
    return render_template("bamboo-matting.html")

@app.route("/bamboo-musical")
def bamboomusical():
    return render_template("bamboo-musical.html")

@app.route("/bamboo-utensils")
def bambooutensils():
    return render_template("bamboo-utensils.html")

@app.route("/bamboo")
def bamboo():
    product=products.find({'productcategory':'bamboo'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("bamboo.html",l=len(data),data=data)

@app.route("/cart")
def cart():
    product=carts.find({'customer':session['username']})
    data=[]
    total_price=0
    for i in product:
        dummy=[]
        print(i)
        cart_product=products.find({'_id':ObjectId(i['product_id'])})
        for j in cart_product:
           total_price+=float(j['productprice'])*int(i['Qty'])
           dummy.append(j['imageurl'])
           dummy.append(j['productname'])
           dummy.append(j['productprice'])
           dummy.append(i['Qty'])
           dummy.append(j['productcolor'])
           dummy.append(j['productrating'])
           dummy.append(i['_id'])
           data.append(dummy)
           

    return render_template("cart.html",data=data,l=len(data),total_price=total_price)

@app.route("/coconut-bowls")
def coconutbowls():
    return render_template("coconut-bowls.html")

@app.route("/coconut-brushes")
def coconutbrushes():
    return render_template("coconut-brushes.html")

@app.route("/coconut-candles")
def coconutcandles():
    return render_template("coconut-candles.html")

@app.route("/coconut-jewelry")
def coconutjewelry():
    return render_template("coconut-jewelry.html")

@app.route("/coconut-mats")
def coconutmats():
    return render_template("coconut-mats.html")

@app.route("/coconut-shellart")
def coconutshellart():
    return render_template("coconut-shellart.html")

@app.route("/coconut-utensils")
def coconututensils():
    return render_template("coconut-utensils.html")

@app.route("/coconut")
def coconut():
    product=products.find({'productcategory':'coconut'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("coconut.html",data=data,l=len(data))

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/customer-dashboard")
def customer_dashboard():
    if 'username' not in session:
        return redirect("/")
    return render_template("customer-dashboard.html")

@app.route("/customer-singup")
def customersingup():
    return render_template("customer-singup.html")

@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route('/earnings')
def earnings():
    # Get the logged-in seller's email from the session (assuming the seller is logged in)
    seller_email = session.get('username')
    if not seller_email:
        return redirect('/')  # Redirect to login if not logged in

    # Fetch all products owned by the seller
    seller_products = products.find({'owner': seller_email})
    
    # Get all product IDs owned by the seller
    seller_product_ids = [str(product['_id']) for product in seller_products]
    
    # Fetch all orders that contain products owned by the seller
    orders = orders1.find()

    total_earnings = 0
    pending_earnings = 0
    completed_sales = 0
    earnings_data = []

    for order in orders:
        order_total = 0
        for product in order['products']:
            # If the product belongs to the seller, calculate the earnings
            if str(product['productid']) in seller_product_ids:
                order_total += product['total_price']
                
        if order_total > 0:  # Only consider orders where the seller's products are present
            earnings_data.append({
                'date': order['created_at'],
                'order_id': order['_id'],
                'products': [p for p in order['products'] if str(p['productid']) in seller_product_ids],
                'total': order_total,
                'status': order['status']
            })
            
            total_earnings += order_total
            
            if order['status'] == 'Delivered':
                completed_sales += 1
            else:
                pending_earnings += order_total

    return render_template('earnings.html', 
                            total_earnings=total_earnings, 
                            pending_earnings=pending_earnings, 
                            completed_sales=completed_sales,
                            earnings_data=earnings_data)

@app.route("/herbal-oils")
def herbaloils():
    return render_template("herbal-oils.html")

@app.route("/herbal-powder")
def herbalpowder():
    return render_template("herbal-powder.html")

@app.route("/herbal-remedies")
def herbalremedies():
    return render_template("herbal-remedies.html")

@app.route("/herbal-slaves")
def herbalslaves():
    return render_template("herbal-slaves.html")

@app.route("/herbal-soaps")
def herbalsoaps():
    return render_template("herbal-soaps.html")

@app.route("/herbal-teas")
def herbalteas():
    return render_template("herbal-teas.html")

@app.route("/herbal")
def herbal():
    product=products.find({'productcategory':'herbal'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("herbal.html",data=data,l=len(data))

@app.route("/leaf-art")
def leafart():
    return render_template("leaf-art.html")

@app.route("/leaf-bookmark")
def leafbookmark():
    return render_template("leaf-bookmark.html")

@app.route("/leaf-baskets")
def leafbaskets():
    return render_template("leaf-baskets.html")

@app.route("/leaf-garlands")
def leafgarlands():
    return render_template("leaf-garlands.html")

@app.route("/leaf-paper")
def leafpaper():
    return render_template("leaf-paper.html")

@app.route("/leaf-plates")
def leafplates():
    return render_template("leaf-plates.html")

@app.route("/leaf-toys")
def leaftoys():
    return render_template("leaf-toys.html")

@app.route("/leaf")
def leaf():
    product=products.find({'productcategory':'leaf'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("leaf.html",data=data,l=len(data))

@app.route("/manage-products")
def manageproducts():
    if 'username' not in session:
        return redirect('/')
    product=products.find()
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['productname'])
        dummy.append(i['productcategory'])
        dummy.append(i['productprice'])
        dummy.append(i['productstock'])
        dummy.append(i['imageurl'])
        dummy.append(i['_id'])
        dummy.append(i['productdescription'])
        dummy.append(i['productcolor'])
        dummy.append(i['productrating'])
        data.append(dummy)

    return render_template("manage-products.html",l=len(data),data=data)

@app.route("/addproduct",methods=['post'])
def addproduct():
    a=request.form.get("product-name")
    b=request.form.get("product-category")
    c=request.form.get("product-price")
    d=request.form.get("product-stock")
    e=request.form.get("imageurl")
    f=request.form.get("product-description")
    g=request.form.get("product-color")
    h=request.form.get("product-rating")
    print(a,b,c,d,e,f,g,h)
    product=products.find_one({"owner": session['username'],"productname":a,"productcategory":b,"productprice":c,"productstock":d,"imageurl":e})
    if(product):
        data=[]
        product=products.find()
        for i in product:
            print(i)
            dummy=[]
            dummy.append(i['productname'])
            dummy.append(i['productcategory'])
            dummy.append(i['productprice'])
            dummy.append(i['productstock'])
            dummy.append(i['imageurl'])
            dummy.append(i['_id'])
            dummy.append(i['productdescription'])
            dummy.append(i['productcolor'])
            dummy.append(i['productrating'])
            data.append(dummy)
        return render_template("manage-products.html",status="product exist",l=len(data),data=data)
    products.insert_one({"owner":session['username'],"productname":a,"productcategory":b,"productprice":c,"productstock":d,"imageurl":e,"productdescription":f,"productcolor":g,"productrating":h})
    return redirect("/manage-products")

@app.route("/orders")
def orders():
    seller_email = session.get('username')  # The seller's email is used as the owner field in products collection
    if not seller_email:
        return redirect('/login')

    # Fetch all products owned by the seller
    seller_products = products.find({'owner': seller_email})
    
    # Get all product IDs owned by the seller
    seller_product_ids = [ObjectId(product['_id']) for product in seller_products]
    
    # Fetch all orders
    orders11 = orders1.find()

    print(seller_product_ids)
    
    # Prepare data for orders involving the seller's products
    seller_orders = []
    for order in orders11:
        seller_order_products = []
        
        # Iterate through products in the order and check if they belong to the seller
        for product in order['products']:
            if ObjectId(product['productid']) in seller_product_ids:
                seller_order_products.append(product)

        # If the order contains products from the seller, add it to the seller_orders list
        if seller_order_products:
            seller_orders.append({
                '_id': order['_id'],
                'fullname': order['fullname'],
                'address': order['address'],
                'contactnumber': order['contactnumber'],
                'products': seller_order_products,
                'total_price': sum([p['total_price'] for p in seller_order_products]),
                'status': order['status'],
                'created_at': order['created_at']
            })

    return render_template('orders.html', orders=seller_orders)

@app.route('/order-details/<order_id>')
def order_details(order_id):
    # Fetch the order details by order_id
    order = orders1.find_one({'_id': ObjectId(order_id)})
    
    if not order:
        return "Order not found", 404

    # Fetch products details for the order
    products = order['products']
    
    # Pass order details to the template
    return render_template('order-details.html', order=order, products=products)

@app.route('/update-order-status/<order_id>', methods=['POST'])
def update_order_status(order_id):
    # Get the new status from the form submission
    new_status = request.form.get('status')
    
    # Update the order status in the database
    orders1.update_one(
        {'_id': ObjectId(order_id)}, 
        {
            '$set': {
                'status': new_status, 
                'updated_at': datetime.now()  # Optionally update the modification timestamp
            }
        }
    )
    
    # Redirect back to the seller's orders page or order details page
    return redirect('/orders')

@app.route("/pottery")
def pottery():
    product=products.find({'productcategory':'pottery'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("pottery.html",data=data,l=len(data))

@app.route("/pottery-bowls")
def potterybowls():
    return render_template("pottery-bowls.html")

@app.route("/pottery-mugs")
def potterymugs():
    return render_template("pottery-mugs.html")

@app.route("/pottery-planters")
def potteryplanters():
    return render_template("pottery-planters.html")

@app.route("/pottery-plate")
def potterplate():
    return render_template("pottery-plate.html")

@app.route("/pottery-teapots")
def potteryteapots():
    return render_template("pottery-teapots.html")

@app.route("/pottery-vases")
def potteryvases():
    return render_template("pottery-vases.html")

@app.route("/products")
def productsdetails():
    return render_template("products.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/ratings")
def ratings():
    return render_template("ratings.html")

@app.route("/sarees")
def sarees():
    product=products.find({'productcategory':'handloom'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("sarees.html",data=data,l=len(data))

@app.route("/sarees-bandini")
def sareesbandini():
    return render_template("sarees-bandini.html")

@app.route("/sarees-cotton")
def sareescotton():
    return render_template("sarees-cotton.html")

@app.route("/sarees-ikat")
def sareesikat():
    return render_template("sarees-ikat.html")

@app.route("/sarees-kanchi")
def sareeskanti():
    return render_template("sarees-kanchi.html")

@app.route("/sarees-paithani")
def sareespaithani():
    return render_template("sarees-paithani.html")

@app.route("/sarees-pochampalli")
def sareespochampalli():
    return render_template("sarees-pochampalli.html")

@app.route("/seller-dashboard")
def sellerdashboard():
    if 'username' not in session:
        return redirect('/')
    return render_template("seller-dashboard.html")

@app.route("/seller-signup")
def sellersignup():
    return render_template("seller-signup.html")

@app.route("/selsignup1", methods=['post'])
def selsignup1():
    a=request.form.get("seller-name")
    b=request.form.get("seller-email")
    c=request.form.get("seller-password")
    print(a,b,c)
    user=uses.find_one({"Email":b})
    if(user):
        return render_template("seller-signup.html", status="Username Already Exists")
    uses.insert_one({"Name":a,"Email":b,"Password":c})
    return render_template("seller-signup.html", status="Registration Successful")

@app.route("/seller1-login")
def seller1login():
    return render_template("seller1-login.html")

@app.route("/selllogin1", methods=['post'])
def selllogin1():
    b=request.form.get("email")
    c=request.form.get("password")
    print(b,c)
    user=uses.find_one({"Email":b})
    if(user):
        if user["Password"]==c:
            session['username']=b
            return redirect("/seller-dashboard")
    return render_template("seller1-login.html", result="Invalid Credentials")

@app.route("/stone-craft")
def stonecraft():
    return render_template("stone-craft.html")

@app.route("/stone-decor")
def stonedecor():
    return render_template("stone-decor.html")

@app.route("/stone-jewelry")
def stonejewelry():
    return render_template("stone-jewelry.html")

@app.route("/stone-mortars")
def stonemortars():
    return render_template("stone-mortars.html")

@app.route("/stone-pathways")
def stonepathways():
    return render_template("stone-pathways.html")

@app.route("/stone-sculptures")
def stonesculptures():
    return render_template("stone-sculptures.html")

@app.route("/stone-utensils")
def stoneutensils():
    return render_template("stone-utensils.html")

@app.route("/stone")
def stone():
    product=products.find({'productcategory':'stone'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("stone.html",data=data,l=len(data))

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/wooden")
def wooden():
    product=products.find({'productcategory':'wooden'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("wooden.html",l=len(data),data=data)

@app.route("/wooden-baskets")
def woodenbaskets():
    return render_template("wooden-baskets.html")

@app.route("/wooden-brushes")
def woodenbrushes():
    return render_template("wooden-brushes.html")

@app.route("/wooden-decor")
def woodendecor():
    return render_template("wooden-decor.html")

@app.route("/wooden-furniture")
def woodenfurniture():
    return render_template("wooden-furniture.html")

@app.route("/wooden-toys")
def woodentoys():
    return render_template("wooden-toys.html")

@app.route("/wooden-utensils")
def woodenutensils():
    return render_template("wooden-utensils.html")

@app.route("/customersignup1",methods=['post'])
def customersignup1():
    a=request.form.get("customername")
    b=request.form.get("customeremail")
    c=request.form.get("customerpassword")
    print(a,b,c)
    user=customers.find_one({"customeremail":b})
    if(user):
        return render_template("customer-singup.html",status="Email already exists")
    customers.insert_one({"customername":a,"customeremail":b,"customerpassword":c})
    return render_template("customer-singup.html",status="Registration Succesfull")

@app.route("/customerlogin1",methods=['post'])
def clog():
    email=request.form.get("email")
    password=request.form.get("password")
    user=customers.find_one({"customeremail":email})
    if(user):
        if user['customerpassword']==password:
            session['username']=email
            return redirect("/customer-dashboard")
    return render_template("customer.html",status="Invalid credentials")

@app.route("/logout")
def logout():
    session['username']=None
    session.clear()
    return redirect("/")

@app.route('/pottery-product/<product_id>',methods=['GET','POST'])
def pottery_product(product_id):
    product=products.find_one({"_id":ObjectId(product_id)})
    return render_template("pottery-product.html",product=product)

@app.route("/editproduct/<product_id>", methods=['GET', 'POST'])
def edit_product(product_id):
    if request.method == 'POST':
        # Get updated data and update product in database
        updated_data = {
            "productname": request.form['product-name'],
            "productcategory": request.form['product-category'],
            "productprice": request.form['product-price'],
            "productstock": request.form['product-stock'],
            "imageurl": request.form['imageurl'],
            "productdescription":request.form['product-description'],
            "productcolor":request.form['product-color'],
            "productrating":request.form['product-rating']
        }
        products.update_one({"_id": ObjectId(product_id)}, {"$set": updated_data})
        return redirect("/manage-products")
    else:
        # Fetch product details and display edit form
        product = products.find_one({"_id": ObjectId(product_id)})
        print(product)
        return render_template("edit-product.html", product=product)

@app.route("/deleteproduct/<product_id>", methods=['POST'])
def delete_product(product_id):
    products.delete_one({"_id": ObjectId(product_id)})
    return redirect("/manage-products")

@app.route("/deletecart/<product_id>", methods=['POST'])
def delete_product_cart(product_id):
    carts.delete_one({"_id": ObjectId(product_id)})
    return redirect("/cart")

@app.route('/addtocart/<product_id>',methods=['GET','POST'])
def addtocart(product_id):
    qty=request.form.get('qty')
    qty=int(qty)
    product=products.find_one({'_id':ObjectId(product_id)})
    carts.insert_one(
            {
                'product_id': ObjectId(product_id),
                'Qty': qty,
                'customer': session['username']
            }
    )
    return redirect('/cart')

@app.route('/orderform', methods=['POST'])
def orderform():
    # Get user input from the form
    fullname = request.form.get('fullname')
    address = request.form.get('address')
    contactnumber = request.form.get('contactnumber')
    
    # Get the cart items for the logged-in customer
    cart_items = carts.find({'customer': session['username']})
    
    data = []
    total_price = 0
    
    # Loop through the cart items and calculate the total price
    for item in cart_items:
        product_id = item['product_id']
        quantity = item['Qty']
        
        # Fetch the product details from the products collection
        product = products.find_one({'_id': ObjectId(product_id)})
        product_price = float(product['productprice'])
        total_item_price = product_price * quantity
        
        # Add product details to order data
        data.append({
            'productid': product['_id'],
            'productname': product['productname'],
            'productcategory': product['productcategory'],
            'quantity': quantity,
            'price': product_price,
            'total_price': total_item_price
        })
        
        # Update the total order price
        total_price += total_item_price
    
    # Create order document
    order = {
        'fullname': fullname,
        'address': address,
        'contactnumber': contactnumber,
        'customer': session['username'],
        'products': data,  # Add the list of products
        'total_price': total_price,
        'status': 'Pending',  # You can change status as per your logic
        'created_at': datetime.now()
    }
    
    # Insert the order into the orders collection
    orders1.insert_one(order)
    
    # Optionally, clear the user's cart after placing the order
    carts.delete_many({'customer': session['username']})
    
    # Redirect to an order confirmation page or show order details
    return render_template('order-confirmation.html', order=order)

@app.route('/order-confirmation/<order_id>')
def order_confirmation(order_id):
    order = orders1.find_one({"_id": ObjectId(order_id)})
    return render_template('order-confirmation.html', order=order)

@app.route('/my-orders')
def my_orders():
    # Retrieve all orders for the logged-in customer
    customer_username = session.get('username')
    if not customer_username:
        return redirect('/login')

    orders11 = orders1.find({'customer': customer_username}).sort('created_at', -1)
    
    return render_template('customer-orders.html', orders=list(orders11))

if __name__=="__main__":
    app.run(port=6010,debug=True)
