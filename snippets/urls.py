from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.snippet_list), #This is for method based views
    # path('<int:pk>/', views.snippet_detail), #This is for method based views
    path('list', views.SnippetList.as_view(),name='snippet-list'), #This is for class based views
    path('<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'), #This is for class based views
    path('users', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(),name='user-detail'),
    path('', views.api_root),
    path('<int:pk>/highlight', views.SnippetHighlight.as_view(),name='snippet-highlight'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
