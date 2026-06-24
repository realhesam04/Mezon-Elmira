from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_products", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['title']
    
    

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    inventory = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='covers/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    
    class Meta:
        ordering = ['-created_at']

class ProductPicture(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f"{self.product.title}"
