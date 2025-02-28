'''
A simple P2P Messager using TCP protocols.

I'll start in python with two sockets (one for sending, one for receiving)
I'll also start by keeping it in the console, and just text.

Later, I'll make a tkinter gui and maybe image sending, or even audio. Maybe even
video calls if I'm feeling crazy. Don't know how all of this is gonna work, but it shouldn't be crazy. 

So, yeah. I guess I'll test it by getting jack or dad or someone to run it on the other end. 
'''


'''
So, I'll have two sockets: one for sending and one for receiving. I think. This requires some multithreading, 
which will definitely be annoying, but I think I can get it down. 

I guess all that's needed right now is to establish a connection and then let messages be sent. Idk. 
    The receive thread waits for a message and unpacks it and prints it. 
    The send thread waits for a message to send and, well, sends it. 

Why is this multithreading? I guess you can't really send a message and receive one at the same time otherwise. 
It'd be nice if you could just bind the events. Idk, I'll figure out how that stuff works. 

It'd be nice if I could just use my other laptop for testing. I think I'll try that. 
'''