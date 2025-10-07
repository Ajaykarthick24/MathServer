from django.shortcuts import render 
def calculate_bmi(request): 
    context={} 
    context['BMI'] = "0" 
    context['w'] = "0" 
    context['h'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        w = request.POST.get('weight','0')
        h = request.POST.get('height','0')
        print('request=',request) 
        print('weight=',w) 
        print('height=',h) 
        BMI = (int(w))/int(h) * int(h) 
        context['bmi'] = BMI 
        context['w'] = w
        context['h'] = h
        print('BMI=',BMI) 
    return render(request,'mathapp/math.html',context)
