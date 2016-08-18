from django import forms

class ScrapeForm(forms.Form):
    hall_ticket_no = forms.CharField(label='Enter hallticket no', max_length=10)

