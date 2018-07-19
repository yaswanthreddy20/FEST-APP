# Create your views here.
from django.shortcuts import render_to_response,HttpResponseRedirect,render
from django.http import HttpResponse
from web.models import Participants,Sponsors,Visitors,Special_nights,Spot,Entry,Vehicle
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import datetime
#edit for each fest
fest_code = 'QK15'
#---------------------------------------------------------------------------------------------------------------------------------------------------
#@login_required(login_url='/login/')
def index(request):
	return HttpResponseRedirect('/static/main.html')
#---------------------------------------------------------------------------------------------------------------------------------------------------

#def login(request):
#	try:
#		return HttpResponse(request.GET)
#		details = request.GET
#		return HttpResponse(details)
#		user = authenticate(username=details['user'],password=details['password'])
#		return HttpResponse('%s %s'%(details['user'],details['password']))
#		if user.is_active:
#			return HttpResponseRedirect('/static/main.html')
#	except:
#		return render(request,'docs/login.html',{})		
#@login_required(login_url='/login/')
def details(request,model,search):
	if model== 'participant':
		result = Participants.objects.filter(id=int(search)).values()[0]
	elif model== 'sponsor':
		result = Sponsors.objects.filter(id=int(search)).values()[0]
	elif model== 'visitor':
		result = Visitors.objects.filter(id=int(search)).values()[0]
	if result==None:
		result={'name':'not present'}
	return render(request,'docs/display1.html',{'result':result})
#---------------------------------------------------------------------------------------------------------------------------------------------------
#@login_required(login_url='/login/')
def spot_reg(request):
	errors = []
	try:
		pre_id = Participants.objects.all().order_by("-id")[0].id+1
	except:
		pre_id=1
	info = request.GET
	try:
		if info['name']:
			try:
				pre_id = Participants.objects.all().order_by("-id")[0].id+1
			except:
				pre_id = 1
			pre_id=("%4.0f"%pre_id).replace(' ','0')	
			person = 'participant'
			b = Participants(name= info['name'],college =info['college'],city = info['city'],mobile=info['mobile'],accomm=info['accomm'],events="--",checklist=info['checklist'],reg_date=datetime.datetime.now(),fest_id=fest_code+str(pre_id)+'P' )
			b.save()
			#return HttpResponse('wow')
		return HttpResponseRedirect('/details/%s/%s'%(person,pre_id))
	except:
		return render(request,'docs/registration.html',{})
#--------------------------------------------------------------------------------------------------------------------------------------------------------------		
#@login_required(login_url='/login/')
def sponsors(request):
	info = request.GET
	try:
		if info['sponsor']:
			person = 'sponsor'
			b = Sponsors(name=info['sponsor'],company = info['org'],reg_date=datetime.datetime.now())
			b.save()
			pre_id = Sponsors.objects.all().order_by("-id")[0].id
		return HttpResponseRedirect('/details/%s/%s'%(person,pre_id))
	except:
		return render(request,'docs/sponsors.html',{})
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#@login_required(login_url='/login/')
def visitors(request):			
	info = request.GET
	try:
		#return HttpResponse('wow1')
		try:
			pre_id = Visitors.objects.all().order_by("-id")[0].id+1
		except:
			pre_id=1
		pre_id=("%4.0f"%pre_id).replace(' ','0')
		person = 'visitor'
		#return HttpResponse('wow2')
		b = Visitors(name=info['visitor'],college=info['v_college'],city= info['v_city'],mobile= info['v_mobile'],purpose='v_purpose',reg_date=datetime.datetime.now(),fest_id=fest_code+str(pre_id)+'V')
		b.save()
		#return HttpResponse('wow3')
		return HttpResponseRedirect('/details/%s/%s'%(person,pre_id))
	except:
		return render(request,'docs/visitors.html',{})
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#@login_required(login_url='/login/')
def vehicle(request):
	info = request.GET
	try:	
		person = 'vehicle'
		b = Vehicle(name=info['name'],vehicle=info['vehicle'],number=info['number'],mobile=info['mobile'],deadline=info['deadline'])
		b.save()
		return render(request,'docs/display.html',{'result':request.GET})
	except:
		return render(request,'docs/vehicles.html',{})
#@login_required(login_url='/login/')
def vehicle_pass(request):
	return render(request,'docs/vehicles.html',{})
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#@login_required(login_url='/login/')
def searchquerie(request):
	name = request.GET['q']
	name = name.lower()
	results = []
	for e in Participants.objects.all():
		if name in e.name.lower() or name in e.fest_id.lower() or name in e.college.lower():
			results.append(e)
			
	return render(request,'docs/details.html',{'results':results})

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def special_nights(request):
	flag = False
	try:
		college_id = request.GET
		result = {}
		check = college_id['value']
		if check.__len__ <9:
			result['presence']=False
			result['First']=False
			flag = True
		#return HttpResponse('wow')
		
		else:
			result['presence']=False
			result['First']=False
			for e in Spot.objects.all():
				#return HttpResponse('wow')
				if check.upper() == e.college_id.upper():
					#return HttpResponse('wow')
					result['presence']=True
					#return HttpResponse('wow')
			for e in Special_nights.objects.all():
				#return HttpResponse('wow')
				if check.upper() in e.college_id.upper():
					return HttpResponse('wow')
					result['presence']=True
					#return HttpResponse('wow')	
			
			for e in Entry.objects.all():
				#return HttpResponse('wow')
				if check.upper() == e.college_id.upper():
					#return HttpResponse('wow')
					result['First']=True
					#return HttpResponse('wow')
		try: 
			print result['presence']
		except:
			result['presence']=False
		#return HttpResponse(result['presence'])
		if result['presence'] == False and flag == False:
			Spot(college_id = check.upper()).save()
		if result['First'] == False and flag == False:
			Entry(college_id = check.upper()).save()
			print 'Hello World',check
		return render(request,'docs/special.html',{'results':result})
	except:
		return render(request,'docs/special.html',{})