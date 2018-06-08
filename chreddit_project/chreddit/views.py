from django.shortcuts import render redirect
from .forms import PostForm, CommentForm, ProfileForm
from .models import Post, Comment, Profile

# Create your views here.

# Post  Index
def post_list(request):
    posts = Post.objects.all().order_by('title')
    return render(request, 'chreddit/post_list.html', {'posts': posts})


# Post Show/Read
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'chreddit/post_detail.html', {'post': post})

# Post New/Create
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'chreddit/post_form.html', {'form': form})

# Post Edit/Update
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'chreddit/post_form.html', {'form': form})

# Post Delete/Destroy
def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')



# Comment  Index
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'chreddit/comment_list.html', {'comments': comments})

# Comment Show/Read
def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'chreddit/comment_detail.html', {'comment': comment})

# Comment New/Create
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
        posts = Post.objects.all()
    return render(request, 'chreddit/comment_form.html', {'form': form})

# Comment Edit/Update
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'chreddit/comment_form.html', {'form': form})

# Comment Delete/Destroy
def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')


# Profile  Index
def profile_list(request):
    profiles = Profile.objects.all().order_by('start_year')
    return render(request, 'chreddit/profile_list.html', {'profiles': profiles})


# Profile Show/Read
def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'chreddit/profile_detail.html', {'profile': profile})

# Profile New/Create
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm()
    return render(request, 'chreddit/profile_form.html', {'form': form})

# Profile Edit/Update
def profile_edit(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'chreddit/profile_form.html', {'form': form})

# Profile Delete/Destroy
def profile_delete(request, pk):
    Profile.objects.get(id=pk).delete()
    return redirect('profile_list')
