from django.shortcuts import render,redirect
from django.views import View
from .models import Product
from django.db.models import Count
from django.contrib import messages
from .models import Customer,Cart,Product
def home(request):
    return render(request,'app/home.html')

class CategoryView(View):
    def get(self,request,val):
        products=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        print(products)
        print(title)
        return render(request,'app/category.html',locals())


class CategoryTitle(View):
    def get(self,request,val):
        products=Product.objects.filter(title=val)
        title=Product.objects.filter(category=products[0].category).values('title')
        # print(products)
        # print(title)
        return render(request,'app/category.html',locals())


class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',locals())
    


def about(request):
    return render(request,'app/about.html')


def contact(request):
    return render(request,'app/contact.html')



#customer registration
from .forms import CustomerRegistrationForm,CustomerProfileForm,MyPasswordChangeForm
class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',locals())
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registered successfully.")

        else:
            messages.warning(request,"Invalid Input Data")

        return render(request,'app/customerregistration.html',locals())


class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        
        if form.is_valid():
            user=request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']

            reg=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
            reg.save()

            messages.success(request,"Congratulations! Profile Saved Successfully.")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'app/profile.html',locals())





# to display all the profile address
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'app/address.html',locals())


#class to update the data 
class UpdateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add) #To add current values into the form 
        return render(request,'app/updateAddress.html',locals())
        
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.state = form.cleaned_data['state']

            # reg=Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
            add.save()
            messages.success(request,"Congratulations! Profile Updated Successfully.")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')


# add to cart 
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(pk=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

def show_cart(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    return render(request,'app/addtocart.html',locals())