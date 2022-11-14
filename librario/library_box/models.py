
from django.core.exceptions import ValidationError
from django.db import models

from library_box import validators

# Create your models here.
class LibraryBox(models.Model):

    class Meta:
        tablename = 'library_box'

    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(to='location.Address')


class BoxContent(models.Model):

    CONTENT_TYPES = [
        'BOOK',
        'DVD',
        'BLURAY',
        'CD',
        'OTHER'
    ]

    class Meta:
        tablename = 'box_content'

    library_box = models.ForeignKey(to='library_box.LibraryBox')
    content_type = models.CharField(max_length=64, validators=[validators.validate_content_type])
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)



