# AI classic game "threeInRow"
Іnstructions
-------------------------
1. Copy and rename ```example.env.py``` to ```env.py```
2. Changes the variable ```FILE_FOR_TRAINING_PATH```
3. Run ```python main.py```  

Classic simple game Three in Row on python 
-------------------------
The game has two modes: user gameplay and AI gameplay.  The user or AI interacts with the field. In this field, the symbols "O", "X", "Y" are randomly generated each game, and the main task is to make three or more identical symbols in a row horizontally or vertically. In the case of a successful game, one point is scored, if a mistake is made in the game, one mistake will be scored. The game continues until the maximum number of points is reached. Successful games are recorded in the training file for the AI. In the second mode, the game process is carried out by the AI. Based on the training file with successful games, the AI trains and starts the game process.
```
     ╒           ╕
       Score: 10
     ╘           ╛

   | A  B  C  D  E
 -----------------
1  | O  Y  O  O  Y  
2  | Y  Y  O  X  Y  
3  | X  X  Y  O  X  
4  | Y  X  X  O  O  
5  | X  Y  X  Y  X  
Enter first coords (for example: A1): A3
Enter second coords (for example: A1): A4

     ╒           ╕
       Score: 20
     ╘           ╛

   | A  B  C  D  E
 -----------------
1  | X  O  Y  O  Y  
2  | X  O  X  X  Y  
3  | Y  Y  O  O  X  
4  | O  X  X  O  X  
5  | O  O  X  X  O   
```
