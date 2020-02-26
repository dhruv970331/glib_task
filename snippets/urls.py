from django.urls import path
from .views import SnippetCreateView,SnippetDetailView,SnippetEditView,SnippetListView
app_name = "snippets"
urlpatterns = [
    path("create/",SnippetCreateView.as_view(),name = 'create'),
    path("<int:pk>/",SnippetDetailView.as_view(),name="snippet-detail"),
    path("<int:pk>/edit",SnippetEditView.as_view(),name="edit"),
    path("<int:pk>/snippets/",SnippetListView.as_view(),name='list')
]