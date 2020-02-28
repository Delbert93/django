"""tictactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import welcome
"""r is a roll string. Basically if the url contains welcome
it will find the page. doesnt matter if its 
kjsdlsakdhswelcomekljalsdkhs or just welcome, either will work
if it does not have welcome somewhere in it it 
will not find that page. if you start with ^ it will match
any string starting with welcome and a $ will match with anything 
ending with welcome. starting with ^ and endding with $ makes it 
only match with exactly welcome. ^$ will match on the empty string.
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome', welcome)
]
