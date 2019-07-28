import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request, make_response
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
	if auth and auth.username == 'username' and auth.password == 'password':
	    return f(*args, **kwargs)

	return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})
    return decorated 
	
@app.route('/add', methods=['POST'])
@requires_auth
def add_emp():
	try:
		_json = request.json
		_userId = _json['userId']
		_jobTitleName = _json['jobTitleName']
		_firstName = _json['firstName']
		_lastName = _json['lastName']
		_preferredFullName = _json['preferredFullName']
		_employeeCode = _json['employeeCode']
		_region = _json['region']
		_phoneNumber = _json['phoneNumber']
		_emailAddress = _json['emailAddress']
		# validate the received values
		if _userId and _jobTitleName and _firstName and _emailAddress and request.method == 'POST':
			# save into db
			sql = "INSERT INTO tbl_emp(userId, jobTitleName, firstName, lastName, preferredFullName, employeeCode, region, phoneNumber, emailAddress) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			data = (_userId, _jobTitleName, _firstName, _lastName, _preferredFullName, _employeeCode, _region, _phoneNumber, _emailAddress)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Employee record added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emps')
@requires_auth
def emps():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT userId Id, jobTitleName title, firstName fName, lastName lName, preferredFullName fullName, employeeCode eCode, region reg, phoneNumber ph, emailAddress email FROM tbl_emp")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/emp/<id>')
def emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT userId Id, jobTitleName title, firstName fName, lastName lName, preferredFullName fullName, employeeCode eCode, region reg, phoneNumber ph, emailAddress email FROM tbl_emp WHERE employeeCode=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def update_emp():
	try:
		_json = request.json
                _userId = _json['userId']
                _jobTitleName = _json['jobTitleName']
                _firstName = _json['firstName']
                _lastName = _json['lastName']
                _preferredFullName = _json['preferredFullName']
                _employeeCode = _json['employeeCode']
                _region = _json['region']
                _phoneNumber = _json['phoneNumber']
                _emailAddress = _json['emailAddress']
		# validate the received values
		if _userId and _jobTitleName and _firstName and _emailAddress and _employeeCode and request.method == 'PUT':
			#save updates
			sql = "UPDATE tbl_emp SET userId=%s, jobTitleName=%s, firstName=%s, lastName=%s, preferredFullName=%s, region=%s, phoneNumber=%s, emailAddress=%s WHERE employeeCode=%s"
			data = (_userId, _jobTitleName, _firstName, _lastName, _preferredFullName, _region, _phoneNumber, _emailAddress, _employeeCode,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Employee record updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_emp WHERE employeeCode=%s", (id,))
		conn.commit()
		resp = jsonify('Employee record deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
#    app.run()
     app.run(host='0.0.0.0', port=80, debug=True)
