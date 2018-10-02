from django.http import HttpResponse
from django import template

def here(request):
	return HttpResponse('I am here')
def math(request,a,b):
	s = a+b
	d = a-b
	p = a*b
	q = a/b
	with open('template/math.html','r') as reader:
		t=template.Template(reader.read())
	c=template.Context({ 's':s,'d':d,'p':p,'q':q })
	return HttpResponse(t.render(c))