from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_signup,name='login-signup'),
    path('login/',views.login,name="log-in"),
    path('signup/',views.signup,name="sign-up"),
    path('index/<int:pk>',views.blog_index,name="blog-index"),
    path('category/<category>',views.blog_category,name="blog-category"),
    path('detail/<int:pk>',views.blog_detail,name="blog-detail"),
    path('post/create/<int:pk>',views.create_post,name="blog-post"),
    path('post/<int:pk>/delete',views.blog_delete,name="post-delete"),
    path('post/<int:pk>/profile',views.show_profile,name="profile"),
]