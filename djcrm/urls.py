from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from leads.views import LandingpageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingpageView.as_view(), name='land'),
    path('leads/',include('leads.urls')),
    path('accounts/',include('accounts.urls')),
    # path('accounts/',include('django.contrib.auth.urls'),name='login'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)