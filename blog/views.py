from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .models import Post,Comment,Category,Authen
from .forms import CommentForm,PostForm,AuthenForm
from django.views.generic import DeleteView
from django.urls import reverse



def login_signup(request):
    return render(request,"blog/login_signup.html",{})



def signup(request):
    form=AuthenForm()
    if request.method=="POST":
        form=AuthenForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data["author"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if(password==confirm_password):
                new_user=Authen(
                    author=author,
                    password=password,
                )
                new_user.save()
                return HttpResponseRedirect(reverse('blog-index',kwargs={'pk': new_user.id}))
            else:
                return render(request,"blog/signup_error.html",{"message":"Password doesn't match"})
        else:
            return render(request, "blog/signup.html", {"form": form, "title": "SIGN UP"})
    else:
        return render(request, "blog/signup.html", {"form": form, "title": "SIGN UP"})




def login(request):
    if request.method=='POST':
        authori=request.POST.get('user-name','')
        password=request.POST.get('password','')
        
        detail=get_object_or_404(Authen,author=authori)
        
        if password==detail.password:
            return HttpResponseRedirect(reverse('blog-index',kwargs={'pk': detail.id}))
        else:
            return render(request,'blog/login_error.html',{"message":"Either UserName or Password is wrong"})
    context={
        "title":"LOG IN"
    }
    return render(request,"blog/login.html",context)





def blog_index(request,pk):
    posts=Post.objects.all().order_by("-created_on")
    context={
        "posts":posts,
        "authen_id":pk,
    }
    return render(request,"blog/index.html",context)






def blog_category(request,category):
    posts=Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context={
        "posts":posts,
        "category":category,
    }
    return render(request,"blog/category.html",context)





def blog_detail(request,pk):
    post=Post.objects.get(pk=pk)
    author_i=Authen.objects.get(post=post)                   #changes
    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    
    comments=Comment.objects.filter(post=post)
    context={
        "authori":author_i,
        "post":post,
        "comments":comments,
        "form":form,
    }
    return render(request,"blog/detail.html",context)




def create_post(request,pk):
    category1=Category.objects.get(pk=2)
    auther=Authen.objects.get(pk=pk)
    form=PostForm()
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=Post(                                      #change removed author
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
                authen=auther,
            )
            post.save()
            post.categories.add(category1)
            return HttpResponseRedirect(request.path_info)
    context={
        "form":form,
        "categories":category1,
    }
    return render(request,'blog/create_post.html',context)




def blog_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    authen=Authen.objects.get(post=post)
    
    if request.method=='POST':
        password=request.POST.get('password','')
        
        if password==authen.password:
            post.delete()
            return HttpResponseRedirect(reverse('blog-index',kwargs={"pk":authen.id}))
        else:
            return render(request,'blog/delete_error.html',{"message":"password doesn't matched:Deletion failed"})
    return render(request,'blog/post_confirm_delete.html',{"post":post})     
