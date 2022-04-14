from django.db import models

# Create your models here.

# HOME SECTION
class Home(models.Model):
    name = models.CharField(max_length=30)
    grettings_1 = models.CharField(max_length=50)
    grettings_2 = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='picture/')
    # save time when modefied
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ABOUT SECTION
class About(models.Model):
    heading = models.CharField(max_length=70)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class Profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=200)


# SKILLS SECTION
class Category(models.Model):
    name = models.CharField(max_length=50)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category,
                                    on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)


# PORTFOLIO SECTION
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    

    def __str__(self):
        return f"Portfoilo {self.id}"

# CONTACT
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    review = models.TextField(max_length=2048)   

    def __str__(self):
        return self.name
