# coding=utf-8
# 调用实例

# 添加作品信息
# JSON OK
# Work.insertWork(workName,workContent,workType = "")

# 获取单个作品信息
# JSON OK
# Work.getSingleWorkInfo(workId)

# 获取全部作品信息
# JSON OK
# Work.getWorkInfo()

# 更新作品名称
# JSON OK
# Work.updateWorkName(workId,newWorkName)

# 更新作品内容
# JSON OK
# Work.updateWorkContent(workId,newWorkContent)

# 更新作品分类
# JSON OK
# Work.updateWorkType(workId,newWorkType)

# 删除作品信息
# JSON OK
# Work.deleteWork(workId)

# 获取用户的作品
# JSON OK
# Work.getUserWork(workId)

import pymysql
from Type.Type import Type
from Works.WorkComment import WorkComment
import json


class Work:

    # 获取单个作品信息
    def getSingleWorkInfo(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work WHERE WorkId = \"" + workId + "\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            results = results[0]
            result = {}
            jsonData = []
            result["workId"] = results[0]
            result["workName"] = results[1]
            result["workContent"] = results[2]
            result["workType"] = results[3]
            result["userId"] = results[4]
            jsonData.append(result)
            print(jsonData)
            return jsonData
        except:
            print("Error: unable to get workInfo")

    # 获取全部作品
    def getWorkInfo():
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result["workId"] = row[0]
                result["workName"] = row[1]
                result["workContent"] = row[2]
                result["workType"] = row[3]
                result["userId"] = row[4]
                jsonData.append(result)
            return jsonData
        except:
            print("Error: unable to get workInfo")

    # 添加作品信息
    def insertWork(workName,workContent,userId,workType = ""):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "INSERT INTO Work(workName,workContent,userId,workType) VALUES('%s','%s','%s','%s');"% \
        (workName,workContent,userId,workType);
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except Exception as e:
            print(e)
            print("Error: unable to insert work")

    # 更改作品名称
    def updateWorkName(workId,newWorkName):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workName = \""+newWorkName+"\" WHERE workId = \""+workId+"\";";
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except:
            print("Error: unable to fetchall userPrefer")

    # 更改作品内容
    def updateWorkContent(workId,newWorkContent):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workContent = \""+newWorkContent+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except:
            print("Error: unable to fetchall userPrefer")

    # 更改作品分类
    def updateWorkType(workId,newWorkType):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "UPDATE Work SET workType = \""+newWorkType+"\" WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except:
            print("Error: unable to fetchall userPrefer")

    # 删除作品
    def deleteWork(workId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "DELETE FROM Work WHERE workId = \""+workId+"\";"
        try:
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            results = Work.getWorkInfo()
            return results
        except:
            print("Error: unable to fetchall userPrefer")

    # 获取用户的作品
    def getUserWork(userId):
        conn = pymysql.connect(
            host="gz-cynosdbmysql-grp-56sj4bjz.sql.tencentcdb.com",
            user="root",
            port=25438,
            password="Lcx010327",
            database="Hokkien");

        # 创建游标
        cursor = conn.cursor();
        sql = "SELECT * FROM Work WHERE userId = \""+userId+"\";"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in results:
                result = {}
                result["workId"] = row[0]
                result["workName"] = row[1]
                result["workContent"] = row[2]
                result["workType"] = row[3]
                result["userId"] = row[4]
                jsonData.append(result)
            return jsonData
        except:
            print("Error: unable to fetchall userPrefer")


if __name__ == "__main__":
    Work.getSingleWorkInfo("10004")
    # results = Work.insertWork("666", "1234567890", "12", workType="")
    # print(results[len(results)-1]['workId'])