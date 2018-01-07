from django.shortcuts import render

# Create your views here.

def index(request):
    new_title = 'EPL 프리뷰 뉴스입니다.'
    content = '맨유 VS 맨시티'
    
    context = {'new_title': new_title, 'content':content}
    return render(request, 'epl/index.html', context)