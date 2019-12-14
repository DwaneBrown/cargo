from django.shortcuts import render,redirect
import datetime as dt
from django.http import HttpResponse,Http404
from .models import Pics

# display todays pics
def pics_of_day(request):
    date = dt.date.today()
    bird = Pics.todays_pics()
    return render(request, 'all-pics/today-pics.html', {"date" : date,"bird":bird})

# display details for pics_of_day
def pics_details(request,pkid):
    try:
        image=Pics.objects.get(id=pkid)
    except DoesNotExist:
        raise Http404()

    return render(request, 'all-pics/today-pics-details.html', {"image":image})


# display pics for past days
def past_days_pics(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(picsToday)

    bird = Pics.days_pics(date)
    return render(request, 'all-pics/past-pics.html', {"date":date,"bird":bird, "title":"Past News"})

# search results 
def search_results(request):
    if 'pics' in request.GET and request.GET["pics"]:
        search_term = request.GET.get("pics")
        searched_pics = Pics.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"pics":searched_pics,"search_term":search_term, "title": "search" })
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message, "title": "search"})

# single pics
def pics(request, pics_id):
    try:
        pics = Pics.objects.get(id = pics_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-pics/pics.html", {"pics":pics})
