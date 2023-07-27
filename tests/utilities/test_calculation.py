from utilities.calculation import Calculation
from utilities.user import User


def test_get_user_history_empty_state():
    Calculation.clear()
    User.clear()

    name = "test"
    email = "test@test.com"
    password = "98765abc"

    user = User()
    user.register(name, email, password)
    login = user.login(email, password)
    user_id = list(login)[0]
    sut = Calculation()
    result = sut.get_user_history(user_id)
    assert result == []
