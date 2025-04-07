from .models import Teacher, Category, Course, Lesson, Assignment, Exam, Question, Answers
from modeltranslation.translator import TranslationOptions,register

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('bio',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('name_lesson', 'content')

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('name_assignment', 'description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('name_exam', )

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('text', 'name_question')

@register(Answers)
class AnswersTranslationOptions(TranslationOptions):
    fields = ('answers',)
