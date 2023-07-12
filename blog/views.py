from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')      
    return render (request,'post_list.html', {'posts':posts})  

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render (request, 'post_detail.html', {'post':post})

def post_new(request):
    if request.method== "POST":
        form = PostForm(request.Post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()    
    return render(request, 'post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect ('post_detail', pk=post.pk)
    else:
          form = PostForm(instance=post)
          return render(request, 'post_edit.html',{'form':form})
#here we put instance(post) it's an object edit post and when we put instance=post mean send save as an post rather form
