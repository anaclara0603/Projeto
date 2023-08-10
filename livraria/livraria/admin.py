from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from .models import Categoria , Editora
admin.site.register(Categoria)
admin.site.register(Editora)