from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    otp = models.IntegerField(default=1234)

    def __str__(self):
        return self.email

class Register(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Billing_Address(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pincode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    note = models.TextField(max_length=50)
    list = models.TextField()

    def __str__(self):
        return self.fname

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.IntegerField()
    people = models.IntegerField()
    message = models.TextField(max_length=75)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Add_product(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    qty = models.IntegerField()
    pic = models.ImageField(upload_to='img')
    dec = models.TextField()
   
    def __str__(self):
        return self.name
    
class Add_to_cart(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    product_id = models.ForeignKey(Add_product,on_delete = models.CASCADE)
    pic = models.ImageField()
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Add_to_wishlist(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    product_id = models.ForeignKey(Add_product,on_delete = models.CASCADE)
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    pic = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name
    
class Payload(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Add_product,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    qty = models.IntegerField()
    total_price = models.IntegerField()
    pic = models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.name
    