from django.test import TestCase

# Create your tests here.
class ImageTestClass(TestCase):
    def setup(self):
        self.image_location = Location(name='Rift-Valley')
        self.image_loaction.save()

        self.image_category = Category(name='Food')
        self.image_category.save()

        self.image_food = Image(name='Kenya', description='there is food', image_location='self.image_location', image_category=self.image_category)
        self.image_food.save_image()
