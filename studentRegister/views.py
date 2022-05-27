from django.shortcuts import render,redirect
from .forms import studentForm
from .models import Student
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def student_list(request):
	#context={'student_list':Student.objects.all()}
	data=Student.objects.all();
	paginator=Paginator(data,2);
	page_number=request.GET.get('page');
	final_data=paginator.get_page(page_number);
	totalPages=final_data.paginator.num_pages
	context={
	   'student_list':final_data,
	   'lastpage':totalPages,
	   'total_page_list':[n+1 for n in range(totalPages)]
	}

	return render(request,"studentRegister/student_list.html",context)

def student_form(request,id=0):
	if request.method=="GET":
		if id==0:
			form=studentForm()
		else:
			student=Student.objects.get(pk=id)
			form=studentForm(instance=student)
		return render(request,"studentRegister/student_form.html",{'form':form})
	else:
		if id==0:
			form=studentForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, 'Your profile is registered successfully!')
				return redirect('list/')
			else:
				messages.error(request, 'First name is already exist!')
				return redirect('/student/')
		else:
			student=Student.objects.get(pk=id)
			form=studentForm(request.POST,instance=student)
			if form.is_valid():
				form.save()
				return redirect('/student/list/')


def student_delete(request,id):
	student=Student.objects.get(pk=id)
	student.delete()
	return redirect('/student/list')
