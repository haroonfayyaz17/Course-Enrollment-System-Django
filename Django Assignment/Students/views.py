from .models import Student
from .forms import StudentForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView


class create(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'Students/create.html'
    success_url = '/students/student'


class delete(DeleteView):
    model = Student
    template_name = 'Students/delete.html'
    success_url = '/students/student'


class update(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'Students/update.html'
    success_url = '/students/student'


class detailView(DetailView):
    model = Student
    template_name = 'Students/detailView.html'


class listView(ListView):
    model = Student
    template_name = 'Students/listView.html'
    queryset = Student.objects.all().order_by('firstName')
    paginate_by = 4
