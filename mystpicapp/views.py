from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Mystery, Profile, Category, Comment
from .forms import MysteryForm, NewUserForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms


def main_page(request):
    mysteries = Mystery.objects.all()
    context = {'mysteries': mysteries}
    return render(request, 'mystpicapp/main.html', context)


def catalog(request):
    categories = Category.objects.order_by("name")
    mysteries = Mystery.objects.all()
    context = {'categories': categories, 'mysteries': mysteries}
    return render(request, "mystpicapp/catalog.html", context)


def catalog2(request, category_name):
    categories = Category.objects.order_by("name")
    mysteries = Mystery.objects.filter(category__name=category_name)
    context = {'categories': categories, 'mysteries': mysteries}
    return render(request, "mystpicapp/catalog.html", context)


def create_mystery(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = MysteryForm(request.POST, request.FILES)
        mystery = Mystery()
        mystery.creator = User.objects.get(username=request.user.username)
        mystery.title = request.POST.get("title")
        mystery.image = request.FILES.get("image")
        mystery.description = request.POST.get("description")
        mystery.answer = request.POST.get("answer")
        category_ids = request.POST.getlist("category")
        mystery.save()
        categories = Category.objects.filter(id__in=category_ids)
        mystery.category.set(categories)

    else:
        form = MysteryForm()

    return render(request, "mystpicapp/createmystery.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = NewUserForm()

    return render(request, "mystpicapp/register.html", {"form": form})


# def profile(request):
#     return render(request, "mystpicapp/profile.html")


def exit_page(request):
    logout(request)
    return HttpResponseRedirect("/")


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mystpicapp/profile.html'

    def get_context_data(self, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        profile_mysteries = Mystery.objects.filter(id=self.kwargs['pk'])
        context['page_user', 'mysteries'] = page_user, profile_mysteries
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'mystpicapp/create_profile.html'
    fields = ['profile_pic']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('main')


def mysteries(request, mystery_id):
    mystery = get_object_or_404(Mystery, id=mystery_id)
    comments = Comment.objects.filter(mystery__id=mystery_id)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        comment = Comment()
        comment.creator = User.objects.get(username=request.user.username)
        comment.mystery = get_object_or_404(Mystery, id=mystery_id)
        comment.text = request.POST.get("text")
        comment.save()

    else:
        form = CommentForm()

    context = {'mystery': mystery, 'comments': comments, 'form': form}

    return render(request, "mystpicapp/mystery.html", context)
