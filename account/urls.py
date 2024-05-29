from django.urls import path
from .views import GetPeople, GetPerson

urlpatterns = [
    path('get_people/', GetPeople.as_view()),
    path('get_person/<int:id>/', GetPerson.as_view())
]