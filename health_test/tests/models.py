from django.db import models


FIELD_TYPE = [
    ('int', 'Число'),
    ('bool', 'Выбор'),
    ('choice', 'Шкала')
]


class Test(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название теста'
    )
    description = models.TextField(
        verbose_name='Описание теста',
        default=f'{title}'
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
    #answer = models.ForeignKey(
    #    'Answer',
    #    null=False,
    #    on_delete=models.CASCADE,
    #    related_name='answer',
    #    verbose_name='Ответ'
    #)

    def __str__(self) -> str:
        return self.title


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


class ParameterTest(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест'
    )
    parameter = models.ForeignKey(
        Parameter,
        on_delete=models.CASCADE,
        verbose_name='Параметер'
    )

    def __str__(self) -> str:
        return f'{self.test} {self.parameter}'

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['test', 'parameter'],
            name='unique_parameter'
        )
        ]
