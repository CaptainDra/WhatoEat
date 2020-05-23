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
    # store some data
]

Cookable = ['you can cook:']
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
        if len(check_box_list) == 0:
            for i in range(len(invResult)):
                tempDic = {'inv':invResult[i],'res':''}
                inptDicLst.append(tempDic)
            return render(
                request,
                'app/menu.html',
                {
                    'title':'menu',
                    'message':'Huh.......Your inventory is empty?',
                    'year':datetime.now().year,
                    'list': inptDicLst,
                }
                )
        for i in range(len(invResult)):
            if invResult[i] == check_box_list[j]:
                tempDic = {'inv':invResult[i],'res':'checked'}
                inptDicLst.append(tempDic)
                if j+1 < len(check_box_list):
                    j += 1
            else:
                tempDic = {'inv':invResult[i],'res':''}
                inptDicLst.append(tempDic)
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
def GetMenu(request):
        assert isinstance(request, HttpRequest)
        if request.POST:
            check_box_list = request.POST.getlist('check_box_list')
            checklist = ['checklist']
            cookable = ['cookable']
            flag = 0
            j = 0
            cookbook =['tomato omelette','1','0','0','1'] #That should be the data from database or come from cache
            if len(check_box_list) == 0:
                return render(
                request,
                'app/GetMenu.html',
                {
                    'title':'Getmenu',
                    'message':'Huh.......How about eat air┓( ´∀` )┏',
                    'year':datetime.now().year,
                    'list': inptDicLst,
                }
            )
            for i in range(len(invResult)):
                if invResult[i] == check_box_list[j]:
                    checklist.append('1')
                    if j+1 < len(check_box_list):
                        j += 1
                else:
                    checklist.append('0')
            for k in range(1,len(cookbook)):
                if cookbook[k] > checklist[k]:
                        flag = 1
            if flag == 0:
                    cookable.append(cookbook)
            else:
                    flag = 0
            return render(
            request,
            'app/GetMenu.html',
            {
                'title':'GetMenu',
                'message':'You can cook:',
                'year':datetime.now().year,
                'list': cookable,
            }
        ) 

