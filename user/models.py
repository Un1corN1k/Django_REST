from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    age = models.IntegerField()
    english_level = models.CharField(max_length=2, choices=[('A1', 'Beginner'), ('A2', 'Elementary'),
                                                            ('B1', 'Intermediate'), ('B2', 'Upper Intermediate'),
                                                            ('C1', 'Advanced'), ('C2', 'Proficient')])

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
