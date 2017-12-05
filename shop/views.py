from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
    )
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from .forms import (
    ChangePasswordForm,
    ContactForm,
    InvoiceAddressForm,
    LoginForm,
    OrderAddressForm,
    ProductAvailabilityForm,
    ProductQuantityForm,
    RegisterForm,
    )
from .models import (
    Address,
    Invoice,
    Order,
    OrderLine,
    Payment,
    Product,
    ProductAvailability,
    ProductCategory,
    ShoppingCart,
    User,
    )


def url_response_redirect(url_name):
    url = reverse('{}'.format(url_name),)
    return HttpResponseRedirect(url)


class ShopView(View):

    def get(self, request):
        products = Product.objects.order_by('?')[:6]
        return render(request, 'shop_home.html', {'products': products})


class RegisterView(View):

    def get(self, request):
        form = RegisterForm
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=username,
                                                email=email, password=password)
            ShoppingCart.objects.create(user=new_user)
            group = Group.objects.get(name='Buyer')
            group.user_set.add(new_user)
            user = authenticate(username=username, password=password)
            login(request, user)
            return url_response_redirect('continue_sign')
        else:
            return render(request, 'register.html', {'form': form})


class EditUserSignView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'edit_user_sign.html'
    fields = ('first_name', 'last_name', 'telephone', 'date_of_birth')
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user


class LogIn(View):

    def get(self, request):
        form = LoginForm
        return render(request, 'loggin.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return url_response_redirect('home_page')
            else:
                return render(
                    request, 'loggin.html',
                    {'form': form,
                     'field.error': 'Invalid username or password'})


class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return url_response_redirect('home_page')


class AddAddressView(LoginRequiredMixin, CreateView):
    model = Address
    template_name = 'add_address.html'
    fields = ('city', 'zip_code', 'street', 'house_no', 'flat_no')
    success_url = '/addresses'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddAddressView, self).form_valid(form)


class EditAddressView(LoginRequiredMixin, UpdateView):
    model = Address
    template_name = 'add_address.html'
    fields = ('city', 'zip_code', 'street', 'house_no', 'flat_no')
    success_url = '/addresses'


class ShowAddressesView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        addresses = Address.objects.filter(user=user)
        return render(request, 'user_addresses.html', {'addresses': addresses})


class UserInfoView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        return render(request, 'user_info.html', {'user': user})


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'edit_user_sign.html'
    fields = ('username', 'first_name', 'last_name',
              'email', 'telephone', 'date_of_birth')
    success_url = '/user'

    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(LoginRequiredMixin, View):

    def get(self, request):
        form = ChangePasswordForm
        return render(request, 'change_password.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            if authenticate(username=user,
                            password=form.cleaned_data['password_old']):
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                user = authenticate(username=user, password=password)
                login(request, user)
                return url_response_redirect('user_info')

        return render(request, 'change_password.html', {'form': form})


class AddProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'shop.add_product'

    def get(self, request):
        form = ProductAvailabilityForm
        return render(request, 'add_product.html', {'form': form})

    def post(self, request):
        form = ProductAvailabilityForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            ProductAvailability.objects.create(
                quantity=form.cleaned_data['quantity'], product=product)
            url = reverse_lazy('product_view', kwargs={'id': product.pk})
            return HttpResponseRedirect(url)


class ProductView(View):

    def get(self, request, id):
        product = Product.objects.get(pk=id)
        product_avability = ProductAvailability.objects.get(product=product)
        quantity = product_avability.quantity
        form = ProductQuantityForm
        return render(request, 'product_view.html',
                      {'product': product, 'form': form, 'quantity': quantity})

    def post(self, request, id):
        form = ProductQuantityForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(pk=id)
            shopping_cart = ShoppingCart.objects.get(user=request.user)
            orders_line = OrderLine.objects.filter(shopping_cart=shopping_cart)
            n = 0
            true_false = False
            if orders_line:
                while n < len(orders_line):
                    if orders_line[n].product == product:
                        orders_line[n].quantity = (
                            orders_line[n].quantity
                            + form.cleaned_data['quantity'])

                        if orders_line[n].product.promo:
                            orders_line[n].price_quantity = (
                                product.promo_price * orders_line[n].quantity)
                        else:
                            orders_line[n].price_quantity = (
                                product.price * orders_line[n].quantity)
                        orders_line[n].save()
                        true_false = True
                        break
                    else:
                        true_false = False
                        n += 1

            if not true_false:
                if product.promo:
                    OrderLine.objects.create(
                        product=product,
                        quantity=form.cleaned_data['quantity'],
                        price_quantity=(form.cleaned_data['quantity']
                                        * product.promo_price),
                        shopping_cart=shopping_cart)
                else:
                    OrderLine.objects.create(
                        product=product,
                        quantity=form.cleaned_data['quantity'],
                        price_quantity=(form.cleaned_data['quantity']
                                        * product.price),
                        shopping_cart=shopping_cart)
            return url_response_redirect('shopping_cart')
        else:
            return Http404('Bad gateway')


class ChangeProductView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        UpdateView):

    permission_required = 'shop.change_product'
    form_class = ProductAvailabilityForm
    template_name = 'add_product.html'

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs.get('pk'))

    def post(self, request, pk):
        form = ProductAvailabilityForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.get(pk=pk)
            product.product_name = form.cleaned_data['product_name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.promo = form.cleaned_data['promo']
            product.promo_percent = form.cleaned_data['promo_percent']
            if form.cleaned_data['image']:
                product.image = None
                product.save()
                product.image = request.FILES['image']
            product.category = form.cleaned_data['category']
            product.save()
            available = ProductAvailability.objects.get(product=product)
            available.quantity = form.cleaned_data['quantity']
            available.save()
        url = reverse_lazy('product_view', kwargs={'id': product.id})
        return HttpResponseRedirect(url)


class ShowCategoryProductView(View):

    def get(self, request, id):
        category = ProductCategory.objects.get(pk=id)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products})


class PromoView(View):

    def get(self, request):
        products = Product.objects.filter(promo=True)
        return render(request, 'promo_products.html', {'products': products})


class NewProductView(LoginRequiredMixin, View):

    def get(self, request):
        products = Product.objects.all().order_by('-add_date')[:6]
        return render(request, 'news_products.html', {'products': products})


class ContactView(View):

    def get(self, request):
        form = ContactForm
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')
            ctx = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }

            content = template.render(ctx)

            email = EmailMessage("New contact form submission",
                                 content,
                                 ".Buy" + " ",
                                 ['dotBuy@gmail.com'],
                                 headers={'Reply-To': contact_email}
                                 )
            email.send()
            return HttpResponseRedirect('contact_us')

        return render(request, 'contact.html', {'form': form})


class ShoppingCartView(View):

    def get(self, request):
        if not request.user.is_authenticated():
            url = reverse('login')
            return HttpResponseRedirect(url)
        user = request.user
        shopping_cart = ShoppingCart.objects.get(user=user)
        orders_lines = (OrderLine.objects.
                        filter(shopping_cart=shopping_cart).filter(order=None))
        product_sum = 0
        for order_line in orders_lines:
            product_sum += order_line.price_quantity
        return render(request,
                      'cart.html',
                      {'products': orders_lines, 'sum': product_sum})


class RemoveProductCart(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'shop.delete_orderline'

    def get(self, request, id):
        order_line = OrderLine.objects.get(pk=id)
        if request.user == order_line.shopping_cart.user:
            order_line.delete()
            return url_response_redirect('shopping_cart')
        else:
            return Http404('Bad request')


class CheckoutView(View):

    def get(self, request):
        user = request.user
        shopping_cart = ShoppingCart.objects.get(user=user)
        orders_lines = (OrderLine.objects.
                        filter(shopping_cart=shopping_cart).filter(order=None))
        product_sum = 0
        for p in orders_lines:
            if not p.order:
                product_sum += p.price_quantity
        form_order = OrderAddressForm(prefix="form_order")
        form_invoice = InvoiceAddressForm(prefix="form_invoice")
        ctx = {
            'products': orders_lines,
            'sum': product_sum,
            'form_order': form_order,
            'form_invoice': form_invoice,
               }
        return render(request, 'checkout.html', ctx)

    def post(self, request):
        form_order = OrderAddressForm(request.POST, prefix="form_order")
        order_valid = form_order.is_valid()
        form_invoice = InvoiceAddressForm(request.POST, prefix="form_invoice")
        invoice_valid = form_invoice.is_valid()
        user = request.user
        shopping_cart = ShoppingCart.objects.get(user=user)
        orders_lines = (OrderLine.objects.
                        filter(shopping_cart=shopping_cart).filter(order=None))
        if order_valid and invoice_valid:
            product_sum = 0
            for p in orders_lines:
                product_sum += p.price_quantity
            order = Order.objects.create(
                user=user, comments=form_order.cleaned_data['comments'],
                sum_product_cost=product_sum,
                send_address_id=form_order.cleaned_data['send_address'])
            Invoice.objects.create(
                order=order,
                bill_address_id=form_invoice.cleaned_data['bill_address'])
            for order_line in orders_lines:
                order_line.order = order
                order_line.save()
                product = ProductAvailability.objects.get(
                    product=order_line.product)
                product.quantity = product.quantity - order_line.quantity
                product.save()
                Payment.objects.create(status=True, order=order)
        return url_response_redirect('pay')


class PayView(View):

    def get(self, request):
        user = request.user
        shopping_cart = ShoppingCart.objects.get(user=user)
        order = Order.objects.filter(user=user).latest('pk')
        orders_lines = (OrderLine.objects
                        .filter(shopping_cart=shopping_cart)
                        .filter(order=order))
        sum_to_pay = 0
        for order_line in orders_lines:
            product = order_line.product
            buy_quantity = order_line.quantity
            availability = ProductAvailability.objects.get(product=product)
            if availability.quantity < buy_quantity:
                if product.promo:
                    sum_to_pay += product.promo_price * availability.quantity
                else:
                    sum_to_pay += product.price * availability.quantity
                availability.quantity = 0
            else:
                if product.promo:
                    sum_to_pay += product.promo_price * buy_quantity
                else:
                    sum_to_pay += product.price * buy_quantity

                availability.quantity = availability.quantity - buy_quantity
            availability.save()
        return render(request, 'pay_success.html', {'sum': sum_to_pay, })
