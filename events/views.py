from django.shortcuts import redirect, render, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect, response
from .models import Event, Venue, Student
from .forms import VenueForm, EventForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

# Create your views here.
def register_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        college = request.POST['college']
        semester = request.POST['semester']
        gender = request.POST['gender']
        event = request.POST['event']
        student = Student(name=name,age=age,email=email,phone=phone,college=college,semester=semester,gender=gender,event=event)
        student.save()
        return redirect('')
    else:
        return render(request,'events/register_event.html',{
            "event" : event
        })

def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = venues.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')
    response.writelines(lines)
    return response


def delete_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('venues')

def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('event_list')

def update_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None ,instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request,'events/update_event.html',{
        "event" : event,
        "form"  : form,
    })


def add_event(request):
    submitted = False
    if(request.method == 'POST'):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'events/add_event.html',{
        "form" : form,
        "submitted" : submitted,
    })

def update_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None ,instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venues')
    return render(request,'events/update_venue.html',{
        "venue" : venue,
        "form"  : form,
    })

def search_venue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request,'events/search_venue.html',{
            'searched' : searched,
            "venues" : venues
            })
    else:
        return render(request,'events/search_venue.html',{})

def show_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request,'events/show_venue.html',{
        "venue" : venue
    })

def venues(request):
    venue_list = Venue.objects.all().order_by('name')
    return render(request,'events/venue.html',{
        "venue_list" : venue_list
    })


def add_venue(request):
    submitted = False
    if(request.method == 'POST'):
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'events/add_venue.html',{
        "form" : form,
        "submitted" : submitted,
    })

def all_events(request):
    event_list = Event.objects.all().order_by('name')
    return render(request,'events/events_list.html',{
        "event_list" : event_list
    })

def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):

    #convert month to uppercase
    month = month.capitalize()

    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calendar
    cal = HTMLCalendar().formatmonth(theyear=year,themonth=month_number)

    #get current year
    now = datetime.now()
    current_year = now.year

    #get current time
    time = now.strftime('%I:%M %p')

    return render(request,'events/home.html',{
        "year" : year,
        "month": month,
        "month_number" : month_number,
        "cal" : cal,
        "current_year" : current_year,
        "time" : time,
    })