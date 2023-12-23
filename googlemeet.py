from flask import Flask, request
import pymongo

app = Flask(__name__)

# Enable CORS for jQuery requests
@app.after_request
def enable_cors(response):
	response.headers["Access-Control-Allow-Origin"] = "*"
	return response

# Handle POST requests from jQuery with multiple parameters
@app.route('/submitData', methods=['POST'])
def submit_data():
	global user
	global email
	global pswd
	global rpswd
	user = request.form.get('user')
	email = request.form.get('email')
	pswd = request.form.get('pswd')
	rpswd = request.form.get('rpswd')

	print(f"Received data from jQuery - user: {user}, email: {email}, pswd: {pswd}, rpswd:{rpswd}")

	# Perform additional processing as needed

	return [user, email, pswd, rpswd]



if __name__ == '__main__':
	app.run(port=5000)



mongo_uri = "mongodb+srv://mk7634044:Manish7666@cluster0.dlwpvps.mongodb.net/"
client = pymongo.MongoClient(mongo_uri)

# Access the database
db = client.webschool

# Create a collection
collection = db.login

# Insert documents into the collection
user_data = {"username": user, "email": email, "password": pswd, "re-password": rpswd}
user_id = collection.insert_one(user_data).inserted_id
print(f"Inserted document with ID: {user_id}")

# Find documents in the collection
#query = {"username": "john_doe"}
#result = collection.find_one(query)
#print(f"Found document: {result}")

# Find all documents in the collection
#all_users = collection.find()




#for user in all_users:
    #print(user)

# Close the connection
client.close()
