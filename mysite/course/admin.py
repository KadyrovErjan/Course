from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import *


class QuestionInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Question
    extra = 1

class AnswersInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Answers
    extra = 1

class LessonInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Lesson
    extra = 1


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    inlines = [LessonInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category, Assignment, Answers)
class ALLAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Exam)
class QuestionAdmin(TranslationAdmin):
    inlines = [QuestionInline]

@admin.register(Question)
class AnswersAdmin(TranslationAdmin):
    inlines = [AnswersInline]


admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Certificate)
admin.site.register(CourseReview)
