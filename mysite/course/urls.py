from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'students', StudentViewSet, basename='students')


urlpatterns = [


    path('', include(router.urls)),
    path('category/', CategoryAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('c/', CourseListAPIView.as_view(), name='course_list'),
    path('c/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('c/create/', CourseDetailUpdateDestroyOwnerAPIView.as_view(), name='course_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('assignment/', AssignmentAPIView.as_view(), name='assignment_list'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('question/', QuestionListAPIView.as_view(), name='question_list'),
    path('certificate/', CertificateListAPIView.as_view(), name='certificate_list'),
    path('review/', CourseReviewAPIView.as_view(), name='review_list'),
    path('cart/', CartAPIView.as_view(), name='cart_list'),
    path('cart_item/', CartItemAPIView.as_view(), name='cart_item_list'),
    path('teacher/', TeacherAPIView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', CourseDetailAPIView.as_view(), name='teacher_detail'),
    path('register/teacher/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('register/student/', StudentRegisterView.as_view(), name='student_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]