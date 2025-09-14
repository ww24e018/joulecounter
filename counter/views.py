# counter/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .models import FoodItemTemplate, FoodItemLog
from .forms import FoodItemTemplateForm, FoodLogForm

@login_required
def overview(request):
    return render(request, 'counter/overview.html')

@login_required
def add_template(request):
    if request.method == 'POST':
        form = FoodItemTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('overview')
    else:
        form = FoodItemTemplateForm()
    return render(request, 'counter/add_template.html', {'form': form})

@login_required
def log_item(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            FoodItemLog.objects.create(template=form.cleaned_data['template'])
            return redirect('overview')
    else:
        form = FoodLogForm()
    return render(request, 'counter/log_item.html', {'form': form})

@login_required
def daily_summary(request, days_back=0):
    date = timezone.now().date() - timedelta(days=days_back)
    logs = FoodItemLog.objects.filter(
        eaten_at__date=date
    ).select_related('template')
    total = logs.aggregate(total=Sum('template__joules'))['total'] or 0
    return render(request, 'counter/daily_summary.html', {
        'date': date,
        'total': total,
        'logs': logs,
        'days_back': days_back
    })
