from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name']


class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username','first_name', 'last_name', 'full_name', 'email']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=Teacher.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'first_name', 'last_name', 'full_name', 'email']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=Student.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LoginSerializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        user=authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh=RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError({'detail': 'Недействительный или уже отозванный токен'})



class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LinksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class CourseListSerializers(serializers.ModelSerializer):
    category = CategoryListSerializers()
    created_by = TeacherSerializers()
    class Meta:
        model = Course
        fields = ['id', 'category', 'course_name', 'created_by', 'price', 'level']

class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name_lesson', 'video_url', 'content', ]

class AssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['name_assignment', 'description', 'due_date']


class ExamListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['name_exam', 'passing_score', 'duration']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['name_question', 'text']


class AnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class CertificateListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['issued_at', 'certificate_url']


class CourseReviewSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    class Meta:
        model = CourseReview
        fields = ['user', 'rating', 'comment']


class CartSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    class Meta:
        model = Cart
        fields = ['user', 'created_date']


class CartItemSerializers(serializers.ModelSerializer):
    course = CourseListSerializers(read_only=True)
    cart = CartSerializers(read_only=True)
    get_total_price = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['cart', 'course', 'quantity', 'get_total_price']

class CategoryDetailSerializers(serializers.ModelSerializer):
    course_list = CourseListSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'course_list']

class CourseDetailSerializers(serializers.ModelSerializer):
    created_by = TeacherSerializers()
    course_lesson = LessonListSerializers(read_only=True, many=True)
    review = CourseReviewSerializers(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'level', 'price', 'course_lesson',
                  'created_by', 'review', 'created_at', 'updated_at']

class CourseCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'