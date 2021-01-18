from django.urls import path
from .views import productlist,cartcreate,viewcart
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('plst',productlist.as_view()),
    path('carturl',cartcreate.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('viewcart',viewcart.as_view()),
    path('whishlist',whishlist.as_view()),
]