from django.shortcuts import render
from django.http import HttpResponse
from eng.models import Book

def index(request):
    return HttpResponse(" This is my Maths Index page: ")
def home(request):
    return render(request, "eng/home.html", {})
def booksmenu(request):
    books = Book()
    books.save()
    res  = Book.objects.all()
    return render(request, "eng/booksmenu.html", {"book_list":res})
def newbooks(request):
    return render(request, "eng/newbooks.html", {})
def SaveBook(request):
    if request.method =="POST":
        if request.POST["id"]==" ":
            books=Book(title=request.POST['Title'], author=request.POST['Author'], edition=request.POST['Edition'], publication=request.POST['Publication'])
            books.save()
        elif request.POST["id"]!=" ":
            bookdb=getbook(int(request.POST["id"]))
            bookdb.ISBN = request.POST["title"]
            bookdb.save()
    else:
        print("cant save the book, save properly:")
    return booksmenu(request)
def getbook(id):
    booklist = Book.objects.filter(id=id)
    book=Book()
    for x in booklist:
        book=x
        break
    return book
def edit(request,isbn):
    return render(request,"eng/edit.html", {})