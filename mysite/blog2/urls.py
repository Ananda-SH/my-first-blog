from django.conf.urls import url

from blog2 import views

urlpatterns = [
    url(r'^$', views.home_page, name='post_list'),
    url(r'^details', views.details_page, name='details_page'),
    url(r'^editreg/(?P<pk>\d+)/$', views.details_edit, name='edit_reg')
]



