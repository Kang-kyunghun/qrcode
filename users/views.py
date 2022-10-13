import json
from xml.dom.minidom import NamedNodeMap

from django.http import JsonResponse
from django.views import View

from users.models import User


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