from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])
    def __str__(self):
        return self.name

  #  def __str__(self):
   #     return self.name

    #def get_absolute_url(self):
     #   return ('category/'+self.slug)

def generate_filename(instance,filename):
    filename=instance.slug+'.jpg'
    return "{0}/{1}".format(instance, filename)



class BlogManager (models.Manager):

    def all (self):
        return super(BlogManager, self).get_queryset().filter(pk_in=[3,5,7])



class Blog (models.Model):
    category = models.ForeignKey (Category, on_delete=models.PROTECT, verbose_name='Категория')
    title = models.CharField (max_length=120, verbose_name='Название')
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename, verbose_name='Изображение')
    text_min = models.TextField(max_length= 350,verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Содержание')
    likes = models.PositiveIntegerField(default=0, verbose_name='Лайки')
    #published = models.DateTimeField('Дата создания', auto_now_add=True)
    dislikes = models.PositiveIntegerField(default=0, verbose_name='Дизлайки')
    objects = models.Manager()
    tags = models.ManyToManyField('Tag', blank=True, related_name='blogs')
    #comments=GenericRelation('comments')


    def __str__(self):
        return "Статья '{0}' из категории '{1}'".format(self.title, self.category.name)


class MyBlog(Blog):
    class Meta:
        proxy=True


class Tag(models.Model):
    title =models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
        return '{}'.format (self.title)


'''class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    content_type = models.ForeignKey(ContentType, on_delete= models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')'''