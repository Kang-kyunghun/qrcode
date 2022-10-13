import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from users.models import User

class QRCodeView(View):
    def get(self, request):
        qr_code_url = {"url" : "https://jack-file-storage.s3.ap-northeast-2.amazonaws.com/qrcode/71cb3949-5b68-4ad5-8b73-cb70334fcb1c"}
        return render(request, 'qrcode/index.html', qr_code_url)


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        print(email)

        if not User.objects.filter(email=data['email']).exists():
            return JsonResponse({'messasge': 'Invalid User'}, status=401)
        
        user = User.objects.get(email=data['email'])
        result = {
            'name' : user.name,
            'email' : user.email
        }
        return JsonResponse({'messasge': result}, status=200)