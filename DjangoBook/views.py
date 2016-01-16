# if we aren't using templates. it doesn't require template file.

# from django.http import HttpResponse, Http404
# import datetime
#
# # it is not necessary to name this file views.py it is just so that other programmers can read and understand the code easily
#
# #creating the function hello, we can name the arguement anything, but by convention it is called request
# def hello(request):
#     return HttpResponse("Hello World")
#
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html="<html><body>It is now %s.</body><html>"%now
#     return HttpResponse(html)
#
# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#
#     html="<html><body>In %s hours(s), it will be %s. <body><html>" % (offset, dt)
#     return HttpResponse(html)
#

# if we are using templates without render function. it requires template file

# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
# import datetime
#
# def current_datetime(request):
#     now = datetime.datetime.now()
#     t=get_template('current_datetime.html')
#     html = t.render(Context({'current_date':now}))
#     return HttpResponse(html)

# if we are using templates along with render function. it requires template file

from django.http import HttpResponse, Http404
from django.shortcuts import render

import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,'current_datetime.html',{'current_date':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    context = {
            "offset":offset,
            "dt":dt
    }
    return render(request,'time_plus.html',context)

def search_form(request):
    return render(request,'search_form.html')

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r'% request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

#if you want to save form data in the data base, you have to add code something like that, but it is not the actual code

# def addbook(request):
#     form = AuthorForm()
#     book_formset = BookFormset(instance=Author())
#
#     if request.POST:
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             author = form.save()
#             book_formset = BookFormset(request.POST, instance=author)
#             if book_formset.is_valid():
#                 book_formset.save()
#             return redirect('/index/')
#
#     return render_to_response('addbook.html',{
#         'form': form, 'formset': book_formset
#     },context_instance=RequestContext(request))

def display_meta(request):
    values = request.META.items()
    sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))
