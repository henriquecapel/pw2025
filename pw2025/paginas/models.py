from django.db import models

class (models.Model):

    

    class Curso:
        verbose_name = _("teste")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
