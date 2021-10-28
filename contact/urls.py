from django.urls import path

from contact.views import contact, contact_list

urlpatterns = [
    path('', contact),
    path('list/', contact_list)
    ]