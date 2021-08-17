from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

# Create your models here.

class Article(models.Model):
    author= models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar",related_name="sa")
    title = models.CharField(max_length=50,verbose_name="Baslik")
    content = RichTextField(verbose_name="Icerik")
    createdDate = models.DateTimeField(auto_now_add=True)
    articleImage=models.FileField(blank=True , null=True,verbose_name="Resim Ekle")

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-createdDate']

class Commet(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="commett",related_name="commet")

    author = models.CharField (max_length=20,verbose_name="Isim")
    content = models.TextField(max_length=100,verbose_name="Icerik")
    createDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    class Meta:
        ordering = ['-createDate']
    

