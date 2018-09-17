from django.http import HttpResponse
from django.shortcuts import render

from apps.home.models import Navigation, Banner, Category


def index(request):
    #获取导航单数据
    navigations=Navigation.objects.all()
    #分类菜单的数据
    categories=Category.objects.all()
    for category in categories:
        category.subs=category.submenu_set.all()
        for sub in category.subs:
            sub.sub2=sub.submenu2_set.all()
    #轮播图数据
    banners=Banner.objects.all()
    return render(request, 'index.html', {'navigations':navigations, 'banners': banners, 'categories': categories})
