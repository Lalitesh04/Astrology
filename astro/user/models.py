from django.db import models

gender_choices = {
    ('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')
}


# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(blank=False, choices=gender_choices, max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    contact = models.BigIntegerField(blank=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "register_table"

    def __str__(self):
        return f"{self.name}"


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    feedback = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,unique=True,blank=False)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=20, unique=True, blank=False)

    class Meta:
        db_table = "Admin_table"

    def __str__(self):
        return f"{self.username}"
