from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from .forms import ArticleForm
from .models import Article

def article_search_view(request):
    query_dict = request.GET # this is a dictionary
    #query = query_dict.get('q')
    try:
        query = int(query_dict.get('query'))
    except:
        query = None    
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {'object': article_obj}
    return render(request ,'articles/search.html', context)


@login_required
def article_create_view(request, id=None):
    form = ArticleForm(request.POST or None)
    context = {'form':form}
 
    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleForm()
        # title = request.cleaned_data.get('title')
        # content = request.cleaned_data.get('content')
        # article_obj = Article.objects.create(title=title, content=content)
        context['object'] = article_obj
        context['created'] = True
    return render(request, 'articles/create.html', context)



def article_list_view(request):
    object_list = Article.objects.all()
    context = {'object_list':object_list}
    return render(request, 'articles/list.html', context)
    
def article_detail_view(request, id=None):
    article_obj = None 
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {'object':article_obj}
    return render(request, 'articles/detail.html', context)