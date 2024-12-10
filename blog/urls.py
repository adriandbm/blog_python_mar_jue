from django.urls import path
from .views import HomePageView, PublicationCreateView, PublicationDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path("publication/new/", PublicationCreateView.as_view(), name="publication_new") ,
    path("publication/<int:pk>/", PublicationDetailView.as_view(), name="publication_detail") ,
    ] 