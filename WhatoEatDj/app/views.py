"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

invResult = [
    'egg','milk','rice','tomato'
]
inptDicLst = [
    # 存放一些原始数据
]

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def inventory(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/inventory.html',
        {
            'title':'Inventory',
            'message':'Choose what you have:',
            'year':datetime.now().year,
        }
    )
    
def menu(request):
    assert isinstance(request, HttpRequest)
    if request.POST:
        print('get post from menu')
        check_box_list = request.POST.getlist('check_box_list')
        j = 0
        result = []
        inv =[]
        #print(len(check_box_list))
        for i in range(len(invResult)):
            if invResult[i] == check_box_list[j]:
                #print(invResult[i],'1')
                tempDic = {'inv':invResult[i],'res':'1'}
                inptDicLst.append(tempDic)
                #inv.append(invResult[i])
                #result.append('1')
                if j+1 < len(check_box_list):
                    j += 1
            else:
                tempDic = {'inv':invResult[i],'res':'0'}
                inptDicLst.append(tempDic)
                #print(invResult[i],'0')
                #inv.append(invResult[i])
                #result.append('0')
        #tempDic = {'inv':inv,'res':result}
        #inptDicLst.append(tempDic)
        #text = request.POST.getlist('text',None)
        #print(inptDicLst)
        return render(
        request,
        'app/menu.html',
        {
            'title':'menu',
            'message':'Confirm what you have:',
            'year':datetime.now().year,
            'list': inptDicLst,
        }
    ) 


