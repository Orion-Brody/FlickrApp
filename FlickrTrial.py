import flickrapi 


def initialize(api_key, api_secret):
	
	return flickrapi.FlickrAPI(api_key, api_secret) #initialize flickr client instance.
	

def authenticate(flickr):

	# auth = flickrapi.OAuth() #creates an instance of the OAuth class.
	# frob = auth.getFrob() #frob is used for authentication.
	# #login_link = auth.loginLink(permission, frob) commented out because unsure what a "permission" is 
	# return auth.getToken(frob) #token is used for API method calls. 

	flickr.authenticate_via_browser(perms='read')






api_key = u'03674b2d1d2a403fcdb92551d4115f2f'
api_secret = u'89f0e506842b6674'

flickr = initialize(api_key, api_secret)

authenticate(flickr)




	


