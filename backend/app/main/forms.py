from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class EnterChatroom(Form):
    """Accepts a nickname and a room."""
    submit = SubmitField('Enter Chatroom')
    
class InitializeChatrooms(Form):
    submit = SubmitField('Ready to chat')
