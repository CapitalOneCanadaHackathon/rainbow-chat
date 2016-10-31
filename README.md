PflagChat! (A.K.A Rainbow.Chat)

IDEA:
This is a project that was developed during the Gift The Code Hackathon Weekend.  It is intended for use by Pflag Toronto. The intent of this project was to create an online chat platform that can act as a 'help line' in addition to the current phone help line that they provide.  The idea was that a link to this chat could be added to the Toronto Pflag website.  The chat would only be open during specific hours when it is known that volunteers will be available to chat. Each anonymous user who accesses the chat will be matched with one volunteer who they can chat with.  Each volunteer may have 2 (this is hard-coded but can be updated) anonymous users that they are speaking to at a time.

The tools we build this project out of:

* Backend: Flask (python) with the flask socket.io extension.
* Database:  We started using SQLite3 (which connects to flask via sqalchemy).  We actually instatiated a database, however we didn't get to hooking it up with our app, yet.
* Frontend: HTML, pure CSS, and of course Javascript (with JQuery).  No frontend framework.
* Design: A lot of our html and css components were borrowed from Material Design. The 'look' of our app is very Material-esk.  The 'Rainbow Chat' icon was developed by our talented team member Megan Hunter.  Please use them and love them.

To run this app, type the following comands into your terminal:
1) cd backend/
2) python chat.py
Then, in your browser, go to localhost:3000/volunteer (for the volunteer home page) and localhost:3000 (for the user homepage - the one that the pflag toronto website would link to)
Note that in order for the user to have anyone to talk to, the volunteer must enter the chatroom first (ideally users wouldn't be able to enter the chat room until a volunteer was there, but we ran out of time).  So, to view the work we have done, please first go to localhost:3000/volunteer and click on enter chatroom.  THEN go to localhost:3000 and click 'enter chatroom'.

Where to find the mock up for the admin page (which unfortunately did not get implemented due to lack of time):
* Mockups in general are found within the `public/` directory.
* Admin page is found at: `public/admin.html`.

As this was a hackathon, unfortunately development best practices were not always followed.  Please take what we have started and do your best to make it awesome.

With love,

Team Go.




