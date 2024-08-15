from django.db import models

class Reservation(models.Model):
    PERSON_CHOICES = [(i, str(i)) for i in range(1, 21)]  # Example: 1-20 persons
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner')
    ]
    meal = models.CharField(max_length=10, choices=MEAL_CHOICES)

    number_of_person = models.IntegerField(choices=PERSON_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.full_name} - {self.date} at {self.time}"
