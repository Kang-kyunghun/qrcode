from django.urls import path

from users.views import UserView, QRCodeView

urlpatterns = [
    path('', UserView.as_view()),
    path('/qrcode', QRCodeView.as_view()),

]
