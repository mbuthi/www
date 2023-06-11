from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.renderIndex, name='renderIndex'),
    path('landing/', views.renderLanding, name='renderLanding'),
new-branch
    path('showdown/', views.renderShowdown, name='renderShowdown'),

 main
    path('reviews', views.renderIndex, name='renderIndex'),
    path('review/<str:reviewID>', views.renderReviewPage, name='renerReviewPage'),
    path('newComment', views.newComment, name='newComment'),
    path('getReviews', views.getReviews, name='getReviews'),
    path('logout', views.logOut, name='logOut'),
    path('login', views.renderlogIn, name='renderLogIn'),
    path('register', views.renderRegister, name='renderRegister'),
    path('registerNewUser', views.registerNewUser, name='registerNewUser'),
    path('loginUser', views.loginUser, name='loginUser'),
    path('new', views.renderNewReview, name='renderNewReview'),
    path('newReview', views.newReview, name='newReview'),
    path('account/<str:id>', views.renderAccountPage, name='renderAccountPage'),
    path('follow', views.followHandler, name='followHandler'),
    path('deleteUser', views.deleteUser, name='deleteUser'),
    path('likecontrol', views.likeControl, name='likeControl'),
    path('top', views.renderTop, name='renderTop'),
    path('editProfile', views.editProfile, name='editProfile'),
 new-branch
] + static('/css/', document_root=settings.CSS_ROOT) + static('/landing/', document_root='main/templates/main/landing/') +\
    static('/showdown/', document_root='main/templates/main/showdown/')

] + static('/css/', document_root = settings.CSS_ROOT) + static('/landing/', document_root = 'main/templates/main/landing/')
 main
