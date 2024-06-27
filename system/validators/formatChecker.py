import os
from django.core.exceptions import ValidationError

"""
    Same as FileField, but you can specify:
    * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
    * max_upload_size - a number indicating the maximum file size allowed for upload.
        2.5MB - 2621440
        5MB - 5242880
        10MB - 10485760
        20MB - 20971520
        50MB - 5242880
        100MB - 104857600
        250MB - 214958080
        500MB - 429916160
"""

def file_size(value):
    limit = 5242880
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')
    
def file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.jpg']
    if not ext in valid_extensions:
        raise ValidationError('Tipo de archivo no soportado. Solo se permiten archivos PNG y JPG')