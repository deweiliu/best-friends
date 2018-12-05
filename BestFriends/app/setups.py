def setups():
    database_setup()

##############################################################
# Azure database setup
from app.database.azure_database import AzureDatabase
def database_setup():
    print("Setting up database")

    # table to store users' information
    AzureDatabase.create("USERS","user_id INTEGER PRIMARY KEY","firstname VARCHAR(20)","surname VARCHAR(20)")

    # table to store users' credentials for accessing bot servie
    AzureDatabase.create("CONVERSATIONS","conversation_id VARCHAR(40) PRIMARY KEY","user_id INTEGER","token VARCHAR(200)","watermark VARCHAR(8)","FOREIGN KEY(user_id) REFERENCES USERS(user_id)")
    
    # table to store users' conversation history
    AzureDatabase.create("MESSAGES","user_id INTEGER","message_index INTEGER","is_from_user BIT","sender_name VARCHAR(20)","datetime SMALLDATETIME","message VARCHAR(400)","PRIMARY KEY (user_id, message_index)","FOREIGN KEY (user_id) REFERENCES USERS(user_id)")

    # table to store comments from the birthday page
    AzureDatabase.create("BIRTHDAYCOMMENTS","username VARCHAR(40) PRIMARY KEY","comment VARCHAR(200)","datetime VARCHAR(50)")
