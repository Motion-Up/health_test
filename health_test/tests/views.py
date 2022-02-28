from django.shortcuts import render, get_object_or_404

from .forms import TestForm
from .models import Test


def index(request):
    tests = Test.objects.all().filter(is_active=True)
    context = {
        'tests': tests
    }
    return render(request, 'tests/index.html', context=context)


def test_detail(request, test_slug):
    test = get_object_or_404(Test, slug=test_slug)
    achievements = test.achievements.all()
    data = {form.name: form for form in achievements}
    form = TestForm(request.POST or None, initial=data or None)
    formula = test.formula

    if request.method == 'POST':
        form = TestForm(request.POST, initial=data)

        # Получаем ответ и пока его никуда не передаем
        if form.is_valid():
            for achieve in achievements:
                data = request.POST.get(f'{achieve.name}')
                formula = formula.replace(f'{achieve.name_for_formula}', data)
            result = float("{0:.2f}".format(eval(formula)))
            context = {
                'result': result,
                'test': test
            }
            return render(request, 'tests/test_detail.html', context=context)

    context = {
        'form': form,
        'test': test
    }
    return render(request, 'tests/test_detail.html', context=context)
