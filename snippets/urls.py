from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.snippet_list), #This is for method based views
    # path('<int:pk>/', views.snippet_detail), #This is for method based views
    path('', views.SnippetList.as_view()), #This is for class based views
    path('<int:pk>/', views.SnippetDetail.as_view()), #This is for class based views
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
