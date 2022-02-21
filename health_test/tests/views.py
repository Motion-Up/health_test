from dataclasses import replace
from django.shortcuts import render, get_object_or_404

from .forms import TestForm
from .models import Test


def index(request):
    tests = Test.objects.all()
    context = {
        'tests': tests
    }
    return render(request, 'tests/index.html', context=context)


def test(request):
    test = get_object_or_404(Test, id=1)
    achievements = test.achievements.all()
    data = {form.name: form for form in achievements}
    form = TestForm(request.POST or None, initial=data or None)
    formula = test.formula

    if request.method == 'POST':
        form = TestForm(request.POST, initial=data)

        if form.is_valid():
            for achieve in achievements:
                data = request.POST.get(f'{achieve.name}')
                formula = formula.replace(f'{achieve.name_for_formula}', data)
            print(eval(formula))
            return render(request, 'tests/test_detail.html')

    context = {
        'form': form
    }
    return render(request, 'tests/test_detail.html', context=context)
