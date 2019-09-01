from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('up/',views.uploader,name='uploader'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('api/chart/data/', views.ChartData.as_view(),name="chart"),
    path('cha/', views.HomeView.as_view(), name='home'),
    path('api/data/', views.get_data, name='api-data'),
    path('dash/',views.dashboard,name="dash")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)