from django.db import models



# Create your models here.
class Veterinarian(models.Model):
    """Model definition for Veterinarian."""

    full_name = models.CharField('Full Name', max_length=50)
    designation = models.CharField('Designation', max_length=50)
    short_bio = models.TextField()
    picture = models.ImageField('Profile Picture', upload_to='veterinarians/')
    facebook = models.URLField('Facebook Profile', default='https://www.google.com/', max_length=200)
    twitter = models.URLField('Twitter Profile', default='https://www.google.com/', max_length=200)
    google = models.URLField('Google Plus', default='https://www.google.com/', max_length=200)
    instagram = models.URLField('Instagram Profile', default='https://www.google.com/', max_length=200)

    class Meta:
        """Meta definition for Veterinarian."""

        verbose_name = 'Veterinarian'
        verbose_name_plural = 'Veterinarians'

    def __str__(self):
        """Unicode representation of Veterinarian."""
        return self.full_name
