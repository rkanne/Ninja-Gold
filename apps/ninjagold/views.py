from django.shortcuts import render
import random 
import time

# Create your views here.
def index(request):
	request.session['gold'] = 0
  	request.session['activities'] = []
	return render(request, 'ninjagold/index.html')

def gold(request):
	if request.POST['building'] == 'farm':
		gold = random.randrange(0, 21)
		request.session['gold'] += gold
		total = request.session['gold']
		current = time.strftime("%Y/%m/%d")+ '  ' + time.strftime("%I:%M:%S %p")
		result = request.session['activities'].append(["<span class ='activities'>Earned", gold ,'golds from the farm! ',current,'</span>'])
		context ={'total': total}
		return render(request, 'ninjagold/index.html', context)
	elif request.POST['building'] == 'cave':
			gold = random.randrange(5, 11)
			request.session['gold'] += gold
			total = request.session['gold']
			current = time.strftime("%Y/%m/%d")+ '  ' + time.strftime("%I:%M:%S %p")
			result = request.session['activities'].append(["<span class ='activities'>Earned", gold ,'golds from the farm! ',current,'</span>'])
			context = {'total': total}
			return render(request, 'ninjagold/index.html', context)
	elif request.POST['building'] == 'house':
    		gold = random.randrange(2, 6)
    		request.session['gold'] += gold
    		total = request.session['gold']
    		current = time.strftime("%Y/%m/%d")+ '  ' + time.strftime("%I:%M:%S %p")
    		result = request.session['activities'].append(["<span class ='activities'>Earned", gold ,'golds from the farm! ',current,'</span>'])
    		context = {'total': total}
    		return render(request, 'ninjagold/index.html', context)
	elif request.POST['building'] == 'casino':
    		gold = random.randrange(-51, 51)
    		request.session['gold'] += gold
    		total = request.session['gold']
    		current = time.strftime("%Y/%m/%d")+ '  ' + time.strftime("%I:%M:%S %p")
    		if(gold < 0):
    			result=request.session['activities'].append(["<span class ='activities_lost'>Entered a casino and lost", gold ,'golds .. Ouch.. ',current,'</span>'])
    			context = {'total': total}
    			return render(request, 'ninjagold/index.html', context)
    		else:
    			result=request.session['activities'].append(["<span class ='activities'>Earned", gold ,'golds from the farm! ',current,'</span>'])
    			context = {'total': total}
      			return render(request, 'ninjagold/index.html', context)

  