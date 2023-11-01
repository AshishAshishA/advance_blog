from django import forms

class AuthenForm(forms.Form):
    author=forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"user_name"})
    )
    password=forms.CharField(
        min_length=8,
        max_length=15,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"password"})
    )
    confirm_password=forms.CharField(
        min_length=8,
        max_length=15,
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"password_confirm"})
    )

class CommentForm(forms.Form):
    author=forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={"class":"form-control1","placeholder":"your name"})
    )
    body=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control1","placeholder":"Leave your comment!"})
    )
    
class PostForm(forms.Form):
    title=forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class":"form-control2","placeholder":"Post Title"}),
    )
    body=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control2","placeholder":"Create Your Post"}),
    )