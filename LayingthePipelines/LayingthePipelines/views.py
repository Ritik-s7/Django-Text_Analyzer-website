from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """return HttpResponse("<h1> Home </h1>\n <h6> <a href = 'http://127.0.0.1:8000/removePunc'> Remove punctuation </a> </h6> \n "
                        "<h6> <a href = "
                        "'http://127.0.0.1:8000/capitalizefirst'> Capitalize first letter </a> </h6> \n <h6> <a href "
                        "= 'http://127.0.0.1:8000/newlineremove'> Remove New Line </a> </h6> \n <h6> <a href = "
                        "'http://127.0.0.1:8000/spaceremove'> Remove Space </a> </h6> \n <h6> <a href = "
                        "'http://127.0.0.1:8000/charcount'> Count Characters </a> </h6>")
    """
    return render(request, 'index.html')


def analyze(request):
    # Get the Text
    djangoText = request.GET.get('text', 'default')

    # Check the checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    CapitalAll = request.GET.get('CapitalAll', 'off')
    newLineRemover = request.GET.get('newLineRemover','off')
    charcounter = request.GET.get('charcounter','off')
    extraSpaceRemover = request.GET.get('extraSpaceRemover','off')

    analyzed = djangoText

    # Remove Punctuations
    if removepunc == "on":
        analyzed = ""
        punctuations = '''[]{}-!@#$%&*()-_\|'";:/?.,<>'''
        for char in djangoText:
            if char not in punctuations:
                analyzed += char
        if CapitalAll == 'on':
            analyzed2 = ""
            for char in analyzed:
                analyzed2 += char.capitalize()
            params = {'purpose': 'Removed Punctuations and  Capitalized Text', 'analyzed_text': analyzed2}
            return render(request, 'analyze.html', params)
        else:
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)

    # Capitalizing First letter
    if CapitalAll == 'on':
        analyzed2 = ""
        for char in analyzed:
            analyzed2 += char.capitalize()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed2}
        return render(request, 'analyze.html', params)

    # Remove New Lines

    elif newLineRemover == 'on':
        analyzed = ""
        for char in djangoText:
            if char is not "\n":
                analyzed += char
        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # Count total characters

    elif charcounter == 'on':
        count = 0
        for char in djangoText:
            count+=1
        params = {'purpose': 'Total number of characters', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    # Remove Extra Spaces

    elif extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djangoText):
            if not(djangoText[index] == " " and djangoText[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")


# def capfirst(request):
#   return HttpResponse("Capitalize First letter \n <h6> <a href = 'http://127.0.0.1:8000/'> BACK </a> </h6>")
'''
def newlineremove(request):
    return HttpResponse("Remove Newline \n <h6> <a href = 'http://127.0.0.1:8000/'> BACK </a> </h6>")
def spaceremove(request):
    return HttpResponse("Remove space \n <h6> <a href = 'http://127.0.0.1:8000/'> BACK </a> </h6>")
def charcount(request):
    return HttpResponse("Count characters \n <h6> <a href = 'http://127.0.0.1:8000/'> BACK </a> </h6>")

'''
