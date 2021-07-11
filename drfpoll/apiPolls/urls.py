from django.urls import path

from . import views

urlpatterns = [
    path('active-polls/', views.PollActiveView.as_view()),
    path('poll-creat/', views.PollCreatView.as_view()),
    path('<int:poll_id>/', views.PollDetailView.as_view()),

    path('questions/', views.QuestionCreatView.as_view()),
    path('questions/<int:question_id>/', views.QuestionDetailView.as_view()),

    path('choices/', views.ChoiceCreatView.as_view()),
    path('choices/<int:choice_id>/', views.ChoiceDetailView.as_view()),

    path('answer/', views.AnswerCreatView.as_view()),
    path('answer/<int:user_id>/', views.AnswerListView.as_view()),
    path('answer/update/<int:answer_id>/', views.AnswerDetailView.as_view()),




]
