from django.urls import path
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('dash/', views.dashboard, name="dash"),
    path('ind/',views.index,name="index"),
    url(r'^chart/$', views.HomeView.as_view(), name='home'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
    path('', views.PostList.as_view(), name='post'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
