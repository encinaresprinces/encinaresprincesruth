from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from PList import views


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^new$', views.new_item, name='new_item'),
    url(r'^(\d+)/view_list$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^signup2$', views.signup2, name='home_page'),
    url(r'^signup3$', views.signup3, name='signup3'),
    url(r'^signup4$', views.signup4, name='signup4'),
    url(r'^certificate$', views.certificate, name='certificate'),
    url(r'^register$', views.register, name='register'),
    url(r'^user$', views.user, name='user'),
    url(r'^admin$', views.admin, name='admin'),
    url(r'^zadmin$', views.zadmin, name='zadmin'),
    url(r'^certificateprint$', views.certificateprint, name='certificateprint'),
    url(r'^print$', views.print, name='print'),







    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    ]