from django.contrib import admin

from .models import Test, Parameter, ParameterTest


class TestAdmin(admin.ModelAdmin):
    def achievements_name(self, obj):
        achievements = ParameterTest.objects.filter(test=obj)
        return [achieve.parameter for achieve in achievements]
    list_display = ('pk', 'title', 'achievements_name', 'formula')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_type', 'name_for_formula')


class ParameterTestAdmin(admin.ModelAdmin):
    list_display = ('test', 'parameter',)


admin.site.register(Test, TestAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ParameterTest, ParameterTestAdmin)
