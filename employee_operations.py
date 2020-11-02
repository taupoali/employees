
import logging
import mysql.connector as mysql
import json

db = mysql.connect(
    host = "aurora-sls-mysql.cluster-caedhp1brovp.eu-west-1.rds.amazonaws.com",
    user = "admin",
    password = "Password1!",
    database = "employees"
)

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"The error '{e}' occurred")


def lambda_handler(event, context):
    if 'body' in event:
        print("Detected body")
        print("The type of event is: {}".format(type(event)))
        extractedbody = event['body']
        print("The type of extractedbody is: {}".format(type(extractedbody)))
        print("The value of extracted body is: {}".format(extractedbody))
        jsonextractedbody = json.loads(extractedbody)
        print("The type of jsonextractedbody is: {}".format(type(jsonextractedbody)))
        print("The value of jsonextractedbody is: {}".format(jsonextractedbody))
        fname = jsonextractedbody['fname']
        print("fname is: {}".format(fname))
    
    if 'fname' in event:
        print("Found fname directly in dict")
        fname = event['fname']

    select_users = 'SELECT first_name, last_name FROM employees WHERE first_name = "'+ fname + '"'
    users = execute_read_query(db, select_users)
    
    #for user in users:
    #    print(user)
    #    pass
    
    response = {
        "statusCode": 200,
        "headers": {
            "myheader": "my_value"
        },
        "body": json.dumps(users),
        "isBase64Encoded": false 
    }


    return(users)