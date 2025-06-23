import pytest
from app import app
from app.models import User
@pytest.fixture()
def app():
	app.config.update({
		"TESTING": True,
	})
	yield app

@pytest.fixture()
def client(app):
	return app.test_client()

@pytest.fixture()
def runner(app):
	return app.test_cli_runner()

@pytest.fixture(scope='module')
def new_user():
	user = User('jjack', 'jjack@athens.edu', '123456')
	return user