from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^$', views.ShopView.as_view(), name='home_page'),
    url(r'^login$', views.LogIn.as_view(), name='login'),
    url(r'^logout$', views.LogOutView.as_view(), name='logout'),
    url(r'^sign$', views.RegisterView.as_view(), name='sign_up'),
    url(r'^continue_sign/$', views.EditUserSignView.as_view(), name='continue_sign'),
    url(r'^add_address$', views.AddAddressView.as_view(), name='add_address'),
    url(r'^addresses$', views.ShowAddressesView.as_view(), name='show_address'),
    url(r'^edit_address/(?P<pk>(\d)+)$', views.EditAddressView.as_view(), name='edit_address'),
    url(r'^user$', views.UserInfoView.as_view(), name='user_info'),
    url(r'^add_product$', views.AddProductView.as_view(), name='add_product'),
    url(r'^change_product/(?P<pk>(\d)+)$', views.ChangeProductView.as_view(), name='change_product'),
    # url(r'^change_product$', ChangeProductView.as_view(), name='change_product'),
    url(r'^product/(?P<id>(\d)+)$', views.ProductView.as_view(), name='product_view'),
    url(r'^category/(?P<id>(\d)+)$', views.ShowCategoryProductView.as_view(), name='category_products'),
    url(r'^edit_user$', views.UserEditView.as_view()),
    url(r'^promo$', views.PromoView.as_view(), name='promo'),
    url(r'^news$', views.NewProductView.as_view(), name='new_products'),
    url(r'^contact_us$', views.ContactView.as_view(), name='contact_us'),
    url(r'^change_password$', views.ChangePasswordView.as_view(), name='change_password'),
    url(r'^cart$', views.ShoppingCartView.as_view(), name='shopping_cart'),
    url(r'remove_product/(?P<id>(\d)+)$', views.RemoveProductCart.as_view(), name='remove_cart'),
    url(r'checkout$', views.CheckoutView.as_view(), name='checkout'),
    url(r'pay$', views.PayView.as_view(), name="pay")
]
