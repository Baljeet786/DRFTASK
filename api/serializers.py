from django.db.models import fields
from .models import Course, CourseChapter, Assignment, UserProfile
from rest_framework import serializers

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'password')


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id','title','description','course','course_chapter']

class CourseChapterSerializer(serializers.ModelSerializer):
    course_chapter_assignments = AssignmentSerializer(many=True,read_only=True)
    class Meta:
        model = CourseChapter
        fields = ['id','name','order','course','created_utc','modified_utc','course_chapter_assignments']
     


class CourseSerializer(serializers.ModelSerializer):
    course_chapter = CourseChapterSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = ['id','name','description','order','created_utc','modified_utc','course_chapter']
      












