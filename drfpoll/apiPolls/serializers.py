from rest_framework import serializers
from .models import Poll, Question, Choice, Answer


class ChoiceListSerializer(serializers.ModelSerializer):
    """ Список вариантов ответа """

    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text']
        read_only_fields = ['id']

    def validate(self, data):
        try:
            obj = Choice.objects.get(question=data.get('question'), choice_text=data.get('choice_text'))
        except Choice.DoesNotExist:
            return data
        else:
            raise serializers.ValidationError('Такой вариант ответа уже существует.')
        return data

class QuestionListSerializer(serializers.ModelSerializer):
    """ Список вопросов """
    choices = ChoiceListSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'poll', 'question_text', 'question_type', 'choices']
        read_only_fields = ['id']


class AnswerSerializer(serializers.ModelSerializer):
    """ Ответ пользовотеля """

    class Meta:
        model = Answer
        fields = ['id', 'user_id', 'poll', 'question', 'choice', 'answer_val']
        read_only_fields = ['id', 'user_id']

    def create(self, validated_data):
        """
            Проверка на то, что должен быть создан один ответ для типа вопроса CHOICE и TEXT
        """

        question = Answer.objects.filter(user_id=validated_data.get('user_id'), question=validated_data.get('question'))
        if question.exists() and validated_data.get('user_id') and validated_data.get('question').question_type in [Question.CHOICE, Question.TEXT]:
            raise serializers.ValidationError('Ответ уже существует.')
        return Answer.objects.create(**validated_data)

    def save(self, user_id):
        """
            Проверка на то, чтобы не было одинакового ответа у авторизованного пользователя
        """

        self.validated_data['user_id'] = user_id
        if Answer.objects.filter(user_id=user_id, question=self.validated_data['question'], answer_val=self.validated_data['answer_val']).exists() and user_id:
            raise serializers.ValidationError('Такой ответ уже существует.')

        super().save()


class AnswerListUserSerializer(serializers.ModelSerializer):
    """ Список ответов пользователя """

    class Meta:
        model = Answer
        fields = ['id', 'user_id', 'poll', 'question', 'choice', 'answer_val']
        read_only_fields = ['id', 'user_id']


class QuestionSerializer(serializers.ModelSerializer):
    """ Список вопросов """

    choices = ChoiceListSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'poll', 'question_text', 'question_type', 'choices']
        read_only_fields = ['id']


class PollSerializer(serializers.ModelSerializer):
    """ Список опросов """
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'poll_title', 'start_date', 'end_date', 'poll_description', 'questions']
        read_only_fields = ['id']

    def create(self, validated_data):
        if validated_data['start_date'] > validated_data['end_date']:
            raise serializers.ValidationError("Дата старта опроса должна быть раньше даты окончания.")
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({'start_date': 'Данное поле нельзя изменить.'})
        if 'end_date' in validated_data and \
            validated_data['end_date'] < instance.start_date:
            raise serializers.ValidationError("Дата старта опроса должна быть раньше даты окончания.")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
