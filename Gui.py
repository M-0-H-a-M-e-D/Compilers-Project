#importing GUI Library
from tkinter import *
from tkinter import ttk

#Importing Graph Libraries
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

#Creating Main Window in GUI
root = Tk()

#Title for main window
root.title("D F A")

#icon for main window
root.iconbitmap('cest.ico')

#Main window dimensions
root.geometry("1900x1060+0+0")

#Creating Scrollbar
main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH,expand=1)
my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0),window=second_frame,anchor="nw")

#Label
Enter_String=Label(second_frame,text="Enter String",font=("Arial",15))
Enter_String.pack(padx=700)

#Textbox to enter string
EnteredString=StringVar()
EnteredString.set("")
String_Input=Entry(second_frame,textvariable=EnteredString,fg="darkblue",border=10, font=("Arial",15))
String_Input.pack()

#Button to check string and draw DFA
my_button=Button(second_frame, text="Evaluate String",font=("Arial",15),bg="#e91e63",fg="white", command = lambda :matplotCanvas()).pack()

#Funtion for checking charater and next state
def check_string(state,char):
    match state:
        case '1':
            if(char.isalpha() or char == '(' or char == ')'):
                state = '2'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return'2'
            elif(ord(char) >= 48 and ord(char) <= 57):
                state = '3'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '3'
            elif(char in '+-*/'):
                state = 'error'
                print(char + '\t' + state)
                Enter_String13 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String13.pack()
                return 'error'
            elif (char.isspace()):
                state = '1'
                return '1'
            else:
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
        case '2':
            if (char.isalpha() or char == '(' or char == ')'):
                state = '2'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '2'
            elif (ord(char) >= 48 and ord(char) <= 57):
                state = '2'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '2'
            elif (char in '+-*/'):
                state = '4'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '4'
            elif (char.isspace()):
                state = '2'
                return '2'
            else:
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
        case '3':
            if (char.isalpha() or char == '(' or char == ')'):
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
            elif (ord(char) >= 48 and ord(char) <= 57):
                state = '3'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '3'
            elif (char in '+-*/'):
                state = '4'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '4'
            elif (char.isspace()):
                state = '3'
                return '3'
            else:
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
        case '4':
            if (char.isalpha() or char == '(' or char == ')'):
                state = '5'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '5'
            elif (ord(char) >= 48 and ord(char) <= 57):
                state = '6'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '6'
            elif (char in '+-*/'):
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
            elif (char.isspace()):
                state = '4'
                return '4'
            else:
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
        case '5':
            if (char.isalpha() or char == '(' or char == ')'):
                state = state
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '5'
            elif (ord(char) >= 48 and ord(char) <= 57):
                state = '5'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return state
            elif (char in '+-*/'):
                state = '4'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '4'
            elif (char.isspace()):
                state = '5'
                return state
            else:
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
        case '6':
            if (char.isalpha() or char == '(' or char == ')'):
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return
            elif (ord(char) >= 48 and ord(char) <= 57):
                state = '6'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return state
            elif (char in '+-*/'):
                state = '4'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return '4'
            elif (char.isspace()):
                state = '6'
                return state
            else:
                state = 'error'
                print(char + '\t' + state)
                Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
                Enter_String12.pack()
                return 'error'
        case 'error':
            print(char + '\t' + state)
            Enter_String12 = Label(second_frame, text=char + '\t' + state, font=("Arial", 10))
            Enter_String12.pack()
            return 'error'

#Printing token and state name
def check_expression(letter):
    if (letter[0].isalpha()):
        print('< ' + letter +' , ' + 'ID >')
        Enter_String12 = Label(second_frame, text='< ' + letter +' , ' + 'ID >', font=("Arial", 10))
        Enter_String12.pack()
        return 'ID'
    elif(letter == '('):
        print('< ' +letter +' , '+ '"(" >')
        Enter_String12 = Label(second_frame, text='< ' +letter +' , '+ '"(" >', font=("Arial", 10))
        Enter_String12.pack()
        return '"("'
    elif(letter == ')'):
        print('< ' +letter +' , ' + '")" >')
        Enter_String12 = Label(second_frame, text='< ' +letter +' , ' + '")" >', font=("Arial", 10))
        Enter_String12.pack()
        return '")"'
    elif(ord(letter[0]) >= 48 and ord(letter[0]) <= 57):
        print('< ' +letter +' , ' + 'Num >')
        Enter_String12 = Label(second_frame, text='< ' +letter +' , ' + 'Num >', font=("Arial", 10))
        Enter_String12.pack()
        return 'Num'
    elif(letter[0] in '+-*/'):
        print('< ' +letter +' , '+  'operator >')
        Enter_String12 = Label(second_frame, text='< ' +letter +' , '+  'operator >', font=("Arial", 10))
        Enter_String12.pack()
        return 'operator'


#Initializing directed graph
G = nx.DiGraph()

#Creating edges
#Creatiing nodes from edges
edges = [[' ','1'],['1','2'],['1','3'],['1','error'],['2','2'],['2','4'],['3','4'],['3','error'],['3','3'],['4','5'],['4','6'],['4','error'],['5','5'],['5','4'],['6','4'],['6','6'],['6','error']]

#addinng edges to graph
G.add_edges_from(edges)

#Setting position of each node
pos={' ':(0,0),'1':(5,0),'2':(10,10),'3':(10,0),'4':(15,0),"6":(20,0),"5":(20,10),'error':(7.5,-10)}

#setting color of accepting states to lightblue and non-accepting to light green
color_map = []
for node in G:
    if (node == "5" or node == "6"):
        color_map.append('lightblue')
    else:
        color_map.append('lightgreen')


round_edges = [['5','4'],['6','4'],['4','5'],['4','6']]
not_round = [[' ','1'],['1','2'],['1','3'],['1','error'],['2','2'],['2','4'],['3','4'],['3','error'],['3','3'],['4','error'],['5','5'],['6','6'],['6','error']]

#Function to plot graph and check string entered
def matplotCanvas():
    state = '1'
    x = EnteredString.get()

    print('element' + '\t' + 'state')
    Enter_String12 = Label(second_frame, text='element' + '\t' + 'state', font=("Arial", 10))
    Enter_String12.pack()

    for i in range(0, len(x)):
        i = i + 1
        state = check_string(state, x[i - 1])

    print('----------------------------------------')
    Enter_String12 = Label(second_frame, text='----------------------------------------', font=("Arial", 10))
    Enter_String12.pack()
    if (state == '5' or state == '6'):
        print('accepted')
        Enter_String12 = Label(second_frame, text='accepted', font=("Arial", 10))
        Enter_String12.pack()
    else:
        print('rejected')
        Enter_String12 = Label(second_frame, text='rejected', font=("Arial", 10))
        Enter_String12.pack()
    print('----------------------------------------')
    Enter_String12 = Label(second_frame, text='----------------------------------------', font=("Arial", 10))
    Enter_String12.pack()
    # regular expression
    letter = x.split()
    for word in letter:
        check_expression(word)
    print('----------------------------------------')
    Enter_String12 = Label(second_frame, text='----------------------------------------', font=("Arial", 10))
    Enter_String12.pack()

    # x + y * 8 - ( sum1 ) * 3
    plt.axis('off')
    f= plt.figure()
    a= f.add_subplot(111)
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1, edgelist=not_round,
        node_size=1000, node_color=color_map, font_size=7,
        labels={node: node for node in G.nodes()}
    )
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1, edgelist=round_edges,
        node_size=1000, node_color=color_map, font_size=7, connectionstyle='arc3, rad = 0.2',
        labels={node: node for node in G.nodes()})
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={
            ('1', '2'): 'letter,"(",")"',
            ('1', '3'): 'Num',
            ('2', '4'): 'Operator',
            ('3', '4'): 'Operator',
            ('4', '5'): 'Operator \nletter,"(",")"',
            ('4', '6'): 'Operator \nNum',
            ('1', 'error'): 'others',
            ('3', 'error'): 'letter',
            ('6', 'error'): 'letter',
            ('2', '2'): 'letter\nNum\n\n\n\n',
            ('3', '3'): 'Num\n\n\n\n',
            ('4', 'error'): 'others', },
        font_color='black',
    )
    #a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    canvas = FigureCanvasTkAgg(f)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill = BOTH, expand = True)
    #toolbar=NavigationToolbar2Tk(canvas,second_frame)
    canvas._tkcanvas.pack(side=TOP, fill = BOTH, expand = True)

#Prevents program from closing
root.mainloop()
