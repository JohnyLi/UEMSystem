# coding=utf-8
from flask import Flask, g,request,render_template,session,redirect
from startSevice import getSQLHandler
def welcomeImpl():
    result = getSQLHandler().SELECT("select * from test")

    return str(result)