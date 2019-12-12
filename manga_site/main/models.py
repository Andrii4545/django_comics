from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '' + self.name

class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return 'tag ' + self.name

class Manga(models.Model):
    title = models.ImageField(upload_to='mangas/titles')
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    data_reliz = models.DateField()
    name = models.CharField(max_length=30)
    tag = models.ManyToManyField(Tags, related_name='manga')
    datas = models.TextField(max_length=250, blank=True)
    def __str__(self):
        return 'Manga ' + self.name

class Glava(models.Model):
    numver = models.IntegerField()
    name = models.CharField(max_length=20)
    num_tom = models.IntegerField()
    manga = models.ForeignKey(Manga,on_delete=models.CASCADE,related_name='glava')
    def __str__(self):
        return 'Glava ' + self.name

def get_image_filename(instance, filename):
    title = instance.glava.name
    slug = slugify(title)
    return "mangas/manga/%s/%s" % (slug,filename)

class Pics(models.Model):
    pic = models.ImageField(upload_to=get_image_filename)
    glava = models.ForeignKey(Glava,on_delete=models.CASCADE,related_name='imgs')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manga = models.ManyToManyField(Manga,related_name='prof',blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Coments(models.Model):
    article_id = models.ForeignKey(Manga, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария',default=datetime.now())
