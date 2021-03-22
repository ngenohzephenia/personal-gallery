from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/',default='')
    name = models.CharField(max_length=200, null=True)
    image_location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    image_category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    description=models.TextField()


    def __str__(self):
        return self.save()

    def delete_image(self):
        self.delete()


    def update_image(self, Name=None, category=None):
        self.name = Name if Name else self.Name
        self.image_category = category if category else self.image_category 
        self.save()



    