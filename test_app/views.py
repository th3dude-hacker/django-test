from django.shortcuts import render

# Create your views here.

class A(object):
    def __init__(self, msg):
        self.msg = msg
    
    def getMsg(self):
        return self.msg

    def setMsg(self, msg):
        self.msg = msg
        return self.msg
