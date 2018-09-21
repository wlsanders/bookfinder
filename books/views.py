from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Books
from django.utils import timezone


# Create your views here.
def home(request):
    books = Books.objects
    return render(request, 'books/home.html', {'books':books})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['amazon_link'] and request.FILES['image']:
            books = Books()
            
            books.title = request.POST['title']
            books.body = request.POST['body']
            if request.POST['amazon_link'].startswith('http://') or request.POST['amazon_link'].startswith('https://'):
                books.amazon_link = request.POST['amazon_link']
            else:
                books.amazon_link = 'http://' + request.POST['amazon_link']
            #books.icon = request.FILES['icon']
            books.image = request.FILES['image']
            books.tagged = request.POST['tag']
            #books.pub_date = timezone.datetime.now()
            #books.hunter = request.user
            books.save()
            
            return redirect('/books/' + str(books.id))
        else:
            return render(request, 'books/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'books/create.html')



def detail(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    return render(request, 'books/detail.html', {'book':book})

@login_required(login_url="/accounts/signup")
def upvote(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Books, pk=book_id)
        book.votes_total += 1
        book.save()
        return redirect('/books/' + str(book.id))

## Need to setup a keyword / tag search 