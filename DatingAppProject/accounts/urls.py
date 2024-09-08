from django. urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('', views.PersonalDetailsView.as_view(), name='details'),
    path('status', views.JobStatusView.as_view(), name='status'),


]