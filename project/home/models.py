from django.db import models


class Home(models.Model):
    # title, desc,  image, price
    title = models.CharField('Name', max_length=120)
    desc = models.TextField('Description')
    image = models.ImageField('image', default='default.png', upload_to='home_images')
    price = models.CharField('Price', max_length=120)

    def __str__(self):
        return self.title



