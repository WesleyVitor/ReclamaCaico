from django.shortcuts import render,redirect,get_object_or_404
from .forms import CadastraReclamacaoForm,LoginUsuarioForm,SignUpForm,RegistroDeComentarioForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Reclamacao,Comentario, Curtida
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import date


# Create your views here.

@csrf_protect
@login_required
def CadastraReclamacao(request):
	if request.method == 'POST':
		form = CadastraReclamacaoForm(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.nome = request.user.username
			obj.foto = form.cleaned_data['foto']
			print(obj.foto)
			obj.save()
			return redirect('/ListaSeu')

	else:
		form = CadastraReclamacaoForm()
	return render(request,'Usuario/home.html',{'form':form,})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request,user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'Usuario/cadastro.html', {'form': form})
def logar(request):
	if request.method == 'POST':
		form = LoginUsuarioForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				login(request,user)
				return redirect('/CadastraReclamacao')
	else:
		form = LoginUsuarioForm()
	return render(request,'Usuario/login.html',{'form':form})
@login_required
def sair(request):
	logout(request)
	return redirect('/')
@login_required
def ListaSeu(request):
	o = User.objects.get(id=request.user.id)
	print(o)
	print(Reclamacao.user)
	if request.user.is_authenticated:
		p = Reclamacao.objects.filter(nome=request.user)
		
	
	return render(request,'Usuario/ListaSeu.html',{'lista':p})

@csrf_protect
@login_required
def RegistroDeComentario(request):
	futuro = date.fromordinal(date.today().toordinal()+1)
	r = Reclamacao.objects.all()
	if request.method == 'POST':
		form = RegistroDeComentarioForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.idd =  Reclamacao.objects.get(id=request.POST.get('idReclama'))
			obj.nome = request.user.username
			
			obj.save()
			
			return redirect('comentariosL',id=request.POST.get('idReclama'))
	else:
		form = RegistroDeComentarioForm()
	for i in r:
		if i.vencimento==date.today():
			i.delete()
			
	Lreclam = Reclamacao.objects.all().order_by("-curtidas")
	Curtidas = Curtida.objects.all()	
	
		#o = Comentario.objects.all()

		
	return render(request,'Usuario/reclamacao.html',{'form':form, 'lista':Lreclam, 'curtidas': Curtidas})
@login_required
def ListaComentarios(request, id):

	o = Comentario.objects.filter(idd_id=id).order_by('data')

	
	
	return render(request,'Usuario/ComentarioL.html',{'o':o})
@login_required
def DeletaReclamacao(request,id):
	delete = Reclamacao.objects.get(id=id)
	delete.delete()
	return redirect('ListaSeu')
@login_required
def EditarReclamacao(request,id):
	editar = get_object_or_404(Reclamacao,id=id)
	if request.method == 'POST':
		form =CadastraReclamacaoForm(request.POST, request.FILES,instance=editar)

		if form.is_valid():
			imagem = form.save(commit=False)
			if not(imagem.foto):
				imagem.foto = edita.foto.url
			form.nome = request.user.username
			form.save()
			return redirect('/ListaSeu')
	else:
		form = CadastraReclamacaoForm(instance = editar)
	return render(request,'Usuario/home.html',{'form':form})

@login_required
def Curtir(request, id):
	publicacao = get_object_or_404(Reclamacao, id=id)
	try:
		c = Curtida.objects.get(usuario=request.user, publicacao=id)
		c.delete()
	except Curtida.DoesNotExist:
		c = Curtida()
		c.usuario = request.user
		c.publicacao = publicacao
		c.save()

	publicacao.curtidas = publicacao.curtida_set.count()
	publicacao.save()
	return redirect('coment')


