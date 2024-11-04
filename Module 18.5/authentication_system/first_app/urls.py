from django.urls import path
from first_app.views import home, signupviews, loginviews, profileviews, logoutviews, passwordchangeviews
urlpatterns = [
    path('', home, name="homepage"),
    path('register/', signupviews, name="signuppage" ),
    path('login/', loginviews, name="loginpage" ),
    path('profile/', profileviews, name="profilepage" ),
    path('logout/', logoutviews, name="logoutpage" ),
    path('changepassword/', passwordchangeviews, name="passwordchange" ),

]