class Star_cinema:
    def __init__(self) -> None:
        self.hall_list=[]


    def entry_hall(self,v):
        self.hall_list.append(v)

class Hall(Star_cinema):
    def __init__(self,row,col,hall_no) -> None:
        self.row=row
        self.col=col
        self.hall_no=hall_no
        self._show_list=[]
        self.seat={}
        val=Star_cinema(row,col,hall_no)
       
        self.entry_hall(val)
       
       
        super().__init__() 
        
        
    def entry_show(self,id,movie_name,time):
        self.id=id
        self._moviename=movie_name
        self._time=time
        show_tuple=(id,movie_name,time)
        self._show_list.append(show_tuple)
        self.seat[id] = [[0 for i in range(self.row)] for i in range(self.col)]
       
       

    
    def book_seats(self,id,row,col):
        
        flag=False
        for i in self._show_list:
            if i[0]==id:
                flag=True


        if (flag==False):
            raise ValueError ('Your choosen show id  is not in our list')    
        
        if (row<0 and row>self._rows-1 and col<0 and col>self.cols -1):
            raise ValueError ('Your choosen seat is out of list')

        if  self.seat[id][row][col]==1:
            raise ValueError ('This seat is already booked')
        else:
         self.seat[id][row][col]=1
        

    
    def view_show_list(self):
        
        print("Now these shows are running : ")
        for i in self._show_list:
            print(i)

   
    def view_available_seats(self, hall_id):
        print(self.seat[hall_id])
    
    
    def __repr__(self) -> str:
        flg=True       
        while(flg==True):
             print("1. view all the show today")
             print("2. view available seats")
             print("3. Book ticket")
             print("4. Exit")

             f=int(input())
             if f==1:
                 for i in self._show_list:
                     print(i)

             elif f==2:
                 print("enter your show id")
                 s=int(input())
                 self.view_available_seats(s)

             elif f==3:
                 print("enter your show id")
                 g=int(input())
                 print(self.seat[g])
                 print("enter your seat row")
                 r=int(input())
                 print("enter your seat column")
                 l=int(input())
                 self.book_seats(g,r,l)
             elif f==4:
                 flg=False

             else:
                 print("wrong input try again")






class Star_cinema:
    def __init__(self) -> None:
        self.hall_list=[]


    def entry_hall(self,v):
        self.hall_list.append(v)

class Hall(Star_cinema):
    def __init__(self,row,col,hall_no) -> None:
        self.row=row
        self.col=col
        self.hall_no=hall_no
        self._show_list=[]
        self.seat={}
        val=(row,col,hall_no)
        cinema=Star_cinema()
        cinema.entry_hall(val)
       
        

       
        super().__init__() 

      
        
        
    def entry_show(self,id,movie_name,time):
        self.id=id
        self._moviename=movie_name
        self._time=time
        show_tuple=(id,movie_name,time)
        self._show_list.append(show_tuple)
        self.seat[id] = [[0 for i in range(self.row)] for i in range(self.col)]
       
       

    
    def book_seats(self,id,row,col):
        
        flag=False
        se=False
       
        for i in self._show_list:
            if i[0]==id:
                flag=True    

        if (row<0 or row>self.row-1 or col<0 or col>self.col -1):
            print("Your choosen seat isnot correct")
        else:
            se=True
            
        if(flag==False):
             print('Your choosen show id  is not in our list')
            

        elif (flag ==True and se==True and self.seat[id][row][col]==1):
            print ('This seat is already booked')
            
        if(flag ==True and se==True and self.seat[id][row][col]!=1):
            self.seat[id][row][col]=1
        

    
    def view_show_list(self):
        
        print("Now these shows are running : ")
        for i in self._show_list:
            print(i)

   
    def view_available_seats(self, hall_id):
        print(self.seat[hall_id])
    
    
    def __repr__(self) -> str:
        flg=True       
        while(flg==True):
             print("1. view all the show today")
             print("2. view available seats")
             print("3. Book ticket")
             print("4. Exit")

             f=int(input())
             if f==1:
                 for i in self._show_list:
                     print(i)

             elif f==2:
                 print("enter your show id")
                 s=int(input())
                 self.view_available_seats(s)

             elif f==3:
                   print("enter your show id")
                   g=int(input())
                   print("enter your seat row")
                   r=int(input())
                   print("enter your seat column")
                   l=int(input())
                  
                   self.book_seats(g,r,l)
             elif f==4:
                 flg=False
                 
                 

             else:
                 print("wrong input try again")
        return "exit the system"






ph=Hall(5,5,1)
ph1=Hall(5,10,2)


ph.entry_show(1,"Super man","9 am")
ph.entry_show(2,"spider Man","10 AM")
ph1.entry_show(3,"spider Man","10 AM")
ph1.entry_show(4,"spider Man","10 AM")


print(ph)
                 

  




                 

  





     
