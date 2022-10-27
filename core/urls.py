from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='product'),
    path('<slug:c_slug>/<slug:product_slug>',views.views,name='views'),
    path('signup/',views.signup,name='signup'),
    
    
]
