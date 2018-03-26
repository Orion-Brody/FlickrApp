# import flickrapi 

# api_key = u'03674b2d1d2a403fcdb92551d4115f2f'
# api_secret = u'89f0e506842b6674'

# flickr = flickrapi.FlickrAPI(api_key)


# class Login(username, password):
# 	print("Enter Username:")
# 	if 

class Number_Storer(object):

	def  __init__(self, number):
		self.number = number

#TODO:FOR ALL METHODS IN WRAPPER CLASS: PASS IN AUTHENTICATION KEY!!!!
	def check_number(self, other_number):
	
		if other_number > self.number:
			print(other_number)
		else:
			print(self.number)

		

	

trial = Number_Storer(2341)
trial.check_number(1000)


	


