from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from tests.models import UserResults, Test
import json


@login_required
def profile(request):
    user_results = UserResults.objects.filter(user=request.user)
    data = [float(result.result) for result in user_results]
    unique = user_results.values('test_id').distinct()
    tests = [Test.objects.get(id=test['test_id']) for test in unique]
    context = {
        'mail': 'ignatdan',
        'data': data,
        'tests': tests
    }
    return render(request, 'account/profile.html', context=context)


@login_required
def get_results(request, test_slug):
    test = get_object_or_404(Test, slug=test_slug)
    user_results = UserResults.objects.filter(user=request.user).filter(
        test=test.id
    )
    results = [float(result.result) for result in user_results]
    if len(results) == 0:
        return redirect('account:profile')
    minimum = int(min(results))
    maximum = int(max(results)) + 1
    # Это нужно для корректно отправки данных для javascript
    results = json.dumps(results)
    day = [result.date.strftime("%Y-%m-%d") for result in user_results]
    context = {
        'mail': 'ignatdan',
        'results': results,
        'min': minimum,
        'max': maximum,
        'test': test,
        'day': day,
        'user_results': user_results
    }
    return render(request, 'account/test_results.html', context=context)


@login_required
def delete_result(request, test_slug, result_id):
    user_result = get_object_or_404(UserResults, id=result_id)
    user_result.delete()
    return redirect('account:get_results', test_slug=test_slug)


@login_required
def edit_result(request, test_slug, result_id):
    user_result = get_object_or_404(UserResults, id=result_id)
    new_result = request.POST.get('result')
    if not new_result:
        return redirect('account:get_results', test_slug=test_slug)
    user_result.result = request.POST['result']
    user_result.save()
    return redirect('account:get_results', test_slug=test_slug)
