from django.urls import path
from . import views



urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('usuario', views.UsuarioView.as_view()),
    path('titulo', views.TituloView.as_view()),
    path('titulo/<int:titulo_id>',views.TituloDetailView.as_view()),
    path('eslogan', views.EsloganView.as_view()),
    path('eslogan/<int:eslogan_id>',views.EsloganDetailView.as_view()),
    path('parrafoobjetivos', views.ParrafoobjetivosView.as_view()),
    path('parrafoobjetivos/<int:parrafoobjetivos_id>',views.ParrafoobjetivosDetailView.as_view()),
    path('subobjetivo1', views.Subobjetivo1View.as_view()),
    path('subobjetivo1/<int:subobjetivo1_id>',views.Subobjetivo1DetailView.as_view()),
    path('subobjetivo2', views.Subobjetivo2View.as_view()),
    path('tec1', views.Tec1View.as_view()),
    path('tec2', views.Tec2View.as_view()),
    path('tec3', views.Tec3View.as_view()),
    path('tec4', views.Tec4View.as_view()),
    path('contacto', views.ContactoView.as_view())
]
