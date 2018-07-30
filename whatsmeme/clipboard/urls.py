from django.urls import path
from . import views

urlpatterns = [
		path('',views.ClipboardListView.as_view(),name="clipboard_list"),
	path('new',views.ClipboardCreateView.as_view(),name="clipboard_new"),
	path('<slug:slug>',views.ClipboardDetailView.as_view(),name="clipboard_detail"),
		] 