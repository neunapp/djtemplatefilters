from django.db import models

# Create your models here.
class Ad(models.Model):
    """ Modelo Anuncios """

    title = models.CharField(
        'Titulo', 
        max_length=50
    )
    content = models.TextField('Contenido')
    amount = models.DecimalField(
        'Honorarios', 
        max_digits=7, 
        decimal_places=3,
        default=0
    )


    class Meta:
      verbose_name = 'Anuncio'
      verbose_name_plural = 'Anuncios'

    def __str__(self):
        return self.title
