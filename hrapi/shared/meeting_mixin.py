# shared/views.py or utils/meeting_logic.py
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .models import TeamLead, Teams
from .models import Employee
from .models import Meeting
from .serializers import MeetingSerializer, MeetingListSerializer

class MeetingCreateMixin:
    def perform_meeting_creation(self, request):
        serializer = MeetingSerializer(data=request.data)
        user = request.user
        user_type = user.user_type

        if serializer.is_valid():
            meeting = serializer.save(organizer=user.username)

            all_admins = CustomUser.objects.filter(user_type='Admin')
            all_hrs = CustomUser.objects.filter(user_type='HR')
            all_teamleads = TeamLead.objects.all()

            if user_type == 'Admin':
                meeting.participants.set(list(all_hrs) + list(all_teamleads) + list(Employee.objects.filter(in_team=True)))
            elif user_type == 'HR':
                meeting.participants.set(list(all_admins) + list(all_teamleads) + list(Employee.objects.filter(in_team=True)))
            elif user_type == 'TeamLead':
                team = Teams.objects.filter(teamlead=user).first()
                employees = team.members.all() if team else []
                meeting.participants.set(list(all_admins) + list(all_hrs) + list(employees))

            return Response(data=MeetingListSerializer(meeting).data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)