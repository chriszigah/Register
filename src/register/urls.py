from django.urls import path
from . import views 

from . views import register, home, dashboard, create_record, update_record, view_record, delete_record

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home.as_view(), name=""),
    path("register/", register.as_view(), name="register" ),
    #path("login", login.as_view(), name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path("logout", auth_views.LogoutView.as_view(template_name='register/index.html'), name='logout'),
    #CRUD
    path("dashboard/", dashboard.as_view(), name="dashboard"),
    path("create-record", create_record.as_view(), name="create-record"),
    path('update-record/<int:pk>/', update_record.as_view(), name="update-record"),
    path('record/<int:pk>/', views.view_record.as_view(), name="record"),
    path('delete-record/<int:pk>', delete_record.as_view(), name="delete-record"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  