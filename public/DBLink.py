# coding=utf-8

import threading
import traceback
import time
import pymssql

from conf.DB_Config import *
from DBUtils.PooledDB import PooledDB
from public.Logger import logger

class SQLServer(object):
    _instance_lock=threading.Lock()
    def __init__(self):
        self.host = DB_HOST
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.db = DB_NAME
        self.pool = self.getPool(DB_ConnNum)

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(SQLServer, "_instance"):
            with SQLServer._instance_lock:
                if not hasattr(SQLServer, "_instance"):
                    SQLServer._instance=SQLServer(*args, **kwargs)
        return SQLServer._instance

    def getPool(self,ConnNum=1):
        return PooledDB(pymssql,ConnNum,host=self.host,user=self.user,password=self.password,database=self.db,charset="utf8")

    def getConn(self):
        return self.pool.connection()

    # def SELECT(self,query,param=()):
    #     conn = self.getConn()
    #     cur = conn.cursor()
    #     result = None
    #     try:
    #         cur.execute(query,param)
    #         result = cur.fetchall()
    #         logger.info(query)
    #     except Exception as e:
    #         logger.error("Error: unable to fecth data with sql query: " + query + "," + str(param))
    #         logger.error(traceback.format_exc())
    #     finally:
    #         cur.close()
    #         conn.close()
    #         return result
    #
    #
    # def UPDATE(self,query,param=()):
    #     conn = self.getConn()
    #     cur = conn.cursor()
    #     try:
    #         cur.execute(query,param)
    #         conn.commit()
    #     except Exception as e:
    #         logger.error("Error: unable to fecth data with sql query: " + query + "," + str(param))
    #         logger.error(traceback.format_exc())
    #         conn.rollback()
    #     cur.close()
    #     conn.close()

class SQLHandler:
    def __init__(self,conn):
        self.conn = conn

    def SELECT(self,query,param=()):
        conn = self.conn
        cur = conn.cursor()
        result = None
        try:
            startTime = time.time()
            cur.execute(query,param)
            result = cur.fetchall()
            logger.info(query + "," + str(param) + " Excute time:" + str(time.time()-startTime))
        except Exception as e:
            logger.error("Error: unable to fecth data with sql query: " + query + "," + str(param))
            logger.error(traceback.format_exc())
        cur.close()
        return result


    def UPDATE(self,query,param=()):
        conn = self.conn
        cur = conn.cursor()
        result = True
        try:
            startTime = time.time()
            cur.execute(query,param)
            conn.commit()
            logger.info(query + "," + str(param) + " Excute time:" + str(time.time() - startTime))
        except Exception as e:
            logger.error("Error: unable to fecth data with sql query: " + query + "," + str(param))
            logger.error(traceback.format_exc())
            conn.rollback()
            result = False
        cur.close()
        return result

    def close(self):
        self.conn.close()



