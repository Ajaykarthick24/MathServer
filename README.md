# Ex.05 Design a Website for Server Side Processing
## Date:07/10/2025

## AIM:
 To design a website to calculate the Body Mass Index (BMI) in the server side.


## FORMULA:
BMI= W/H2
BMI --> Body Mass Index
 W --> Weight
 H --> Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html
<html>
    <head>
        <title>BMI Calculator</title>
        <style>
        body{
          background-color:gold;
          border-top: 30;
        }
        .m{
          background-color: slateblue;
          border-style: linear;
          margin-top: 400px;
          margin-left: 400px;
          margin-right: 400px;
          
        }
            .main{
                font-size: 300%;
                text-align: center;
                background-color: silver;
                 margin-left: 100px;
                  margin-right: 100px;
                  padding: 100px;
                  
                  
            }
            .a{
                font-size: 200%;
                text-align: center;
                background-color: silver;
                 margin-left: 100px;
                  margin-right: 100px;
                
                 
            }
            form{
              text-align: center;
              background-color: silver;
               margin-left: 100px;
             margin-right: 100px;
             padding: 100px;
            }
           
        </style>
    </head>
    <body>

       <div class="m">
        <div class="main">BMI CALCULATOR</div>
        <div class="a">
         Ajay karthick M(25010418)</div>
        <form method="post">
          {% csrf_token %}
           
           
            <label>Weight(kg)=</label>
            <input type="text" name="weight" value="{{w}}"><br><br>
             <label>Height(cm)=</label>
            <input type="text" name="height" value="{{h}}"><br><br>
            <button type="submit">Calculate</button><br><br>
            <label>BMI=</label>
            <input type="text" name="bmi" value="{{bmi}}">
        </div>
        </form>
        
        
    </body>
</html>

viwes.py

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

urls.py

from django.contrib import admin
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('bmi/',views.calculate_bmi,name="bmi"),
    path('',views.calculate_bmi,name="bmicalculator")
]
```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-10-07 085123.png>)

## HOMEPAGE:

![alt text](<Screenshot 2025-10-07 085143.png>)
## RESULT:
The program for performing server side processing is completed successfully.
