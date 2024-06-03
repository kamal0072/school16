from django.db import models

# Create your models here.
class MyUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    def __str__(self):
        return self.username
    
class Page(models.Model):
    myuser=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Post(models.Model):
    myuser = models.ForeignKey(to=MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    desc = models.TextField()
    auther = models.CharField(max_length=20)


class Song(models.Model):
    myuser = models.ManyToManyField(to=MyUser)
    name = models.CharField(max_length=200)
    duration = models.DateField()
    singer_name = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=20)

    def sung_by(self):
        return ",".join([str(p) for p in self.myuser.all()])