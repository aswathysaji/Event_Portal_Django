from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('<int:year>/<str:month>/',views.home,name="home"),
    path('events',views.all_events,name="event_list"),
    path('add_venue',views.add_venue,name="add-venue"),
    path('venues',views.venues,name="venues"),
    path('show_venue/<venue_id>',views.show_venue,name="show-venue"),
    path('search_venue',views.search_venue,name="search-venue"),
    path('update_venue/<venue_id>',views.update_venue,name="update-venue"),
    path('add_event',views.add_event,name="add-event"),
    path('update_event/<event_id>',views.update_event,name="update-event"),
    path('register_event/<event_id>',views.register_event,name="register-event"),
    path('delete_event/<event_id>',views.delete_event,name="delete-event"),
    path('delete_venue/<venue_id>',views.delete_venue,name="delete-venue"),
    path('venue_text',views.venue_text,name="venue-text"),
]