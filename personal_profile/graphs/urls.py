from django.urls import path
from .views import blog_list, blog_detail, blog_delete
from maps.views import default_map

urlpatterns = [
	path('',blog_list),
	path('<id>/',blog_detail),
	path('<id>/delete/',blog_delete),
	path('maps/', default_map),
]