from cryptography.fernet import Fernet
import base64
#key = Fernet.generate_key()
#f = Fernet(key)
#msg = "THIS IS A SECRET"
#token = f.encrypt(msg.encode())
#print("the encrypted token is ", token.decode())
#decrypted = f.decrypt(token).decode()
#print("The decrypted msg is ", decrypted)

class DataRepo():

	def __init__(self):
		pass

	def get_users(self):
		pass

class MessageHandler():
	"""Encrypts or Decrypts the message"""
	def __init__(self, key = Fernet.generate_key()):
		self.key = key
		self.fernet = Fernet(self.key)
	
	def get_key(self):
		return self.key

	def msg_encrypter(self, msg : str):
		"""Encrypts the message"""
		encrypted_msg = self.fernet.encrypt(msg.encode())
		return encrypted_msg.decode()

	def msg_decrypter(self, encrypted_msg : str):
		"""Decrypts the encrypted msg"""
		decrypted_msg = self.fernet.decrypt(encrypted_msg.encode())
		return decrypted_msg.decode()


class User():
	"""USER CRUD"""
	def __init__(self, name, password):
		self.name = name
		self.password = password
		self.key = None

	def create_key(self):
		"""Making key"""
		key_str = f"{self.name}%2D{self.password}"
		key_str_bytes = key_str.encode("utf-8")
		bs64_version = base64.b64encode(key_str_bytes)
		self.key = bs64_version
		return bs64_version

	def crypto_key(self):
		self.key = Fernet.generate_key()

	def save_new_user(self):
		"""New user creation"""
		#if user not in Users file save it in the user file
		pass
		
	def get_key(self):
		return self.key
	
def main():
	user_name = input("Enter username: ")
	user_password = input("Enter password: ") 
	user = User(user_name, user_password)
	print(user.crypto_key())
	print("Type of the key: ",type(user.get_key()))
	message_handler = MessageHandler(user.get_key())
	message_from_user = input("Enter some text to be saved: ")
	encrypted = message_handler.msg_encrypter(message_from_user)
	print("The Key is : ", message_handler.get_key()) 
	print("The Encrypted message is: ", encrypted)
	decrypted = message_handler.msg_decrypter(encrypted)
	print("THe decrypted message is: ", decrypted)
	

if __name__ == "__main__":
	main()
		
