from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def postdetail(request):
    data = Post.objects.all().order_by('id')
    paginator = Paginator(data, 3, orphans=2)
    print("Paginator : ", paginator)
    # print("Paginator : ", paginator.count)
    # print("Paginator : ", paginator.per_page)
    # print("Paginator : ", paginator.get_page(4))
    page_no=request.GET.get('page')
    print("Page Number : ", page_no)
    print("Page Number : ", page_no)
    page_obj = paginator.get_page(page_no)
    print('Page Object : ', page_obj)
    return render(request, 'detail.html', {'page_obj' : page_obj})