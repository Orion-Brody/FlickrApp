
import flickrapi
import webbrowser


api_key = u'03674b2d1d2a403fcdb92551d4115f2f'
api_secret = u'89f0e506842b6674'

user_id = input("Enter Username:") #stores username input as the user_id. 

flickr = flickrapi.FlickrAPI(api_key, api_secret, username=user_id) #initialize flickr client instance.

flickr.authenticate_via_browser() #authenticates the flickr user, has the user check in online. 

print(flickr.trait_names)










	


