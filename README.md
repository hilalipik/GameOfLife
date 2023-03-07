Game of life is a zero-player game, which means it is detemined by it's initial state. You get to decide what the board looks like at the start of the game, using a text file according to the format.
Every square on the board represents a cell, which can be dead or alive. In each generation a cell can die, revive or stay the same according to it's neighbours(the 6 surrounding cells).

Rules:
    [1] Any live cell with two or three live neighbours survives.
    [2] Any dead cell with three live neighbours becomes a live cell.
    [3] All other live cells die in the next generation, and all other dead cells stay dead.

Format:
    Every dead cell is represented by a space - ' '
    Every living cell is represented by a star - '*'
    Separate the cells with a comma - ','
    You can have as many lines and columns as you'd like.

    See blinker.txt for example