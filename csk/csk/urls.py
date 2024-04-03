from django.contrib import admin
from django.urls import path
from mapapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofrightcylinder/',views.surfacearea,name="surfaceareaofrightcylinder"),
    path('',views.surfacearea,name="surfaceareaofrightcylinderroot")
]