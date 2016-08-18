from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import ScrapeForm
from .models import *
import itertools

def get_marks(request):
    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScrapeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            hallticket = form.cleaned_data['hall_ticket_no']
            print 'Hallticket ' + hallticket +' received'
            sub_name,internal_marks,external_marks,total_marks,result,name,percentage = Scrape().marks(hallticket)
            return render(request, 'output.html', {'data': zip(sub_name,internal_marks,external_marks,total_marks,result),'name':name, 'percentage':percentage })

    # if a GET (or any other method) we'll create a blank form
    else:
    	form = ScrapeForm()

    return render(request, 'input.html', {'form': form})
