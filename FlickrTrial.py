

# my_number = 100

# def check_number( other_number):
	
# 	if other_number > my_number:
# 		print(other_number)
# 	else:
# 		print(my_number)

# check_number(101)






















import flickrapi 





def initialize(api_key, api_secret):
	
	return flickrapi.FlickrAPI(api_key) #initialize flickr client instance.
	

def authenticate(api_key, api_secret, flickr):
	#todo: 
	

	auth = flickrapi.Auth() #creates an instance of the Auth class.
	frob = auth.getFrob() #frob is used for authentication.
	#login_link = auth.loginLink(permission, frob) commented out because unsure what a "permission" is 
	return auth.getToken(frob) #token is used for API method calls. 



api_key = u'03674b2d1d2a403fcdb92551d4115f2f'
api_secret = u'89f0e506842b6674'

flickr = initialize(api_key, api_secret)

token = authenticate(api_key, api_secret, flickr)




	


