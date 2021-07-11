from django.contrib import admin
from .models import *


class QuestionInline(admin.TabularInline):
    model = Question

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Poll._meta.fields]
    list_filter = ('poll_title', 'start_date', 'end_date')
    list_display_links = ('poll_title',)
    search_fields = ('poll_title',)
    ordering = ('start_date',)
    inlines = [QuestionInline]
    date_hierarchy = 'start_date'


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]
    list_filter = ('question_type',)
    list_display_links = ('poll', 'id', 'question_text')
    search_fields = ('question_text',)
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Choice._meta.fields]
    list_display_links = ('question', 'id',)
    search_fields = ('question', 'user_answer',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Answer._meta.fields]
    list_filter = ('poll', 'question')
    list_display_links = ('poll', 'id', 'answer_val',)
    search_fields = ('user_id', 'poll', 'question')
