from django.forms import ModelForm
from .models import Contact,Comment



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","phone_number","description"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["first_name","text"]
