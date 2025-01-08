from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from .models import Books,Author
from .forms import BookForm,AuthorForm
# Create your views here.



def createBook(request):

    books=Books.objects.all()

    if request.method=='POST':
        form=BookForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=BookForm()

    return render(request,'admin/book.html',{'form':form,'books':books})



def create_Author(request):

    if request.method=='POST':
        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('booklist')
    else:
        form=AuthorForm()

    return render(request,'admin/author.html',{'form':form})




def listBook(request):

    books=Books.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)



    return  render(request,'admin/list.html',{'books':books,'page':page})




def detailsview(request,book_id):

    book=Books.objects.get(id=book_id)

    return render(request,"admin/detail.html",{'book':book})




def UpdateBook(request,book_id):

    book=Books.objects.get(id=book_id)

    if request.method=='POST':
        form = BookForm(request.POST,files=request.FILES,instance=book)

        if form.is_valid():
            form.save()

            return redirect('booklist')
    else:
        form=BookForm(instance=book)

    return render(request,'admin/update.html',{'form':form})




def deleteview(request,book_id):

    book=Books.objects.get(id=book_id)

    if request.method=='POST':
        book.delete()

        return  redirect('booklist')

    return  render(request,'admin/delete.html',{'book':book})




def index(request):
    return render(request,'admin/index.html')




def Search_Book(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Books.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admin/search_book.html',context)









