from django.urls import path, include
from rest_framework import routers
from .views import *
from .auth_views import register_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('roles', RolViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('instructores', InstructorViewSet)
router.register('cursos', CursoViewSet)
router.register('inscripciones', InscripcionViewSet)
router.register('eventos', EventoViewSet)
router.register('categorias', CategoriaEventoViewSet)
router.register('noticias', NoticiaViewSet)
router.register('contacto', MensajeContactoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register_user, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]