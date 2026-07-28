from django.db import models

PROPERTY_TYPES = [
    ('Apartment', 'Apartment'),
    ('House', 'House'),
    ('Land', 'Land'),
]


class Property(models.Model):
    TRANSACTION_TYPES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]

    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=200)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES, default='Apartment')

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        default='sale',
        verbose_name="Transaction Type"
    )

    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.price} EUR"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/gallery/')

    def __str__(self):
        return f"Image for {self.property.title}"
        
