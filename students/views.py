from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<center><h1>index page</h1></center>")
def contact(request):
    return HttpResponse("<center><h1>contact page</h1></center>")
def students(request):
    return render( request,'students/pages/index.html')
def details(request,name,id):
#'key':'value'  e.g student_name armaghan
    return render( request,'students/pages/students_details.html',{'student_name':name ,'Roll_number':id}) # making dictionary

# second method
#context = {'student_name':name,'Roll_number':id}
#return render(request,'students/pages/students_details.html',context=context)

# Third Method
#arrays = [name,id]
#return render(request,'students/pages/students_details.html',('dump':arrays))