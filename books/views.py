from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

# Create your views here.

def search(request):
    # errors = False
    # if 'q' in request.GET and request.GET['q']:
    errors =[]
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            # errors = True
            errors.append('Enter a search item.')
        elif len(q):
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title = q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    # else:
        # return HttpResponse('Please submit a valid search term.')
    return render(request,'search_form.html',{'error':errors})
