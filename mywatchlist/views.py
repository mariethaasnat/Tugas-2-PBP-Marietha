from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_watchlist = WatchlistItem.objects.all()
    watched_movies = WatchlistItem.objects.filter(watched = True).count()
    unwatched_movies = WatchlistItem.objects.filter(watched = False).count()

    if watched_movies >= unwatched_movies :
        bonus_text = "Selamat, kamu sudah banyak menonton!"
    else :
        bonus_text = "Wah, kamu masih sedikit menonton!"

    context = {
        'movie_watchlist': data_watchlist,
        'Nama': 'Marietha Asnat Nauli Sitompul',
        'ID': '2106752413',
        'bonus_text' : bonus_text
    }
    return render(request, "mywatchlist.html", context)

def show_xml (request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json (request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id (request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id (request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")