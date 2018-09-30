from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from json import dumps
#from flask.ext.jsonpify import jsonify
from flask import jsonify
import MySQLdb
import re

app = Flask(__name__)
api = Api(app)

class Add(Resource):
	def get(self):
		ip = request.args.get('ip')
                r=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
                if r:
                    db = MySQLdb.connect("localhost","root","@19135nm","test")
                    cur = db.cursor()
                    cur.execute("SELECT test FROM test;")
                    results = cur.fetchall()
                    a=1
                    for i in results:
                        if i[0] == ip :
                            a=0
                    if a == 1:
                        sql="INSERT INTO `test` (test) VALUES (\"%s\");" %ip
                        cur.execute(sql)
                        db.commit()
                    else:
                        return "IP already in the list"
	            sql1="SELECT test FROM test;"
	            cur.execute(sql1)
	            db.commit()
	            data = cur.fetchall()
                    cur.close()
	            db.close()
	            return jsonify(data)
                else:
                    print "Please provide valid IP"
                    return "Invalid IP format"


class Delete(Resource):
        def get(self):
                ip = request.args.get('ip')
                r=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
                if r:
                    db = MySQLdb.connect("localhost","root","@19135nm","test")
                    cur = db.cursor()
                    cur.execute("SELECT test FROM test;")
                    results = cur.fetchall()
                    a=1
                    for i in results:
                        if i[0] == ip :
                            a=0
                    if a == 0:
                        sql="DELETE FROM `test` WHERE test=\"%s\";" %ip
                        cur.execute(sql)
                        db.commit()
                    else:
                        return "IP not in the list"
                    sql1="SELECT test FROM test;"
                    cur.execute(sql1)
                    db.commit()
                    data = cur.fetchall()
                    cur.close()
                    db.close()
                    return jsonify(data)
                else:
                    print "Please provide valid IP"
                    return "Invalid IP format"



class List(Resource):
        def get(self):
                db = MySQLdb.connect("localhost","root","@19135nm","test")
                cur = db.cursor()
                sql="SELECT test FROM test;"
                cur.execute(sql)
                data = cur.fetchall()
                cur.close()
                db.close()
                return jsonify(data)



api.add_resource(Add,'/add')
api.add_resource(Delete,'/delete')
api.add_resource(List,'/list')
app.run(debug=True ,port='5002')
