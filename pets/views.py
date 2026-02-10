from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from pets.models import Pet
from photos.models import Photo


# Create your views here.

def pet_add(request: HttpRequest) -> HttpResponse:
    return render(request, 'pets/pet-add-page.html')

def pet_details(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.prefetch_related(
        Prefetch(
            'photo_set',
            queryset=Photo.objects.prefetch_related('tagged_pets', 'like_set')
        )
    ).get(slug=pet_slug)

    context = {'pet': pet}
    return render(request, 'pets/pet-details-page.html', context)

def pet_edit(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-edit-page.html')

def pet_delete(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-delete-page.html')