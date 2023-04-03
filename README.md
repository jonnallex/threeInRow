﻿# threeInRow
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

Otherwise the 2 characters will be swapped:
```
     ╒           ╕
       Score: 40
     ╘           ╛

   | A  B  C  D  E
 -----------------
1  | Y  O  Y  O  X  
2  | X  Y  X  O  X  
3  | X  Y  X  X  O  
4  | O  X  Y  X  O  
5  | O  Y  O  O  Y  
Enter first coords (for example: A1): C1
Enter second coords (for example: A1): D1

     ╒           ╕
       Score: 40
     ╘           ╛

   | A  B  C  D  E
 -----------------
1  | Y  O  O  Y  X  
2  | X  Y  X  O  X  
3  | X  Y  X  X  O  
4  | O  X  Y  X  O  
5  | O  Y  O  O  Y  
```
