from django.views     import View
from django.http      import JsonResponse

# health check
class HelloView(View):
    def get(self,request):
        return JsonResponse({"Hello": "Project A"}, status = 200)