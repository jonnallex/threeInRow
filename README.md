# threeInRow
Іnstructions
-------------------------
1. Copy and rename ```example.env.py``` to ```env.py```
2. Changes the variable ```FILE_FOR_TRAINING_PATH```
3. Run ```python main.py```  

Classic simple game Three in Row on python 

If you move the symbols so that 3 or more symbols become horizontal or vertical, it will update the field and add +10 points 
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
