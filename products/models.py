from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    category_id = models.IntegerField(primary_key=True,unique=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    sub_category_id = models.IntegerField(primary_key=True,unique=True)
    
    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    sub_category = models.ManyToManyField(SubCategory)
    price = models.DecimalField(null=False,max_digits=10,decimal_places=2)
    currency = models.CharField(max_length=3)
    in_stock = models.BooleanField(default=True)
    stock_left = models.IntegerField()
    slug = models.SlugField(unique=True,max_length=100,null=True)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    
    
    
