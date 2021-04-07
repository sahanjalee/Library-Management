from django.urls import path
from .views import allbooks,search,addbook,deletebook,issuerequest,myissues,issue_book,return_book,requestedissues,myfines,allfines,deletefine
urlpatterns = [
    path('',allbooks,name='home'),
    path('search/',search),
    path('addbook/',addbook),
    path('deletebook/<int:bookID>/',deletebook),
    path('request-book-issue/<int:bookID>/',issuerequest),
    path('my-issues/',myissues),
    path('my-fines/',myfines),
    path('all-issues/',requestedissues),
    path('all-fines/',allfines),
    path('issuebook/<int:issueID>/',issue_book),
    path('returnbook/<int:issueID>/',return_book),
    path('delete-fine/<int:fineID>/',deletefine),
]
