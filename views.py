from django.shortcuts import render,redirect
from .models import*


from django.conf import settings
from django.core.mail import send_mail
import random
import razorpay

# Create your views here.
def index(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])

        con = {
            'uid' : uid
        }
        return render(request,'index.html',con)
    else:
        return render(request,'login.html')

def aboutUs(request):
    return render(request,'aboutUs.html')

def menu(request):
    return render(request,"menu.html")

def events(request):
    return render(request,"events.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cuid = Contact.objects.create(name=name,
                                      email=email,
                                      subject=subject,
                                      message=message)
        con = {
            'cuid': "sucessfully added data..!"
        } 
        return render(request,"contact.html",con)
    else:
        return render(request,"contact.html")

def reservation(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        rnid = Reservation.objects.create(name=name,
                                          email=email,
                                          phone=phone,
                                          date=date,
                                          time=time,
                                          people=people,
                                          message=message)
        con = {
            'rnid' : "Reservation is booked sucessfully..!"
        }
        return render(request,"reservation.html",con)
    else:
        return render(request,"reservation.html")

def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        con = {
                'uid' : uid 
        }
        return render(request,"index.html",con)
    else:
        try:
            if request.POST:
                email = request.POST['email']
                password = request.POST['password']
                uid = User.objects.get(email=email,)

                if uid.password == password:
                    request.session['email'] = uid.email

                    return render(request,"index.html")
                else:
                    con={
                        'eid' : "Invalid Password..!"
                    }
                return render(request,"login.html",con)
            else:
                return render(request,'login.html')
        except:
            con={
                'eid' : "Invalid Email.."
            }
            return render(request,"login.html",con)

def logout(request):
    if 'email' in request.session:
        del request.session['email']

        return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def forget_password(request):
    if request.POST:
        email = request.POST['email']
        otp = random.randint(1111,9999)

        try:
            uid = User.objects.get(email=email)
            uid.otp=otp
            uid.save()

            send_mail("forgot password","your otp is"+str(otp),'gohiljayb10@gmail.com',[email])
            con = {
                'email' : email
            }
            return render(request,'confirm_password.html',con)
        except:
            con = {
                'eid' : "Invalid Email.."
            }
            return render(request,'forget_password.html',con)
    else:
        return render(request,'forget_password.html')

def confirm_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        new_password = request.POST['new_password']
        c_password = request.POST['c_password']
        
        uid = User.objects.get(email = email)
        if str(uid.otp) == otp:

            if new_password == c_password:
                uid.password = new_password
                uid.save()

                con = {
                    'email': email,
                    'uid' : uid
                    }
                return render(request,'login.html',con)
            else:
                con = {
                    'email' : email,
                    'oid' : "Invalid Confirm password.."
                    }
                return render(request,'confirm_password.html',con)
        else:
            con = {
                'email' : email,
                'oid' : "Invalid OTP.."
            }
            return render(request,'confirm_password.html',con)
    else:
        con = {
            'email' : email,
            'oid' : "Invalid OTP.."
            }
        return render(request,'confirm_password.html',con)

def registration(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        rid = Register.objects.create(name=name,
                                      email=email,
                                      password=password)
        return render(request,"login.html")
    else:
        return render(request,"registration.html")

def order(request):
    pid = Add_product.objects.all()
    cid = Category.objects.all()

    con = {
        'pid' : pid,
        'cid' : cid
    }
    return render(request,"order.html",con)

def category(request,id):
    pid = Add_product.objects.filter(category_id=id)
    cid = Category.objects.all()

    con={
        'pid' : pid,
        'cid' : cid
    }
    return render(request,"order.html",con)

def add_to_cart(request,id):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = Add_product.objects.get(id=id)
        pcid = Add_to_cart.objects.filter(user_id=uid,product_id=pid).exists()
        
        if pcid:
            pcid = Add_to_cart.objects.get(product_id=id)
            pcid.qty = pcid.qty + 1
            pcid.total_price = pcid.qty * pcid.price
            pcid.save()

            return redirect('shopping_cart')
        else:
            pid = Add_product.objects.get(id=id)
            
            acid = Add_to_cart.objects.create(user_id = uid,
                                            product_id= pid,
                                            name = pid.name,
                                            pic = pid.pic,
                                            price = pid.price,
                                            qty = pid.qty,
                                            total_price = pid.qty * pid.price
                                            )
            return redirect('shopping_cart')
    else:
        return render(request,"order.html")

def shop_detail(request,id):
    vid = Add_product.objects.get(id=id)

    con={
        'vid' : vid
    }
    return render(request,"shop_detail.html",con)

def shopping_cart(request):
    uid = User.objects.get(email=request.session['email'])
    cid = Add_to_cart.objects.filter(user_id=uid)
    con = {
        'cid' : cid,
    }
    return render(request,"shopping_cart.html",con)

def plus(request,id):
    pid = Add_to_cart.objects.get(id=id)
    if pid:
        pid.qty= pid.qty + 1
        pid.total_price= pid.qty * pid.price
        pid.save()

        return redirect('shopping_cart')
    else:
        return render(request,'shopping_cart.html')
    
def minus(request,id):
    mid = Add_to_cart.objects.get(id=id)
    if mid.qty == 1:
        mid.delete()
        return redirect('shopping_cart')
    else:
        if mid:
            mid.qty = mid.qty - 1
            mid.total_price = mid.qty * mid.price
            mid.save()

            return redirect('shopping_cart')
        else:
            return render(request,'shopping_cart.html')

def remove(request,id):
    did = Add_to_cart.objects.get(id=id).delete()

    return redirect('shopping_cart')

def billing_address(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        aid = Billing_Address.objects.filter(user_id=uid).exists
        cid = Billing_Address.objects.get(user_id=uid)

        if aid : 
            l1 = []
            pid = Add_to_cart.objects.filter(user_id=uid)
            for i in pid:
                l1.append(f"name ={i.name} price={i.price} qty={i.qty} total_price={i.total_price}")
            cid.list=l1
            cid.save()
            return redirect('checkout')

    except:
        if request.POST:
            fname = request.POST['fname']
            lname = request.POST['lname']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            phone = request.POST['phone']
            email = request.POST['email']
            note = request.POST['note']

            bid = Billing_Address.objects.create(user_id=uid,
                                                fname=fname,
                                                lname=lname,
                                                address=address,
                                                city=city,
                                                state=state,
                                                pincode=pincode,
                                                phone=phone,
                                                email=email,
                                                note=note)
            l1 = []
            aid = Add_to_cart.objects.filter(user_id=uid)
            for i in aid:
                l1.append(f"name = {i.name} price= {i.price} qty={i.qty} total_price={i.total_price} ")
                bid.list = l1
                bid.save()

            return redirect('checkout')
        else:
            return render(request,"billing_address.html")
    
def checkout(request):
    uid = User.objects.get(email=request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count
    ctid = Add_to_cart.objects.all()
    prod = Add_to_cart.objects.filter(user_id=uid)

    l1 = []
    sub_total = 0
    total = 1

    for i in prod:
        z = i.price * i.qty
        l1.append(z)
        a = sum(l1)
    sub_total = sub_total + a
    total = sub_total + 50

    amount = total*100 
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({

                                    'amount':amount,
                                   'currency':'INR',
                                   'payment_capture':1
    })
    con = {
        'lid' : lid,
        'ctid' : ctid,
        'response' : response,
        'prod' : prod,
        'sub_total' : sub_total,
        'total' : total,
    }

    for i in prod:
        Payload.objects.create(user_id=i.user_id,
                               product_id=i.product_id,
                               name=i.name,
                               price=i.price,
                               qty=i.qty,
                               total_price=i.total_price,
                               pic=i.pic)

    return render(request,'checkout.html',con)

def wishlist(request):
    uid = User.objects.get(email=request.session['email'])
    lid = Add_to_cart.objects.filter(user_id=uid).count()
    cart_id = Add_to_cart.objects.filter(user_id=uid)
    wid = Add_to_wishlist.objects.filter(user_id=uid)

    con = {
        'lid' : lid,
        'cart_id' : cart_id,
        'wid' : wid
    }
    return render(request,'wishlist.html',con)

def add_to_wishlist(request,id):
    uid = User.objects.get(email=request.session['email'])
    pid = Add_product.objects.get(id=id)

    wid = Add_to_wishlist.objects.create(user_id=uid,
                                         product_id=pid,
                                         name = pid.name,
                                         price = pid.price,
                                         pic = pid.pic)
    return redirect('wishlist')

def wishlist_remove(request,id):

    wid = Add_to_wishlist.objects.get(id=id).delete()
    return redirect('wishlist')

def change_address(request):
    uid = User.objects.get(email=request.session['email'])
    did = Billing_Address.objects.get(user_id=uid).delete()

    return redirect('billing_address')

def payload(request):
    uid = User.objects.get(email=request.session['email'])
    did=Add_to_cart.objects.all().delete()
    oid=Payload.objects.filter(user_id=uid)
    aid = Billing_Address.objects.filter(user_id=uid)
    con = {
        'oid' : oid,
        'aid' : aid
    }
    return render(request,"payload.html",con)

def error(request):
    return render(request,'error.html')

def my_address(request):
    uid = User.objects.get(email=request.session['email'])
    aid = Billing_Address.objects.filter(user_id=uid)
    con={
        'aid':aid
    }

    return render(request,'my_address.html',con)

