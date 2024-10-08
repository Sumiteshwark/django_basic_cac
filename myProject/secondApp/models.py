from django.db import models
from django.utils import timezone

class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
  description = models.TextField(default="")

  def __str__(self):
    return self.name  # To display name in admin panel, by default it is like <ChaiVariety: ChaiVariety object (1)>