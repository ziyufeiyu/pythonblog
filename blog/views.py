from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse
from .models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def hello(request):
    return HttpResponse('欢迎使用Django！')


def global_variable(request):
    allcategory = Category.objects.all().order_by("index")
    remen = Article.objects.filter(recommend__id=2).order_by('modified_time')[:6]
    tags = Tag.objects.all()
    media_prefix = settings.MEDIA_URL
    return locals()


# 首页
def index(request):
    banner = Banner.objects.filter(is_active=True)[0:4]  # 查询所有幻灯图数据，并进行切片
    recommend = Article.objects.filter(recommend__id=1)[:3]  # 查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-modified_time')[:6]
    hot = Article.objects.all().order_by('views')[:6]  # 通过浏览数进行排序
    right_hot = Article.objects.filter(recommend__id=2)[:6]
    link = Link.objects.all()
    # 把查询出来的分类封装到上下文里
    context = {
        'banner': banner,  # 把查询到的幻灯图数据封装到上下文
        'recommend': recommend,
        'allarticle': allarticle,
        'hot': hot,
        'right_hot': right_hot,
        'link': link,
    }
    return render(request, 'index.html', locals())


#  列表页
def list(request,lid):
    list = Article.objects.filter(category_id=lid).order_by("-modified_time")  # 获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)  # 获取当前文章的栏目名
    recommend = Article.objects.filter(recommend__id=2)[:6]  # 右侧的热门推荐
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 8)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    link = Link.objects.all()
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request, 'list.html', locals())


# 内容页
def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    hot = Article.objects.all().order_by('?')[:5]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(modified_time__gt=show.modified_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(modified_time__lt=show.modified_time, category=show.category.id).last()
    Article.objects.filter(id=sid).update(views=show.views + 1)

    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag).order_by('-modified_time')  # 通过文章标签进行查询文章
    remen = Article.objects.filter(recommend__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss).order_by("-modified_time")  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(recommend__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())


