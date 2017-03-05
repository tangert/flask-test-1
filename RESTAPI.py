import requests
from helpers import response

def test(request):
	resp = response({'success':True, 'data':'your backend works!'})
	return resp