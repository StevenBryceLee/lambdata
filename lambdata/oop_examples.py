import pandas as pd
import numpy as np

class Simulator:
    '''
    This class simulates escaping from a maze from the POV of a bot

    The bot is given a random orientation on start, and can only view
    adjacent cells.

    The simulation ends when the bot reaches the exit
    '''

    def nextMove(self, inputGrid):
        inputarr = np.array(inputGrid)
        wall = ['#']*3

        #Check for exit
        for count,row in enumerate(inputarr):
            if 'e' in row.tolist():
                rowidx = count
                colidx = row.tolist().index('e')
                if (rowidx == 0) & (row[1] != '#'):
                    return 'UP'
                else:
                    return 'LEFT' if colidx == 0 else 'RIGHT'
                if (rowidx == 1):
                    return 'LEFT' if colidx == 0 else 'RIGHT'
                if (rowidx == 2) & (row[1] != '#'):
                    return 'DOWN'
                else:
                    return 'LEFT' if colidx == 0 else 'RIGHT'

        #Find a wall to the left
        if ((inputarr[:,0].tolist() == wall) & (inputarr[0,1] != '#')):
            return 'UP'
        #Find a wall to the right
        if ((inputarr[:,-1].tolist() == wall)  & (inputarr[-1,1] != '#')):
            return 'DOWN'
        #Find a wall above
        if ((inputarr[0,:].tolist() == wall)  & (inputarr[1,-1] != '#')):
            return 'RIGHT'
        #Find a wall below
        if ((inputarr[-1,:].tolist() == wall)  & (inputarr[1,0] != '#')):
            return 'LEFT'

        #No walls found, default 'UP'
        if  (inputarr[0,1] != '#'):
            return 'UP'
        elif (inputarr[1,-1] != '#'):
            return 'RIGHT'
        elif (inputarr[-1,1] != '#'):
            return 'DOWN'
        else:
            return 'LEFT'


    def checkDone(self, inputBoard):
        for row in inputBoard:
            if 'e' in row:
                return False
        return True

    def printBoard(self, inputBoard):
        for x in inputBoard:
            print(x)

    def Simulate(self, inputBoard):
        print('in simulate')
        self.printBoard(inputBoard)
        #Create the initial board position from the POV of the bot
        orientation = ['UP','LEFT','DOWN','RIGHT']
        orient = orientation[np.random.choice(len(orientation))]
        print(f'starting orientation: {orient}\n')
        #Start the position
        smallboard,position = self.botView(inputBoard,orient)

        print('Initial Board\n')
        self.printBoard(smallboard)
        #Return the new position of the bot
        moveDict = {'UP':{'LEFT':(0,-1),
                            'RIGHT':(0,1),
                            'UP':(-1,0),
                            'DOWN':(1,0)},
                    'DOWN':{'RIGHT':(0,-1),
                            'LEFT':(0,1),
                            'DOWN':(-1,0),
                            'UP':(1,0)},
                    'LEFT':{'UP':(0,-1),
                            'DOWN':(0,1),
                            'LEFT':(1,0),
                            'RIGHT':(-1,0)},
                    'RIGHT':{'DOWN':(0,-1),
                            'UP':(0,1),
                            'RIGHT':(1,0),
                            'LEFT':(-1,0)}}

        #for i in range(3):
        while(not self.checkDone(inputBoard)):
            move = self.nextMove(smallboard)
            print(f'Given orientation and move: {orient} {move}')
            #Update the large board
            newrow,newcol = np.array(position) + np.array(moveDict[orient][move])
            #Update the bot orientation
            orientIdx = (orientation.index(orient) + orientation.index(move)) % len(orientation)
            orient = orientation[orientIdx]
            print(f'new orientation: {orient} index: {orientIdx}')
            inputBoard[newrow][newcol] = 'b'
            inputBoard[position[0]][position[1]] = '-'
            #Update the small board
            smallboard, position = self.botView(inputBoard,orient)
            self.printBoard(smallboard)
            print()

            self.printBoard(inputBoard)


    def botView(self, wholeGrid, direction):
        rowidx = 0
        colidx = 0
        #print(f'in botView, direction: {direction}')
        for count,row in enumerate(wholeboard):
            if 'b' in row:
                rowidx = count
                colidx = row.index('b')
        # self.printBoard(wholeGrid)
        smallGrid = [row[colidx-1:colidx+2] for row in wholeGrid[rowidx-1:rowidx+2]]
        #Define the number of rotations
        rotDict = {'UP':0,'DOWN':2,'RIGHT':1,'LEFT':3}
        # print('in botView\nCurrent Board:\n')
        # self.printBoard(smallGrid)
        # print(f'direction: {direction}')
        # print(f'rotDict: {rotDict[direction]}')
        return (np.rot90(smallGrid,rotDict[direction]).tolist()
                ,(rowidx,colidx)
                )

if __name__ == '__main__':
    # Define a maze
    boardstring = '''#######
#--#-b#
#--#--#
#--#--#
e-----#
#-----#
#######'''.split('\n')
    wholeboard = [list(row) for row in boardstring]
    sim = Simulator()

    sim.Simulate(wholeboard)
