from django.shortcuts import render
import json
import requests
# Create your views here.


# for viewing the validation for ID Api
def id_index(request):
    resp = requests.get('http://127.0.0.1:8000/api/id/')
    data = resp.json()
    lidi = []
    
    # looping for the data came from the API and creating the validation response based on the inputs received in API.
    for da in data:
        print(len(da['values']))
        di={'filled':False, 'partially_filled':False, 'trigger':da['invalid_trigger'], 
        'parameters':{}}    # Initialization of Dictionary which will be further appended for the response parameters
        li=[]
        val = da['values']
        
        # Creation for the valid response when the multiple values are allowed
        if da['support_multiple']==True:
            for i in range(len(val)):
                if val[i]['entity_name']==da['type1'][0]:
                    for d in da['support_values']:
                            if(d==val[i]['value']):
                                    li.append(d)  
            # creating the valid dictionary based on the values feild in the JSON response                        
            if len(li)==0:
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':{}}

            elif len(li)<len(val):
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':{}}

            else:
                di= {'filled':True, 'partially_filled':False, 'trigger':'', 
                'parameters':{da['key']: li}} 
            lidi.append(di)    

        # Creation for the valid response when the multiple values are not allowed an donly first one has to be picked    
        elif da['pick_first']==True: 
            for i in range(len(val)):
                if val[i]['entity_name']==da['type1'][0]:
                    for d in da['support_values']:
                            if(d==val[i]['value']):
                                    li.append(d)  
            if len(li)==0:
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':''}

            elif len(li)<len(val) and li[0]!=val[0]['value']:
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':''}

            else:
                di= {'filled':True, 'partially_filled':False, 'trigger':'', 
                'parameters':{da['key']: li[0]}} 
            lidi.append(di)
        print(di)
    return render(request, 'id/index.html', {'list': lidi})



# for viewing the validation for Age Api
def age_index(request):
    resp = requests.get('http://127.0.0.1:8000/api/age/')
    data = resp.json()
    lidi = []
    
    # looping for the data came from the API and creating the validation response based on the inputs received in API.
    for da in data:
        print(len(da['values']))
        di={'filled':False, 'partially_filled':False, 'trigger':da['invalid_trigger'], 
        'parameters':{}}   # Initialization of Dictionary which will be further appended for the response parameters
        li=[]
        val = da['values']
        
         # Creation for the valid response when the multiple values are allowed
        if da['support_multiple']==True:
            for i in range(len(val)):
                if val[i]['entity_type']==da['type1'][0]:
                    exec("%s = %d" % (da['var_name'],val[i]['value']))
                    if(eval(da['constraint'])):
                        li.append(val[i]['value'])  
                        
                # creating the valid dictionary based on the values feild in the JSON response 
                if len(li)==0:
                    di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                    'parameters':{}}

                elif len(li)<len(val):
                    di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                    'parameters': {da['key']: li}}

                else:
                    di= {'filled':True, 'partially_filled':False, 'trigger':'', 
                    'parameters':{da['key']: li}} 
            lidi.append(di)    
    
        # Creation for the valid response when the multiple values are not allowed an donly first one has to be picked    
        elif da['pick_first']==True: 
            for i in range(len(val)):
                if val[i]['entity_type']==da['type1'][0]:
                    exec("%s = %d" % (da['var_name'],val[i]['value']))
                    if(eval(da['constraint'])):
                        li.append(val[i]['value'])
            if len(li)==0:
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':''}

            elif len(li)<len(val) and li[0]!=val[0]['value']:
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':''}
            elif len(li)<len(val) and li[0]==val[0]['value']:
                di= {'filled':False, 'partially_filled':True, 'trigger':da['invalid_trigger'], 
                'parameters':{da['key']: li[0]}}
            else:
                di= {'filled':True, 'partially_filled':False, 'trigger':'', 
                'parameters':{da['key']: li[0]}} 
            lidi.append(di)
        print(di)
    return render(request, 'age/index.html', {'list': lidi})    
