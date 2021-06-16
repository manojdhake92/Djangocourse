from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    upper_case = request.POST.get('upper_case', 'off')

    if removepunc == "on":
        analyzed = remove_punctuation(djtext)
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = djtext.strip()
        djtext = analyzed

    if upper_case == 'on':
        analyzed = djtext.upper()
        djtext = analyzed

    if upper_case != 'on' and removepunc != 'on' and extraspaceremover != 'on':
        return HttpResponse("Please select any operation!")
    params = {'analyzed_text': djtext}
    return render(request, 'analyze.html', params)


def remove_punctuation(djtext):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    return analyzed
