from django.contrib import admin

from .models import Test, Parameter, ParameterTest, AnswerTest, Answer


class TestAdmin(admin.ModelAdmin):
    def achievements_name(self, obj):
        achievements = ParameterTest.objects.filter(test=obj)
        return [achieve.parameter for achieve in achievements]

    def answer_name(self, obj):
        answer_name = AnswerTest.objects.filter(test=obj)
        return [answer.answer for answer in answer_name]
        
    list_display = ('pk', 'title', 'achievements_name', 'formula', 'answer_name',)
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
