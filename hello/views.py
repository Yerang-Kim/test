from django.views     import View
from django.http      import JsonResponse

# health check
class HelloView(View):
    def get(self,request):
        return JsonResponse({"Health": "Check"}, status = 200)