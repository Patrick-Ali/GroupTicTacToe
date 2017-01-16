from tkinter import * # Python module which allows the creation of a GUI 
from random import randint # Python module which provides a random number generator 
from tkinter import ttk # Libary of the python module tkinter which is used for widgets such as combobox's
import time   # Python module which has access to local time providing an easy way to implement timed delays in my program
import socket # Python Module which allows the code to create a socket which can be used to connect to a server 

CANVAS_WIDTH= 600 #Global fixed variable: Sets a max width for the creation of the canvas
CANVAS_HEIGHT= 600 #Global fixed variable: Sets a max height for the creation of the canvas
check_l_O=[]
check_l_X=[]
rol=10

class AI():
	def __init__(self,Window):
		self.Turn = Window.Turn
		self.AIturn = Window.AIturn
		self.x = Window.x
		self.y = Window.y
		self.x0 = Window.x0
		self.x1 = Window.x1
		self.x2 = Window.x2
		self.win = False
		
	def Win(self):
		
		pass 
				
	def Move(self):
		check = False
		while check == False:
			self.x = randint(0,2)
			self.y = randint(0,2)
				  
			
			if self.x == 0:
				for n,i in enumerate(self.x0): #Gets the index of each item in the list 
					if i==self.y: # checks to see if the index of the list is the same as the Y coordinate 
						self.x0[n]=self.Turn # Assigns the the Current turn to the item of that index in the list
						print(self.x0,self.x1,self.x2)
						check = True
						return True # So the draw function within the window class knows if there already is a X or O in that position or not
						
						
			elif self.x == 1: #Repeated as above for the next list
				for n,i in enumerate(self.x1):
					if i==self.y:
						self.x1[n]=self.Turn
						print(self.x0,self.x1,self.x2)
						check = True
						return True
					
						
			elif self.x == 2: #Repeated as above for the next list
				for n,i in enumerate(self.x2):
					print(n,i)
					if i==self.y:
						self.x2[n]=self.Turn
						print(self.x0,self.x1,self.x2)
						check = True
						return True
	
	
		
		

class Game(): #This class consists of game mechanics
	def __init__(self,Window):
		self.Turn = Window.Turn #inherited Turn from Window class
		self.x = Window.x #inherited x from Window class
		self.y = Window.y #inherited y from Window class
		self.x0 = Window.x0 #inherited board from Window class
		self.x1 = Window.x1
		self.x2 = Window.x2

	def transform_cord(self,x):
		global rol,check_l_O,check_l_X

		if rol<=30:      # The STOP of the recursion!

			check_l_OO=check_l_O             # Updating local variables to current state in order to append new cord
			check_l_XX=check_l_X
			z=0                                # Variable used to convert to row/col cordinates (Number:2)
			for el in x:                       # Iterate through current list and checks if a cord. is taken by "O" or "X"
				if el!=z:
					if el=="O":
						check_l_OO.append(rol+(z+1)) # If the cord. is taken by "O" use LocalVar(z,rol) to convert it in row/col cord.
					else:
						check_l_XX.append(rol+(z+1)) # If the cord. is taken by "X" use LocalVar(z,rol) to convert it in row/col cord.
				z+=1
		rol+=10
		if rol==20:
			Game.transform_cord(self,self.x1)                   # Calls the function with the second list
		elif rol==30:
			Game.transform_cord(self,self.x2)                   # Calls the function with the third list
		else:
			rol=10
			check_l_O= list(set(check_l_O+check_l_OO))
			check_l_X= list(set(check_l_X+check_l_XX))
			print(check_l_O,check_l_X)




	def check(self):

		turn_p = self.Turn                      # Check if it is the first turn or not  #!!!!!!!!!!!!!!!!!!!!

		check_win=False                  # Check if someone has won
		check_l=[]                       # Adjusts the function to work with the two check_lists //line 21-22
		global check_l_O
		global check_l_X


		Game.transform_cord(self,self.x0)

		if turn_p == "O":
			check_l=check_l_O
		else:
			check_l=check_l_X

		row="row_1"          # A key for accessing the  dictionary
		col="col_1"          # A key for accessing the  dictionary
		cord={"row_1":0,"row_2":0,"row_3":0,"col_1":0,"col_2":0,"col_3":0}
		digit=0                          # The digit check (0-row/1-col)
		n=1                              # Defines the number of the row or col, depending on the digit (checking number)
		row_or_col=row                   # Changes the function to work with row or col (lines 64/65)
		print(check_win,2)
		count=0
		while count!=6:        # works till the iteration is done (6 updates) 3 for row and 3 for col
			count+=1
			if n>3:                          # Switches the iteration to "col" after its done with the "row"
				digit=1                      # The "col" is in the second digit so it switches to index[1]
				n=1                          # reset checking number (referred in line 82)
				row_or_col=col               # Switches the key for the dict. to work with "col"

			for el in check_l:               # iterates every element in the list

				check_l_el=str(el)
				if check_l_el[digit] == str(n):    # Checks the elements | digit=0 ro "row" | digit=1 for "col"
					cord[row_or_col]+=1        # ~~~~~~~~~~~~~~~~~~~1)

			n+=1                             # upgrade the counter, up to 3, since there are 3 rows and 3 cols in the board
			row_or_col=row_or_col[:4]+str(n) # update the dict. key

		z=0
		x=(11,33,22,13,31) #CHECKS THE "diagonal' COMBINATIONS

		for el in cord:     # Checks for a winner
			if cord[el]>=3:
				 check_win=True
				 break

		for el in x[0:3]:
			if el in check_l:
				z+=1
			if z==3:
				 check_win=True
				 break
		z=0

		for el in x[2:]:
			if el in check_l:
				z+=1
			if z==3:
				 check_win=True
		print ("CHECKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
		print (check_l, "list")
		print (check_win, "WIN ")

		return check_win

	def Check(self): #Each time a O or X is drawn on the grid this function is called to assign the placed X or O in a grid position if that poisiton is not already ocupied
		print(self.x,self.y)
		if self.x == 0:
			for n,i in enumerate(self.x0): #Gets the index of each item in the list
				if i==self.y: # checks to see if the index of the list is the same as the Y coordinate
					self.x0[n]=self.Turn # Assigns the the Current turn to the item of that index in the list
					print(self.x0,self.x1,self.x2)
					return True # So the draw function within the window class knows if there already is a X or O in that position or not


		elif self.x == 1: #Repeated as above for the next list
			for n,i in enumerate(self.x1):
				if i==self.y:
					self.x1[n]=self.Turn
					print(self.x0,self.x1,self.x2)
					return True


		elif self.x == 2: #Repeated as above for the next list
			for n,i in enumerate(self.x2):
				print(n,i)
				if i==self.y:
					self.x2[n]=self.Turn
					print(self.x0,self.x1,self.x2)
					return True

					

	def Win(self): # This functions checks the current board state agaisnt a set of win conditions when a X or O is drawn on the board
		if self.x0[0] == self.x1[0] and self.x1[0]== self.x2[0]: #Checks that there are 3 of the same item in the list which means that there are three on the board in a row. 
			if self.x0[0] == "X" or self.x0[0] == "O": # ensures that it is an X or O
				print("Winnner is ", self.x0[0]) # Displays who has won
				return self.x0[0]
			
		elif self.x0[1] == self.x1[1] and self.x1[1]== self.x2[1]:
			if self.x0[1] == "X" or self.x0[1] == "O":
				print("Winnner is ", self.x0[1])
				return self.x0[1]
			
		elif self.x0[2] == self.x1[2] and self.x1[2]== self.x2[2]:
			if self.x0[2] == "X" or self.x0[2] == "O":
				print("Winnner is ", self.x0[2])
				return self.x0[2]

		elif self.x0[0] == self.x1[1] and self.x1[1]== self.x2[2]:
			if self.x0[0] == "X" or self.x0[0] == "O":
				print("Winnner is ", self.x0[0])
				return self.x0[0]
			
		elif self.x0[2] == self.x1[1] and self.x1[1]== self.x2[0]:
			if self.x0[2] == "X" or self.x0[2] == "O":
				print("Winnner is ", self.x0[2])
				return self.x0[2]
			
		elif self.x0[0] == self.x0[1] and self.x0[1]== self.x0[2]:
			if self.x0[0] == "X" or self.x0[0] == "O":
				print("Winnner is ", self.x0[0])
				return self.x0[0]
			
		elif self.x1[0] == self.x1[1] and self.x1[1]== self.x1[2]:
			if self.x1[0] == "X" or self.x1[0] == "O":
				print("Winnner is ", self.x1[0])
				return self.x1[0]
			
		elif self.x2[0] == self.x2[1] and self.x2[1]== self.x2[2]:
			if self.x2[0] == "X" or self.x2[0] == "O":
				print("Winnner is ", self.x2[0])
				return self.x2[0]


	
class Window(): # This class only contains functions that are directly changing or using the GUI

	
	def __init__(self,root, port=12346): # Function defines variables to be used within the Window class 
		self.root= root
		self.Turn = " " # Variable that is called or changed to determine if it is X's or O's turn 
		self.colour= "black"
		self.x0=[0,1,2] # Board displayed as a list 
		self.x1=[0,1,2]
		self.x2=[0,1,2]
		self.ok = True
		self.GameMode = ""
		self.Count = 0
		self.GUI() # Runs the GUI function within the Window class. Allows elements from GUI to be called elsewhere in the code
		self.p = " " # This stands for the player so they are either player one who is sending or player two who is reciving 
		self.m = " " # This stands for the players initsl mark, esssentialy if they are an X or an O, used for the purpose of determing what player two's mark is
		self.a = False # This can be consider an activation variable for the multiplayer move button, as when it is true it should allow the multiplayer move button to be visible
		self.client = '' # The part of the code that will ofrm the connection when the game mode has been switched to multiplayer
		global check_l_O, check_l_X
		check_l_O=[]
		check_l_X=[]
		self.WINNER = " "
		self.diff = "Advanced"

				
	   
	def GUI(self): # Function that creates the Tkinter GUI

		self.root.title("TicTacToe") # Names the TKinter window
		self.root.resizable(0,0) # Means that ratio of the window cannot be changed


		self.start=Button(self.root,text="Play") # Button titled "Play" in the GUI
		self.start.bind("<Button-1>", self.Play ) # When the button is clicked with the left mouse button the Play function within the Window class is called
		self.start.grid(row=1, column=3)# The button is placed within a grid in the TKinter window

		self.OTurn=Button(self.root,text="O")# Button titled "O" in the GUI
		self.OTurn.bind("<Button-1>", self.Turn_O) # When the button is clicked with the left mouse button the Turn_O function within the Window class is called
		self.OTurn.grid(row=1, column=4 )# The button is placed within a grid in the TKinter window

		self.XTurn=Button(self.root, text="X")# Button titled "X" in the GUI
		self.XTurn.bind("<Button-1>", self.Turn_X)# When the button is clicked with the left mouse button the Turn_X function within the Window class is called
		self.XTurn.grid(row=1, column=5)# The button is placed within a grid in the TKinter window

		self.Move=Button(self.root, text="Multiplayer Move")# Button titled "Multiplayer Move" in the GUI
		self.Move.bind("<Button-1>", self.Multiplayer)# When the button is clicked with the left mouse button the Multiplayer function within the Window class is called      

		self.HelpButton = Button(self.root,text = "Help")# Button titled "Help" in the GUI
		self.HelpButton.bind("<Button-1>",self.Help)# When the button is clicked with the left mouse button the Help function within the Window class is called
		self.HelpButton.grid(row=4, columnspan=1)# The button is placed within a grid in the TKinter window

		self.OptionsButton = Button(self.root,text= "Options") #Button titled Options in the GUI
		self.OptionsButton.bind("<Button-1>",self.Options) # When the button is clicked with the left mouse button the Options function is called wihtin the Window class
		self.OptionsButton.grid(row=4, column=9)# The button is placed within a grid in the Tkinter window

		self.cv= Canvas(root, bg= "white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT ) # Creates a canvas which . Uses global variable to get size of canvas.
		self.cv.grid(row=3, column = 0, columnspan= 10)# Places the canvas on a grid
		self.cv.bind("<ButtonPress-1>",self.Draw_Event) # If the user presses the left mouse button within the created canvas the Draw function within the Window class is called

		
	def Multiplayer(self, event):

		""" This activates the games listening mode in multiplayer, essentialy once the 'Multiplayer Move' button is clicked this will activate changing the game from sending to reciving """

		try: # This is a worst case scenario error handler as it is unliely that the wrong type of information is input due to the game using a GUI but this is here as a safety net
			
			event.widget.grid_remove() # This removes the 'Multiplayer Move' button from the screen so as prevent it being clicked in error during the players turn     
			Activation = "ACTIVATE" # This lets the other client know that this client has turned into listening mode and it is safe to proceed into sending mode
			self.client.send(Activation.encode("utf-8")) # The code that turns 'ACTIVATE' into binary that can be transported to the server
			Window.Player2(event) # The code that will allow the game to recive data and turn it into something meaningful
			
		except TypeError:
			
			Window.Multiplayer(event) # It will rerun the above code until the above code has completed its run

			
	def Turn_O(self, event):# Function that changes the users turn from its previously assigned turn to "O"
		if self.Count == 1:
			self.Turn = "O"
			
			if self.GameMode == "Multiplayer" and self.p == 1: # This checks that the game mode is set to multiplayer and that the current instance of this class is set to player 1
				
				if self.data != "Player 1, Choose Marker, X or OREADY": # This is a worst case scenario catch, as sometimes when both clients connect at the same time the activation message will be sent at the
																		# same time as the information that tells the player they are player one and should select their marker meaning the game will break
																		# This provides a fix for this by bypassing the wait for player two to be ready code when this problem occurs
					
					Activate = self.client.recv(1024) # If the codes works correctly then this code should activate, in which beofre player one can select their marker they have to wait until player two is ready 
					Activate = Activate.decode("utf-8").rstrip("\r\n") # This turns the word 'ACTIVATE' into binary bits which can be sent accross the connection for the server to read
					if Activate == "READY": # Once the above code is complete it will check that the correct activation code has been sent, namely that the client for player two has sent that it is ready to recive player ones marker 
						 msg = self.Turn # This turns the self.Turn into a message that can be sent
						 self.client.send( msg.encode('utf-8')) # The code that turns 'msg' into binary that can be transported to the server
					
				else: # Should the worst case scenario activate then we know player two is ready as evidenced by the add on 'READY' to the code we were expecting so we move onto the next stage
					msg = self.Turn # This turns the self.Turn into a message that can be sent
					self.client.send( msg.encode('utf-8')) # The code that turns 'msg' into binary that can be transported to the server
				 
			elif self.GameMode == "1 Player":
				self.AIturn = "X"
			print(self.Turn)

	def Turn_X(self, event):# Function that changes the users turn from its previously assigned turn to "X"
		if self.Count == 1:
			self.Turn = "X"
			
			if self.GameMode == "Multiplayer" and self.p == 1:
				
				if self.data != "Player 1, Choose Marker, X or OREADY": # This is a worst case scenario catch, as sometimes when both clients connect at the same time the activation message will be sent at the
																		# same time as the information that tells the player they are player one and should select their marker meaning the game will break
																		# This provides a fix for this by bypassing the wait for player two to be ready code when this problem occurs
					
					Activate = self.client.recv(1024) # If the codes works correctly then this code should activate, in which beofre player one can select their marker they have to wait until player two is ready 
					Activate = Activate.decode("utf-8").rstrip("\r\n") # This turns the word 'ACTIVATE' into binary bits which can be sent accross the connection for the server to read
					if Activate == "READY": # Once the above code is complete it will check that the correct activation code has been sent, namely that the client for player two has sent that it is ready to recive player ones marker 
						 msg = self.Turn # This turns the self.Turn into a message that can be sent
						 self.client.send( msg.encode('utf-8')) # The code that turns 'msg' into binary that can be transported to the server
					
				else: # Should the worst case scenario activate then we know player two is ready as evidenced by the add on 'READY' to the code we were expecting so we move onto the next stage
					msg = self.Turn # This turns the self.Turn into a message that can be sent
					self.client.send( msg.encode('utf-8')) # The code that turns 'msg' into binary that can be transported to the server
				 
							 
			elif self.GameMode == "1 Player":
				self.AIturn = "O"
				
			print(self.Turn)

	def Player2(self, event):

		""" This code is to set to activate either when the user is set to player two initaly or they are changing their game from sending to reciving, it is designed
			to recive the information the server is sending and pass it onto the 'Darw_Recev' function """
		
		try: # This will be a safety net for this function as the information being recived should always be the right type for conversion, like a string number into an integer 
			
				print("Listening") # Making sure that the client has switched to what it should have to be able to receve information
						
				x = self.client.recv(1024) # This allows it to recive the x coordinate for the marker it is going to draw 
				x = x.decode("utf-8").rstrip("\r\n") # This turns the x coordintate from a string of binary bits into simething the client can use, unfortuanly this is a string type as this is all that can be sent along the connection
				x = int(x) # Thus you need to connvert x from a string to an integer so that it can be used by the game

				print(x)# This is to make sure that x is what we sent
						
				y = self.client.recv(1024) # This allows it to recive the x coordinate for the marker it is going to draw 
				y = y.decode("utf-8").rstrip("\r\n") # This turns the y coordintate from a string of binary bits into simething the client can use, unfortuanly this is a string type as this is all that can be sent along the connection
				y = int(y)# Thus you need to connvert x from a string to an integer so that it can be used by the game

				print(y) # This is to make sure that x is what we sent

				Activate = self.client.recv(1024) # This code is to make sure that both clients stay on the same level, basicaly one client is not in listening mode while the other is sending 
				Activate = Activate.decode("utf-8").rstrip("\r\n")# This turns what ever activate is from a string of buinary bits into something readable and useful to the client

				if Activate == "ACTIVATE": # If the informmatiob recived is the right activation code then the code can move onto the next stage
					Window.Draw_Event_Recv(event, x, y) # This will activate the 'Draw_Event_Recv' function which turns the coordinates we have received into something we can see on the board
					
		except TypeError: # In the event the unlikely happens this should activate forcing the game to repeat this function until the code has run fully
				Windows.Player2(event)# This is a callback to this function so that it repeats the function everytime there is a TypeError
					

					

	def Change_Game(self, event): # Function that changes the type of game
		self.Reset()
		self.GameMode = self.selectmode.get()
		
		
		   
	def Reset(self): # This function contains a set of commands that are run to reset the game so it can be played from scratch 
		self.cv.delete("all")#Clears all elements from the canvas
		self.x0=[0,1,2] # Board displayed as a list 
		self.x1=[0,1,2] #Reverts the board back to its original values 
		self.x2=[0,1,2]
		self.Turn = " "
		self.AIturn = " "
		self.colour= "black"
		self.Count = 1
		self.WINNER = " "
		global check_l_O, check_l_X
		check_l_O = []
		check_l_X = []

	
	def Play(self,event): # Draws a grid for the TicTacToe game to be played  on. If called during a game the game is reset.
		
		try:# There is a chance that this function can produce a connection error when you attempt to replay the game so this 'try except' code will catch this and perform the appropiate error handling
			
			self.Reset()#Runs the Reset function within the window class
			self.cv.create_line(200, 0, 200, 600)#Draws 4 lines that split the canvas into a 3 by 3 grid 
			self.cv.create_line(400, 0, 400, 600)

			self.cv.create_line(0, 200, 600, 200)
			self.cv.create_line(0, 400, 600, 400)
			print("play")
			
			if self.GameMode == "Multiplayer": # The following code will be activated when the play button is pressed and game mode is 'Multiplayer'
				
					event.widget.grid_remove()# This removes the play button from the screen so as to prevent anyone pressing it accedently during the game, as pressing it rests the game and can cause it to crash when running over the server
					
					port = 12346 # This is essentialy the door that it should go through to reach the server, as ports are virtual 'doors' that applications can use to access things outside them 
					self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # This is what creates the socket for the client to use to send and recive information, AF_INET revers to the address family (in this case IPv4 and it relevant protocols) and SOCK_STREAM refers to the type of socket being used
					self.client.connect(('localhost', port))# In this line we are essentialy binding the socket to use the information provided as its connection, local host being the machine you are running the code on and the port being where you want to the steream of information to flow from and to
					
					data = self.client.recv(1024)# As this is the intial stage of the connection we need to determine who is player one and player two thus the server decideds and pass this information on to the clients through this 
					data = data.decode("utf-8").rstrip("\r\n")# This turns the data recived into something useful to the program, as in not a string of binary bits but something a person can more easily understand and program for
					self.data = data # As seen earlier in the X_Turn and 0_Turn fucntions this piece of information is used for error handeling of one of the clients operting to fast for the server
					print (data)# This is for the purpose of checking that everything is working as it should
					
					if data == 'Player 2': # At this stage player one goes onto to chosse their marker whiile player two waits here to findout the results
						send1 = "READY" # This will be the message sent to player one once player two is ready to recive information from player one
						time.sleep(1) # This attempts to slow down the pace of information being sent to the server and player one so that player one can  catchup with the information the server is sending 
						self.client.send(send1.encode("utf-8"))# Once the client has waited it will turn ready into a string of binary bits that can be sent to the server
						mark = self.client.recv(1024)# Once player one has chossen their marker they will have to inform player two so that player two can draw the correct marker based on player ones choice
						mark = mark.decode('utf-8').rstrip('\r\n') # This turns the sting of binary bits into something meaningful 
						print(mark)# This is to essentialy check what marker player two has recived 
						
						if mark == "You are X, please wait for player 1": # This will activate if player one chose X as their marker
							self.Turn = "O" # Sets the turn marker to 'O' as we want the board to draw an 'X' where player one sends it, the turn switcher will turn it into an 'X'
							self.p = 2 # Sets the player as player two
							Window.Player2(event) # This activates the 'Player2' function which is used to recive the coordinates of where player one has made their move

						elif mark == "You are O, please wait for player 1": # This will activate if player one chose O as their marker
							self.Turn = "X" # Sets the turn marker to 'O' as we want the board to draw an 'X' where player one sends it, the turn switcher will turn it into an 'X'
							self.p = 2 # Sets the player as player two
							Window.Player2(event) # This activates the 'Player2' function which is used to recive the coordinates of where player one has made their move
					else:
						self.p = 1 # This will activate if the information recived is not 'Player 2' and set the player to player one
			
		except OSError as e: # When the user wants to play again the connection is closed so as to refresh all the variables, as such it will generate an connection error meaning the connection has to be reestablished which is waht this does
				Window.Play(event)# This reruns the 'Play' function so as to reestablishe the connection and refresh/reset the variables

	def Help(self,event): # Opens a small window which provides the user with useful information about how to use the program
		h_text = open("README.txt","r").read() # Opens and reads a text file containing useful information for a user

		info = Toplevel() # Creates a new window and assigns it to a variable 
		info.title("Help")# Lables the window

		content= Label(info)# The content of the window is filled with text extracted from the text file
		content.config(text = h_text)
		content.pack() # format
		
		close = Button(info, text= "close", command=info.destroy) 
		close.pack() #fomat

	def Options(self,event): # Displays options to the user
		game_modes = ["2 Player","1 Player", "Multiplayer"]
		Themes = ["Black&White", "Random"]
		self.Colours = ["","red","green","blue","cyan","yellow","magenta","cyan","pink","orange"]
		
		option = Toplevel() # Creates a new window and assigns it to a variable 
		option.title("Options")# Lables the window
		
		description = Label(option) #adds a label in the new window
		description.config(text="Select a game mode") #text shown in label
		description.pack()#format

		self.selectmode = ttk.Combobox(option) #adds a drop down box to the new window
		self.selectmode.config(values = game_modes) #users can select one of the game modes from the game_modes list
		self.selectmode.pack()#format

		selectbutton = Button(option, text="select")
		selectbutton.bind("<ButtonPress-1>",self.Change_Game)
		selectbutton.pack()

		description2 = Label(option) # adds a label in the new window 
		description2.config(text="Select a theme")# text shown in label
		description2.pack()#format

		self.selecttheme = ttk.Combobox(option)# adds a drop down box to the new window
		self.selecttheme.config(values=Themes)# users can select one of the themes from the Themes list
		self.selecttheme.pack()#format

		selecttbutton = Button(option, text="select") # Button titled select below the drop down box in the new window
		selecttbutton.bind("<ButtonPress-1>",self.Theme)# When the button is pressed it calls the Theme funcation within the Window class 
		selecttbutton.pack()# format

		close = Button(option, text= "close", command=option.destroy) # Button labeled close that will shutdown the Options window 
		close.pack() #fomat
		
		print("Options")
		
	def Theme(self,event): # Theme is an event function which assisgns a colour to a variable depending on the option that the user selected 

		if self.selecttheme.get() == "Random": # If the user has selected Random from the drop down box then this statement is true
			self.colour = self.Colours[randint(1,9)] # self.colour is a varibale within the Window class which is used to assign colours to objects drawn on the canvas. A random integer is created to select an item from a list and assign it to this variable/ 
			print(self.colour)

		elif self.selecttheme.get() == "Black&White":# If the user has selected Black&White from the drop down box then this statement is true
			self.colour= "black" # the variable self.colour is assigned the string "black"
			print(self.colour)

	def sendCode(self):

		 """ When run the below code will move a multiplayer game into its final stage as it sends the winning move, closes tje connection and sends the restart code to the server """

		 if self.GameMode == "Multiplayer": #This activates if the game mode is set to multiplayer and one of the players has won the game
					
					print("Sending")# This is to check that things are working as they should
					send1 = "ACTIVATE" # This is the message that will allow the other to realise that it has lost the game as this activates the other clients draw function which activates the check win function
					send2 = "EXIT" # This is a message to the server telling it that this game is over and it should restart so as to refresh/reset its variables 
					send3 = self.x # This is the x coordinate of the winning move
					send3 = str(send3)# As x is an intager and the connection can only send strings the x coordinate needs to be connverted into an string
					send4 = self.y # This is the y coordinate of the winning move 
					send4 = str(send4)# As y is an intager and the connection can only send strings the y coordinate needs to be connverted into an string

					if self.p != 2: # If the person winning is not player two, as the switching between listening and sending also switch the player between player one and two meaning player two will always recive and never send while player one will always send but never recive thus player two should never have the winning move
									
						self.client.send(send3.encode("utf-8")) # This turns the y coordinate into something that can be sent accross the connection
						
						time.sleep(1) # This creates a small delay so that the messages do not get jumbeled up into one big message
						
						self.client.send(send4.encode("utf-8")) # This turns the x coordinate into something that can be sent accross the connection
						
						time.sleep(1) # This creates a small delay so that the messages do not get jumbeled up into one big message
						
						self.client.send(send1.encode("utf-8"))# This turns the activation code into something that can be sent accross the connection
															   
						time.sleep(1) # This creates a small delay so that the messages do not get jumbeled up into one big message
									  
						self.client.send(send2.encode("utf-8"))# This turns the restart code into something that can be sent accross the connection
															  
						self.client.shutdown(1)# This stops the connection sending any messages out
											   
						self.client.close()# This stops the connection reciving any messages

	def winnerCode(self):

		w = self.Turn
		
		winner = Toplevel()
		winner.title("Game Over")

		description = Label(winner)
		description.config(text = "The winner is {}".format(w) )
		description.pack()

		close = Button(winner, text="close",command=winner.destroy)
		close.bind("<ButtonPress-1>",self.Reset())
		close.pack()
		
	def Display_Winner(self): #Function called when an X or O is drawn on the canvas it then calls the Win function within the game class to check if any win conditions have been met
		w = Game.check(self)
		if w == True: # if the win conditions have been met then it will create a pop up window displaying the winner
			
			self.start.grid(row=1, column=3)# The button is play button placed back within the grid in the TKinter window
			
			if self.GameMode == "Multiplayer": #This activates if the game mode is set to multiplayer and one of the players has won the game
				
				try: # When this is run through fully it will close connections to everything which can produce an connection error
				
					Window.sendCode() # Activates the send code
					Window.winnerCode() # Activates the winning code if there is no error
						
				except OSError: # It is likely that an connection error will occur due to the connection being severed but you still need to display the winner so this should activate it
								
					Window.winnerCode()# Activates the winning code
						
			else: # If the user is not playing multiplayer and they win then they still need to be told they win so this condition will be meet
				  
			   Window.winnerCode()# Then the win code is activated
			   
		else: # If there is no winner then this code should do nothing
			pass

	def tieCode(self):

		""" This is the code used to create the tie pop-up when the game has reached a tie as decided by the Display_Tie function"""
		
		Tie = Toplevel()
		Tie.title("Game Over")

		description = Label(Tie)
		description.config(text = "IT IS A TIE!" )
		description.pack()

		close = Button(Tie, text="close",command=Tie.destroy)
		close.bind("<ButtonPress-1>",self.Reset())
		close.pack()
		

	def Display_Tie(self):

		""" This function is called once the the number of turns (count increases for every move taken) reaches nine as  this is the maximum number of moves available to the player """
		
		c = self.Count # Makes self.Count a loacl variable that can be used to count the number of turns have been played so far
			
		if c == 9: # If the tie condition has been met then it will create  a pop up window telling the players that it is a tie
					   
				self.start.grid(row=1, column=3)# The button is play button placed back within the grid in the TKinter window
			
				if self.GameMode == "Multiplayer": #This activates if the game mode is set to multiplayer and one of the players has won the game
					
					try: # When this is run through fully it will close connections to everything which can produce an connection error
					
						Window.sendCode() # Activates the send code
						Window.tieCode() # Activates the winning code if there is no error
							
					except OSError: # It is likely that an connection error will occur due to the connection being severed but you still need to display the winner so this should activate it
									
						Window.tieCode()# Activates the winning code
							
				else: # If the user is not playing multiplayer and they win then they still need to be told they win so this condition will be meet
					  
				   Window.tieCode()# Then the win code is activated
				   
		else: # If there is no winner then this code should do nothing
			pass

	def Draw_Event_Recv(self,event, x, y):
	    
		""" This function takes the coordinates either given in the Player2, Win or Tie functions so to draw either an "X" or "O" """
		
		print("Drawing what you sent")# This is a test to see if this function is working
		self.x = x # As this function recives the x coordinate from either the Player2, Win or Tie functions so as to set the function self.x which the draw function will use to draw the marker on the grid 
		self.y = y # As this function recives the y coordinate from either the Player2, Win or Tie functions so as to set the function self.x which the draw function will use to draw the marker on the grid
		print(x)# This is a test to make sure that the function is reciving the correct x coordinate
		print(y) # This is a test to make sure that the function is reciving the correct x coordinate
		if self.Turn != " ":
			if self.GameMode == "Multiplayer": # The following code will activate only if the current game mode is multiplayer
				g = Game.Check(self) # Calls the function within the Game class to check that the user is not trying to draw and X or O on a grid position that is already occupied by an X or O.
				self.ok = g # This Game function returns a boolean value which is stored as a variable so it can be accessed by other parts of the Window class
				self.a = False # This makes sure that the draw function does not ;place the 'Multiplayer Move' button on the grid just yet
				self.Draw()
				self.Count +=1
				print("Count" + str(self.Count))
				
	
	def Draw_Event(self,event): # This function finds out the location of the users click on the canvas and uses that to draw an "X" or "O"
	    
		if self.GameMode == "Multiplayer" and self.p == 2: # This is what will initaly activate player two's listening mode
			Window.Player2(event) # This activates the Player2 function which lets the client know that it should be listening rather than sending
		else:
			self.xx = event.x #Positions of the mouse event 
			self.yy = event.y 
			print(self.xx)
			print(self.yy)
			x = int(self.cv.canvasx(event.x)/200)# This calcualtion finds the the coordinates of the mouse click on the grid then converts this to coordinates based on the width and height of the canvas. This number is then rounded to provide a grid position in relation to a 3 by 3 grid. 
			y = int(self.cv.canvasy(event.y)/200)
			self.x = x
			self.y = y
			print(x)
			print(y)
			if self.Turn != " ":
				print(self.Count)
				if self.GameMode == "2 Player":
					g=Game.Check(self) # Calls the function within the Game class to check that the user is not trying to draw and X or O on a grid position that is already occupied by an X or O.
					self.ok = g # This Game function returns a boolean value which is stored as a variable so it can be accessed by other parts of the Window class
					self.Draw()
					self.Count +=1
					print(self.Count)
				elif self.GameMode == "1 Player":
					a = Game.Check(self)
					self.ok = a
					self.Draw() 
					c = AI.Move(self)
					self.ok = c
					self.Draw()
					self.Count +=1
					print(self.Count)
					
				elif self.GameMode == "Multiplayer": # This code will activate if the game mode is set to Multiplayer
									 
					if self.p == 1: # The following code will activate if the player is set to player 1
						print("Sending")# This is to test that the code is working
						send1 = str(x) # This is saying that the first piece of infornation to send is the x coordinate as a string as this is what can be sent over this connection
						send2 = str(y) # This is saying that the second piece of infornation to send is the y coordinate as a string as this is what can be sent over this connection

						g=Game.Check(self) # Calls the function within the Game class to check that the user is not trying to draw and X or O on a grid position that is already occupied by an X or O.
						self.ok = g # This Game function returns a boolean value which is stored as a variable so it can be accessed by other parts of the Window class
						print (self.ok)
						self.a = True # This sets the 'button activator' to true so that the multiplayer nove button will appear once this turn is complete so that it can be sent to the other player  
						self.Draw()# This calls the Draw function which places the marking on the bard for the player to see which squares are marked
						if self.ok == True:
							try: # This tells the program to try the following code block unless any mentioned exceptions happen
							    
								self.client.send(send1.encode("utf-8"))# This turns the x coordinate into something that can be sent accross the connection
					
								time.sleep(1)# This creates a small delay so that the messages do not get jumbeled up into one big message
								
								self.client.send(send2.encode("utf-8")) # This turns the y coordinate into something that can be sent accross the connection
						
								self.Count += 1 # This adds one to the count of the turn, so that once a player has made their thurn then it will add one to the count
								
								print("Count" + str(self.Count)) # This is to test to make sure the count function is working as it should be

							except OSError as e: # This will look for operating system errors and record them as and check them against any conditions that are set
							    
								if e.winerror == 10038: # This error occures when the client has troube sending the server the information due to a loss of connection
									Window.Reset()# As this error normaly only happens when you attempt to replay the game this will attempt to reset the board
		
	def Draw(self):
		print("Drawing") # This is for the purpose of error detection as it tells the programer if this piece of code has been activated and when
		print(self.ok)
		if self.Turn == "O" or self.AIturn == "X":#Only runs if the O button was the last one pressed
			if self.ok == True: # Only draws the shape if there is nothing alrady in that position
				self.cv.create_oval(self.x*200,self.y*200, (self.x+1)*200,(self.y+1)*200,outline=self.colour,width = 3) #An oval is created on the canvas at the point where the mouse event is made
				self.Display_Winner() # This checks whether the tie functions parameters have been meet to such an extent that the game can end
				self.Display_Tie() # This checks whether the tie functions parameters have been meet to such an extent that the game can end
				self.Turn = "X"
				self.XTurn.config(bg = "pink")
				self.OTurn.config(bg = "white")
				self.AIturn = "O"
				if self.GameMode == "Multiplayer" and self.p == 1 and self.a == True: # This checks that the game mode is multiplayer, the player is player one and that the button activation variable is true
					self.Move.grid(row=1, column=6)# This will place the 'Multiplayer Move' button on the board allowing the player to make their move and send it to the other player
				if self.p == 2: # If the above code conditions are not meet then the following code will be run
					self.a = False #This will reafirm that the button actiation variable should be false and the button should not be visible
					self.p = 1 # As this is the end of player twos turn they now become player one, esentialy they switch from being the reciver to the sender
			   
			else: # If there is something already there it stops 
			   pass 
			
		elif self.Turn == "X" or self.AIturn == "O": #Only runs if the X buton was the last one pressed 
			if self.ok == True:# Only draws the shape if there is nothing alrady in that position
				self.cv.create_line(self.x*200,self.y*200, (self.x+1)*200,(self.y+1)*200,fill = self.colour) #Creates a line across the grid position that is selected by the mouse 
				self.cv.create_line(self.x*200,(self.y+1)*200,(self.x+1)*200,self.y*200,fill = self.colour) # the x positon indicates which part of the grid the line needs to be created in then it is either multlipied by 200 or/and added 1 to find the corner positions of the grid whihc the lines can be drawn from. 
				self.Display_Winner() # This checks whether the tie functions parameters have been meet to such an extent that the game can end
				self.Display_Tie() # This checks whether the tie functions parameters have been meet to such an extent that the game can end
				self.Turn = "O"
				self.OTurn.config(bg = "pink")
				self.XTurn.config(bg = "white")
				self.AIturn ="X"
				if self.GameMode == "Multiplayer" and self.p == 1 and self.a == True: # This checks that the game mode is multiplayer, the player is player one and that the button activation variable is true
					self.Move.grid(row=1, column=6)# This will place the 'Multiplayer Move' button on the board allowing the player to make their move and send it to the other player
				if self.p == 2: # If the above code conditions are not meet then the following code will be run
					self.a = False #This will reafirm that the button actiation variable should be false and the button should not be visible
					self.p = 1 # As this is the end of player twos turn they now become player one, esentialy they switch from being the reciver to the sender
			   

				
		else:# If there is something already there it stops
				pass
			
if __name__ == "__main__": # Main code within the program which is not executed when the program is imported        
	root = Tk()     
	Window= Window(root)
	root.mainloop()

