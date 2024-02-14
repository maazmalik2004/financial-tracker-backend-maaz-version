# maazserver/views.py
from django.http import JsonResponse
from django.views import View

class YourModelListView(View):
    def get(self, request, *args, **kwargs):
        data = {
  "income": 10,
  "expense": 20,
  "balance": -10,
  "graphImageUrl": "default-graph-url.jpg"
}

        return JsonResponse(data)
