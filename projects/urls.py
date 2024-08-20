from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectsByCategoryView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('category/<str:category>/', ProjectsByCategoryView.as_view(), name='projects_by_category'),
]