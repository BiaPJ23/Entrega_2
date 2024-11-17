from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model 

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        'Post', 
        on_delete=models.CASCADE, 
        related_name='comments',
        )
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.author} em {self.post.title}'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True) 
    posts = models.ManyToManyField('Post', related_name='categories') 

    def __str__(self):
        return self.name
