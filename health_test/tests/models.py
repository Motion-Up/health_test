from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


FIELD_TYPE = [
    ('int', 'Число'),
    ('bool', 'Выбор'),
    ('choice', 'Шкала')
]


User = get_user_model()


class Test(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название теста'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )
    description = models.TextField(
        verbose_name='Описание теста',
    )
    achievements = models.ManyToManyField(
        'Parameter',
        through='ParameterTest',
        verbose_name='Все параметры'
    )
    formula = models.CharField(
        max_length=400,
        verbose_name='Формула'
    )
    answers = models.ManyToManyField(
        'Answer',
        verbose_name='Все ответы',
        through='AnswerTest',
        related_name='choice_answer'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='tests/',
        blank=True,
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Статус готовности'
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('test', kwargs={'test_slug': self.slug})

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'


class Parameter(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Имя параметра'
    )
    name_for_formula = models.CharField(
        max_length=200,
        verbose_name='Имя для формулы'
    )
    field_type = models.CharField(
        max_length=10,
        choices=FIELD_TYPE
    )

    def __str__(self) -> str:
        return f'{self.name} - {self.name_for_formula}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['name', 'name_for_formula', 'field_type'],
            name='unique_parameter'
        )
        ]
        verbose_name = 'Параметры'
        verbose_name_plural = 'Параметры'


class Answer(models.Model):
    answer = models.TextField(
        verbose_name='Ответ',
    )

    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест',
        related_name='choice_test',
    )

    def __str__(self) -> str:
        return f'{self.answer}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['test', 'answer'],
            name='unique_answer'
        )
        ]
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'


class ParameterTest(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест',
    )
    parameter = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        verbose_name='Параметер',
    )

    def __str__(self) -> str:
        return f'{self.test} {self.parameter}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['test', 'parameter'],
            name='unique_parameter_test'
        )
        ]
        verbose_name = 'Параметр - Тест'
        verbose_name_plural = 'Параметр - Тест'


class AnswerTest(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест'
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        verbose_name='Ответ'
    )

    def __str__(self) -> str:
        return f'{self.test} {self.answer}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['test', 'answer'],
            name='unique_answer_test'
        )
        ]
        verbose_name = 'Ответ - Тест'
        verbose_name_plural = 'Ответ - Тест'


class UserResults(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    result = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ответы пользавателей'
        verbose_name_plural = 'Ответы пользавателей'
