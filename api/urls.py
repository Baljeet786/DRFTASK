from django.contrib import admin
from django.urls import path
from .views import AssignmentList, AssignmentListCreate, AssignmentRetrieveUpdateDestroy, CourseChapterList, CourseChapterListCreate, CourseChapterRetrieveUpdateDestroy, CourseList, CourseListCreate, CourseRetrieveUpdateDestroy
from rest_framework.authtoken.views import obtain_auth_token
from .views import  RegisterAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
      
    path('assignments/', AssignmentList.as_view()),
    path('assignment/', AssignmentListCreate.as_view()),
    path('assignment/<pk>/', AssignmentRetrieveUpdateDestroy.as_view()),
    path('coursechapters/', CourseChapterList.as_view()),
    path('coursechapter/', CourseChapterListCreate.as_view()),
    path('coursechapter/<pk>/', CourseChapterRetrieveUpdateDestroy.as_view()),
    path('courses/', CourseList.as_view()),
    path('course/', CourseListCreate.as_view()),
    path('course/<pk>/', CourseRetrieveUpdateDestroy.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='create-token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]