from django.urls import path
from . import views
app_name = 'blog'
urlpatterns=[
   path('FAQ/',views.FAQ,name='blog-FAQ'),
   path('notifications/',views.notifications,name='blog-notifications'),
   path('',views.PostListView.as_view(),name='post_list'),
   path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]

