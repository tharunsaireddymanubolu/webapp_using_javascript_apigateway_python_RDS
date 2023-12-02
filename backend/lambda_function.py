import pymysql
import sys
import boto3
import os
import json

def lambda_handler(event, context):

    data = json.loads(event['body'])
    name = data['name']
    email = data['email']
    age = data['age']
    feedback = data['feedback']
    rating = data['rating']
    
    status = "Success"
    code = "200"
    message = "Survey Submitted Successfully"
    
    ENDPOINT="Your End RDS ENDPOINT"
    PORT="3306"
    USER="admin"
    REGION="us-east-1"
    DBNAME="customers"
    
    try:
        conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd="Your DB Password", port=int(PORT), database=DBNAME)
        cur = conn.cursor()
        cur.execute("""INSERT INTO customers.customer (name, email, age, feedback, rating) VALUES (%s, %s, %s, %s, %s)""", (name, email, age, feedback, rating))
        conn.commit()
    
        #cur.execute("""SELECT * from customers.customer""")
        #query_results = cur.fetchall()
        #for row in query_results:
            #print(row[0])
        

    except Exception as e:
        print("Database connection failed due to {}".format(e)) 
        status = "Failed"
        code = "400"
        message = "Failde To Submit Survey"

    finally:
        cur.close()
        conn.close()
    
    res = {}
    res['Id'] = code
    res['Status'] = status
    res['message'] = message
    
    response_data = {
        'statusCode': 200,
        'body': json.dumps(res),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET, PUT, DELETE',
        },
    }
    
    return response_data
    
