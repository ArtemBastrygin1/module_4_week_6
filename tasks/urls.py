from tasks.apps import TasksConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    TaskViewSet,
    TagViewSet,
    CommentViewSet,
    CategoryViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

app_name = TasksConfig.name

rooter = DefaultRouter()
rooter.register('tasks', TaskViewSet)
rooter.register('tags', TagViewSet)
rooter.register('comments', CommentViewSet)
rooter.register('categories', CategoryViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + rooter.urls




