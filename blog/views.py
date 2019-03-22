from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post, Category

def post_list_view(request, category_name=None):
	posts=Post.objects.filter(public=True).order_by('date_publish')
	context = {
		'object_list':Post.objects.all(),
		'categories_list':Category.objects.all(),
		# 'category_name':category_name,
		# 'menu':Category.objects.all()
	}
	return render(request,'blog/post_list.html',context)

def post_detail_view(request, post_id):
	context = {
			'object': get_object_or_404(Post, id=post_id),
			'categories_list':Category.objects.all(),
			'category_name': None,
	}
	return render(request,'blog/post_detail.html',context)

def post_category_view(request, category_name):
	c = Category.objects.get(name=category_name)
	context = {
			
			'categories_list': c.post_set.all(),
			'name': category_name,
			'menu':Category.objects.all(),
			'selected':category_name,
			'object_list':c
	}
	return render(request, 'blog/post_category.html', context)