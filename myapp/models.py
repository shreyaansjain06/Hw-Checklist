from django.db import models

# Default value for color attributes
DEFAULT_COLOR = 'white'

class Item(models.Model):
    click_count = models.IntegerField(default=0)
    c1_color = models.CharField(max_length=20, default=DEFAULT_COLOR)

    c2_color = models.CharField(max_length=20, default=DEFAULT_COLOR)

    c3_color = models.CharField(max_length=20, default=DEFAULT_COLOR)


    def __str__(self):
        return f"Item(c1_color={self.c1_color})"

class Student(models.Model):
    name = models.CharField(max_length=100)
    
    Gr = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Gr")
    ELA = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="ELA")
    Math = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Math")
    Reading = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Reading")
    Sci = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Sci")
    S_S = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="S_S")
    Computer = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Computer")
    Test = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Test")
    Language = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Language")
    Other = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="Other")

    def __str__(self):
        return self.name
