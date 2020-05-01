from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('CadastraReclamacao',views.CadastraReclamacao,name='reclamacao'),
	path('CadastraUsuario',views.signup,name='signup'),
	path('',views.logar,name='logar'),
	path('SairUsuario',views.sair,name='sair'),
	#path('ListaReclamacao',views.ListaReclamacao,name='LReclamacao'),
	path('ListaSeu',views.ListaSeu,name='ListaSeu'),
	#path('Forum',views.ComentarioE,name='Forum'),
	path('Coment',views.RegistroDeComentario,name='coment'),
	#path('ListComent',views.listaComent,name='listaComent'),
	path('ComentarioL/<int:id>',views.ListaComentarios,name='comentariosL'),
	path('DeletaReclamacao/<int:id>',views.DeletaReclamacao,name='DeletaReclamacao'),
	path('EditarReclamacao/<int:id>',views.EditarReclamacao,name='EditarReclamacao'),
	path('Curtir/<int:id>', views.Curtir, name="Curtir"),
	
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

