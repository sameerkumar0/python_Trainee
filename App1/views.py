from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

## Function based view

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# List all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# Show book details
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

# Create a new book
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book-list')

    return render(request, 'books/book_form.html')

# Update an existing book
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book-list')

    return render(request, 'books/book_form.html', {'book': book})

# Delete a book
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book-list')

    return render(request, 'books/book_confirm_delete.html', {'book': book})



# user registration




# Registration View
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)
        return redirect("book-list")  # Redirect to book list after successful registration

    return render(request, "registration/register.html")

# Login View
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("book-list")  # Redirect to book list after login
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "registration/login.html")

# Logout View
def logout(request):
    logout(request)
    return redirect("login")
