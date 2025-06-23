from app.models import User

def test_new_user():
	user = User('jjack', 'jjack@athens.edu', 'Qwerty123')
	assert user.username == 'jjack'
	assert user.email == 'jjack@athens.edu'
	assert user.password_hash == 'Qwerty123'
def test_setting_password(new_user):
	new_user.set_password('MyNewPassword')
	assert new_user.password_hash != 'MyNewPassword'
	assert new_user.check_password('MyNewPassword')
	assert not new_user.check_password('MyNewPassword2')


