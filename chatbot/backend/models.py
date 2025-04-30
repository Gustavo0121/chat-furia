"""Models."""

from django.db import models


class Message(models.Model):
    """Message."""

    SENDER_CHOICES = [
        ('user', 'User'),
        ('bot', 'Bot'),
    ]

    content = models.TextField()
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta."""

        ordering = ['timestamp']

    def __str__(self):
        """__Str__."""
        return f'{self.sender}: {self.content[:50]}'
