# coding: utf8
import pymssql
import json
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect
from forms import LoginForm
from django.contrib import auth

def main(request):
	if request.user.is_authenticated():
	   	return render_to_response('index.html', locals())
	else:
		return HttpResponseRedirect('/login')


def return_data(request):
	if request.is_ajax and request.method == 'POST'and request.user.is_authenticated():
		if request.POST['par'] == '1':
			conn = pymssql.connect(host='192.168.2.77',user='vasa',password='Rfqkfc 123',database='Stack_test')
			#conn = pymssql.connect(host='192.168.2.33',user='django',password='gfhfwtnjvjk',database='Stack_test')
			cur = conn.cursor()
			cur.execute("SELECT stack.[Лицевые счета].ROW_ID, stack.[Лицевые счета].Счета, stack.[Города].Название, stack.[Города].Сокращение, stack.[Города].ROW_ID FROM stack.[Лицевые счета] INNER JOIN stack.[Города] ON stack.[Лицевые счета].[Улица-Лицевой счет] = stack.[Города].ROW_ID WHERE (stack.[Лицевые счета].Тип = 2) Order by stack.[Города].Название")
			res = [[row[0], row[2], row[3]] for row in cur]
			conn.close()
			return HttpResponse(json.dumps(res))
		if request.POST['par'] == '2':
			conn = pymssql.connect(host='192.168.2.77',user='vasa',password='Rfqkfc 123',database='Stack_test')
			#conn = pymssql.connect(host='192.168.2.33',user='django',password='gfhfwtnjvjk',database='Stack_test')
			cur = conn.cursor()
			cur.execute("SELECT [ROW_ID], [Счета], [Номер], [Фамилия] FROM [stack].[Лицевые счета] where[Тип] = 3 and [Счета] = %s Order by [Номер], [Фамилия] " % request.POST['id'].encode('utf-8'))
			res = [[row[0], row[2], row[3]] for row in cur]
			conn.close()
			return HttpResponse(json.dumps(res))
		if request.POST['par'] == '3':
			conn = pymssql.connect(host='192.168.2.77',user='vasa',password='Rfqkfc 123',database='Stack_test')
			#conn = pymssql.connect(host='192.168.2.33',user='django',password='gfhfwtnjvjk',database='Stack_test')
			cur = conn.cursor()
			cur.execute("SELECT [ROW_ID], [Счета], [Номер], [Фамилия] FROM [stack].[Лицевые счета] where [Тип] = 4 and [Счета]=%s Order by [Номер], [Фамилия]" % request.POST['id'].encode('utf-8'))
			res = [[row[0], row[2], row[3]] for row in cur]
			conn.close()
			return HttpResponse(json.dumps(res))
		# Vse ls na adres
		if request.POST['par'] == '4':
			conn = pymssql.connect(host='192.168.2.77',user='vasa',password='Rfqkfc 123',database='Stack_test')
			#conn = pymssql.connect(host='192.168.2.33',user='django',password='gfhfwtnjvjk',database='Stack_test')
			cur = conn.cursor()
			cur.execute("SELECT stack.[Лицевые счета].[ROW_ID], stack.[Лицевые счета].[Счета], stack.[Лицевые счета].[Номер], stack.[Лицевые счета].[Примечание], stack.[Карточки регистрации].ФИО FROM [stack].[Лицевые счета] INNER JOIN stack.[Карточки регистрации] ON stack.[Лицевые счета].[Счет-Наниматель] = stack.[Карточки регистрации].[ROW_ID] where [Тип] = 5 and [Счета]=%s Order by [Номер]" % request.POST['id'].encode('utf-8'))
			res = [[row[0], row[2], row[3], row[4]] for row in cur]
			print(res)
			conn.close()
			return HttpResponse(json.dumps(res))
		# Vse ludi na ls
		if request.POST['par'] == '5':
			conn = pymssql.connect(host='192.168.2.77',user='vasa',password='Rfqkfc 123',database='Stack_test')
			#conn = pymssql.connect(host='192.168.2.33',user='django',password='gfhfwtnjvjk',database='Stack_test')
			cur = conn.cursor()

			cur.execute("SELECT stack.[Карточки регистрации].[Дата рождения], stack.[Карточки регистрации].Фио, stack.[Карточки регистрации].[Дата прописки], "+
			"stack.[Карточки регистрации].[Дата выписки], stack.Классификаторы.Название, stack.[Документы владения].Номер, stack.[Документы владения].ДатНач, "+
			"stack.[Документы владения].Примечание, "+
			"stack.[Документы владения].ДатаРег, stack.[Документы владения].Совместная, stack.[Документы владения].Доля_Числитель,stack.[Документы владения].Доля_Знаменатель,stack.[Документы владения].Основание, stack.[Карточки регистрации].Рождение, stack.[Карточки регистрации].Выбытие, stack.[Карточки регистрации].[Дата смерти], stack.[Карточки регистрации].[Вид регистрации] "+
			"FROM "+
			"stack.[Карточки регистрации] LEFT OUTER JOIN stack.Классификаторы ON stack.[Карточки регистрации].[Человек-Родство] = stack.Классификаторы.ROW_ID "+
			"LEFT OUTER JOIN stack.[Документы владения] ON stack.[Карточки регистрации].ROW_ID = stack.[Документы владения].[Человек-Владение] "+
			"WHERE(stack.[Карточки регистрации].[Человек-Лицевой] = %s)" % request.POST['id'].encode('utf-8'))

			#cur.execute("SELECT stack.[Карточки регистрации].[ROW_ID], stack.[Карточки регистрации].[Счет-Наниматель], stack.[Карточки регистрации].[Фио], stack.[Карточки регистрации].[Дата прописки], stack.[Карточки регистрации].[Дата выписки],  stack.Классификаторы.Название  FROM stack.[Карточки регистрации] INNER JOIN stack.Классификаторы ON stack.[Карточки регистрации].[Человек-Родство] = stack.Классификаторы.ROW_ID where stack.[Карточки регистрации].[Человек-Лицевой]= %s" % request.POST['id'].encode('utf-8'))
			res = [[row[1], str(row[2]), str(row[3]),row[4], row[5],str(row[6]),row[7],str(row[8]),row[10],row[11],str(row[0]),row[12],row[13],row[14],str(row[15]), row[16]] for row in cur]
			conn.close()
			return HttpResponse(json.dumps(res))
		# Vse params na ls
		if request.POST['par'] == '6':
			conn = pymssql.connect(host='192.168.2.77',user='vasa',password='Rfqkfc 123',database='Stack_test')
			#conn = pymssql.connect(host='192.168.2.33',user='django',password='gfhfwtnjvjk',database='Stack_test')
			cur = conn.cursor()
			cur.execute("SELECT stack.[Лицевые счета].Номер, stack.Свойства.[Виды-Параметры], stack.Свойства.ДатНач, stack.Свойства.ДатКнц, stack.Свойства.Значение,stack.[Виды параметров].Название FROM stack.[Лицевые счета] INNER JOIN stack.Свойства ON stack.[Лицевые счета].ROW_ID = stack.Свойства.[Счет-Параметры] INNER JOIN stack.[Виды параметров] ON stack.Свойства.[Виды-Параметры] = stack.[Виды параметров].ROW_ID WHERE stack.[Свойства].[Счет-Параметры] = %s" % request.POST['id'].encode('utf-8'))
			res = [[row[5], row[4]] for row in cur]
			print(res)
			conn.close()
			return HttpResponse(json.dumps(res))

		else:
			return HttpResponse("none")
	else:
		return HttpResponse("noneG")


	# login user
def login(request):
	dt = {'error': ''}
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		form = LoginForm(request.POST or None)
		if form.is_valid():
			user = auth.authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
			if user is not None:
				request.session['user'] = {}
				auth.login(request, user)
				return HttpResponseRedirect('/')
			else:
				dt = {'error': 'Некорректные данные!'}
		return render_to_response('login.html', dt)


def logout(request):
    auth.logout(request)
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponseRedirect('/login')

