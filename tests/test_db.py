from db.tables import users, friends
from models import User, Friend
from conftest import async_session


async def test_users():
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


async def test_friends():
    async with async_session() as session:
        login1 = "test_login1"
        login2 = "test_login2"
        password = "test_password"

        users_layer = users.UsersLayer(session)
        user1 = await users_layer.create_user(login1, password)
        user2 = await users_layer.create_user(login2, password)

        assert user1.id != user2.id

        friends_layer = friends.FriendsLayer(session)
        friend1 = await friends_layer.create_friend(user1.id, user2.id)
        friend2 = await friends_layer.create_friend(user2.id, user1.id)

        assert friend1.friend_id != friend2.friend_id

        user1_friend_list = await friends_layer.get_friends_by_user_id(user1.id)
        assert isinstance(user1_friend_list, list)
        assert len(user1_friend_list) == 1
        assert user1_friend_list[0].friend_id == user2.id

        user2_friend_list = await friends_layer.get_friends_by_user_id(user2.id)
        assert isinstance(user2_friend_list, list)
        assert len(user2_friend_list) == 1
        assert user2_friend_list[0].friend_id == user1.id

        user1_friend_delete = await friends_layer.delete_friend(user1.id, user2.id)
        assert user1_friend_delete.friend_id == user2.id

        user2_friend_delete = await friends_layer.delete_friend(user2.id, user1.id)
        assert user2_friend_delete.friend_id == user1.id
