from django.db import models
from django.utils import timezone

# Objeto que se guarda en la bdd de django
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)        ## txt con nro limitado de caracteres
    text = models.TextField()                       ## txt con largo ilimitado
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title