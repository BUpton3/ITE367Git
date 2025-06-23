from app import app
def test_home_page():
	'''
	GIVEN a flask application configured for testing
	WHEN the '/' page is requested (GET)
	THEN check that the response is valid
	'''
	flask_app = app
	# create a test client using the flask application configured for testing
	with flask_app.test_client() as test_client:
		response = test_client.get('/login')
		assert response.status_code == 200
		assert b"Sign In" in response.data
		assert b"Click to Register" in response.data