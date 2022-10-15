from django.urls import path, include

from ping.views import PingView

urlpatterns = [
    path('ping', PingView.as_view()),
    path('attendents', include('users.urls'))
]
