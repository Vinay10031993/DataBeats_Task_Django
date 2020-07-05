# DataBeats_Task_Django



Prerequisites:
1. Ubuntu, Python 2.7, PIP


2. Create a Virtualenv

3. Activate virtual environment


Install dependencies:
pip install -r requirements.txt




RESTAPI'S
1. SQLLIte is in the project with db.sqlite3 file

2. Build a registration, and login APIs using a custom user model with mobile number with country code as input instead of an email address
url: http://127.0.0.1:8000/apis/signup/v1.0?phone=9876545678&country=IN&email=vv@hm.com&password=123456

For Registration:

Request-Type: POST

INPUT:Form-data
		   phone: 9883773662 ----> Mandatory
		   country: 'IN'  ----> Mandatory
		   password: 122344 -----> Mandatory
		   email: optional
OUTPUT:
{
    "notification": {
        "is_auth": true,
        "code": 200,
        "hint": "Success",
        "token": "gAAAAABfAibvuwdyxi-MxHU4uTB7f7a5WlFtCQ1CuJcAby_Ow0mzs6dqSNzZE9Wq5W_UWBvUsrff9js3ySZHMHquUxM0DNPgig==",
        "message": "User created successfully",
        "type": "Success"
    },
    "data": {}
}




For Login:
url: http://127.0.0.1:8000/apis/login/
Request-Type: POST

Input Type: JSON DATA
Input: 

{
    "phone":6424026819,
    "password": 12345
}

Output:
{
    "notification": {
        "message": "Success",
        "code": "200",
        "type": "Success",
        "is_auth": true,
        "hint": "Response Sent"
    },
    "data": {
        "country": "IN",
        "token": "gAAAAABfAiTVZ4KIdJmZ3Hcgx0K8qRJ1RynBx0ajZPfSCeASmwo_z02o1JTiXC8rGwSqKvXp9TFmTOm6M6NftHaCu6OldHKB5Q==",
        "user_id": 6,
        "email": null
    }
}



3. Build an OTP API for validation and verification


#########fOR GENERATING OTP##########
REQUEST-TYPE: POST
INPUT-TYPE: JSON

URL:  http://127.0.0.1:8000/apis/generate_otp/

INPUT: 
{
    "phone":6424026819
}

OUTPUT:
{
    "notification": {
        "message": "Success",
        "code": "200",
        "type": "Success",
        "is_auth": true,
        "hint": "Response Sent"
    },
    "data": {
        "otp": 121288
    }
}


##########FOR VALIDATING OTP ################


URL:  http://127.0.0.1:8000/apis/validate_otp/
INPUT: 

{
    "phone":6424026819,
    "otp": 121288
}


OUTPUT:
{
    "notification": {
        "message": "OTP Verification Successful",
        "message": "Success",
        "code": "200",
        "type": "Success",
        "is_auth": true,
        "hint": "Response Sent"
    },
    "data": {}
}





4. Build an API that will store the information to the database when the customer purchased an item. The information should consist of Name of the customer, date of purchase, product name, quantities, the total price, payment method

INPUT-TYPE: JSON

REQUEST-TYPE: PUT

INPUT:
{
    "items":[{
        "product_name":"Meptrate-650",
        "total": 120,
        "quantity": 12 
        },{
        "product_name":"HCGQ-650",
        "total": 300,
        "quantity": 5 
        },{
        "product_name":"CHlorophynine",
        "total": 360,
        "quantity": 12 
        }],
    "user_phone": 6424026819,
    "billed_total": 789,
    "payment_type": "CASH"


}



OUTPUT:

{
    "notification": {
        "is_auth": true,
        "code": 200,
        "hint": "Success",
        "token": null,
        "message": "Details Updated successfully",
        "type": "Success"
    },
    "data": {}
}




5. Build an API that displays all the products in a product category based on range price

INPUT-TYPE: JSON

REQUEST-TYPE: GET

INPUT:
ACCESS-TOKEN IN HEADERS


OUTPUT:
{
    "notification": {
        "message": "Success",
        "code": "200",
        "type": "Success",
        "is_auth": true,
        "hint": "Response Sent"
    },
    "data": [
        {
            "Price": "123.00",
            "Product_Type": "SYRUP",
            "Product_Name": "GELYUSIL",
            "Expiry": "22-2029"
        },
        {
            "Price": "92.00",
            "Product_Type": "SYRUP",
            "Product_Name": "ASCH0RIL",
            "Expiry": "22-2029"
        },
        {
            "Price": "43.00",
            "Product_Type": "GEL",
            "Product_Name": "OMNI GEL",
            "Expiry": "22-2023"
        },
        {
            "Price": "52.00",
            "Product_Type": "TAB",
            "Product_Name": "DOLO 650MG",
            "Expiry": "22-2029"
        },
        {
            "Price": "54.00",
            "Product_Type": "GEL",
            "Product_Name": "Safromacin",
            "Expiry": "22-2033"
        },
        {
            "Price": "12.00",
            "Product_Type": "TAB",
            "Product_Name": "DOLOKING 650MG",
            "Expiry": "22-2029"
        },
        {
            "Price": "250.00",
            "Product_Type": "POWDER",
            "Product_Name": "FISTPOWER POWDER 1KG",
            "Expiry": "22-2025"
        },
        {
            "Price": "22.00",
            "Product_Type": "TAB",
            "Product_Name": "Selmond 1mG",
            "Expiry": "22-2029"
        }
    ]
}



6. Describe the procedure, in brief, to connect Django REST Framework to 3rd party database servers and what changes need to be made in order to run it successfully
ANS:
In General, If two systems different systems needs a communication, the basic medium for the transfer of data is through the lightweight component JSON, We need to define some API's, where the data which we need to get the source should be secure and fast.usually when we are talking about a RESTful API we are referring to Web Services  It’s a common way to expose parts of your application to third-parties (external applications and Websites). It simply make available the information you store in your databases using a common format, such as XML or JSON. This way, an external application can interact with your application and your data, without having to connect directly into your database. This way, it doesn’t matter if your database is MySQL or PostgreSQL, or if your application was written in Java or Python. But RESTful APIs can also be used to modify data
