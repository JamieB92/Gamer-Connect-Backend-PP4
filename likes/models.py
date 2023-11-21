from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Like model associated with 'owner' and 'post', where 'owner' represents a User instance and 'post' represents a Post instance. 
    The 'unique_together' constraint ensures that a user cannot like the same post more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-liked_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'