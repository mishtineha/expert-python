from django.conf.urls import url
from . import views
app_name = 'App'

urlpatterns =[
    url(r'home/',views.hello,name = 'hello'),
    url(r'alluser/',views.alluser,name = 'alluser'),
    url(r'^(?P<parameter>[0-9]+)/$',views.showuser,name = 'showuser'),
    url(r'creditsto/',views.creditsto,name = 'creditsto'),
    url(r'transfer/(?P<parameter2>[0-9]+)/$',views.transfer,name = 'transfer'),
    url(r'last/',views.last,name = 'last'),
    url(r'TransferDetails/',views.TransferDetails,name = 'tDetails'),
    url(r'Cancel/',views.Cancel,name = 'Cancel'),
    url(r'showuser2/(?P<parameter3>[0-9]+)/$',views.showuser2,name = 'showuser2'),
    ]
