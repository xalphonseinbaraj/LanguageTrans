from django.shortcuts import render, redirect
from django.http import HttpResponse
from textblob import TextBlob
def translator(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        lang = request.POST.get('lang')
        print('text:', text, 'lang:', lang)
        # translate the language
        translator = TextBlob(text)
        #translator.translate(from_lang=)
        # detect the language
        dt = translator.detect_language()
        dt2 = dt
        translated = translator.translate(from_lang=dt,to= lang)
        tr = translated
        content = {
            'translated': tr,'u_lang': dt2,'t_lang':lang
        }
        return render(request,'translator_app/translated.html', content)
    return render(request, 'translator_app/translator.html')


# Create your views here.
def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text:', text, 'lang:', lang)
    #translate the language
    translator= TextBlob(text)

    #detect the language
    dt=translator.detect(text)
    dt2=dt.lang
    translated=translator.translate(text,lang)
    tr=translated.text
    return render(request,'translated.html',{'translated': tr,'u_lang': dt2,'t_lang':lang})