from bottle import *
import time

@route('/')
def welcome():
    print(dict(request.headers))
    if 'text/html' in request.headers.get('Accept', '*/*'):
        response.content_type = 'text/html'
        return '<h1> howdy! </h1>'
    response.content_type = 'text/plain'
    return 'Hello'

#Dynamic module 
@route('/now')
def time_service():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age = 1')
    return time.ctime()

#Dynamic route
@route('/upper/<word>')
def upper_case_service(word):
    response.content_type = 'text/plain'
    return word.upper()


#THis is how to make something happen in server
import math

@route('/area/circle')
def area_circle_service(radius):
    return math.pi*radius ** 2.0


#For some reason it is below
if __name__ == '__main__':

    run(host = 'localhost', port = 8080)

