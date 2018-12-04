# coding=utf-8

import threading
import traceback
import time
import pymssql

from conf.DB_Config import *
from DBUtils.PooledDB import PooledDB
from public.Logger import logger

class SQLServer(object):
    """
    SQL Sever 连接 (单例)
    """
    _instance_lock=threading.Lock()
    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.db = DB_NAME
        self.DB_ConnNum=DB_ConnNum
    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(SQLServer, "_instance"):
            with SQLServer._instance_lock:
                if not hasattr(SQLServer, "_instance"):
                    SQLServer._instance=SQLServer(*args, **kwargs)
        return SQLServer._instance

    def start(self):
        self.makePool(self.DB_ConnNum)

    def makePool(self,ConnNum):
        print("====================开始创建数据库连接池...==============================")
        startTime = time.time()
        retry = 0
        while(1):
            try:
                self.pool = PooledDB(
                    pymssql,
                    ConnNum,
                    host=self.host,user=self.user,password=self.password,database=self.db,charset="utf8")
                break
            except Exception as e:
                logger.error("连接数据库失败 ")
                retry += 1
                logger.info("尝试第%s次重新创建数据库连接池..."%retry)
        print("<<<<< 创建时间:"+str(time.time()-startTime)+" 连接数:"+str(ConnNum)+" >>>>>")
        print("====================创建数据库连接池完成！==============================")




    def getConn(self):
        try:
            self.pool
        except:
            self.start()
        conn = self.pool.connection()
        return conn

class SQLHandler:
    """
    每一次访问会获得一个分配的连接
    处理sql语句时进行预编译，防止sql注入
    """
    def __init__(self,conn):
        self.conn = conn

    def SELECT(self,query,param=()):
        """
        主要处理select语句
        :param query: str      sql请求
        :param param: tuple    填入参数,tuple格式
        :return: result: tuple 或 None
        """
        conn = self.conn
        cur = conn.cursor()
        result = None
        try:
            startTime = time.time()
            cur.execute(query,param)
            result = cur.fetchall()
            logger.info(query + "," + str(param) + " Execute time:" + str(time.time()-startTime))
        except Exception as e:
            logger.error("Error: unable to fecth data with sql query: " + query + "," + str(param))
            logger.error(traceback.format_exc())
        cur.close()
        return result


    def UPDATE(self,query,param=()):
        """
        处理update和delete语句
        :param query: str      sql请求
        :param param: tuple    填入参数,tuple格式
        :return: bool
        """
        conn = self.conn
        cur = conn.cursor()
        result = True
        try:
            startTime = time.time()
            cur.execute(query,param)
            conn.commit()
            logger.info(query + "," + str(param) + " Execute time:" + str(time.time() - startTime))
        except Exception as e:
            logger.error("Error: unable to fecth data with sql query: " + query + "," + str(param))
            logger.error(traceback.format_exc())
            conn.rollback()
            result = False
        cur.close()
        return result

    def close(self):
        self.conn.close()



