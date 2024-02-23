from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator, EmailValidator


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Dish Categories'
        ordering = ('position',)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    ingredients = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('position',)
        constraints = [
            models.UniqueConstraint(fields=['position', 'category'], name='unique_position_per_each_category'),
        ]
        unique_together = ['id', 'slug']


class Gallery(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='gallery/')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f'{self.title}'


class FooterItem(models.Model):
    address = RichTextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    working_hours = RichTextField()
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    regex_validator = RegexValidator(
        r'^\+?380\d{9}$',
        'Phone number must be entered in the format: "+380xxxxxxxxx".')
    phone = models.CharField(max_length=255, validators=[regex_validator])
    email_validator = EmailValidator()
    email = models.EmailField(validators=[email_validator])
    date = models.DateField()
    time = models.TimeField()
    people_number = models.PositiveSmallIntegerField()
    message = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)

    is_confirmed = models.BooleanField(default=False)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Chef(models.Model):
    name = models.CharField(max_length=255)
    chef_position = models.TextField(blank=True)
    about = RichTextField()
    photo = models.ImageField(upload_to='chefs/')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Chefs'
        ordering = ('position',)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='events/')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Events'
        ordering = ('position',)

    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    email = models.EmailField()
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    opening_hours_mon_fri = RichTextField()
    opening_hours_sat_sun = RichTextField()
    is_visible = models.BooleanField(default=True)










