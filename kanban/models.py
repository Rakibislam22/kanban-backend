from django.db import models

class Task(models.Model):
    # Defining priority choices for the task
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    # Defining status choices for the Kanban board
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    tags = models.CharField(max_length=255, blank=True, null=True) # Storing tags as a comma-separated string
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title