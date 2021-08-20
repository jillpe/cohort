from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
    path('jobtitles/', views.jobtitles_index, name='index'),
    path('jobtitles/<int:jobtitle_id>/', views.jobtitles_detail, name='detail'),
    path('jobtitles/create/', views.JobTitleCreate.as_view(), name='jobtitles_create'),
     path('jobtitles/<int:pk>/update/', views.JobTitleUpdate.as_view(), name='jobtitles_update'),
#     path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('jobtitles/<int:jobtitle_id>/add_comment/', views.add_comment, name='add_comment'),
    path('jobtitles/<int:jobtitle_id>/delete_comment/<int:comment_id>', views.delete_comment, name="delete_comment"),
    path('jobtitles/<int:jobtitle_id>/update_comment/<int:comment_id>', views.update_comment, name="update_comment"),
#     path('finches/<int:finch_id>/asooc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
#     path('toys/', views.ToyList.as_view(), name='toys_index'),
#     path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
#     path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
#     path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
#     path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]