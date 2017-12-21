from django.conf.urls import url

from pages import views
from pages.views import HomePage, AboutPage

urlpatterns = [
    url(r'^/', views.homePageView, name='pages'),
    url(r'^home/', HomePage.as_view(), name='home'),
    url(r'^about/', AboutPage.as_view(), name='about'),
   ]