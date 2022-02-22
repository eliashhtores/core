from django.db import models


class PostManager(models.Manager):

    def get_published_posts(self):
        return self.filter(status='P')
