from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
# Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체를 Django가 전달해준다.
def post_list(request):
    my_name = '장고웹프레임워크'
    http_method = request.method

    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method : {method}</p>
    #     <p>Http headers User-Agent : {header}</p>
    #     <p>Http Path : {mypath}</p>
    # '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path))

    from django.utils import timezone
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})

