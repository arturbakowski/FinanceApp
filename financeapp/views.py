from django.shortcuts import render, redirect
from financeapp.models import *
from .forms import *
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect


from django.http import HttpResponse


def home(request):
    return render(request, 'financeapp/home.html')

""" WYKORZYSTANIE FORMULARZY Z .FORMS
def add_income(request):
    form = IncomeForm()
    form.save(commit=True)
    return redirect('incomes')
"""

'''

def incomes(request):
    if request.method == 'POST':
        new_income_text = request.POST['income_text']
        new_amount = request.POST['income_amount']
        Income.objects.create(income_name=new_income_text, amount=new_amount)
    else:
        new_income_text = ''
        new_amount = ''

    return render(request, 'financeapp/incomes.html', {
        'new_income_text': new_income_text, 'new_amount': new_amount
    })


def expenses(request):
    return render(request, 'financeapp/expenses.html')


def analysis(request):
    return render(request, 'financeapp/analysis.html')


def savings(request):
    return render(request, 'financeapp/savings.html')

'''


class Incomes(generic.ListView):
    template_name = 'financeapp/incomes.html'
    context_object_name = 'lista_przychodow'
    model = Income

    def get_queryset(self):
        return Income.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Incomes, self).get_context_data(**kwargs)
        context['incometype'] = IncomeType.objects.all()
        context['months'] = Month.objects.all()
        # And so on for more models
        return context


class Expenses(generic.ListView):
    template_name = 'financeapp/expenses.html'

    def get_queryset(self):
        return Expense.objects.all()


class Savings(generic.ListView):
    template_name = 'financeapp/savings.html'

    def get_queryset(self):
        return Saving.objects.all()


def analysis(request):
    return render(request, 'financeapp/analysis.html')


def add_income(request):
    if request.method == 'POST':
        new_income_text = request.POST['income_text_template']
        new_amount = request.POST['income_amount_template']
        income_type = request.POST['income_type_template']
        month = request.POST['income_month_template']
        Income.objects.create(income_name=new_income_text, amount=new_amount, income_type_id=income_type,
        income_month_id=month)
    else:
        new_income_text = ''
        new_amount = ''
        income_type = ''
        month = ''

    return HttpResponseRedirect(reverse('financeapp:incomes'))

 #   return render(request, 'financeapp/incomes.html', {
 #       'new_income_text': new_income_text, 'new_amount': new_amount
 #   })
