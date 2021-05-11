from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')

def analyze(request):
    # Get the Text
    djangoText = request.POST.get('text', 'default')

    # Check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    CapitalAll = request.POST.get('CapitalAll', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')

    analyzed = "Please choose atleast one option on previous page"
    params = {'purpose': 'ERROR', 'analyzed_text': analyzed}

    # Remove Punctuations
    if removepunc == "on":
        analyzed = ""
        punctuations = '''[]{}-!@#$%&*()-_\|'";:/?.,<>'''
        for char in djangoText:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djangoText = analyzed

    # Capitalizing First letter
    if CapitalAll == 'on':
        analyzed = ""
        for char in djangoText:
            analyzed += char.capitalize()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        djangoText = analyzed

    # Remove New Lines

    if newLineRemover == 'on':
        analyzed = ""
        for char in djangoText:
            if char is not "\n" and char is not "\r":
                analyzed += char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        djangoText = analyzed

    # Count total characters

    elif charcounter == 'on':
        count = 0
        for char in djangoText:
            count += 1
        counter = {'purpose': 'Total number of characters', 'analyzed_text': f"Total number of characters : {count}"}
        return render(request, 'analyze.html', counter)

    # Remove Extra Spaces

    if extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djangoText):
            if not (djangoText[index] == " " and djangoText[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}


    return render(request, 'analyze.html', params)


def ContactUs(request):
    return render(request,"ContactUs.html")
