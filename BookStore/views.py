from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from BookStore.models import Author, City, Category, Book


# Create your views here.
@never_cache
def home(request):
    return render(request, 'home.html')

@login_required
@never_cache
def add_author(request):
    if request.method == 'GET':
        cities = City.objects.all()
        data = {"cities": cities}
        return render(request, 'addauthor.html', data)

    else:
        a = Author()
        a.AuthorName = request.POST['auth_name']
        a.AuthorDob = request.POST['auth_dob']
        a.AuthorGender = request.POST['ddlgender']
        a.AuthorEmail = request.POST['auth_email']
        a.AuthorPhone = request.POST['auth_phone']
        a.AuthorCity = City.objects.get(CityName=request.POST['ddlcity'])
        a.save()
        return redirect('displayauthor')

@login_required
@never_cache
def display_author(request):
    authors = Author.objects.all()
    data1 = {"authors": authors}
    return render(request, "displayauthor.html", data1)

@login_required
@never_cache
def delete_author(request, id):
    a = Author.objects.get(id=id)
    a.delete()
    return redirect('displayauthor')

@login_required
@never_cache
def edit_author(request, id):
    author = Author.objects.get(id=id)
    cities = City.objects.all()
    if request.method == "GET":
        data3 = {'author': author, 'city': cities}
        return render(request, 'editauthor.html', data3)
    else:
        author.AuthorName = request.POST['auth_name']
        author.AuthorDob = request.POST['auth_dob']
        author.AuthorGender = request.POST['ddlgender']
        author.AuthorEmail = request.POST['auth_email']
        author.AuthorPhone = request.POST['auth_phone']
        author.AuthorCity = City.objects.get(CityName=request.POST['ddlcity'])
        author.save()
        return redirect('displayauthor')

@login_required
@never_cache
def add_book(request):
    if request.method == 'GET':
        author = Author.objects.all()
        categories = Category.objects.all()
        data = {"authors": author,'categories':categories}
        return render(request, 'addbook.html', data)

    else:
        books = Book()
        books.BookName = request.POST['bookname']
        books.BookDescription = request.POST['bookdesc']
        books.BookPublishedOn = request.POST['bookpub']
        books.BookPrice = request.POST['bookprice']
        books.BookAuthor = Author.objects.get(AuthorName=request.POST['book_author'])
        books.BookCategory = Category.objects.get(CategoryName=request.POST['book_category'])
        books.save()
        return redirect('displaybook')

@login_required
@never_cache
def display_book(request):
    books = Book.objects.all()
    data = {'books':books}
    return render(request,'displaybook.html',data)

@login_required
@never_cache
def edit_book(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all()
    categories = Category.objects.all()
    data = {"book": book, "authors": authors, "categories": categories}

    if request.method == "GET":
        return render(request, 'editbook.html', data)
    elif request.method == "POST":
        # Update the existing book object
        book.BookName = request.POST['bookname']
        book.BookDescription = request.POST['bookdesc']
        book.BookPublishedOn = request.POST['bookpub']
        book.BookPrice = request.POST['bookprice']
        book.BookAuthor = Author.objects.get(id=request.POST['book_author'])
        book.BookCategory = Category.objects.get(id=request.POST['book_category'])
        book.save()
        return redirect('displaybook')

@login_required
@never_cache
def delete_book(request, id):
    a = Book.objects.get(id=id)
    a.delete()
    return redirect('displaybook')


@never_cache
def login_fun(request):
    if request.method == 'GET':
        return render(request, "login.html")

    else:
        uname = request.POST["tbusername"]
        pword = request.POST["tbpass1"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(request, user)
            request.session['name'] = user.username
            return redirect("home")
        else:
            return redirect("login")


@never_cache
def register_fun(request):
    if request.method == 'GET':
        return render(request, "register.html")

    else:
        p1 = request.POST["tbpass1"]
        p2 = request.POST["tbpass2"]
        un = request.POST["tbusername"]
        em = request.POST["tbemail"]
        if p1 == p2:
            u = User.objects.create_superuser(un, em, p1)
            u.save()
            return redirect("login")
        else:
            return redirect('register')



@never_cache
def logout_fun(request):
    del request.session['name']
    logout(request)
    return redirect("login")