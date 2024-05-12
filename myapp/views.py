# views.py
from django.shortcuts import render,redirect,get_object_or_404
from .models import Student, Item
from .forms import CreateNewList
from django.urls import reverse
from django.shortcuts import render
from datetime import date  # Import for date handling

from .models import Student, Item
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Student, Item

@csrf_exempt
def update_click_count(request, student_id,subject):
    if request.method == 'POST':
        data = json.loads(request.body)  # Get JSON data from request
        subject = data.get('subject')  # Get the subject to update

        student = Student.objects.get(id=student_id)
        item = getattr(student, subject)  # Get the related Item
        # Increment click count or reset if it reaches 4
        if item.click_count >= 3:
            item.click_count = 0  # Reset count and make it inactive
        else:
            item.click_count += 1  # Increment count and activate
        
        if item.click_count==0:
            item.c1_color = "white"
            item.c2_color = "white"
            item.c3_color = "white"
        
        elif item.click_count==1:
            if(item.c1_color=="white"):
                item.c1_color = "black"
            item.c2_color = "white"
            item.c3_color = "white"

        elif item.click_count==2:
            if(item.c1_color=="white"):
                item.c1_color = "black"
            if(item.c2_color=="white"):
                item.c2_color = "black"
            item.c3_color = "white"

        elif item.click_count==3:
            if(item.c1_color=="white"):
                item.c1_color = "black"
            if(item.c2_color=="white"):
                item.c2_color = "black"
            if(item.c3_color=="white"):
                item.c3_color = "black"

        item.save()  # Save the changes
        item_details = {
                'c1_color': item.c1_color,

                'c2_color': item.c2_color,

                'c3_color': item.c3_color,

                'click_count': item.click_count,  # If tracking click count
            }
        return JsonResponse({'status': 'success', 'click_count': item.click_count,'item':item_details})

    return JsonResponse({'status': 'failed'}, status=400)
@csrf_exempt
def update_longpress(request, student_id,subject,circle):
    if request.method == 'POST':
        data = json.loads(request.body)  # Get JSON data from request
        subject = data.get('subject')  # Get the subject to update

        student = Student.objects.get(id=student_id)
        item = getattr(student, subject)  # Get the related Item
        if 1==circle:
            item.c1_color ="green"
        if 2==circle:
            item.c2_color ="green"
        if 3==circle:
            item.c3_color ="green"
        item.save()  # Save the changes
        item_details = {
                'c1_color': item.c1_color,

                'c2_color': item.c2_color,

                'c3_color': item.c3_color,

                'click_count': item.click_count,  # If tracking click count
            }
        return JsonResponse({'status': 'success', 'click_count': item.click_count,'item':item_details})

    return JsonResponse({'status': 'failed'}, status=400)

def index(request):
    students = Student.objects.all()
    today = date.today()

    if request.method == "POST":
        if request.POST.get("save"):
            # Handle saving student completion status (existing logic)
            for item in students:
                item.complete = request.POST.get("c" + str(item.id)) == "clicked"
                item.save()

        elif request.POST.get("newStudent"):
            # Handle creating a new student (existing logic)
            name = request.POST.get("new")
            if len(name) > 2:
                Student.objects.create(
                    name=name,
                    Gr=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    ELA=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Math=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Reading=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Sci=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    S_S=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Computer=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Test=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Language=Item.objects.create(
                    c1_color="white",  # Change as needed

                ),
                    Other=Item.objects.create(
                    c1_color="white",  # Change as needed

                )
                )
                return redirect("index") 
            else:
                print("invalid")

    return render(request, "ready.html", {"students": students, "today": today})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    # if request.method == "POST":
    student.delete()  # This might also delete related Item objects due to CASCADE
    return redirect(reverse('index'))  # Redirect to a safe place after deletion

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = CreateNewList(request.POST or None)  
    return render(request, 'update.html',{'student': student,'form':form })
def do_update_student(request, id):
    student = get_object_or_404(Student, id=id)
    name = request.POST.get('name') 
    student.name = name
    student.save()
    return redirect('index')
