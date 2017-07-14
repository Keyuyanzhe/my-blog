# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


# python_2_unicode_compatible 装饰器用于兼容Python2
@python_2_unicode_compatible
class Category(models.Model):
    """
    分类Category只需要一个简单的分类名name就可以了
    Django模型必须继承models.Model类
    CharField是字符型，max_length参数指定最大长度，超过长度不能存入数据库
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    """
    标签Tag也比较简单，和Category一样
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    """
    文章数据库，涉及的字段更多
    """
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文
    body = models.TextField()
    
    #文章创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下CharField要求必须存入数据，否则报错
    # 指定CharField的blank=True参数值后就能允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    # 分类与标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，User是从django.contrib.auth.models导入的
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
