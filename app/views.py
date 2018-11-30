from django.http import HttpResponse
from django.shortcuts import render

# templates/app   templates/firstapp
from django.views import generic

from app.forms import SearchForm
from app.models import User, Curriculum

def tables(request):
    return render(
        request,
        'app/tables.html'
    )

def dashboard(request):
    return render(
        request,
        'app/index.html'
    )

def a(request):
    return render(
        request,
        'app/a.html'
    )

def b(request):
    return render(
        request,
        'app/b.html'
    )


def detail2(request):
    id = request.GET['id']
    c = Curriculum.objects.get(id=id)
    return render(
        request,
        'app/curriculum_detail.html',
        {'object' : c}
    )

class DetailView(generic.DetailView):
    model = Curriculum
    context_object_name = 'object'

class ListView(generic.ListView):
    model = Curriculum

class SearchFormView(generic.FormView):
    form_class = SearchForm
    template_name = 'app/search.html'

    def form_valid(self, form):
        search_word = '%s' % self.request.POST['search_word']
        list = Curriculum.objects.filter(name__contains=search_word)
        context = {}
        context['form'] = form
        context['search_word'] = search_word
        context['object_list'] = list
        return render(self.request, self.template_name, context)


def user(request):
    user = User.objects.get(id=1) # a

    return render(
        request,
        'app/user.html',
        {'user':user}
    )

def index(request):
    return HttpResponse('Index')

def template(request):
    words = ['python', 'java', 'jquery']
    dic = {'a':1, 'b':'XYZ', 'c':[1, 2, 3]}
    name = 'ggoreb'
    age = 30.0

    return render(
        request,
        'app/template.html',
        {
            'words':words, 'dic':dic,
            'name':name, 'age':age
        }
    )














