from django.http import HttpResponse
from django.shortcuts import render
import operator

def home (Request):
    return render(Request, 'home.html')

def count(Request):
    fulltext = Request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary ={}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else :
            #add to dictionary
            worddictionary[word] = 1

            sortedword = sorted (worddictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(Request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedword':sortedword})

def about (Request):
    return render(Request,'about.html')
