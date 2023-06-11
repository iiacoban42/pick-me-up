"""API request handling. Map requests to the corresponding HTMLs."""
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render

from .recommender import blend_playlist, find_youtube_urls_of_spotify_playlist


def home(request):
    """Render index.html page"""
    ren = render(request, "home/index.html")
    return ren


def recommend_chitchat_music(context=None):
    """Recommend chitchat background playlist"""
    lofi_girl_live = "https://www.youtube.com/watch?v=jfKfPfyJRdk"

    return {"url": lofi_girl_live}


def recommend_study_music(context=None):
    """Recommend study background playlist"""
    lofi_girl_live = "https://www.youtube.com/watch?v=jfKfPfyJRdk"

    return {"url": lofi_girl_live}


def recommend_gaming_music(context=None):
    """Recommend gaming background playlist"""

    gaming_lofi = "https://www.youtube.com/watch?v=FFfdyV8gnWk"
    fps_tactical_music =  "https://www.youtube.com/watch?v=bNZH3pQjClU"
    match context:
        case "fps":
            return {"url": fps_tactical_music}
        case "party":
            return {"url": gaming_lofi}
        case _:
            return {"url": gaming_lofi}


def get_new_track(request, activity, context=None):
    """Recommend gaming background playlist"""
    match activity:
        case "just chatting":
            return  JsonResponse(recommend_chitchat_music(context))
        case "studying":
            return  JsonResponse(recommend_study_music(context))
        case "gaming":
            return  JsonResponse(recommend_gaming_music(context))
        case _:
            return HttpResponseBadRequest()


def get_new_playlist(request, context, preferences):
    blend = blend_playlist(context, preferences, intersect=True)
    yt_urls = find_youtube_urls_of_spotify_playlist(blend)
    
    return JsonResponse({"urls": yt_urls})
