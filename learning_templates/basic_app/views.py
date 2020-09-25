from django.shortcuts import render

# Create your views here.
def index(request):
    # Con esto introducimos filtro (después lo incluimos en index.html).
    context_dict = {'text':'hello world', 'number':100}
    return render(request, "basic_app/index.html", context_dict)
    # return render(request, "index.html")

def other(request):
    return render(request, "basic_app/other.html")
    # return render(request, "other.html")

def relative(request):
    return render(request, "basic_app/relative_url_templates.html")
    # return render(request, "relative_url_templates.html")