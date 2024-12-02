from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Article/image")
    create_data = models.DateTimeField(auto_now=True)
    blog_link = models.URLField(blank=True, null=True)
    def __str__(self) -> str:
        return f"{self.title}"


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url_GitHub = models.URLField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Portfolio/image")
    create_data = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Faqat yangi yozuvlar uchun
            last_portfolio = Portfolio.objects.filter(author=self.author).last()
            self.id = (last_portfolio.id + 1) if last_portfolio else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    def __str__(self) -> str:
        return f"{self.title}"

class Comment(models.Model):
    first_name = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
