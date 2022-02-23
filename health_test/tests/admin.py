import re

from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import Test, Parameter, ParameterTest, AnswerTest, Answer


class TestAdmin(admin.ModelAdmin):
    def achievements_name(self, obj):
        achievements = ParameterTest.objects.filter(test=obj)
        return [achieve.parameter for achieve in achievements]

    def answer_name(self, obj):
        answer_name = AnswerTest.objects.filter(test=obj)
        return [answer.answer for answer in answer_name]

    def save_model(self, request, obj, form, change):
        '''Сделаем проверку теста на правильность заполнения формулы
        и в случае успеха статус меняем на is_active'''
        test = obj
        if test.id is not None:
            formula = test.formula
            if test.achievements:
                for achieve in test.achievements.all():
                    formula = formula.replace(f'{achieve.name_for_formula}', '')
            if len(re.findall(r'[а-яА-Яa-zA-Z]', formula)) != 0:
                test.is_active = False
                test.save()
                return super().save_model(request, obj, form, change)
            test.is_active = True
            test.save()
            return super().save_model(request, obj, form, change)
        obj.save()

    list_display = ('pk', 'title', 'achievements_name', 'formula', 'answer_name', 'is_active')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_type', 'name_for_formula',)


class ParameterTestAdmin(admin.ModelAdmin):
    list_display = ('test', 'parameter',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer',)


class AnswerTestAdmin(admin.ModelAdmin):
    list_display = ('test', 'answer',)


admin.site.register(Test, TestAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ParameterTest, ParameterTestAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(AnswerTest, AnswerTestAdmin)
