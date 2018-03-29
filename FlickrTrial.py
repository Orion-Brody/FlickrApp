
import flickrapi
import webbrowser


api_key = u'03674b2d1d2a403fcdb92551d4115f2f'
api_secret = u'89f0e506842b6674'

flickr = flickrapi.FlickrAPI(api_key, api_secret) #initialize flickr client instance.
# flickr.get_request_token()
# flickr.authenticate_via_browser()
print(flickr.token_valid())
# url = flickr.auth_url()
# webbrowser.open(url)
# token = flickr.get_access_token()

# flickr.flickr_oauth.get_request_token()
# flickr.flickr_oauth.auth_for_test(perms=perms)
# token = flickr.flickr_oauth.get_access_token()
# flickr.token_cache.token = token







	


