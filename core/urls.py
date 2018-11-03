from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from articles.views import ArticleViewSet
from charts.views import ChartViewSet, ProgressChartViewSet
from users.views import UserViewSet, UserCreateViewSet
from patients.views import PatientViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'charts', ChartViewSet)
router.register(r'progress_charts', ProgressChartViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Article 관련
    path('api/v1/', include("articles.urls")),

    # Profile 관련
    path('api/v1/', include("profiles.urls")),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
