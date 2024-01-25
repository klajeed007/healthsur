from django.http import HttpResponse
from .models import *
from tkinter import messagebox
from django.template import loader
from django.db.models import Sum
from django.http import HttpResponse, response
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import *


def conview(request):

	r1 = ContactMessage.objects.filter(result='0').count()
	r1 = int(r1)
	print('ระดับความเสี่ยงน้อย ',r1)

	r2 = ContactMessage.objects.filter(result='1').count()
	r2 = int(r2)
	print('ระดับความเสี่ยงน้อย-ปานกลาง ',r2)

	r3 = ContactMessage.objects.filter(result='2').count()
	r3 = int(r3)
	print('ระดับความเสี่ยงปานกลาง ',r3)	

	r4 = ContactMessage.objects.filter(result='3').count()
	r4 = int(r4)
	print('ระดับความเสี่ยงสูง ',r4)	

	r5 = ContactMessage.objects.filter(result='4').count()
	r5 = int(r5)
	print('ระดับความเสี่ยงเสี่ยงสูงมาก ',r5)	

	result_list = ['ระดับความเสี่ยงน้อย','ระดับความเสี่ยงน้อย-ปานกลาง','ระดับความเสี่ยงปานกลาง','ระดับความเสี่ยงสูง','ระดับความเสี่ยงเสี่ยงสูงมาก']
	result_number = [r1,r2,r3,r4,r5]
	



	
	alr0 = DmAlert.objects.filter(alertresult='0').count()
	alr0 = int(alr0)
	print('0 คะแนน ',alr0)

	alr1 = DmAlert.objects.filter(alertresult='1').count()
	alr1 = int(alr1)
	print('1 คะแนน',alr1)

	alr2 = DmAlert.objects.filter(alertresult='2').count()
	alr2 = int(alr2)
	print('2 คะแนน ',alr2)

	alr3 = DmAlert.objects.filter(alertresult='3').count()
	alr3 = int(alr3)
	print('3 คะแนน ',alr3)

	alr4 = DmAlert.objects.filter(alertresult='4').count()
	alr4 = int(alr4)
	print('4 คะแนน ',alr4)

	alr5 = DmAlert.objects.filter(alertresult='5').count()
	alr5 = int(alr5)
	print('5 คะแนน ',alr5)

	alr6 = DmAlert.objects.filter(alertresult='6').count()
	alr6 = int(alr6)
	print('6 คะแนน ',alr6)

	alr7 = DmAlert.objects.filter(alertresult='7').count()
	alr7 = int(alr7)
	print('7 คะแนน ',alr7)

	alr8 = DmAlert.objects.filter(alertresult='8').count()
	alr8 = int(alr8)
	print('8 คะแนน ',alr8)

	#alr9 = DmAlert.objects.filter(alertresult='9').count()
	#alr9 = int(alr9)
	#print('9 คะแนน ',alr9)

	#alr10 = DmAlert.objects.filter(alertresult='10').count()
	#alr10 = int(alr10)
	#print('10 คะแนน ',alr10)


	alertresult_list = ['0 อาการ','1 อาการ','2 อาการ','3 อาการ','4 อาการ','5 อาการ','6 อาการ','7 อาการ','8 อาการ'
	#,'9 คะแนน','10 คะแนน'
	]
	alertresult_number = [alr0,alr1,alr2,alr3,alr4,alr5,alr6,alr7,alr8
	#alr9,alr10
	]
	




	br0 = DmBefore.objects.filter(bresult='0').count()
	br0 = int(br0)
	print('0 คะแนน ',br0)

	br1 = DmBefore.objects.filter(bresult='1').count()
	br1 = int(br1)
	print('1 คะแนน',br1)

	br2 = DmBefore.objects.filter(bresult='2').count()
	br2 = int(br2)
	print('2 คะแนน ',br2)

	br3 = DmBefore.objects.filter(bresult='3').count()
	br3 = int(br3)
	print('3 คะแนน ',br3)

	br4 = DmBefore.objects.filter(bresult='4').count()
	br4 = int(br4)
	print('4 คะแนน ',br4)

	br5 = DmBefore.objects.filter(bresult='5').count()
	br5 = int(br5)
	print('5 คะแนน ',br5)

	br6 = DmBefore.objects.filter(bresult='6').count()
	br6 = int(br6)
	print('6 คะแนน ',br6)

	br7 = DmBefore.objects.filter(bresult='7').count()
	br7 = int(br7)
	print('7 คะแนน ',br7)

	br8 = DmBefore.objects.filter(bresult='8').count()
	br8 = int(br8)
	print('8 คะแนน ',br8)

	br9 = DmBefore.objects.filter(bresult='9').count()
	br9 = int(br9)
	print('9 คะแนน ',br9)

	br10 = DmBefore.objects.filter(bresult='10').count()
	br10 = int(br10)
	print('10 คะแนน ',br10)


	bresult_list = ['0 คะแนน','1 คะแนน','2 คะแนน','3 คะแนน','4 คะแนน','5 คะแนน','6 คะแนน','7 คะแนน','8 คะแนน','9 คะแนน','10 คะแนน'
	]
	bresult_number = [br0,br1,br2,br3,br4,br5,br6,br7,br8,br9,br10
	]






	ar0 = DmAfter.objects.filter(aresult='0').count()
	ar0 = int(ar0)
	print('0 คะแนน ',ar0)

	ar1 = DmAfter.objects.filter(aresult='1').count()
	ar1 = int(ar1)
	print('1 คะแนน',ar1)

	ar2 = DmAfter.objects.filter(aresult='2').count()
	ar2 = int(ar2)
	print('2 คะแนน ',ar2)

	ar3 = DmAfter.objects.filter(aresult='3').count()
	ar3 = int(ar3)
	print('3 คะแนน ',ar3)

	ar4 = DmAfter.objects.filter(aresult='4').count()
	ar4 = int(ar4)
	print('4 คะแนน ',ar4)

	ar5 = DmAfter.objects.filter(aresult='5').count()
	ar5 = int(ar5)
	print('5 คะแนน ',ar5)

	ar6 = DmAfter.objects.filter(aresult='6').count()
	ar6 = int(ar6)
	print('6 คะแนน ',ar6)

	ar7 = DmAfter.objects.filter(aresult='7').count()
	ar7 = int(ar7)
	print('7 คะแนน ',ar7)

	ar8 = DmAfter.objects.filter(aresult='8').count()
	ar8 = int(ar8)
	print('8 คะแนน ',ar8)

	ar9 = DmAfter.objects.filter(aresult='9').count()
	ar9 = int(ar9)
	print('9 คะแนน ',ar9)

	ar10 = DmAfter.objects.filter(aresult='10').count()
	ar10 = int(ar10)
	print('10 คะแนน ',ar10)


	aresult_list = ['0 คะแนน','1 คะแนน','2 คะแนน','3 คะแนน','4 คะแนน','5 คะแนน','6 คะแนน','7 คะแนน','8 คะแนน','9 คะแนน','10 คะแนน'
	]
	aresult_number = [ar0,ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10
	]




###################################################################




	sq1r1 = satisfied.objects.filter(sq1='1').count()
	sq1r1 = int(sq1r1)
	print('1 คะแนน',sq1r1)

	sq1r2 = satisfied.objects.filter(sq1='2').count()
	sq1r2 = int(sq1r2)
	print('2 คะแนน ',sq1r2)

	sq1r3 = satisfied.objects.filter(sq1='3').count()
	sq1r3 = int(sq1r3)
	print('3 คะแนน ',sq1r3)

	sq1r4 = satisfied.objects.filter(sq1='4').count()
	sq1r4 = int(sq1r4)
	print('4 คะแนน ',sq1r4)

	sq1r5 = satisfied.objects.filter(sq1='5').count()
	sq1r5 = int(sq1r5)
	print('5 คะแนน ',sq1r5)




	sq2r1 = satisfied.objects.filter(sq2='1').count()
	sq2r1 = int(sq2r1)
	print('1 คะแนน',sq2r1)

	sq2r2 = satisfied.objects.filter(sq2='2').count()
	sq2r2 = int(sq2r2)
	print('2 คะแนน ',sq2r2)

	sq2r3 = satisfied.objects.filter(sq2='3').count()
	sq2r3 = int(sq2r3)
	print('3 คะแนน ',sq2r3)

	sq2r4 = satisfied.objects.filter(sq2='4').count()
	sq2r4 = int(sq2r4)
	print('4 คะแนน ',sq2r4)

	sq2r5 = satisfied.objects.filter(sq2='5').count()
	sq2r5 = int(sq2r5)
	print('5 คะแนน ',sq2r5)




	sq3r1 = satisfied.objects.filter(sq3='1').count()
	sq3r1 = int(sq3r1)
	print('1 คะแนน',sq3r1)

	sq3r2 = satisfied.objects.filter(sq3='2').count()
	sq3r2 = int(sq3r2)
	print('2 คะแนน ',sq3r2)

	sq3r3 = satisfied.objects.filter(sq3='3').count()
	sq3r3 = int(sq3r3)
	print('3 คะแนน ',sq3r3)

	sq3r4 = satisfied.objects.filter(sq3='4').count()
	sq3r4 = int(sq3r4)
	print('4 คะแนน ',sq3r4)

	sq3r5 = satisfied.objects.filter(sq3='5').count()
	sq3r5 = int(sq3r5)
	print('5 คะแนน ',sq3r5)



	sq4r1 = satisfied.objects.filter(sq4='1').count()
	sq4r1 = int(sq4r1)
	print('1 คะแนน',sq4r1)

	sq4r2 = satisfied.objects.filter(sq4='2').count()
	sq4r2 = int(sq4r2)
	print('2 คะแนน ',sq4r2)

	sq4r3 = satisfied.objects.filter(sq4='3').count()
	sq4r3 = int(sq4r3)
	print('3 คะแนน ',sq4r3)

	sq4r4 = satisfied.objects.filter(sq4='4').count()
	sq4r4 = int(sq4r4)
	print('4 คะแนน ',sq4r4)

	sq4r5 = satisfied.objects.filter(sq4='5').count()
	sq4r5 = int(sq4r5)
	print('5 คะแนน ',sq4r5)




	sq5r1 = satisfied.objects.filter(sq5='1').count()
	sq5r1 = int(sq5r1)
	print('1 คะแนน',sq5r1)

	sq5r2 = satisfied.objects.filter(sq5='2').count()
	sq5r2 = int(sq5r2)
	print('2 คะแนน ',sq5r2)

	sq5r3 = satisfied.objects.filter(sq5='3').count()
	sq5r3 = int(sq5r3)
	print('3 คะแนน ',sq5r3)

	sq5r4 = satisfied.objects.filter(sq5='4').count()
	sq5r4 = int(sq5r4)
	print('4 คะแนน ',sq5r4)

	sq5r5 = satisfied.objects.filter(sq5='5').count()
	sq5r5 = int(sq5r5)
	print('5 คะแนน ',sq5r5)

#### คิดความพึงพอใจ

	cr1 = [sq1r1,sq1r2,sq1r3,sq1r4,sq1r5]
	cr2 = [sq2r1,sq2r2,sq2r3,sq2r4,sq2r5]
	cr3 = [sq3r1,sq3r2,sq3r3,sq3r4,sq3r5]
	cr4 = [sq4r1,sq4r2,sq4r3,sq4r4,sq4r5]
	cr5 = [sq5r1,sq5r2,sq5r3,sq5r4,sq5r5]

	countq1 = sq1r1+sq1r2+sq1r3+sq1r4+sq1r5
	countq2 = sq2r1+sq2r2+sq2r3+sq2r4+sq2r5
	countq3 = sq3r1+sq3r2+sq3r3+sq3r4+sq3r5
	countq4 = sq4r1+sq4r2+sq4r3+sq4r4+sq4r5
	countq5 = sq5r1+sq5r2+sq5r3+sq5r4+sq5r5

	sumr1 = (sq1r1 + sq2r1 + sq3r1 + sq4r1 + sq5r1)*1
	sumr2 = (sq1r2 + sq2r2 + sq3r2 + sq4r2 + sq5r2)*2
	sumr3 = (sq1r3 + sq2r3 + sq3r3 + sq4r3 + sq5r3)*3
	sumr4 = (sq1r4 + sq2r4 + sq3r4 + sq4r4 + sq5r4)*4
	sumr5 = (sq1r5 + sq2r5 + sq3r5 + sq4r5 + sq5r5)*5

	satisq1 = (sq1r1*1) + (sq1r2*2) + (sq1r3*3) + (sq1r4*4) + (sq1r5*5)
	satisq2 = (sq2r1*1) + (sq2r2*2) + (sq2r3*3) + (sq2r4*4) + (sq2r5*5)
	satisq3 = (sq3r1*1) + (sq3r2*2) + (sq3r3*3) + (sq3r4*4) + (sq3r5*5)
	satisq4 = (sq4r1*1) + (sq4r2*2) + (sq4r3*3) + (sq4r4*4) + (sq4r5*5)
	satisq5 = (sq5r1*1) + (sq5r2*2) + (sq5r3*3) + (sq5r4*4) + (sq5r5*5)


### ค่าเฉลี่ย

	results1 = satisq1/countq1
	results2 = satisq2/countq2
	results3 = satisq3/countq3
	results4 = satisq4/countq4
	results5 = satisq5/countq5

	average_s = (results1 + results2 + results3 + results4 + results5)/5

	sresult_list = ['พึงพอใจน้อยที่สุด','พึงพอใจน้อย','พึงพอใจปานกลาง','พึงพอใจมาก','พึงพอใจมากที่สุด'
	]

	rs1 = results1
	rs2 = results2
	rs3 = results3
	rs4 = results4
	rs5 = results5



	context = {'result_list':result_list, 'result_number':result_number, 
	'alertresult_list':alertresult_list, 'alertresult_number':alertresult_number,
	'bresult_list':bresult_list, 'bresult_number':bresult_number,
	'aresult_list':aresult_list, 'aresult_number':aresult_number,
	'sresult_list':sresult_list,
	'average_s':average_s,
	'rs1':rs1,
	'rs2':rs2,
	'rs3':rs3,
	'rs4':rs4,
	'rs5':rs5,	
	'cr1':cr1,
	'cr2':cr2,
	'cr3':cr3,
	'cr4':cr4,
	'cr5':cr5

	}


	return render(request,'home/dashboard.html',context)


def conview1(request):
	test = 'ระดับความเสี่ยงน้อย'
	context['test'] = test
	return render(request,'home/dashboard.html',context)



def Home(request):
	return render(request,'home/home.html')

def dashboard(request):
	return render(request,'home/dashboard.html')

#def Calscore (request):
	#return 
def popup(res):
	#res2 = "ผลปรเมินของคุณคือ" + res
	messagebox.showinfo("ผลคะแนนประเมิน","ผลประเมินความเสี่ยงของคุณคือ ระดับความเสี่ยง" + res)



	
def Services(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		age = int(data.get('age'))
		bmi = int(data.get('bmi'))
		wtoh = int(data.get('wtoh'))
		ht = int(data.get('ht'))
		pardimen = int(data.get('pardimen'))
		fpg = int(data.get('fpg'))
		uname = data.get('uname')

		print (age,bmi,wtoh,ht,pardimen,fpg)
		
		score = age + bmi + wtoh + ht + pardimen + fpg
		#int(score)

		if (fpg >= 5):	
			if score >= 17:
				result = 4

			elif score >= 15:
				result = 3

			elif score >= 11:
				result = 2

			elif score >= 8:
				result = 1

			else:
				result = 0


		else:
			if score >= 15:
				result = 4	
		
			elif score >= 13:
				result = 3

			elif score >= 10:
				result = 2

			elif score >= 9:
				result = 1

			else:
				result = 0


		if result == 4:
			res = "ระดับความเสี่ยงสูงมาก (30% ขึ้นไป)"
			#popup(res)
		elif result == 3:
			res = "ระดับความเสี่ยงสูง (21-30%)"
			#popup(res)
		elif result == 2:	
			res = "ระดับความเสี่ยงปานกลาง-สูง (11-20%)"	
			#popup(res)
		elif result == 1:	
			res = "ระดับความเสี่ยงน้อย-ปานกลาง (6-10%)"
			#popup(res)
		else:	
			res = "ระดับความเสี่ยงน้อย (0-5%)"
			#popup(res)

		new = ContactMessage()
		new.age = age
		new.bmi = bmi
		new.wtoh = wtoh
		new.ht = ht
		new.pardimen = pardimen
		new.fpg = fpg
		new.result = result
		new.uname = uname
		new.save()
		print (res)

		context['status'] = 'success'
		context['result'] = res

	return render(request,'home/service.html',context)

def Services1(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		urine = int(data.get('urine'))
		tried = int(data.get('tried'))
		eat = int(data.get('eat'))
		wound = int(data.get('wound'))
		eye = int(data.get('eye'))
		dehy = int(data.get('dehy'))
		hungry = int(data.get('hungry'))
		pain = int(data.get('pain'))
		uname = data.get('uname')
		print (data,tried,eat,wound,eye,dehy,hungry,pain)
		
		alertresult = urine + tried + eat + wound + eye + dehy + hungry + pain

		new = DmAlert()
		new.urine = urine
		new.tried = tried
		new.eat = eat
		new.wound = wound
		new.eye = eye
		new.dehy = dehy
		new.hungry = hungry
		new.pain = pain
		new.alertresult = alertresult
		new.uname = uname
	
		new.save()
		print (alertresult)

		context['status'] = 'success'
		context['result'] = alertresult

	return render(request,'home/service1.html',context)

def Services2(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		bq1 = int(data.get('bq1'))
		bq2 = int(data.get('bq2'))
		bq3 = int(data.get('bq3'))
		bq4 = int(data.get('bq4'))
		bq5 = int(data.get('bq5'))
		bq6 = int(data.get('bq6'))
		bq7 = int(data.get('bq7'))
		bq8 = int(data.get('bq8'))
		bq9 = int(data.get('bq9'))
		bq10 = int(data.get('bq10'))
		uname = data.get('uname')
		print (bq1,bq2,bq3,bq4,bq5,bq6,bq7,bq8,bq9,bq10)
		
		bresult = bq1 + bq2 + bq3 + bq4 + bq5 + bq6 + bq7 + bq8 + bq9 + bq10

		new = DmBefore()
		new.bq1 = bq1
		new.bq2 = bq2
		new.bq3 = bq3
		new.bq4 = bq4
		new.bq5 = bq5
		new.bq6 = bq6
		new.bq7 = bq7
		new.bq8 = bq8
		new.bq9 = bq9
		new.bq10 = bq10
		new.bresult = bresult
		new.uname = uname
	
		new.save()
		print (bresult)

		context['status'] = 'success'
		context['result'] = bresult

	return render(request,'home/service2.html',context)

def Services3(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		aq1 = int(data.get('aq1'))
		aq2 = int(data.get('aq2'))
		aq3 = int(data.get('aq3'))
		aq4 = int(data.get('aq4'))
		aq5 = int(data.get('aq5'))
		aq6 = int(data.get('aq6'))
		aq7 = int(data.get('aq7'))
		aq8 = int(data.get('aq8'))
		aq9 = int(data.get('aq9'))
		aq10 = int(data.get('aq10'))

		uname = data.get('uname')
		#before2 = bresult.DmBefore.objects.filter(uname=uname)
		print (aq1,aq2,aq3,aq4,aq5,aq6,aq7,aq8,aq9,aq10)
		
		aresult = aq1 + aq2 + aq3 + aq4 + aq5 + aq6 + aq7 + aq8 + aq9 + aq10

		new = DmAfter()
		new.aq1 = aq1
		new.aq2 = aq2
		new.aq3 = aq3
		new.aq4 = aq4
		new.aq5 = aq5
		new.aq6 = aq6
		new.aq7 = aq7
		new.aq8 = aq8
		new.aq9 = aq9
		new.aq10 = aq10
		new.aresult = aresult
		new.uname = uname
		new.before2 = DmBefore.objects.filter(uname=uname).values('bresult')
		new.alertresult = DmAlert.objects.filter(uname=uname).values('alertresult')
		new.riskresult = ContactMessage.objects.filter(uname=uname).values('result')
		new.save()
		print (aresult)

		context['status'] = 'success'
		context['result'] = aresult

	return render(request,'home/service3.html',context)


def Services4(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.copy()
		sq1 = int(data.get('sq1'))
		sq2 = int(data.get('sq2'))
		sq3 = int(data.get('sq3'))
		sq4 = int(data.get('sq4'))
		sq5 = int(data.get('sq5'))
		advice = data.get('advice')
		print (sq1,sq2,sq3,sq4,sq5)
		
		sresult = (sq1 + sq2 + sq3 + sq4 + sq5)/5

		new = satisfied()
		new.sq1 = sq1
		new.sq2 = sq2
		new.sq3 = sq3
		new.sq4 = sq4
		new.sq5 = sq5
		new.advice = advice
		new.sresult = sresult
	
		new.save()
		print (sresult)

		context['status'] = 'success'
		context['result'] = sresult

	return render(request,'home/service4.html',context)
