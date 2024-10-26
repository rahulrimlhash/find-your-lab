from django.urls import path

from .views import (

    profile,
    profile_edit,
    orders_by_user,
    filtered_report,

)


app_name = 'custom_users'

urlpatterns = [

    path('profile/', profile, name='profile'),

    path('profile-edit/', profile_edit, name='profile-edit'),

    path('orders-by-user/', orders_by_user, name='orders-by-user'),

    path('filtered-reports-by-user/<int:id>/', filtered_report, name='filtered-reports-by-user'),
]
