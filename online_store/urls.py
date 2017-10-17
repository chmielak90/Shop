"""online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from shop.views import (ShopView, LogIn, LogOutView, RegisterView, EditUserSignView,
                        AddAddressView, EditAddressView, ShowAddressesView, UserInfoView, AddProductView,
                        ProductView, UserEditView, PromoView, NewProductView, ContactView, ChangePasswordView,
                        ShoppingCartView, ChangeProductView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ShopView.as_view(), name='home_page'),
    url(r'^login$', LogIn.as_view(), name='login'),
    url(r'^logout$', LogOutView.as_view(), name='logout'),
    url(r'^sign$', RegisterView.as_view(), name='sign_up'),
    url(r'^continue_sign/$', EditUserSignView.as_view(), name='continue_sign'),
    url(r'^add_address$', AddAddressView.as_view(), name='add_address'),
    url(r'^addresses$', ShowAddressesView.as_view(), name='show_address'),
    url(r'^edit_address/(?P<pk>(\d)+)$', EditAddressView.as_view(), name='edit_address'),
    url(r'^user$', UserInfoView.as_view(), name='user_info'),
    url(r'^add_product$', AddProductView.as_view(), name='add_product'),
    url(r'^change_product', ChangeProductView.as_view(), name='change_product'),
    url(r'^product/(?P<id>(\d)+)$', ProductView.as_view(), name='product_view'),
    url(r'^edit_user$', UserEditView.as_view()),
    url(r'^promo$', PromoView.as_view(), name='promo'),
    url(r'^news$', NewProductView.as_view(), name='new_products'),
    url(r'^contact_us$', ContactView.as_view(), name='contact_us'),
    url(r'^change_password$', ChangePasswordView.as_view(), name='change_password'),
    url(r'^cart$', ShoppingCartView.as_view(),name='shopping_cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
