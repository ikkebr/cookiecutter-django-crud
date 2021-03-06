from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class {{ cookiecutter.model_name }}(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{{ cookiecutter.model_name }} ({})'.format(self.id or 'Unsaved')

    def get_absolute_url(self):
        return reverse('{{ cookiecutter.model_name|lower }}_detail', args=[str(self.id)])

