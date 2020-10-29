from django.shortcuts import render
import json
import requests
# Create your views here.

def id_index(request):
    resp = requests.get('http://127.0.0.1:8000/api/id/')
    data = resp.json()
    lidi = []
    for da in data:
        print(len(da['values']))
        di={'filled':False, 'partially_filled':False, 'trigger':da['invalid_trigger'], 
        'parameters':{}}
        li=[]
        st=''
        val = da['values']
        if da['support_multiple']==True:
            for i in range(len(val)):
                if val[i]['entity_name']==da['type1'][0]:
                    for d in da['support_values']:
                            if(d==val[i]['value']):
                                    li.append(d)  
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

def age_index(request):
    resp = requests.get('http://127.0.0.1:8000/api/age/')
    data = resp.json()
    lidi = []

    for da in data:
        print(len(da['values']))
        di={'filled':False, 'partially_filled':False, 'trigger':da['invalid_trigger'], 
        'parameters':{}}
        li=[]
        st=''
        val = da['values']
        if da['support_multiple']==True:
            for i in range(len(val)):
                if val[i]['entity_type']==da['type1'][0]:
                    exec("%s = %d" % (da['var_name'],val[i]['value']))
                    if(eval(da['constraint'])):
                        li.append(val[i]['value'])  
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