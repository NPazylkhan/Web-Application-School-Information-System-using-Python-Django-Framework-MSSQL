from django.shortcuts import render
from .models import Person, Position, Depart, Workers, Image
from .forms import PersonForm, ImageForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from mssql.settings import EMAIL_HOST_USER
from . import forms


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'sql/success.html', {'recepient': recepient})
    return render(request, 'sql/sendemail.html', {'form':sub})


def sendmail(request):
    send_mail(
        'Subject',
        'Email message',
        'nurmakhanpazylkhan@gmail.com',
        ['npazylhan@gmail.com','nurmahan_9898@mail.ru'],
        fail_silently=True,
    )
    return HttpResponse('Mail successfully sent')


def general(request):
    iis = Image.objects.all()
    context = {'iis':iis}
    return render(request, 'layout/basic.html', context)
 

def index(request):
    bs = Person.objects.order_by('-id')
    ps = Position.objects.all()
    context = {'bs':bs, 'ps':ps}
    return render(request, 'sql/index.html', context)


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(year__icontains=query)
            results= Person.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'sql/search.html', context)
        else:
            return render(request, 'sql/search.html')
    else:
        return render(request, 'sql/search.html')


def doc(request):
    if request.method == 'GET':     
        query = request.GET.get('d')
        query1 = request.GET.get('f')
        submitbutton= request.GET.get('submit')
        if query and query1 is not None:
            lookups= Q(id__exact=query) & Q(firstname__exact=query1)
            results= Person.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'sql/doc.html', context)
        else:
            return render(request, 'sql/doc.html')
    else:
        return render(request, 'sql/doc.html')


def dir(request):
    if request.method == 'GET':     
        query = request.GET.get('d')
        query1 = request.GET.get('f')
        submitbutton= request.GET.get('submit')
        if query and query1 is not None:
            lookups= Q(id__exact=query) & Q(firstname__exact=query1)
            results= Person.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'sql/dir.html', context)
        else:
            return render(request, 'sql/dir.html')
    else:
        return render(request, 'sql/dir.html')


class PersonCreateForm(CreateView):
    template_name = 'sql/create.html'
    form_class = PersonForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateImageView(CreateView): # new
    model = Image
    form_class = ImageForm
    template_name = 'sql/image.html'
    success_url = '/'

    def get_context_data(request):
        bs = Person.objects.all()
        context = {'bs':bs}
        return context


class PersonDeleteForm(DeleteView):
    model = Person
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class PersonDetailView(DetailView):
    model = Person

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class PersonEditView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = '/'

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class PositionIndexView(TemplateView):
    template_name = 'sql/position.html'

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['ps'] = Position.objects.all()
        return context


class DepartIndexView(TemplateView):
    template_name = 'sql/depart.html'

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['ds'] = Depart.objects.all()
        return context


class WorkersIndexView(TemplateView):
    template_name = 'sql/workers.html'

    def get_context_data( self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['ws'] = Workers.objects.all()
        return context

        
# class BbByRubricView(ListView):
#     template_name = 'bboard/by_rubric.html'
#     context_object_name = 'bbs'


#     def get_queryset(self):
#         return Bb.objects.filter(rubric = self.kwargs['rubric_id'])

#     def get_context_data( self, *args, **kwargs):
#         context = super().get_context_data( *args, **kwargs)
#         context['rubrics'] = Rubric.objects.all()
#         context['current_rubrics'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
#         return context


