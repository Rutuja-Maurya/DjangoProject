from django.shortcuts import render,redirect
from django.http import HttpResponse
from AdminApp.models  import Food,Category,Accounts,OrderMaster
from UserApp.models import UserInfo,MyCart
from django.contrib import messages
#from django.contrib.auth import authenticate, login

# Create your views here.
def homepage(request):
    cats = Category.objects.all()
    foods = Food.objects.all()
    return render(request,"homepage.html",{"cats":cats,"foods":foods})

def ShowFood(request,id):
    cat = Category.objects.get(id=id)
    foods = Food.objects.filter(cat_fk = id)
    cats = Category.objects.all()
    return render(request,"homepage.html",{"foods":foods,"cats":cats,"cat":cat})

def ViewDetails(request,id):
    food = Food.objects.get(id=id)
    cats = Category.objects.all()
    return render(request,"ViewDetails.html",{"food":food,"cats":cats})

# def AddToCart(request):
#     if(request.method == "POST"):
#         if("uname" in request.session):                    
#             fid = request.POST["fid"]
#             qty = request.POST["qty"]
#             uname = request.session["uname"]
#             item = MyCart()
#             item.user = UserInfo.objects.get(username = uname)
#             item.food = Food.objects.get(id=fid)
#             item.qty = qty
#             item.save()
#             return redirect(ShowCart)
#         else:
#             return redirect("/Login")
        
# def MakePayment(request):
#     if(request.method == "GET"):
#         return render(request,"MakePayment.html",{})
#     else:
#         cardno = request.POST["cardno"]
#         cvv  = request.POST["cvv"]
#         expiry = request.POST["expiry"]
#         try:
#             buyer = Accounts.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
#         except:
#             return redirect(MakePayment)
#         else:
#             owner = Accounts.objects.get(cardno='222',cvv='222',expiry='12/2030')
#             amount = request.session["total"]
#             buyer.balance -= amount
#             owner.balance +=amount
#             buyer.save()
#             owner.save()
#             #delete all items from cart
#             items = MyCart.objects.filter(user = request.session["uname"])
#             order = OrderMaster()
#             order.user = UserInfo.objects.get(username = request.session["uname"])
#             order.amount = request.session["total"]
#             details = []
#             for item in items:
#                 details.append(item.food.food_name)
#                 item.delete()
            
#             order.details = ",".join(details)
#             order.save()

#             return redirect(homepage)


# def ShowCart(request):
#     items = MyCart.objects.filter(user = request.session["uname"])
#     total = 0 
#     for item in items:
#         total += item.qty * item.food.price

#     request.session["total"] = total

#     cats = Category.objects.all()
#     return render(request,"ShowCart.html",{"items":items,"cats":cats})

def ModifyCart(request):
    action = request.POST["action"] #action -> remove / update
    fid = request.POST["fid"]   #Hidden field  
    item = MyCart.objects.get(user = request.session["uname"],food = fid)
    
    if(action == "Remove"):
        item.delete()
    else: #update
        item.qty = request.POST["qty"]
        item.save() #update
    return redirect(ShowCart)
    # fid = request.POST["fid"]    
    # item = MyCart.objects.get(user = request.session["uname"],food = fid)
    # item.delete()
    # return redirect(ShowCart)

# def Login(request):
#     if(request.method == "GET"):
#         return render(request,"Login.html",{})
#     else:
#         uname = request.POST["uname"]
#         pwd = request.POST["pwd"]
#         try:
#             user = UserInfo.objects.get(username=uname,password=pwd)
#         except:
#             #return HttpResponse("User not present")
#             return redirect(Login)
#         else:
#             request.session["uname"]=uname
#             return redirect(homepage)

def SignUp(request):
    if(request.method == "GET"):
        return render(request,"SignUp.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        email = request.POST["email"]
        address = request.POST["address"]
        pincode = request.POST["pincode"]
        phone = request.POST["phone"]

        try:
            #user = UserInfo.objects.get(username=uname,email=email)
            user = UserInfo.objects.get(username=uname)            
        except:
            #return HttpResponse("User not present")
            user = UserInfo(uname,pwd,email,address,pincode,phone)
            user.save()
            return redirect(homepage)
        else:
            return redirect(SignUp)

def Logout(request):
    request.session.clear()
    return redirect(homepage)

# def AddToCart(request):
#     if request.method == "POST":
#         uname = request.session.get("uname")  # Use get() to handle the missing key gracefully

#         if uname:
#             fid = request.POST.get("fid")
#             qty = request.POST.get("qty")

#             if fid and qty:
#                 # Check if the item already exists in the cart
#                 existing_item = MyCart.objects.filter(user__username=uname, food_id=fid).first()

#                 if existing_item:
#                     # Item already exists, you can show a prompt here if you want
#                     # For example:
#                     return HttpResponse("This item is already in the cart.")

#                 item = MyCart()
#                 item.user = UserInfo.objects.get(username=uname)
#                 item.food = Food.objects.get(id=fid)
#                 item.qty = qty
#                 item.save()
#                 return redirect(ShowCart)
#             else:
#                 return HttpResponse("Invalid data provided.")
#         else:
#             return redirect("/Login")

#updated
def AddToCart(request):
    if request.method == "POST":
        uname = request.session.get("uname")  # Use get() to handle the missing key gracefully

        if uname:
            fid = request.POST.get("fid")
            qty = request.POST.get("qty")

            if fid and qty:
                # Check if the item already exists in the cart
                existing_item = MyCart.objects.filter(user__username=uname, food_id=fid).first()

                if existing_item:
                    # Item already exists, show alert using JavaScript
                    alert_message = "This item is already in the cart."
                    return render(request, "ViewDetails.html", {"alert_message": alert_message})

                item = MyCart()
                item.user = UserInfo.objects.get(username=uname)
                item.food = Food.objects.get(id=fid)
                item.qty = qty
                item.save()
                return redirect(ShowCart)
            else:
                return HttpResponse("Invalid data provided.")
        else:
            return redirect("/Login")

#updated
def ShowCart(request):
    username = request.session.get("uname")
    user_info = UserInfo.objects.get(username=username)
    items = MyCart.objects.filter(user = user_info)
    total = 0 
    for item in items:
        total += item.qty * item.food.price

    request.session["total"] = total

    cats = Category.objects.all()
    return render(request,"ShowCart.html",{"items":items,"cats":cats, "user_info": user_info})


def MakePayment(request):
    if(request.method == "GET"):
        return render(request,"MakePayment.html",{})
    else:
        cardno = request.POST["cardno"]
        cvv  = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = Accounts.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            owner = Accounts.objects.get(cardno='222',cvv='222',expiry='12/2030')
            amount = request.session["total"]
            buyer.balance -= amount
            owner.balance +=amount
            buyer.save()
            owner.save()
            #delete all items from cart
            items = MyCart.objects.filter(user = request.session["uname"])
            order = OrderMaster()
            order.user = UserInfo.objects.get(username = request.session["uname"])
            order.amount = request.session["total"]
            details = []
            for item in items:
                details.append(item.food.food_name)
                item.delete()
            
            order.details = ",".join(details)
            order.save()

            return redirect(ordersuccessful)
        
def ordersuccessful(request):
    username = request.session.get("uname")
    user_info = UserInfo.objects.get(username=username)
    items = MyCart.objects.filter(user=user_info)
    total = 0 
    for item in items:
        total += item.qty * item.food.price
    return render(request, "ordersuccessful.html",{"items":items,"user_info": user_info,"total": total})

def Contact(request):
    return redirect(Contact)




def Login(request):
    if request.method == "GET":
        return render(request, "Login.html", {})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(username=uname, password=pwd)
        except UserInfo.DoesNotExist:
            # If the user is not found, add an error message to the template context.
            messages.error(request, "Invalid username or password.")
            return redirect(Login)
        else:
            request.session["uname"] = uname
            return redirect(homepage)
