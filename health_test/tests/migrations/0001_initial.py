# Generated by Django 4.0.2 on 2022-02-16 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Параметр')),
                ('name_for_formula', models.CharField(max_length=200, verbose_name='Имя для формулы')),
                ('field_type', models.CharField(choices=[('int', 'Число'), ('bool', 'Выбор'), ('choice', 'Шкала')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ParameterTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Тест')),
                ('formula', models.CharField(max_length=400, verbose_name='Формула')),
                ('achievements', models.ManyToManyField(through='tests.ParameterTest', to='tests.Parameter')),
            ],
        ),
        migrations.AddField(
            model_name='parametertest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.test'),
        ),
        migrations.AddConstraint(
            model_name='parametertest',
            constraint=models.UniqueConstraint(fields=('test', 'parameter'), name='unique_parameter'),
        ),
    ]
