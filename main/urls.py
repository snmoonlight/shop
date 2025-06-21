from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('beznal', views.beznal),
    path('nal', views.nal),
    path('vozv', views.vozv),
    path('jorn', views.jorn),
    path('otch', views.otch),
    path('<int:pk>/bupdate', views.BUpdateView.as_view(), name='bupdate'),
    path('<int:pk>/nupdate', views.NUpdateView.as_view(), name='nupdate'),
    path('<int:pk>/vupdate', views.VUpdateView.as_view(), name='vupdate')
]
