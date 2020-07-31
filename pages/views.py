from django.shortcuts import render
from .apps import PagesConfig

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def result(request):
    # if request.method == 'GET':
    ssc_p = request.GET.get('ssc_p')
    hsc_p = request.GET.get('hsc_p')
    degree_p = request.GET.get('degree_p')
    etest_p = request.GET.get('etest_p')
    mba_p = request.GET.get('mba_p')    
    workex = PagesConfig.work_encoder.transform([request.GET.get('workex')])[0]
    specialisation = PagesConfig.spec_encoder.transform([request.GET.get('specialisation')])[0]
    degree_t = PagesConfig.deg_encoder.transform([request.GET.get('degree_t')])[0]
    gender = PagesConfig.gen_encoder.transform([request.GET.get('gender')])[0]
    
    vector = [[gender, ssc_p, hsc_p, degree_p, degree_t, workex, etest_p, specialisation, mba_p]]
    result = PagesConfig.classifier.predict(vector)
    var = ''
    if result == 1:
        var = 'Placed'
    else:
        var = 'Not Placed'
    context = {
        'output': var
    }
    return render(request, 'pages/result.html', context)