from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("about",views.about,name="about"),
    path("skills/",views.skills,name="skills"),
    path("skills",views.skills,name="skills"), 
    path("projects/",views.projects,name="projects"),
    path("projects",views.projects,name="projects"),
    path("contact",views.contact_view,name="contact"),
    path("contact/",views.contact_view,name="contact"),
]
