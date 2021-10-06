
Chinese = {0:'Ling',1:'Yi',2:'Er',3:'San',4:'Si',5:'Wu',6:'Liu',7:'Qi',8:'Ba',9:'Jiu',10:'Shi'}
def mandarine():
    try:
        Output = int(input('Enter any Number:\t'))
        try:
                if Output < 11:
                    print(Chinese[Output])

                elif Output > 10 and type(Output  // 10 ) == int and Output % 2 == 0:
                    print(Chinese[Output / 10] +' '+ Chinese[10])
                elif Output > 10 and type(Output/10) == float and Output % 2 != 0 :
                    print(Chinese[Output//10] + ' ' + Chinese[10] + ' ' + Chinese[Output % 10]) 
        except:
                if Output > 10 and type(Output/10) == float and Output % 2 == 0 :
                    print(Chinese[Output//10] + ' ' + Chinese[10] + ' ' + Chinese[Output % 10])
  
    except:
        print('Pls , Input an int')
    
                
           
mandarine()



    