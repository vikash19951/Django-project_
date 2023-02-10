from django.shortcuts import render

# Create your views here.
def course_duration(request):
    course_durations ={
        "Python": '3 month',
        "Django": '1 month',
        "Flask":'1 month'
    } 
    return render(request, 'course/courseone.html', course_durations)