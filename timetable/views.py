from django.shortcuts import render

from django.http import HttpResponse

from datamgmt.models import Group

def index(request):
    group_list = Group.objects.all()
    context = {'group_list': group_list}
    return render(request, 'timetable/main.html', context)

def generate(request, group_id):
    
    return HttpResponse("Timetable"+ str(group_id))