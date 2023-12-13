from django.shortcuts import render
import random
# Подключить js script от bootstrap как статический файл
def example(request):
    return render(request, 'core/index.html')
    
def reg(request):
    return render(request, 'core/reg.html')
    
def magic_number(request):
    if request.method == 'POST':
        if int(request.POST['number'])==random.randint(0, 3):
            return render(request, 'core/magic_number.html', {'result1':'win'})
        else:
            return render(request, 'core/magic_number.html', {'result1':'lose'})
    else:
        return render(request,'core/magic_number.html') 


