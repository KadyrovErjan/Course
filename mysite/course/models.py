from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

USER_ROLE = (
        ('client', 'client'),
        ('teacher', 'teacher'),
        ('administrator', 'administrator')
    )

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=34)
    profile_picture = models.ImageField(upload_to='profile_image')
    role = models.CharField(max_length=15, choices=USER_ROLE, default='client')


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Teacher(UserProfile):
    experience = models.PositiveSmallIntegerField(default=1)
    teacher_role = models.CharField(max_length=15, choices=USER_ROLE, default='teacher')
    bio = models.TextField()

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Teacher'

class Student(UserProfile):
    student_role = models.CharField(max_length=15, choices=USER_ROLE, default='client')

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Student'

class Links(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    links_url = models.URLField()

    def __str__(self):
        return f'{self.student}'

class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_list')
    course_name = models.CharField(max_length=32)
    description = models.TextField()
    LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced')
    )
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES,default='beginner')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    name_lesson= models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_lesson')

    def __str__(self):
        return self.name_lesson


class Assignment(models.Model):
    name_assignment = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='students')


    def __str__(self):
        return self.name_assignment

class Exam(models.Model):
    name_exam = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.PositiveSmallIntegerField()
    duration = models.TimeField()


    def __str__(self):
        return self.name_exam

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    name_question = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name_question}'

class Answers(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=64)
    true_answers = models.BooleanField(default=False)


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return self.student

class CourseReview(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - отзыв'



class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.course} -- {self.quantity}'

