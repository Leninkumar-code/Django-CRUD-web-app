from django.shortcuts import render,redirect
from app_crud.models import student
from app_crud.forms import StudentForm
from django.urls import reverse
# Create your views here.


# -----------This function is only view the contents of database------------>
def display (a):
    dis = student.objects.all()
    return render (a,'view.html',{'disp' : dis})

# ------------This can be create a new row --------------------------------->
def create (b):
    form = StudentForm()
    if b.method == 'POST':
        forms = StudentForm(b.POST)
        if forms.is_valid():
            forms.save()
            return redirect(reverse('display'))
    return render (b,'create.html',{'forms':form})

# -----------It will delete the whole row ---------------------------------->
def delete_(req,id):
    det=student.objects.get(id=id)
    det.delete()
    return redirect(reverse('display'))

# -----------It can update/or edit the datas in a row ----------------------->
def update_(req,id):
    upd=student.objects.get(id=id)
    frm_obj=StudentForm(instance=upd)
    if req.method=='POST':
        u=StudentForm(req.POST,instance=upd)
        if u.is_valid():
            u.save()
            return redirect(reverse('display'))
    return render(req,'create.html',{'forms':frm_obj})
    
    
    
    