from .models import User,QuestionFeedback,Questions
from rest_framework.response import Response
from ousers.serializers import UserProfileSerializer,QuestionFeedbackSerializer,QuestionSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from  rest_framework.views import APIView
from ousers.permissions import IsAdminUser, IsLoggedInUserOrAdmin

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrive' or self.action == 'update' or self.action == 'delete':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class QuestionFeedbackViewSet(viewsets.ModelViewSet):
    
    queryset = QuestionFeedback.objects.all()
    serializer_class = QuestionFeedbackSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
