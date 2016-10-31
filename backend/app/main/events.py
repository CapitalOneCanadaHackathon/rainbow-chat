from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from app import ROOMS

@socketio.on('joined', namespace='/chat')
def joined(message, room):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    join_room(room)

    print(room)
    emit('room', {'msg': room})
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)

@socketio.on('text', namespace='/chat')
def text(message, room):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    # room = session.get('room')

    print('---------------------------')
    print(room)
    emit('message', {'msg':  message['msg'], 'room': room['room'], 'name': session.get('name')}, room=room['room'])
    #emit('message', {'msg': session.get('name') + ':' + message['msg'], 'room': room['room']}, room=room['room'])


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

