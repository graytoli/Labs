from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import LongURL
import random

letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_code():
    code = []
    for i in range(8):
        character = random.choice(letter) + str(random.randint(0, 9))
        code.insert(random.randint(0, len(code)), random.choice(character))
    return ''.join(code)

def index(request):
    if request.method == 'POST':
        long_url = LongURL()
        long_url.url = request.POST['url']
        long_url.code = generate_code()
        long_url.save()
        return render(request, "info.html", {"long_url": long_url})
    return render(request, "redirector.html")

def redirect(request, code):
    long_url = LongURL.objects.get(code=code)
    return HttpResponseRedirect(long_url.url)


