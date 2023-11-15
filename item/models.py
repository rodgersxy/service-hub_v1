from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    """
    Represents a category for items in the application.

    Attributes:
        name (str): The name of the category.
    """
    name = models.CharField(max_length=255)

    class Meta:
        """
        Meta class for Category model.

        Attributes:
            ordering (tuple): A tuple specifying the default ordering of categories by name.
            verbose_name_plural (str): A human-readable name for the model in plural form.
        """
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
         Returns a string representation of the Category instance.

        Returns:
            str: A string representation of the category.
        """
        return self.name

class Item(models.Model):
    """
    Represents an item for sale in the application.

    Attributes:
        category (Category): The category to which the item belongs.
        name (str): The name of the item.
        description (str, optional): A description of the item (optional).
        price (float): The price of the item.
        image (ImageField, optional): An image of the item (optional).
        is_sold (bool): Indicates whether the item has been sold.
        created_by (User): The user who created the item.
        created_at (datetime): The date and time when the item was created.
    """
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the Item instance.

        Returns:
            str: A string representation of the item.

        """
        return self.name
