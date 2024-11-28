from django.db import models
from django.contrib.auth.models import User  

class Restaurant(models.Model):
    name = models.CharField(max_length=100)  # Restaurant name
    description = models.TextField()  # Restaurant description
    picture = models.URLField()  # URL for the restaurant's picture

    def __str__(self):
        return self.name
    
class Menu_items(models.Model):
    food_name = models.CharField(max_length=100,default="food")  # Food name
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Food price
    description = models.TextField()  # Description of the food item
    picture = models.URLField()  # URL for the food's picture
    restaurant = models.ForeignKey(
        Restaurant, 
        on_delete=models.CASCADE, 
        related_name="menu_items"
    )  # Foreign key linking to Restaurant

    def __str__(self):
        return f"{self.food_name} - {self.restaurant.name}"



class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user placing the order
    menu_item = models.ForeignKey(Menu_items, on_delete=models.CASCADE)  # Link to the menu item being ordered
    address = models.TextField()  # Address for the order
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the item being ordered
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Total price for the order
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the order

    def save(self, *args, **kwargs):
        # Calculate total price based on the quantity and the price of the menu item
        self.price = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return f"Order by {self.user.username} for {self.menu_item.food_name} (x{self.quantity})"