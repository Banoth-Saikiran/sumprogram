#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")



def xyz():
    return render_template("add.html")



@app.route("/detail",methods=["GET","POST"])



def abc():
    if(request.method=='POST'):
        n1=int(request.form['num1'])
        n2=int(request.form['num2'])
        total=n1+n2
        return render_template("add.html",kiran=total)
if __name__=="__main__":
    app.run()

