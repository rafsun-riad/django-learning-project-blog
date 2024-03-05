from django.shortcuts import render
from datetime import date
from .models import Tag, Author, Post

# Create your views here.

posts_list = [

]


def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(posts_list, key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_post})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": posts_list})


def post_detail(request, slug):
    identified_post = next(post for post in posts_list if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
