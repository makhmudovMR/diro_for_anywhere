from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from smart_selects.db_fields import ChainedForeignKey
from ckeditor.fields import RichTextField


class Test(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')
    is_activate = models.BooleanField(default=False, verbose_name='Активный?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):

    test = models.ForeignKey('Test', on_delete=models.CASCADE, verbose_name='Тест')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    question = RichTextUploadingField(blank=True, null=True, verbose_name='Вопрос')
    trueAnswer = models.ForeignKey('Answer',  related_name='+', null=True, blank=True, verbose_name='Верный ответ')

    '''
    trueAnswer = ChainedForeignKey('Answer',
                                   chained_field='test',
                                   chained_model_field="test",
                                   show_all=False,
                                   auto_choose=True,
                                   sort=True,
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)
    '''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    PA = 'PA'
    SA = 'SA'
    TYPE_OF_ANSWERS = [
        (PA, 'Вариант ответа'),
        (SA, 'Ответ вводимый через текстовое поле')
    ]

    test = models.ForeignKey('Test', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Тест')
    question = ChainedForeignKey('Question',
                                 chained_field='test',
                                 chained_model_field="test",
                                 show_all=False,
                                 auto_choose=True,
                                 sort=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Вопрос')
    # question = models.ForeignKey('Question', on_delete=models.CASCADE)
    type_of_answer = models.CharField(choices=TYPE_OF_ANSWERS, default=PA, max_length=50)
    answer = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ответ')


    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Person(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фамилия')
    email = models.EmailField(max_length=150, blank=True, null=True, verbose_name='Электронная почта')

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class PersonAnswer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Пользователь')
    # answer = models.CharField(max_length=255, blank=True, null=True)
    answer = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ответ пользователя')

    def __str__(self):
        return "{0}, {1}, {2}".format(self.question.title, str(self.person), self.answer)

    class Meta:
        verbose_name = 'Ответы пользователя'
        verbose_name_plural = 'Ответы пользователей'


"""
functions
"""


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Person.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)