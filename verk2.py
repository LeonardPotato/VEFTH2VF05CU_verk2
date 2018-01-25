import os
from bottle import route, run, static_file,request,error

@route("/")
def index():
    return "<a href='/a'>Liður a</a>" \
           " <a href='/b'>Liður b</a>"#Græni textinn fer inn sem html code, getur sett td h2 tag a hann . link er http://localhost:8080/

@route("/a") #verk 1a Menu
def a():
    return "<a href='/sida/1'>Síða 1</a> <br>"\
           "<a href='/sida/2'>Síða 2</a><br>" \
           "<a href='/sida/3'>Síða 3</a><br>"

@route("/sida/<n>") # Dynamic routing
def param(n):         #
    return "<h1>Þetta er síða " + n + "</h1>"

@route("/bottle")
def bottle():
    return "<h1>Using bottlepy</h1>" \
           "<a href='/bottle/blabladaemi'>Click here</a>"# link er http://localhost:8080/bottle

@route('/mynd')
def mynd():
    return '<a href="/result?mynd=cologne"><img src="/static/cologne.jpg" width="200">' \
           '<a href="/result?mynd=krakow"><img src="/static/krakow.jpg" width="200">' \
           '<a href="/result?mynd=berlin"><img src="/static/berlin.jpg" width="200">'

@route('/result')
def result():
    mynd = request.query.mynd

    return '<h2>Þú valdir ' + mynd + '</h2>' \
                                     '<img src="/static/'+mynd+'.jpg">'

@error(404)
def error404(error):
    return 'Villa 404, Ekkert fannst.'

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='./myfiles')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
