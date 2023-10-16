from db.tables import users, friends
from models import User, Friend
from conftest import async_session


async def test_user():
    async with async_session() as session:
        login = "test_login"
        password = "test_password"
        users_layer = users.UsersLayer(session)
        user = await users_layer.create_user(login, password)
        assert isinstance(user, User)
        user_read = await users_layer.get_user_by_id(user.id)
        assert user_read.id == user.id
        old_login = user.login
        user_update = await users_layer.update_user(user.id, login="update_login")
        assert user_update.id == user.id
        assert user_update.login != old_login
        user_delete = await users_layer.delete_user(user.id)
        assert user is user_update
        assert user is not user_delete
        total_user = await users_layer.get_user_by_id(user.id)
        assert total_user is None


