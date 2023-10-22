from db.tables import (
    users,
    friends,
    chats,
    chat_members,
    messages
)
from models import (
    User,
    Friend,
    Chat,
    ChatMember,
    Message
)
from conftest import async_session


async def test_users():
    async with async_session() as session:
        login = "test_login"
        password = "test_password"
        user = await users.create_user(session, login, password)
        assert isinstance(user, User)
        user_read = await users.get_user_by_id(session, user.id)
        assert user_read.id == user.id
        old_login = user.login
        user_update = await users.update_user(session, user.id, login="update_login")
        assert user_update.id == user.id
        assert user_update.login != old_login
        user_delete = await users.delete_user(session, user.id)
        assert user is user_update
        assert user is not user_delete
        total_user = await users.get_user_by_id(session, user.id)
        assert total_user is None


async def test_friends():
    async with async_session() as session:
        login1 = "test_login1"
        login2 = "test_login2"
        password = "test_password"

        user1 = await users.create_user(session, login1, password)
        user2 = await users.create_user(session, login2, password)

        assert user1.id != user2.id

        friend1 = await friends.create_friend(session, user1.id, user2.id)
        friend2 = await friends.create_friend(session, user2.id, user1.id)

        assert friend1.friend_id != friend2.friend_id

        user1_friend_list = await friends.get_friends_by_user_id(session, user1.id)
        assert isinstance(user1_friend_list, list)
        assert len(user1_friend_list) == 1
        assert user1_friend_list[0].friend_id == user2.id

        user2_friend_list = await friends.get_friends_by_user_id(session, user2.id)
        assert isinstance(user2_friend_list, list)
        assert len(user2_friend_list) == 1
        assert user2_friend_list[0].friend_id == user1.id

        user1_friend_delete = await friends.delete_friend(session, user1.id, user2.id)
        assert user1_friend_delete.friend_id == user2.id

        user2_friend_delete = await friends.delete_friend(session, user2.id, user1.id)
        assert user2_friend_delete.friend_id == user1.id


async def test_chats():
    async with async_session() as session:
        chat = await chats.create_chat(session)

        chat_get = await chats.get_chat_by_id(session, chat.id)
        chat_delete = await chats.delete_chat(session, chat_get.id)
        assert chat_get.id == chat_delete.id

        chat_get = await chats.get_chat_by_id(session, chat.id)
        assert chat_get is None


async def test_chat_members():
    async with async_session() as session:
        login = "test_login"
        password = "test_password"
        user = await users.create_user(session, login, password)
        chat = await chats.create_chat(session)

        chat_member = await chat_members.create_chat_member(session, user.id, chat.id)
        assert chat_member.chat_id == chat.id
        assert chat_member.user_id == user.id

        chat_members_in_chat = await chat_members.get_chat_members_by_chat_id(session, chat.id)
        assert chat_member in chat_members_in_chat

        chat_member_delete = await chat_members.delete_chat_member(session, user.id, chat.id)
        assert chat_member_delete.id == chat_member.id

        chat_members_in_chat = await chat_members.get_chat_members_by_chat_id(session, chat.id)
        assert isinstance(chat_members_in_chat, list)
        assert len(chat_members_in_chat) == 0


async def test_messages():
    async with async_session() as session:
        login = "test_login"
        password = "test_password"
        text_message = "message_text"
        user = await users.create_user(session, login, password)
        chat = await chats.create_chat(session)

        message = await messages.create_message(session, text_message, user.id, chat.id)
        assert message.text == text_message
        assert message.user_id == user.id
        assert message.chat_id == chat.id

        message_get = await messages.get_message_by_id(session, message.id)
        assert message is message_get

        update_text_message = "update_message"
        message_update = await messages.update_message(session, message.id, text=update_text_message)
        assert message_update.text == message.text

        message_delete = await messages.delete_message(session, message.id)
        assert message.id == message_delete.id

        message_get = await messages.get_message_by_id(session, message.id)
        assert message_get is None
