from django.urls import path
from . import views 

from . views import Register, Home, Dashboard, CreateRecord, UpdateRecord, ViewRecord, DeleteRecord

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", Home.as_view(), name=""),
    path("register/", Register.as_view(), name="register" ),
    #path("login", login.as_view(), name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path("logout", auth_views.LogoutView.as_view(template_name='register/index.html'), name='logout'),
    #CRUD
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("create-record", CreateRecord.as_view(), name="create-record"),
    path('update-record/<int:pk>/', UpdateRecord.as_view(), name="update-record"),
    path('record/<int:pk>/', views.ViewRecord.as_view(), name="record"),
    path('delete-record/<int:pk>', DeleteRecord.as_view(), name="delete-record"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  