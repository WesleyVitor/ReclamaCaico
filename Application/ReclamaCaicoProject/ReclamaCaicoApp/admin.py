from django.contrib import admin
from .models import Reclamacao,Comentario, Curtida
from django.contrib.auth.models import User
# Register your models here.




admin.site.register(Reclamacao)
admin.site.register(Comentario)
admin.site.register(Curtida)
