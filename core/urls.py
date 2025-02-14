from django.urls import path


from .views import home, about, contato

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("contato/", contato, name="contato"),
]
