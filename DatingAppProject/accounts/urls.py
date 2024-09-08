from django. urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('', views.PersonalDetailsView.as_view(), name='details'),
    path('job_status', views.JobStatusView.as_view(), name='job_status'),
    path('job_details', views.JobDetailsView.as_view(), name='job_details'),



]