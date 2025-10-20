import turtle

def draw_tree(level, branch_length):
    ''' A recursive function to draw trees
        level - the number of levels of branches
        branchlength - the length of branch to draw
    '''
    # as long as we're not at the leaf level
    if level > 0:

        # 1. draw a branch
        turtle.forward(branch_length)

        # 2. Turn left and make a mini tree
        turtle.left(40)
        draw_tree(level-1, branch_length/1.61)

        # 3. turn right and make a mini tree 
        turtle.right(80)
        draw_tree(level-1, branch_length/1.61)

        # 4. Go back
        turtle.left(40)
        draw_tree(branch_length)

        # otherwise if we are at the leaf level 0
    else:
        # stamp the leaf
        turtle.color("green")
        turtle.stamp()
        turtle.color("brown")

    # move the turtle 
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -180)
    turtle.left(90)
    turtle.pendown()

    # setup drawing
    turtle.color("brown")
    turtle.width(3)
    turtle.shape("triangle")

    # draw a tree using a recrusive fuction
    draw_tree(2, 120)
