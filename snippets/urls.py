from django.urls import path, include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


#binding viewSets 
from snippets.views import SnippetViewSet, UserViewSet #, api_root
# from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from rest_framework.schemas import get_schema_view
# Adding schema view to our snippets app
schema_view = get_schema_view(title='Pastebin API')


# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # url(r'^schema/$', schema_view),
    path('', include(router.urls))
]

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })

# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


# urlpatterns = [
#     path('', views.api_root),
#     # path('', views.snippet_list), #This is for method based views
#     # path('<int:pk>/', views.snippet_detail), #This is for method based views
#     # path('list', views.SnippetList.as_view(),name='snippet-list'), #This is for class based views
#     path('list', snippet_list,name='snippet-list'), #This is for class based views  
#     # path('<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'), #This is for class based views
#     path('<int:pk>/', snippet_detail, name='snippet-detail'), #This is for class based views    
#     # path('users', views.UserList.as_view(),name='user-list'),
#     path('users', user_list, name='user-list'),    
#     # path('users/<int:pk>', views.UserDetail.as_view(),name='user-detail'),
#     path('users/<int:pk>', user_detail, name='user-detail'),    
#     # path('<int:pk>/highlight', views.SnippetHighlight.as_view(),name='snippet-highlight'),
#     path('<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
    
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
