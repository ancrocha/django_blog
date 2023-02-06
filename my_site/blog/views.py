from django.shortcuts import render, get_object_or_404

from .models import Post

from datetime import date

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # - is for descend order. [:3] only firts 3. [-3:] wont work.

    return render(request, "blog/index.html", {
        "posts": latest_posts,
    }
    )

def posts(request):
    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    indentified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",{
        "post": indentified_post,
        "post_tag": indentified_post.tags.all()
    })