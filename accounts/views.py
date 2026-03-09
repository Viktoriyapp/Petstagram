from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm

# Create your views here.

UserModel = get_user_model()

# def register(request: HttpRequest) -> HttpResponse:
#     return render(request, 'accounts/register-page.html')


class RegisterAppUserView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('common:home')


def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'accounts/login-page.html')

def profile_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-details-page.html')

def profile_edit(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-edit-page.html')

def profile_delete(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-delete-page.html')