from django.urls import path
from .views import LogoutView, UserSearchView, UsersViewSet, LoginViewSet, UserProfileUpdateAPIViewSet, CreateUsersViewSet
# from .views import register_user

urlpatterns = [
    path('user_profile/', UsersViewSet.as_view()),
    path('user_profile/create_user/', CreateUsersViewSet.as_view()),
    path('user_profile/<int:id>/', UsersViewSet.as_view()),
    path('user_profile/update/<int:id>/',
         UserProfileUpdateAPIViewSet.as_view()),
    path('logins/', LoginViewSet.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
