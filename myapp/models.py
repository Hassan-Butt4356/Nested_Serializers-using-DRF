from django.db import models


class Site(models.Model):
    url = models.CharField(max_length=100)



class AccessKey(models.Model):
    key = models.CharField(max_length=100)


class MyUser(models.Model):
    username = models.CharField(max_length=100)


class Profile(models.Model):
    sites = models.ManyToManyField(Site)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    access_key = models.ForeignKey(AccessKey, null=True, on_delete=models.CASCADE)


class Avatar(models.Model):
    image = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, related_name='avatars', on_delete=models.CASCADE)




class Data(models.Model):
    user=models.OneToOneField(MyUser, on_delete=models.CASCADE,related_name='user_data')
    age=models.CharField(max_length=25)
    email=models.EmailField(max_length=155)
    is_merchant=models.BooleanField(default=True)

class SecurityQuestion(models.Model):
    data=models.ForeignKey(Data, on_delete=models.CASCADE,related_name='data')
    questions=models.CharField(max_length=255)

    def __str__(self):
        return self.questions
    
    def change_question(self,question):
        self.questions=question


class Tag(models.Model):
    name=models.CharField(max_length=155)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    tags=models.ManyToManyField(Tag)
    title=models.CharField(max_length=155)
    description=models.CharField(max_length=355)

    def __str__(self):
        return self.title