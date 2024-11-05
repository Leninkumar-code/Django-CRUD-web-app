from django.contrib import admin
from django.urls import path
from app_crud import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.display,name='display'),
    path('create/',views.create),
    path('del/<id>',views.delete_),
    path('upd/<id>',views.update_),
]
