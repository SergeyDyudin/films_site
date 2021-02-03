from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Records


@login_required
def records_list(request):
    rec_list = Records.objects.all().order_by('-date')
    paginator = Paginator(rec_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'records/records_list.html', {'page_obj': page_obj})


@login_required
def record(request, record_id):
    record_data = get_object_or_404(Records, id=record_id)
    return render(request, 'records/record.html', {'record_data': record_data})
