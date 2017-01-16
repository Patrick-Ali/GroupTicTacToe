# Code from Week 6 getting_select.py by Doctor David Croft has been incorperated into this server

# Helpful Websites:
# https://docs.python.org/3/library/select.html
# https://mail.python.org/pipermail/tutor/2013-May/095756.html
# http://code.activestate.com/recipes/408997-when-to-not-just-use-socketclose/

import socket, select, random # Importing socket and select which will form the basis of the server and the  random module will be used to determine whop goes first        


# This is the server code stored in the class 'Chat', making them all an object of chat
class Chat:

	""" This class is designed to run the server code as for every instance of this class they will have a socket which can be used to allow clients to connect to the server """
	
	def __init__(self, port=12346): # This part of the code will activate everytime class 'Chat' is ran as this creates the socket, opens the port and listens for the clients

		""" This function builds the socket for each instance of this class by taking in the port number, which is already provided """

		self.connections = [] # Create an empty list that the client connections will be stored in

		self.server = socket.socket() # Create the server socket 
		
		self.server.bind(('', port)) # This bind the server to the machine it is currently working on and the port already stated 

		self.server.listen(2) # This tells it to listen for two clients only, as for the game you only want two people to connect and no one eles                 

	
	def shutdown(self): # This shuts the server down when certain actions have been taken, like keyboard interupt or restarting the server

		""" This function closes the socket that was created in the above function and all connections linked to that socket """

		for c in self.connections: # Closes all connections in the self.connections list
			
			c.close() # This means connection close, as in for all connections in the connections list it should shut them down

		self.server.shutdown(1) # This stops the server sending any messages as indicated by the one
		
		self.server.close() # This stops the server reciving any messages


	def poll(self): # This allows for multiplexing, which means that it will send the infromating to select machines and not all machines

		""" This function allows for the back and forth communication between the clients, so that clients can send and recive messages as the server relays them """
		
		while True: # Loops the main server code until the keyboard interupt is activated, this way clients can disconect and then reconect without the server shutting down

			
			try: #This tells the server to try the following code

				
				# As part of the select module this tells the code to read (intake) information from self.connections and the server (self.server)
				# It also tells the server that it can write to the following connections, in this case anything in self.connections
				# Also it can recive errors from the clients connected to it, in this case errors will come from self.connections
				# The number at the end represents the time in which the server should wait for a reply in miliseconds, in this case it is 0
				# This way it will not block the connections when the time runs out as it allows for imediate connection
				read, write, error = select.select( self.connections+[self.server], self.connections, self.connections, 0 )
				

				n = random.randint(1, 2) # This is what is used to determine which connections are player one and player two

				First = "Player 1, Choose Marker, X or O" # This is the message that it will send to player one
				
				Seond = "Player 2" # This is the message that it will send to player 2

				count = 0 # This will be used in a calculation to determine the number of people connected
				
				try: #This tells the server to try the following code
					
					for conn in read: # for connections in the list 'read' it should do the following
						
						
						 if conn is self.server: # if the connection is itself then thge server will execute the following code
							 
							 print('Connected!')  # This prints to the server not the client, as it shows that a client has connected successfuly

							 
							 c, addr = conn.accept() # This tells the server to acceppt clients by saying connection address connection accept
									     
							 self.connections.append(c) # Updates the self.connections list so that it has a connection init 
							
							 for i in range (len(self.connections)):
								 count += 1

														
							 if count == 2:

								 # Using the random module from earlier in the code it should randomly select who is player one
								 if n == 1:
									 self.connections[1].send(First.encode('utf-8')) # if n is 1 then allow connection two to be player 1
									 self.connections[0].send(Seond.encode('utf-8')) # if n is 1 then allow connection one to be player 2
									
								 elif n == 2:
									 self.connections[0].send(First.encode('utf-8')) # if n is 2 then allow connection one to be player 1
									 self.connections[1].send(Seond.encode('utf-8')) # if n is 2 then allow connection two to be player 2
													

						 
						 else: # If the connection is not the server then this code should activate
							 
							# The following block of code is a receptor for server, as anything the client sends this recies it
							
							 msg = conn.recv(1024) # Message is connection receve              
							 msg = msg.decode('utf-8').rstrip('\r\n') # Turn it from a string of binary numbers into something readable by humans       

							 # These variables are for the inital phase of the game where player one selects their marker
							 X = "You are X, please wait for player 1"
							 O = "You are O, please wait for player 1"

							 # This send player ones selection to player 2 so that they know what marker they are                                                   
							 for other in self.connections:
									 if other != conn and msg == "O":
										 other.send( X.encode('utf-8'))
									 elif other != conn and msg == "X":
										 other.send( O.encode('utf-8'))

							
							 if msg == 'X' or msg == 'O': # This makes sure that the marker does not go to player 1, essentialy a safety net
								 continue # This takes us back to the beginning of loop so that the server does not send this message to player 1

							# This begins restarting the server so as to reset all the variables 
							 if msg == "EXIT":
								 print ("\n" * 50)
								 Chat.shutdown(self)

							 rtrnmsg = msg # The following code generates the message that will be sent to other player
							 
							 print( '%s -> %s' % (msg,rtrnmsg)) # This prints on the server to show what message is being sent

								  
								
							# The following code makes sure that the message is only being sent to connections other than
							# the one connected, i.e. if it is player ones turn then they will send it to player 2 and not recive it self
							 for other in self.connections:
								 if other != conn:
									 other.send( rtrnmsg.encode('utf-8') ) # This turns the message we are sending into binary bits that a computer can read.
																	 
								

				# This will specificaly look for the 'can't send message' error in windows and begin the process of restating the server
				except OSError as e: # Checks for operating system errors in relation to the server as they happen and saves them as e
					if e.winerror == 10057:
						Chat.poll(self)
					elif e.winerror == 10054:
						Chat.poll(self) 
						
			# The above exception soloution results in a ValueError whihc this one should catch and then restart this method allowing for clients to connect and disconet as they wish wihtout the server crashing.
			except (ValueError):
				self.connections = [] # Makes the connection list empty
				continue
			
		
			

# This is what will activate the chat server when run                  
if __name__ == '__main__':
        try:
                try:
                        c = Chat()
                        while True:
                                c.poll()
                except KeyboardInterrupt:
                        c.shutdown() # This shuts down the server but triggers an error of loss of connection which will trigger the below error handler to initate the final part of shutting the server down
		
        except OSError as e: # Checks for operating system errors in relation to the server as they happen and saves them as e
                if e.winerror == 10057:
                         exit() # As when we press Ctrl-C we want to exit the program and essentialy shut the server down it will generate a connection failure error which will trigger this which will close the server down
	
							
