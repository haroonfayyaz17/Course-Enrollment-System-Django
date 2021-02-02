from .models import Enrollment
from .forms import EnrollmentForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView


class create(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/create.html'
    success_url = '/enrollments/enrollment'


class delete(DeleteView):
    model = Enrollment
    template_name = 'enrollments/delete.html'
    success_url = '/enrollments/enrollment'


class update(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/update.html'
    success_url = '/enrollments/enrollment'


class detailView(DetailView):
    model = Enrollment
    template_name = 'enrollments/detailView.html'


class listView(ListView):
    model = Enrollment
    template_name = 'enrollments/listView.html'
    paginate_by = 4
    queryset = Enrollment.objects.all().order_by('id')
