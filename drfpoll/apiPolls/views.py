from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework.decorators import api_view
from django.http import Http404



from django.utils import timezone

from .models import Poll, Question, Choice, Answer
from .serializers import QuestionListSerializer, ChoiceListSerializer, AnswerSerializer, PollSerializer, AnswerListUserSerializer


class PollActiveView(APIView):
    """ Вывод списка активных опросов """

    def get(self, request):
        polls = Poll.objects.filter(end_date__gte=timezone.now(), start_date__lte=timezone.now())
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class PollCreatView(APIView):
    """ Создание опроса """

    permission_classes = [permissions.IsAdminUser,]

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PollDetailView(APIView):
    """
    Получеие, обновление и удаление опроса.
    """

    permission_classes = [permissions.IsAdminUser,]

    def get_object(self, poll_id):
        try:
            return Poll.objects.get(pk=poll_id)
        except Poll.DoesNotExist:
            raise Http404

    def get(self, request, poll_id):
        poll = self.get_object(poll_id)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def put(self, request, poll_id):
        poll = self.get_object(poll_id)
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, poll_id):
        poll = self.get_object(poll_id)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionCreatView(APIView):
    """ Создание вопроса """

    permission_classes = [permissions.IsAdminUser,]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetailView(APIView):
    """
    Получеие, обновление и удаление вопроса.
    """

    permission_classes = [permissions.IsAdminUser,]

    def get_object(self, question_id):
        try:
            return Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionListSerializer(question)
        return Response(serializer.data)

    def put(self, request, question_id):
        question = self.get_object(question_id)
        serializer = QuestionListSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question = self.get_object(question_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChoiceCreatView(APIView):
    """ Создание вариантов ответа """

    permission_classes = [permissions.IsAdminUser,]

    def get(self, request):
        choices = Choice.objects.all()
        serializer = ChoiceListSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChoiceListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChoiceDetailView(APIView):
    """
    Получеие, обновление и удаление вариантов ответа.
    """

    permission_classes = [permissions.IsAdminUser,]

    def get_object(self, choice_id):
        try:
            return Choice.objects.get(pk=choice_id)
        except Choice.DoesNotExist:
            raise Http404

    def get(self, request, choice_id):
        choice = self.get_object(choice_id)
        serializer = ChoiceListSerializer(choice)
        return Response(serializer.data)

    def put(self, request, choice_id):
        choice = self.get_object(choice_id)
        serializer = ChoiceListSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, choice_id):
        choice = self.get_object(choice_id)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerCreatView(APIView):
    """ Ответ пользователя """

    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetailView(APIView):
    """
    Получеие, обновление и удаление ответа пользователя.
    """

    def get_object(self, answer_id):
        try:
            return Answer.objects.get(pk=answer_id)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, answer_id):
        answer = self.get_object(answer_id)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, answer_id):
        answer = self.get_object(answer_id)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_id):
        answer = self.get_object(answer_id)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerListView(APIView):
    """ Ответ пользователя """

    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, user_id):
        answers = Answer.objects.filter(user_id=user_id)
        serializer = AnswerListUserSerializer(answers, many=True)
        return Response(serializer.data)
