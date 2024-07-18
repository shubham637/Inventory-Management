import datetime
from random import randint

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.views.decorators.cache import never_cache
# importing plan
from django.contrib.auth import get_user_model
import pandas as pd
from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.item.models import Item
from apps.location.models import Store, Area
from apps.product.models import Product

User = get_user_model()
from django.http import HttpResponseRedirect


@method_decorator(never_cache, name='dispatch')
class AdminLoginView(View):
    template_name = 'administrator/login.html'
    success_url = 'admin-dashboard'
    login_url = 'admin-login'
    success_message = 'You have successfully logged in.'
    failure_message = 'Please check credentials.'

    def get(self, request):
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            return HttpResponseRedirect(reverse(self.success_url))
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,
                            password=password)
        if user and (user.is_superuser or user.is_staff):
            login(request, user)
            messages.success(request, self.success_message)
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            messages.error(request, self.failure_message)
            return HttpResponseRedirect(reverse(self.login_url))


class AdminLogoutView(AdminRequiredMixin, LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('admin-login')


class AdminChangePasswordView(AdminRequiredMixin, LoginRequiredMixin, View):
    template_name = 'administrator/change_password.html'

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password has been successfully updated!')
        else:
            messages.error(request, 'Error occured while changing password, please enter a proper password.')
            return render(request, self.template_name, {'form': form})
        return redirect('admin-dashboard')


class AdminDashboardView(AdminRequiredMixin, LoginRequiredMixin, View):

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     customer_id = self.kwargs.get('customer_id')
    #     context['customer'] = get_object_or_404(User, id=customer_id)
    #     context['stores'] = Store.objects.filter(customer_id=customer_id)
    #     return context

    def get(self, request):
        users_count = User.objects.filter(user_type='user').count()
        customer_count = User.objects.filter(user_type='customer').count()
        item_count = Item.objects.filter().count()
        product_count = Product.objects.filter().count()
        store_count = Store.objects.filter().count()
        area_count = Area.objects.filter().count()
        context = {
                    'users_count': users_count,
                    'customer_count': customer_count,
                    'item_count': item_count,
                    'product_count': product_count,
                    'store_count': store_count,
                    'area_count': area_count,
                   }

        # hello = AjayDatatableView()
        return render(request, 'administrator/dashboard.html', context)

