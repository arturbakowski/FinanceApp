from django.db import models


class IncomeType(models.Model):
    type_name = models.TextField(default='')

    def __str__(self):
        return self.type_name


class ExpenseType(models.Model):
    type_name = models.TextField(default='')

    def __str__(self):
        return self.type_name


class SavingType(models.Model):
    type_name = models.TextField(default='')

    def __str__(self):
        return self.type_name


class Month(models.Model):
    month_name = models.TextField(default='')

    def __str__(self):
        return self.month_name


class Income(models.Model):
    income_name = models.TextField(default='')
    amount = models.TextField(default='')
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    income_month = models.ForeignKey(Month, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.income_name


class Expense(models.Model):
    expense_name = models.TextField(default='')
    amount = models.TextField(default='')
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.expense_name


class Saving(models.Model):
    saving_name = models.TextField(default='')
    amount = models.TextField(default='')
    saving_type = models.ForeignKey(SavingType, on_delete=models.CASCADE)

    def __str__(self):
        return self.saving_name

