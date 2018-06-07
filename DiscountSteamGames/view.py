# -*- coding: utf-8 -*-
"""
最簡單的版本, 沒有 javascript 單純顯示遊戲清單
"""
from database.mysql_connect import connectMysql
from django.shortcuts import render
 
def getGameList(request):
    context = {}
    
    pageSize = 25
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])
    
    # connect MySQL database
    db = connectMysql()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM game_list ORDER BY discount DESC')
    #rows = cursor.fetchone()
    rows = cursor.fetchall()
    context['gameList'] = rows[page*pageSize: (page+1)*pageSize]
    if page > 1:
        context['previous_page'] = page-1
    context['next_page'] = page+1
    
    
    return render(request, 'game_list.html', context)