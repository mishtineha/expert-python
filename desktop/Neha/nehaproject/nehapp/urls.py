from django.conf.urls import url
from . import views
app_name = 'nehapp'

urlpatterns =[
    url(r'neha/',views.index,name = 'index'),
    url(r'^(?P<parameter>[0-9]+)/$',views.showparms,name = 'showparms'),
    url(r'temp/',views.temp,name = 'temp'),
    url(r'/favorite/',views.favorite,name = 'favorite'),
    url(r'(?P<par>[0-9]+)/fav/',views.fav,name = 'fav'),
    url(r'add/',views.adding,name = 'adding'),
    url(r'action/',views.action,name = 'action'),
    url(r'show/',views.show,name = 'show'),
    url(r'search/',views.search,name = 'search'),
    url(r'signup/',views.signup,name = 'signup'),
    url(r'first_page/',views.first_page,name = 'first_page'),
    url(r'login/',views.login,name = 'login'),
    url(r'eg/',views.eg,name = 'eg'),
   
    url(r'logout/',views.logout,name = 'logout'),

    
    ]
