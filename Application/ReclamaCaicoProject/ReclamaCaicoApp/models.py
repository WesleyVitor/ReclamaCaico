from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import date

# Create your models here.

class Reclamacao(models.Model):
	titulo = models.CharField(max_length=50,default="w",help_text="Digite o titulo da Reclamacao")
	nome = models.CharField(max_length=200,help_text='Digite o seu nome de usuario')
	
	bairro = models.CharField(max_length=200,help_text="Digite o Bairro da Reclamacao")
	rua = models.CharField(max_length=200,help_text="Digite o Rua da Reclamacao")
	#Ncasa = models.IntegerField()
	foto = models.FileField(upload_to='Reclamacao', null=True)
	descricao = models.TextField(max_length=300,default='w')
	#user = models.ForeignKey(User,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	curtidas = models.IntegerField(null=True)
	vencimento = models.DateField(default=date.fromordinal(date.today().toordinal()+30))

class Login(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

class Comentario(models.Model):
	text1 = models.TextField(max_length=1000)
	idd = models.ForeignKey(Reclamacao,on_delete=models.CASCADE)
	data = models.DateField(default=date.today())
	nome = models.CharField(max_length=200)

class Curtida(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	publicacao = models.ForeignKey(Reclamacao, on_delete=models.CASCADE, null=True)
	class Meta:
		unique_together = ('usuario', 'publicacao')