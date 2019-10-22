from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginApiView, UserProfileViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet)
# router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginApiView.as_view()),
    # path('hello-api/', HelloViewSet.as_view()),

]
