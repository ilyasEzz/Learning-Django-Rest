from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


# class HelloApiView(APIView):
#     """ Test APIView """

#     serializer_class = HelloSerializer

#     def get(self, request, format=None):
#         """Returns a list of APIView Features"""

#         an_apiview = [
#             'Uses HTTP methods as function',
#             'Is similar to a tradditional django view',
#             'is mapped manually to URLS'
#         ]

#         context = {
#             'message': 'Hello Universe',
#             'an_apiview': an_apiview
#         }

#         return Response(context)

#     def post(self, request):
#         """ Create a hello message with our name """

#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#     def put(self, request, pk=None):
#         """ Update an object """
#         return Response({'method': 'PUT'})

#     def patch(self, request, pk=None):
#         """ Update partially an object """
#         return Response({'method': 'PATCH'})

#     def delete(self, request, pk=None):
#         """ Delete an object """
#         return Response({'method': 'DELETE'})


# class HelloViewSet(ViewSet):
#     """ Test Api View Set """

#     serializer_class = HelloSerializer

#     def list(self, request):
#         api_viewset = [
#             'Uses actions (list, create, retrieve, update, partial_update)',
#             'Automaticly maps to URLS, USING Routers',
#             'add more functionnality for less code'
#         ]

#         context = {
#             'message': 'Hello Universe',
#             'api_viewset': api_viewset
#         }

#         return Response(context)

#     def create(self, request):
#         """ Create a new hello message """
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#     def retrieve(self, request, pk=None):
#         """ Getting an object by his primary key """
#         return Response({'http_method': 'GET'})

#     def update(self, request, pk=None):
#         """ Updating an object by his primary key """
#         return Response({'http_method': 'PUT'})

#     def partial_update(self, request, pk=None):
#         """ Upddating partially an object by his primary key """
#         return Response({'http_method': 'POST'})

#     def destroy(self, request, pk=None):
#         """ Removing an object by his primary key """
#         return Response({'http_method': 'DELETE'})


class UserProfileViewSet(ModelViewSet):
    """ Creating and  updating profiles """

    queryset = UserProfile.objects.all()

    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfile,)
