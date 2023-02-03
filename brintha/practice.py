#  from flask import Flask,template_rendered
# venkat=Flask(__name__)
# #print(__name__)
# @venkat.route('/')    #generating url to show
# def ks():
#     return "ks"
# if __name__=='__main__':
#    venkat.run(debug=True)

from flask import Flask
prabha=Flask(__name__)
@prabha.route("/")
@prabha.route("/name")
def function():
   return "hello world"
if __name__ =='__main__':
    prabha.run(debug=True)   

