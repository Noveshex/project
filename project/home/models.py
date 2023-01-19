from django.db import models


class Product(models.Model):
    # slug, title, desc,  image, price
    slug = models.SlugField('Product')
    title = models.CharField('Model of Product', max_length=120)
    desc = models.TextField('Description')
    image = models.ImageField('image', default='default.png', upload_to='home_images')
    price = models.CharField('Price', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'





