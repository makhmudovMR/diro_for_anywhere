from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from . import models
from .forms import SignInForm, SignUpForm

import re


"""
service functions
"""


"""
view functions
"""


def hello_view(requets):
    return HttpResponse('Hi')


def main_view(requset):
    return render(requset, 'main/main.html', {})


def sign_in_view(request):
    form = SignInForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return redirect(reverse('main:test'))

    context = {
        'form': form,
    }
    return render(request, 'main/sign_in.html', context)


def sign_up_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        new_user.username = username
        new_user.set_password(password)
        new_user.email = email
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        person = models.Person.objects.get(user=new_user)
        person.first_name = first_name
        person.last_name = last_name
        person.email = email
        person.save()

        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
        return redirect(reverse('main:test'))
    context = {
        'form': form,
    }
    return render(request, 'main/sign_up.html', context)


@login_required
def test_view(request):
    '''
    Задание: Заблокировать пройденные пользователём тесты
    '''
    all_test = models.Test.objects.filter(is_activate=True)
    person = models.Person.objects.get(user=request.user)
    person_answers = models.PersonAnswer.objects.filter(person=person)

    # print(all_test)

    done_test = set()
    for item in person_answers:
        if item.question.test in all_test:
            done_test.add(item.question.test)

    context = {
        'tests': all_test,
        'done_test': done_test
    }
    return render(request, 'main/tests.html', context)


@login_required
def question_view(request, id):
    test = models.Test.objects.get(id=id)
    questions = models.Question.objects.filter(test=test)
    answers = models.Answer.objects.filter(question__in=questions)
    print(answers)
    context = {
        'id': id,
        'questions': questions,
        'answers': answers
    }
    return render(request, 'main/question.html', context)


@login_required
def user_panel_view(request):
    person = models.Person.objects.get(user=request.user)
    tests = models.Test.objects.all()
    questions = models.Question.objects.filter(test__in=tests)
    # person_answer = models.PersonAnswer.objects.filter(question__in=questions, person=person)
    person_answers = models.PersonAnswer.objects.filter(person=person)

    # print(all_test)

    done_test = set()
    for item in person_answers:
        if item.question.test in tests:
            done_test.add(item.question.test)

    context = {
        "person": person,
        "person_answer": person_answers,
        "tests": done_test,
    }

    return render(request, 'main/user_panel.html', context)


@login_required
def test_result_view(request, id):
    test = models.Test.objects.get(id=id)
    person = models.Person.objects.get(user=request.user)
    questions = models.Question.objects.filter(test=test)
    person_answers = models.PersonAnswer.objects.filter(question__in=questions, person=person)
    context = {
        'test': test,
        'person_answers': person_answers,
    }
    return render(request, 'main/test_result.html', context)


@login_required
def all_users_view(request):
    persons = models.Person.objects.all()
    # print(persons)
    context = {'all_users': persons}
    return render(request, 'main/all_users.html', context)


@login_required
def users_tests_view(request, id):
    person = models.Person.objects.get(id=id)
    all_ = models.PersonAnswer.objects.filter(person=person)
    set_ = set()
    for item in all_:
        set_.add(item.question.test)
    context = {
        'all_test': set_,
    }
    return render(request, 'main/user_tests.html', context)


@login_required
def user_test_result_view(request, id):
    test = models.Test.objects.get(id=id)
    person = models.Person.objects.get(user=request.user)
    questions = models.Question.objects.filter(test=test)
    person_answers = models.PersonAnswer.objects.filter(question__in=questions, person=person)
    context = {
        'test': test,
        'person_answers': person_answers,
    }
    return render(request, 'main/user_test_result.html', context)


"""
    handlers
"""


def handle_test(request):
    adict = dict(request.POST)
    print(adict)
    for key in adict:
        if re.match(r"^\d+$", key) != None:
            # print(key)
            id_question = int(key)
            question = models.Question.objects.get(id=id_question)
            person_guess = adict[key][0]
            person = models.Person.objects.get(user=request.user)
            models.PersonAnswer(question=question, answer=person_guess, person=person).save()

    return redirect(reverse('main:user_panel'))


def logout_from_system(request):
    logout(request)
    return redirect(reverse('main:main'))

