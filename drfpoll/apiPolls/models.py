from django.db import models


class Poll(models.Model):
    """ Опрос """

    poll_title = models.CharField("Название", max_length=100)
    start_date = models.DateTimeField("Дата старта")
    end_date = models.DateTimeField("Дата окончания")
    poll_description = models.TextField("Описание", max_length=200)

    def __str__(self):
        return self.poll_title

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

class Question(models.Model):
    """ Вопрос """

    TEXT = 'text'
    CHOICE = 'choice'
    MULTICHOICE = 'multichoice'

    TYPE = [
        (TEXT, 'Ответ текстом'),
        (CHOICE, 'Один вариант'),
        (MULTICHOICE, 'Несколько вариантов'),
    ]

    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE, verbose_name="Опрос")
    question_text = models.CharField("Вопрос", max_length=200)
    question_type = models.CharField("Тип вопроса", max_length=11, choices=TYPE, default=TEXT)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Choice(models.Model):
    """ Вариант ответа """

    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, verbose_name="Вопрос")
    choice_text = models.CharField("Вариант ответа", max_length=200, )

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"


class Answer(models.Model):
    """ Ответ пользователя"""

    user_id = models.IntegerField("id пользователя", null=True)
    poll = models.ForeignKey(Poll, related_name='answers', on_delete=models.CASCADE, verbose_name="Опрос")
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, verbose_name="Вопрос")
    choice = models.ForeignKey(Choice, related_name='answers', on_delete=models.CASCADE, null=True, verbose_name="Вариант ответа")
    answer_val = models.CharField("Ответ", max_length=200, null=True)

    def __str__(self):
        return self.answer_val

    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователей"
