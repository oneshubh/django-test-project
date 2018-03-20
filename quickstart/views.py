# from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, QuestionSerializer
from polls.models import Question


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows questions to be viewed or edited.
    """
    # q = get_object_or_404(Question, pk=question_id)
    # question = get_object_or_404(Question, pk=1)    
    queryset = Question.objects.all()
    # queryset = question.choice_set.all()
    serializer_class = QuestionSerializer
