def add_class(): #добавим класс в структуру
    strg_=input()
    #print(strg_, len(strg_))
    if ":" not in strg_: 
        strg_+=" : Object"
    ch, str_pr = strg_.split(" : ")
    
    global graph
    graph.update({ch: str_pr.split(" ")})

def check_child():
    global test, output
    for ind_child, child in enumerate(test[1:], start=1):
        #print("\nБерем РЕБ=", ind_child, child)  

        #может этого реб уже выводили         
        if child in output: pass#print (child, "- REB already Output")
        else: #не проверяли ли мы этого дет раньше, нет ли в списке впереди
            if child in test[:ind_child-1]:
                output.append(child)
#                print (child)#, "- REB Vyvod Povtor")
            else: 
                for parent in test[ind_child-1::-1]: 
                    check_pair(child, parent) 

def check_pair(child, parent):
    global test, ch_pare
    #Проверим не проверяли ли мы эту пару дет-род раньше, нет ли в списке проверено           
        #print("   Берем ROD=", parent)                    
    if child+"<--"+parent in ch_pare: pass
    else: 
        ch_pare.append(child+"<--"+parent)
#        print("      Добавим чек пар", ch_pare)
        #print(" ", child, "<-Find-",  parent)
        find(child, parent)

def find(child, gr_parent, path=[]):
    global graph, output
    #Проверим не проверяли ли мы эту пару дет-род раньше, нет ли в списке проверено           
    #check_pair(child, gr_parent, test)
         
#    print(child, gr_parent, output)
        #path = path + [child]
    if (child not in graph) or (gr_parent not in graph): return "No"
        #if child == gr_parent: return "Yes"
    if gr_parent in graph[child]: 
        if child not in output: print (child)#,"END")
        output=output+[child]
    else: 
        for rod in graph[child]:
            if child not in output:
                #check_child()
                find(rod, gr_parent)

#graph={'ArithmeticError': ['Object'], 'ZeroDivisionError': ['ArithmeticError'], 'OSError': ['Object'], 'FileNotFoundError': ['OSError']}
#test=['ZeroDivisionError', 'OMG', 'OSError', 'ZeroDivisionError', 'FileNotFoundError']
#graph={'ArithmeticError': ['Object'], 'ZeroDivisionError': ['ArithmeticError'], 'OSError': ['Object'], 'FileNotFoundError': ['OSError']}
#test=['ZeroDivisionError', 'OMG', 'OSError', 'ZeroDivisionError', 'FileNotFoundError']
#graph={'winter': ['Object'], 'is': ['Object'], 'coming': ['Object'], 'OMG': ['winter', 'is', 'coming']}
#test=["winter", "is", "OMG", "coming", "is", "OMG"]
#graph={'A': ['Obj'], 'B': ['Obj'], 'C': ['Obj'], 'D': ['A', 'B', 'C']}
#test=["A", "C", "C", "D", "C", "C", "B"]
graph={}
test=[]
output=[]
ch_pare=[]

quant_clases=int(input())
while quant_clases > 0:
    quant_clases-=1
    add_class()

#print(graph)

quant_querry=int(input())
while quant_querry > 0:
    quant_querry-=1
    test.append(input())

check_child()