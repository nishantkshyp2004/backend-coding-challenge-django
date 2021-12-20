from django.db import models

TAGS_CHOICES = [("office", "office"),
                ("shopping", "shopping"),
                ("holiday", "holiday"),
                ("study", "study"),
                ("personal", "personal"),
                ("friends", "friends"),
                ("home", "home"),
                ("family", "family")]

VISIBILITY_CHOICES = [("public", "public"),
                      ("private", "private")]


class NoteTaking(models.Model):
    """
    NoteTaking Model class.
    """
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    tags = models.CharField(choices=TAGS_CHOICES, default='personal',
                            max_length=100)
    visibility = models.CharField(choices=VISIBILITY_CHOICES, default='public',
                                  max_length=100)
    owner = models.ForeignKey('auth.User', related_name='note_taking',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
