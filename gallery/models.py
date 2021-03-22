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

    def __str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__category__icontains=search_term)
        return images    


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)



class Category(models.Model):
    category = models.CharField(max_length=80, null= True)

    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category    