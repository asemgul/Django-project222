from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from .models import Flightofusers, Comment
#import datetime


#homepage
def index(request):
    return render(request, 'pages/home.html')


#info-center page
def info(request):
    return render(request, 'pages/info.html')


#pagination
def pagination(request):
    return True


#search
def search(request):
    context = {'res': None}
    try:
        search_text = request.POST['search_text']
        print(search_text)
        res = []
        flights = Flight.objects.all()
        for flight in flights:
            if search_text.find(flight.from_city.city_name) >= 0 or search_text.find(flight.to_city.city_name) >= 0:
                res.append(flight)
        context['res'] = res
        print(res)
    except:
        pass
    return render(request, 'pages/search.html', context)


#passengers page
def passenger(request):
    return render(request, 'pages/forpassengers.html')


#info about avia tours
def avia_tour(request):
    return render(request, 'pages/avia.html')


#info fro arrived
def arrived(request):
    return render(request, 'pages/arr.html')


#info for departured
def for_departure(request):
    return render(request, 'pages/dep.html')


#schedule and booking
def departure(request):
    city_name = 'Алматы'
    city = City.objects.get(city_name=city_name)
    flights = Flight.objects.filter(from_city=city)
    flights_are_departured = areDepartured(flights)
    combined_list = zip(flights, flights_are_departured)
    context = {'combined_list': combined_list}
    return render(request, "pages/vylety.html", context)


def arrival(request):
    city_name = 'Алматы'
    city = City.objects.get(city_name=city_name)
    flights = Flight.objects.filter(to_city=city)
    flights_are_arrived = areArrived(flights)
    combined_list = zip(flights, flights_are_arrived)
    context={'combined_list': combined_list}
    return render(request, "pages/prilet.html", context)


def book(request):
    return render(request, 'pages/booking.html')


#home
def almaty(request):
    return render(request, 'pages/home.html')


#home button
def help(request):
    return render(request, 'pages/info.html')


#contacts page
def contact(request):
    return render(request, 'pages/contact.html')


#show search results
def show_flights(request):
    context={'from_city': None, 'to_city': None, 'departure_date': None, 'flights': None, 'travel_type': None, 'number_of_people': None} # travel_type stands for econom or business
    try:
        from_city = City.objects.get(city_name=request.POST['from_city'])
        to_city = City.objects.get(city_name=request.POST['to_city'])
        departure_date = request.POST['departure_date']
        day = Day.objects.get(day_of_month=get_day_from(departure_date))
        travel_type = request.POST['econom_or_business']
        number_of_people = int(request.POST['number_of_adults']) + int(request.POST['number_of_children'])
        flights = Flight.objects.filter(from_city=from_city, to_city=to_city, flight_days=day)
        if travel_type == 1:
            flights.filter(fligth_econom_places__gt=number_of_people)
        elif travel_type == 2:
            flights.filter(flight_business_places__gt=number_of_people)
        context['from_city'] = from_city
        context['to_city'] = to_city
        context['flights'] = flights
        context['departure_date'] = departure_date
        context['travel_type'] = travel_type
        context['number_of_people'] = number_of_people

    except:
        pass
    print(context)
    return render(request, 'pages/show_flights.html', context)


#booking flights
def book_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    try:
        number_of_people = int(request.POST['number_of_people'])
        travel_type = int(request.POST['travel_type'])
        if travel_type == 1:
            flight.fligth_econom_places -= number_of_people
        elif travel_type == 2:
            flight.flight_business_places -= number_of_people
        flight.save()
    except:
        pass
    return render(request, 'pages/home.html')


# flights
def areArrived(flights):
    current_time = datetime.datetime.now()
    current_time_in_minutes = current_time.hour * 60 + current_time.minute
    res = []
    for flight in flights:
        flight_end = flight.flight_end_time
        flight_end_in_mitutes = flight_end.hour * 60 + flight_end.minute
        res.append(current_time_in_minutes > flight_end_in_mitutes)
    return res


def areDepartured(flights):
    current_time = datetime.datetime.now()
    current_time_in_minutes = current_time.hour * 60 + current_time.minute
    res = []
    for flight in flights:
        flight_start = flight.fligth_start_time
        flight_start_in_mitutes = flight_start.hour * 60 + flight_start.minute
        res.append(current_time_in_minutes > flight_start_in_mitutes)
    return res


def get_day_from(date): # format is like yyyy-mm-dd
    day = int(date[8:])
    return day


#about us page
def onas(request):
    return render(request, 'pages/onas.html')


#register page
def registeruser(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            lastname = form.cleaned_data.get("last_name")
            otchestvo = form.cleaned_data.get('patronymic_name')
            telephone = form.cleaned_data.get('telephone')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/registeruser.html', {'form': form}) #pages?


#profile page
@login_required
def profile(request):
    user = request.user
    flights = Flightofusers.objects.filter(user=user)
    return render(request, 'pages/profile.html', locals())


def flight_detail(request, pk):
    flight = Flightofusers.objects.get(pk=pk)

    if request.method == "POST":
        text = request.POST.get('text')
        comment = Comment.objects.create(user=request.user, text=text, flight=flight)
        return redirect(flight.get_absolute_url())
    return render(request, 'pages/flight-detail.html', locals())


def register(request):
    return render(request, 'pages/register.html')


def register_success(request):
    return render(request, 'pages/register_success.html')


def invalid_login(request):
    return render(request, 'pages/invalid_login.html')


def homeuser(request):
    flights = Flightofusers.objects.all()
    n = Notification.objects.filter(user=request.user, viewed=False)
    return render(request, 'pages/homeuser.html', {'notification': n}, locals())


def notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    return render(request, 'pages/notification.html', {'notification': n})


def delete_not(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect('pages/homeuser.html')


def schedule(request):
    return render(request, 'pages/schedule.html')




"""def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/pages/logged_in')
    else:
        return HttpResponseRedirect('/pages/invalid')


def logged_in(request):
    return render_to_response('logged_in.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.login(request)
    return render_to_response('logout.html')"""