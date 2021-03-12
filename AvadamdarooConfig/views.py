from django.shortcuts import render, redirect
from Blog.models import Article
from Business.models import Brands, Agents


def Index(request):
    article=Article.objects.filter(status='p')
    brands=Brands.objects.all()
    agents=Agents.objects.all()
    context={
    "brands":brands,
    "agents":agents,
    'articles':article

    }
    return render(request,'AvadamConfig/index.html',context)


from django.utils.translation import activate

def change_lang(request):
	activate(request.GET.get('lang'))
	return redirect(request.GET.get('next'))    