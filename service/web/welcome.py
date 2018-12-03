# coding=utf-8
from flask import Flask, g,request,render_template,session,redirect
from startService import getSQLHandler
def welcomeImpl():
    result = getSQLHandler().SELECT("select * from test")

    return render_template()