from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
    path('jobtitles/', views.jobtitles_index, name='index'),
    path('jobtitles/<int:jobtitle_id>/', views.jobtitles_detail, name='detail'),
    path('jobtitles/create/', views.JobTitleCreate.as_view(), name='jobtitles_create'),
    path('jobtitles/<int:pk>/update/', views.JobTitleUpdate.as_view(), name='jobtitles_update'),
    path('jobtitles/<int:jobtitle_id>/add_comment/', views.add_comment, name='add_comment'),
    path('jobtitles/<int:jobtitle_id>/delete_comment/<int:comment_id>', views.delete_comment, name="delete_comment"),
    path('jobtitles/<int:jobtitle_id>/update_comment/<int:comment_id>', views.update_comment, name="update_comment"),
    path('applicants/', views.applicants_detail, name='applicants_detail'),
    path("jobtitles/assoc_job/<int:jobtitle_id>/",views.assoc_job, name="assoc_job",),
    path("jobtitles/unassoc_job/<int:jobtitle_id>/",views.unassoc_job, name="unassoc_job",),
    path('jobtitles/<int:jobtitle_id>/asooc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('jobtitles/<int:jobtitle_id>/unasooc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),
    path('jobtitles/<int:jobtitle_id>/assoc_user/', views.assoc_user, name='assoc_user'),
    path('jobtitles/<int:jobtitle_id>/unassoc_user/', views.unassoc_user, name='unassoc_user'),
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]