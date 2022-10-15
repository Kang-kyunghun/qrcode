from django.urls import path

from users.views import UserView, QRCodeView, UserCodeView

urlpatterns = [
    path('', UserView.as_view()),
    path('/qrcode', QRCodeView.as_view()),
    path('/upload', UserCodeView.as_view())

]
