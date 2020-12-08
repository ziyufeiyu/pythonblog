from django.contrib import admin

# Register your models here.
from .models import Banner, Category, Tag, Recommend, Article, Link


# 导入需要管理的数据库表
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'recommend', 'user', 'views', 'modified_time')
    exclude = ('summary',)
    search_fields = ('title',)  # 指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter = ('modified_time', 'category')  # 指定列表过滤器，右边将会出现一个快捷的日期过滤选项，
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-modified_time',)
    # 后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')
    list_editable = ['text_info', 'link_url']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')
    list_editable = ['name', 'index']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


@admin.register(Recommend)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')
    list_editable = ['name', 'linkurl']
