
from .serializers import CourseSerializer, AssignmentSerializer, CourseChapterSerializer
from .models import  Course, CourseChapter, Assignment
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from .serializers import  RegisterSerializer
from .permissions import WriteByAdminOnlyPermission

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": "new user registered successfully!"
        })



class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    


class CourseChapterList(generics.ListAPIView):
    serializer_class = CourseChapterSerializer
    queryset = CourseChapter.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    


class AssignmentList(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, WriteByAdminOnlyPermission]
    

class CourseListCreate(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    


class CourseChapterListCreate(generics.ListCreateAPIView):
    serializer_class = CourseChapterSerializer
    queryset = CourseChapter.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    



class AssignmentListCreate(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    


class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    



class CourseChapterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CourseChapterSerializer
    queryset = CourseChapter.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    



class AssignmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    








