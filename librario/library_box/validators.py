
from django.core.exceptions import ValidationError

from library_box.models import BoxContent


def validate_content_type(ct: str):
    if ct.upper() not in BoxContent.CONTENT_TYPES:
        raise ValidationError(f'Content type {ct} not valid. Use only values in {BoxContent.CONTENT_TYPES}.')