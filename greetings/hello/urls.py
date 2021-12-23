from django.urls import path
from hello.views import hello, goodbye

urlpatterns = [
    #app named hello
    path('', hello, name='hello'),
    #adding dynamic capability by accepting a string
    path('<str:name>', hello, name='hello_soandso'),
    path('goodbye/<str:name>', goodbye, name='name')
]