from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe

# Create your models here.
class Image(models.Model):
    alt=models.TextField()
    file=ThumbnailerImageField(upload_to="products")
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def image(self):
        return mark_safe('<a href="{}" target="_blank"'
                            '<img src="{1} width="150" height="150"/>'
                            '</a>'.format(self.file.url, self.file['admin_preview'].url)
        
                            )

    def image_icon(self):
        return mark_safe('<a href="{}" target="_blank"'
                            '<img src="{1} width="100" height="100"/>'
                            '</a>'.format(self.file.url, self.file['admin_preview_icon'].url)

        
                            )