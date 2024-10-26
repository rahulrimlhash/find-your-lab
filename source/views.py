from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# allauth decorator @verified_email_required
from allauth.account.decorators import verified_email_required
from allauth.account.views import SignupView, LoginView, PasswordResetView

from tests.models import Test, TestCategory

@login_required()
def home(request):
    all_tests = Test.objects.all()
    all_category = TestCategory.objects.all().order_by('-id')

    query = request.GET.get('q')

    if query:
        all_tests = all_tests.filter(Q(test_name__icontains=query)).distinct()

    paginator = Paginator(all_tests, 12)
    page = request.GET.get('page')
    all_tests_paginator_data = paginator.get_page(page)

    template = 'home.html'

    context = {
        'all_tests': all_tests,
        'all_tests_paginator_data': all_tests_paginator_data,
        'all_category': all_category,
    }

    return render(request, template, context)

########################################################################################


class DevelopersView(TemplateView):
    template_name = 'developers.html'



