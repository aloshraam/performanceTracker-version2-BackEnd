from django.urls import path
from adminapi import views
from adminapi.views import get_csrf_token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register("hr",views.HrView,basename="hr")
router.register("teamlead",views.TeamleadView,basename="teamlead")
router.register("employee",views.EmployeesView,basename="employee")
router.register("meeting",views.MeetingView,basename="meeting")
router.register("technology",views.TechnologiesView,basename="tech")





urlpatterns = [
    
    path('token/',views.CustomAuthToken1.as_view(), name='token'),
    path('attendance/', views.AttendanceListView.as_view(), name='attendance-list'),
    path('csrf/', get_csrf_token, name='get_csrf_token')
    
] +router.urls
