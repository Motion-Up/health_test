from modeltranslation.translator import (
    TranslationOptions, translator)

from .models import (
    Test, Parameter, Answer
)


class TestTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = ('ru', 'en')


class ParameterTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('ru', 'en')


class AnswerTranslationOptions(TranslationOptions):
    fields = ('answer',)
    required_languages = ('ru', 'en')


translator.register(Test, TestTranslationOptions)
translator.register(Parameter, ParameterTranslationOptions)
translator.register(Answer, AnswerTranslationOptions)
