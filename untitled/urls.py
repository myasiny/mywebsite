from django.contrib import admin
from django.urls import path, include

from myblog.views import splash

urlpatterns = [
    path('', splash, name='splash'),
    path('blog/', include('myblog.urls')),
    path('admin/', admin.site.urls)
    # path('about/', include('aboutme.urls'))
]
