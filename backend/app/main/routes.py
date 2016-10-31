from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import EnterChatroom, InitializeChatrooms

EMPTY_ROOMS = [i for i in range(1000)]
VOLUNTEER_ROOMS = []


@main.route('/', methods=['GET', 'POST'])
def index():
    """"Login form to enter a room."""
    form = EnterChatroom()
    if form.validate_on_submit():
        session['name'] = 'Anonymous'
        print('---------------')
        print(session)
        print(session.__dict__)
        print('---------------')
        if VOLUNTEER_ROOMS:
            room = VOLUNTEER_ROOMS.pop()
            return render_template('chat.html', name=session.get('name'), rooms=[room])
        else:
            print("BAHHHHHH")
    return render_template('index.html', form=form)


# @main.route('/chat')
# def chat():
#     """Chat room. The user's name and room must be stored in
#     the session."""
#     name = session.get('name', '')
#     if name == '':
#         return redirect(url_for('.index'))
#     return render_template('chat.html', name=name, room=rooms)

@main.route('/volunteer', methods=['GET', 'POST'])
def volunteer_welcome():
    form = InitializeChatrooms()
    if form.validate_on_submit():
        session['name'] = 'Volunteer'
        print('---------------')
        print(session)
        print(session.__dict__)
        print('---------------')
        if EMPTY_ROOMS:
            room1 = EMPTY_ROOMS.pop()
            room2 = EMPTY_ROOMS.pop()
            VOLUNTEER_ROOMS.extend([room1, room2])

            return render_template('chat.html', name=session.get('name'), rooms=[room1, room2])
        else:
            print("BAHHHHHH")
    return render_template('volunteer.html', form=form)

