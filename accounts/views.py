from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm

def index(request):
    form_buscar = BuscarPostForm(request.GET)
    posts = Post.objects.all()

    if form_buscar.is_valid():
        termino = form_buscar.cleaned_data.get('termino')
        if termino:
            posts = posts.filter(titulo__icontains=termino)

    return render(request, 'accounts/index.html', {'posts': posts, 'form_buscar': form_buscar})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'accounts/autor_form.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'accounts/categoria_form.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'accounts/post_form.html', {'form': form})