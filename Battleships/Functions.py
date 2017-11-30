from Tkinter import *
from random import randint
def g(l):
    l.config(text = "Player 2's chance")
def h(l):
    l.config(text = "Player 1's chance")
class Ship:
    occupiedPositions=[]	#This list contains all the positions of ship as tuples of previously created ships.
    def __init__(self,l,name):
        self.length=l	#This attribute gives the length of the ship.
        self.placing()	#This is method of this class which places the ships randomly.
        self.name=name	#This attribute gives us the name of the ship.(eg PATROL SHIP etc)
        if(len(Ship.occupiedPositions)==0):
            Ship.occupiedPositions.extend([i for i in self.position])
        else:
            while (self.check()==False):
                self.placing()
            Ship.occupiedPositions.extend([i for i in self.position])

    def check(self):
        #This checks whether the positions of the ship being created, are already occupied by previously created ships
        for i in self.position:
            if i in Ship.occupiedPositions:
                return False
        return True

    def placing(self):
        #This method will place the ships in such a way that they lie completely in the Grid. 
        r=randint(0,9)
        c=randint(0,9)
        self.point=(r,c) #chooses a point on the grid randomly.
        self.position=[] #This list contains the positions of the ship that have been created.
        self.position.append(self.point)

        if(c>5 and r<4):
            #If the selected point(self.point) is on the top right corner, ship can be placed downwards or leftwards.
            optionset=[3,4]
            option=optionset[randint(0,1)]

        if(c<4 and r<4):
            #If the selected point(self.point) is on the top left corner, ship can be placed downwards or rightwards.
            optionset=[2,3]
            option=optionset[randint(0,1)]

        if(c<4 and r>5):
	    	#If the selected point(self.point) is on the  bottom left corner, ship can be placed upwards or rightwards.
            optionset=[1,2]
            option=optionset[randint(0,1)]

        if(c>5 and r>5):
	    	#If the selected point(self.point) is on the bottom right corner, ship can be placed upwards or leftwards.
            optionset=[1,4]
            option=optionset[randint(0,1)]


        if (c==4 or c==5):
	    '''If the selected point(self.point) has column number 4 or 5 then ship can be placed both, leftwards or rightwards and also
	      upwards or downwards depending on the row chosen'''
            if(r<4):
                optionset=[2,3,4]
                option=optionset[randint(0,2)]

            if (r==4 or r==5):
                optionset=[1,2,3,4]
                option=optionset[randint(0,3)]

            if (r>5):
                optionset=[1,2,4]
                option=optionset[randint(0,2)]
        if (r==4 or r==5):
	    '''If the selected point(self.point) has row number 4 or 5 then ship can be placed both, upwards or downwards and also
	       leftwards or rightwards depending on the row chosen'''
            if (c<4):
                optionset=[1,2,3]
                option=optionset[randint(0,2)]
            if (c>5):
                optionset=[1,3,4]
                option=optionset[randint(0,2)]

        if(option == 1):
            self.caseUp()
        if(option == 2):
            self.caseRight()
        if(option == 3):
            self.caseDown()
        if(option == 4):
            self.caseLeft()


    def caseUp(self):
	   '''This places the ship upwards from the chosen random point
	       It adds the ship positions to the self.position list'''
           for i in range(self.length-1):
                    self.position.append((self.point[0]-(1+i),self.point[1]))

    def caseRight(self):
	    '''This places the ship rightwards from the chosen random point
	       It adds the ship positions to the self.position list'''
            for i in range(self.length-1):
                    self.position.append((self.point[0],self.point[1]+(i+1)))

    def caseDown(self):
	    '''This places the ship downwards from the chosen random point
		It adds the ship positions to the self.position list'''
            for i in range(self.length-1):
                    self.position.append((self.point[0]+(i+1),self.point[1]))

    def caseLeft(self):
	    '''This places the ship leftwards from the chosen random point
	    It adds the ship positions to the self.position list'''
            for i in range(self.length-1):
                    self.position.append((self.point[0],self.point[1]-(1+i)))

    def checkDestroyed(self,temploc,shiploc):
	'''This method will check how many positions of a particular ship have been hit'''
        check=0
        for i in shiploc:
            if i in temploc:
                check+=1
        return check



#This class is of Player 1 
class User1:
    hitcount = 0  # number of times ship positions hit by User1
    gameRunning = 1 # variable which has value 1 if game is running and becomes 0 once it is over
    def __init__(self,user1Grid,label, label2):
        self.Grid=user1Grid  # list of lists each containing 10 buttons of computer grid
                             # object of User1 class (required to call player 1 turn)
        self.label=label    # label whose text can be changed to display that a ship has been destroyed
        self.label2=label2
        self.placeShips()    # makes ship objects and adds their positions to shipLocations list

        self.tempLocations=[]    #list containing position of buttons which are clicked
        self.f()

        self.shipObjects=[self.AirCarrier,self.Battleship,self.Submarine,self.Destroyer1,self.Destroyer2,self.Patrol1,self.Patrol2] #list containing all ship objects
                                                                                                                            #used in hit method
    def f(self):
        for i in self.shipLocations:
            self.Grid[i[0]][i[1]].config(command=self.hit(i[0],i[1]))
        self.allLocations=[]
        for i in range(10):
            for j in range(10):
                self.allLocations.append((i,j))
        for i in self.allLocations:
            if i not in self.shipLocations:
                self.Grid[i[0]][i[1]].config(command=self.miss(i[0],i[1]))
    def placeShips(self):

        '''
        creates all ship objects and adds the positions as tuples to the list shipLocations

        '''
        self.AirCarrier=Ship(5,"Aircraft Carrier")
        self.Battleship=Ship(3,"Battleship")
        self.Submarine=Ship(4,"Submarine")
        self.Destroyer1=Ship(2,"Destroyer")
        self.Destroyer2=Ship(2,"Destroyer")
        self.Patrol1=Ship(1,"Patrol ship")
        self.Patrol2=Ship(1,"Patrol ship")

        self.shipLocations=[]
        self.shipLocations.extend(self.AirCarrier.position)
        self.shipLocations.extend(self.Battleship.position)
        self.shipLocations.extend(self.Submarine.position)
        self.shipLocations.extend(self.Destroyer1.position)
        self.shipLocations.extend(self.Destroyer2.position)
        self.shipLocations.extend(self.Patrol1.position)
        self.shipLocations.extend(self.Patrol2.position)



    def hit(self,i,j):
        '''
        A button corresponding to a position in shipLocations is bound with this function. It accepts the position of the button and returns a function which
        changes button colour to red and increases hitcount if a new button is pressed. It also adds the button position to tempLocations.
        It calls the checkDestroyed method of Ship class to check if a ship has been completely destroyed and if so, calls the method shipDestroyed.
        It also calls the function of User2 class for player 2's turn.
        It finally calls Endgame method if all the ships have been destroyed.
        '''
        def func():
           if User1.gameRunning==1:
              if (i,j) not in self.tempLocations:
                    self.Grid[i][j].config(bg="red")
                    self.tempLocations.append((i,j))
                    User1.hitcount=User1.hitcount+1
                    for k in self.shipObjects:
                       if k.checkDestroyed(self.tempLocations,k.position)==k.length:
                          self.shipDestroyed(k.name)
                          self.shipObjects.remove(k)
                    if (User1.hitcount<18):
                        h(self.label2)
                        
                    else:
                        self.Endgame()

        return func

    def miss(self,i,j):
        def func():
            '''
            A button corresponding to a position where no ship is present is bound with this function. It accepts the position of button clicked
            and returns a function which changes the button colour to yellow. After that, it calls the function of User2 class.
            '''
            if User1.gameRunning==1:
              if (i,j) not in self.tempLocations:
                self.Grid[i][j].config(bg="yellow")
                self.tempLocations.append((i,j))
                h(self.label2)
                
        return func



    def Endgame(self):
        '''
        It opens a new window displaying a text that User1 has won. It changes the variable gameRunning to 0
        to indicate that game has ended.

        '''
        User1.gameRunning=0
        window2=Tk()
        window2.title("All ships destroyed")
        label=Label(window2,text="Congratulations! Player 2 has won the game.")
        label.config(bg="white",font=30)
        label.pack()
        window2.mainloop()

    def shipDestroyed(self,name):
        '''
        This method changes the text of the label to inform when a ship has been completely destroyed.

        '''
        self.label.config(text=("Player 1's' "+name+" has been destroyed"))
#This class is of Player 2
class User2:
    hitcount=0  # number of times ship positions hit by User2
    gameRunning=1 # variable which has value 1 if game is running and becomes 0 once it is over
    def __init__(self,user2Grid,label, label2):
        self.Grid=user2Grid  # list of lists each containing 10 buttons of computer grid
                             # object of User2 class (required to call player 2 turn)
        self.label=label    # label whose text can be changed to display that a ship has been destroyed
        self.label2 = label2
        self.placeShips()    # makes ship objects and adds their positions to shipLocations list

        self.tempLocations=[]    #list containing position of buttons which are clicked
        self.f()

        self.shipObjects=[self.AirCarrier,self.Battleship,self.Submarine,self.Destroyer1,self.Destroyer2,self.Patrol1,self.Patrol2] #list containing all ship objects
                                                                                                                            #used in hit method
    def f(self):
        for i in self.shipLocations:
            self.Grid[i[0]][i[1]].config(command=self.hit(i[0],i[1]))
        self.allLocations=[]
        for i in range(10):
            for j in range(10):
                self.allLocations.append((i,j))
        for i in self.allLocations:
            if i not in self.shipLocations:
                self.Grid[i[0]][i[1]].config(command=self.miss(i[0],i[1]))
    def placeShips(self):

        '''
        creates all ship objects and adds the positions as tuples to the list, shipLocations

        '''
        self.AirCarrier=Ship(5,"Aircraft Carrier")
        self.Battleship=Ship(3,"Battleship")
        self.Submarine=Ship(4,"Submarine")
        self.Destroyer1=Ship(2,"Destroyer")
        self.Destroyer2=Ship(2,"Destroyer")
        self.Patrol1=Ship(1,"Patrol ship")
        self.Patrol2=Ship(1,"Patrol ship")

        self.shipLocations=[]
        self.shipLocations.extend(self.AirCarrier.position)
        self.shipLocations.extend(self.Battleship.position)
        self.shipLocations.extend(self.Submarine.position)
        self.shipLocations.extend(self.Destroyer1.position)
        self.shipLocations.extend(self.Destroyer2.position)
        self.shipLocations.extend(self.Patrol1.position)
        self.shipLocations.extend(self.Patrol2.position)



    def hit(self,i,j):
        '''
        A button corresponding to a position in shipLocations is bound with this function. It accepts the position of the button and returns a function which
        changes button colour to red and increases hitcount if a new button is pressed. It also adds the button position to tempLocations.
        It calls the checkDestroyed method of Ship class to check if a ship has been completely destroyed and if so, calls the method shipDestroyed.
        It also calls the function of User1 class for player 1's turn.
        It finally calls Endgame method if all the ships have been destroyed.
        '''
        def func():
           if User2.gameRunning==1:
              if (i,j) not in self.tempLocations:
                    self.Grid[i][j].config(bg="red")
                    self.tempLocations.append((i,j))
                    User2.hitcount=User2.hitcount+1
                    for k in self.shipObjects:
                       if k.checkDestroyed(self.tempLocations,k.position)==k.length:
                          self.shipDestroyed(k.name)
                          self.shipObjects.remove(k)
                    if (User2.hitcount<18):
                        g(self.label2)
                        
                    else:
                        self.Endgame()

        return func

    def miss(self,i,j):
        def func():
            '''
            A button corresponding to a position where no ship is present is bound with this function. It accepts the position of button clicked
            and returns a function which changes the button colour to yellow. After that, it calls the function of User1 class.
            '''
            if User2.gameRunning==1:
              if (i,j) not in self.tempLocations:
                self.Grid[i][j].config(bg="yellow")
                self.tempLocations.append((i,j))
                g(self.label2)
                
        return func



    def Endgame(self):
        '''
        It opens a new window displaying a text that User1 has won. It changes the variable gameRunning to 0
        to indicate that game has ended.

        '''
        User1.gameRunning=0
        window2=Tk()
        window2.title("All ships destroyed")
        label=Label(window2,text="Congratulations! Player 1 has won the game.")
        label.config(bg="white",font=30)
        label.pack()
        window2.mainloop()

    def shipDestroyed(self,name):
        '''
        This method changes the text of the label to inform when a ship has been completely destroyed.

        '''
        self.label.config(text=("Player 2's' "+name+" has been destroyed"))
