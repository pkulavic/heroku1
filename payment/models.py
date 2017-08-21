from django.db import models
from tutorprofile.models import TutorProfile
class StripeCustomer(models.Model):
    customer_id = models.CharField(max_length=120)
    customer_email = models.CharField(max_length=120)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_email
