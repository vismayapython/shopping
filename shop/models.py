from django.db import models
from django.db.models import CASCADE
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class categ(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class products(models.Model):

    objects = None
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    img = models.ImageField(upload_to='product')
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
