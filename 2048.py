from tkinter import Frame, Label, CENTER

import LogicsFinal
import constants as c

## frame allows you to create a frmae button box 
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        ##tkinter has grid manager which allow us to make all visit as a 
        ## form of grid 
        ## it is visualises a a grid now (rows and column)
        self.grid()
        ##every thing in a frame has a master thing 
        ## it sets the title of the frame as 2048
        self.master.title('2048')
        ##<key> comes to play if any key is pressed so when any key is 
        ## pressed it will go to the self.key_down function
        self.master.bind("<Key>", self.key_down)
        ## it makes a map in which we connects the constraints key to the
        ## move up down left right funuction with w,s,a,d 
        self.commands = {c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down,
                         c.KEY_LEFT: LogicsFinal.move_left, c.KEY_RIGHT: LogicsFinal.move_right
                        }
        ## grid cells will be created as an empty
        self.grid_cells = []
        ## it actully created cells in our grid
        self.init_grid()
        ## it starts a game and add two 2's at the start
        self.init_matrix()
        ## it continously upgrade the change according to the UI
        ## like colours of the cell etc..
        self.update_grid_cells()
        ## so the initiall things are done 
        ## now the playing loop can be started 
        self.mainloop()

    def init_grid(self):
        ## this creates a grid size 400x400 in the frame which is our main grid
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        ## now by this we can visualize this frame as our main grid
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                ## creates a cell
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                ## add cell in a row grid
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                ## inside cell we created a label
                ## lable means 2,4,8 which we create initialy the text 
                ## was empty
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                ## this grid is append into the cells
                t.grid()
                grid_row.append(t)
            # now the row is appended into the main grid
            self.grid_cells.append(grid_row)


    def init_matrix(self):
        ## it return a matrix of 4x4 from logic file
        ## we change that matrix which is reflected in our UI
        self.matrix = LogicsFinal.start_game()
        ## add new two 2's in the matrix and grid
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                # if the value in the matrix is 0 then it will change 
                ## the colour of that place in UI grid accordinglly
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    ## if the number is not 0 then it will update the number
                    ## and go into the constant class and change the 
                    # cell colour accordingly present in the constants class
                    ## fg=c.CELL_COLOR_DICT[new_number] = it will change the 
                    ## number colour according to the constrant class
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()
    ## event means which key is pressed
    def key_down(self, event):
        key = repr(event.char)
        ## if key is present in our self.commands then this will work
        if key in self.commands:
            ## it executes the command according to the map present in the 
            ## self.command function
            ## it will pass a matrix as a command
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            # if changed happen then it will work
            if changed:
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if LogicsFinal.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if LogicsFinal.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)



gamegrid = Game2048()
