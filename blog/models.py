from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.
# 分类

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# 标签
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# 文章
@python_2_unicode_compatible
class Article(models.Model):
    # 标题
    title = models.CharField(max_length=100)
    # 正文（ 内容）
    content = models.TextField()
    # 分类
    category = models.ForeignKey(Category)
    # 标签
    tag = models.ManyToManyField(Tag, blank=True)
    # 摘要
    excerpt = models.CharField(max_length=300, blank=True)
    # 作者
    author = models.ForeignKey(User)
    # 时间（创建时间和修改时间）
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
