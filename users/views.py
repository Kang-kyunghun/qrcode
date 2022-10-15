import json
import io
import csv
import qrcode


from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from users.models import Attendent
from utiles.s3 import s3_handler

class QRCodeView(View):
    def get(self, request):
        qrcode_uuid = request.GET['key']
        
        qr_code_url = {"url" : f"https://jack-file-storage.s3.ap-northeast-2.amazonaws.com/qrcode/{qrcode_uuid}"}
        return render(request, 'qrcode/index.html', qr_code_url)

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        print(email)

        if not Attendent.objects.filter(email=data['email']).exists():
            return JsonResponse({'messasge': 'Invalid User'}, status=401)
        
        user = Attendent.objects.get(email=data['email'])
        result = {
            'name' : user.name,
            'email' : user.email
        }
        return JsonResponse({'messasge': result}, status=200)

class UserCodeView(View):
    def post(self, request):
        attendents = Attendent.objects.all()

        for attendent in attendents:
            email = attendent.email
            
            qr_image = qrcode.make(email)
            buf      = io.BytesIO()
            qr_image.save(buf, format = 'png')
            buf.seek(0)

            image_url = s3_handler.upload_qr(buf)

            if not image_url:
                return JsonResponse({'messasge': 'error'}, status=400)

            attendent.storage_key = image_url
            attendent.save()
        return JsonResponse({'messasge': 'result'}, status=200) 