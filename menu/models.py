from django.db import models


class MenuOrder(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    rate = models.CharField(max_length=50)

    def __str__(self):
        return self.event_name


class MenuSection(models.Model):
    menu_order = models.ForeignKey(
        MenuOrder,
        on_delete=models.CASCADE,
        related_name="sections"
    )

    category = models.CharField(max_length=100)
    items = models.TextField()

    def get_items(self):
        return [
            item.strip()
            for item in self.items.split("\n")
            if item.strip()
        ]