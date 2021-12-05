# Py_2048
My attempt at remaking the classic game 2048

Note this runs on the terminal.  
To run type "python3 game.py" and hit enter.  
I tested it in python 3.97 and 3.10.

Log 03/12:  
*theres something wrong with the logic some numbers dissapear for some unknown reason __ I cant quite confirm my hypothesis but it seems as if the vertical movements are faulty*.  
05/12:.  
*Update the problem isnt just the verticals, the problem appears to be that when a move is made and introduces a new number this number also moves and in the case where its adjacent to a similar number they combine and my earlier observation of dissapearing numbers is explained.  
*This sould be fairly easy to get rid off, I'll add the new number after the board is moved around.  
*idk lol one row had [0,2,8,4] and turned to [0,2,2,4] I cant explain what exactly happens but the moving is obviously bad.  
*I've decided to remake my movement methods but not before testing the old ones.
*Upon further investigation the old methods seem to work properly and the problem lies elsewhere but I do feel like i found a more efficient way of moving the board which i'll use.  
*The problem was the clean and populate functions they were creating and producing an array with too many values.  
"""
I will be uploading the file later when I finish tweaking it  
