from TP6_functions import fill_goals, show_goals, show_outcomes

'''EJERCICIO 8'''

'''all_goals = fill_goals(all_goals) #lleno la tabla'''
#tabla para probar el programa sin tener que ingresar datos:
all_goals = [[0,4,2,1,3,2,1,0,0,1], [5,0,3,2,0,1,2,4,2,2], [0,2,0,1,1,1,1,5,2,0], [1,0,2,0,1,1,2,3,2,0], [4,3,2,1,0,2,3,4,1,1], [0,0,2,0,4,0,1,1,2,3], [3,1,1,2,4,1,0,1,1,2], [2,2,2,4,1,0,0,0,1,1], [3,1,1,2,3,2,1,1,0,1], [1,4,2,3,4,1,2,0,1,0]]

show_goals(all_goals)   #muestro la tabla completa
print("")
show_outcomes(all_goals)