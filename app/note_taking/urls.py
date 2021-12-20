from django.urls import path, include
from rest_framework.routers import DefaultRouter
from note_taking import views

router = DefaultRouter()
router.register(r'notetaking', views.NoteTakingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
