
from django.urls import path
from .views import *
urlpatterns = [
    path('signup',signup,name='signup'),
    path('logout',logout_view,name='logout'),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
    #     activate, name='activate'),  
    path('userlogin',userlogin,name='userlogin'),    
    path('userprofile',userprofile,name='userprofile'),
    
    path('profilereview',profilereview,name='profilereview'),    
    path('postview',postview,name='postview'),    
    path('chatview',chatview,name='chatview'),    
    path('mapview',mapview,name='mapview'),    
    path('riderhome',riderhome,name='ridehome'),    
    path('ride/details',rideDtails,name='prevrideDtails'),
        path('view_map/<int:id>',view_map,name="view_map")

]