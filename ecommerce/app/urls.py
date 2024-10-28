from django.contrib import admin
from django.urls import path
from .views import home,CategoryView,ProductDetail,CategoryTitle,about,contact,CustomerRegistrationView,ProfileView,address,UpdateAddress,MyPasswordChangeForm,add_to_cart,show_cart
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm
urlpatterns = [
    path('',home,name=""),
    path('category/<slug:val>',CategoryView.as_view(),name='category'),
    path('category-title/<val>',CategoryTitle.as_view(),name='category-title'),
    path('product-detail/<int:pk>',ProductDetail.as_view(),name='product-detail'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('address/',address,name='address'),
    path('updateAddress/<int:pk>',UpdateAddress.as_view(),name='updateAddress'),

    #add to cart
    path("add-to-cart/",add_to_cart,name="add-to-cart"),
    path("cart/",show_cart,name="cart"),
    


    # Authentication
    path('registration/',CustomerRegistrationView.as_view(),name="registration"),
    path('accounts/login/',auth_view.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm),name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/password_change.html',form_class=MyPasswordChangeForm,success_url="/passwordchangedone"),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'),name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    # path('login/', auth_view.LoginView.as_view(), name='login'),

    # password reset
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),

    
]