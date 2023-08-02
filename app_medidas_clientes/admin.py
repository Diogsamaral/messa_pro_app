from django.contrib import admin
from .models import Pessoa

# Registre o modelo Pessoa para que ele apareça no admin do Django
admin.site.register(Pessoa)