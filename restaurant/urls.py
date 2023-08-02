from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
