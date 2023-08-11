# I have created this file - Hrithik


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    #return  HttpResponse("Home")
def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        #Analyze the text
        pucntuations = '''!()-[]{}:;'"\,<>./^?@#&$%*_~'''
        analyzed=""
        for char in djtext:
            if char not in pucntuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Pucntuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'UpperCase', 'analyzed_text':analyzed}
        djtext = analyzed

    if (removenewline == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Newline Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]=="  "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'Total characters', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and removenewline != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Error! Please check the checkbox")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request,'about.html')


