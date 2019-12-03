from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'home'

urlpatterns = [
    #homepage
    url(r'^$', views.index, name='home'),

    #infopage
    url(r'^info/', views.info, name='info'),

    #forpassengers
    url(r'^forpassengers/', views.passenger, name='forpassengers'),

    #departure
    url(r'^vylety/', views.departure, name='vylety'),

    #arrival
    url(r'^prilet/', views.arrival, name='prilet'),

    #book
    url(r'^booking/', views.book, name='booking'),

    #almaty
    url(r'^home/', views.almaty, name='home'),

    #about us
    url(r'^onas/', views.onas, name='onas'),

    #user's registration page
    url(r'^register', views.register, name='register'),

    #cantacts of airport
    url(r'^contact', views.contact, name='contact'),

    #search
    url(r'^results/', views.search, name='search'),
    path("show_flights", views.show_flights, name="show_flights"),
    path("search_results", views.search, name="search_results"),

    #booking
    path("book_flight/<int:flight_id>", views.book_flight, name="book_flight"),

    #users stuff
    path('registeruser/', views.registeruser, name="register"),

    #path('about/', views.about, name='users-about'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('flight/<int:pk>/', views.flight_detail, name='flight-detail'),
]
