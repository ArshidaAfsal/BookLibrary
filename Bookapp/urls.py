from django.urls import path
from  . import views

urlpatterns = [
    path('createbook',views.createBook,name='createbook'),
    path('author/',views.create_Author,name='author'),
    path('booklist',views.listBook,name="booklist"),
    path('detailview/<int:book_id>/',views.detailsview,name='details'),
    path('updateview/<int:book_id>/',views.UpdateBook,name='update'),
    path('deleteview/<int:book_id>/',views.deleteview,name='delete'),
    path('index',views.index,name='index'),
    path('search/',views.Search_Book,name="search_book"),



]