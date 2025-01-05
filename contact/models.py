from django.db import models


class ContactRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    customer_feedback = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name} - {self.email}"
