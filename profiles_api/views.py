from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function',
            'Is similar to a tradditional django view',
            'is mapped manually to URLS'
        ]

        context = {
            'message': 'Hello Universe',
            'an_apiview': an_apiview
        }

        return Response(context)
