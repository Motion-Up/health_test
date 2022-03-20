# Generated by Django 4.0.2 on 2022-03-18 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Ответы',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='AnswerTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Ответ - Тест',
                'verbose_name_plural': 'Ответ - Тест',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя параметра')),
                ('name_for_formula', models.CharField(max_length=200, verbose_name='Имя для формулы')),
                ('field_type', models.CharField(choices=[('int', 'Число'), ('bool', 'Выбор'), ('choice', 'Шкала')], max_length=10)),
            ],
            options={
                'verbose_name': 'Параметры',
                'verbose_name_plural': 'Параметры',
            },
        ),
        migrations.CreateModel(
            name='ParameterTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.parameter', verbose_name='Параметер')),
            ],
            options={
                'verbose_name': 'Параметр - Тест',
                'verbose_name_plural': 'Параметр - Тест',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название теста')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание теста')),
                ('formula', models.CharField(max_length=400, verbose_name='Формула')),
                ('image', models.ImageField(blank=True, upload_to='tests/', verbose_name='Картинка')),
                ('is_active', models.BooleanField(default=False, verbose_name='Статус готовности')),
                ('achievements', models.ManyToManyField(through='tests.ParameterTest', to='tests.Parameter', verbose_name='Все параметры')),
                ('answers', models.ManyToManyField(related_name='choice_answer', through='tests.AnswerTest', to='tests.Answer', verbose_name='Все ответы')),
            ],
            options={
                'verbose_name': 'Тесты',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test', verbose_name='Тест')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='parametertest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test', verbose_name='Тест'),
        ),
        migrations.AddConstraint(
            model_name='parameter',
            constraint=models.UniqueConstraint(fields=('name', 'name_for_formula', 'field_type'), name='unique_parameter'),
        ),
        migrations.AddField(
            model_name='answertest',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.answer', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='answertest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test', verbose_name='Тест'),
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_test', to='tests.test', verbose_name='Тест'),
        ),
        migrations.AddConstraint(
            model_name='parametertest',
            constraint=models.UniqueConstraint(fields=('test', 'parameter'), name='unique_parameter_test'),
        ),
        migrations.AddConstraint(
            model_name='answertest',
            constraint=models.UniqueConstraint(fields=('test', 'answer'), name='unique_answer_test'),
        ),
        migrations.AddConstraint(
            model_name='answer',
            constraint=models.UniqueConstraint(fields=('test', 'answer'), name='unique_answer'),
        ),
    ]
