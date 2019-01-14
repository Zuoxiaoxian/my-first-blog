from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('blog.urls')), # 将  'http://127.0.0.1:8000/' 请求转到blog.urls， 并看看那里面有没有进一步的指示
    url(r'^admin/', include(admin.site.urls)),
]
