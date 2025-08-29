from django.core.validators import MinValueValidator
from django.db import models



class Tranzit(models.Model):
    title = models.CharField(max_length=255)
    amount = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    type = models.CharField(choices=(
            ('Income', 'Income'),
            ('Expense', 'Expense')
        )
    )
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
