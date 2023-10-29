from TP6_functions import show_array, add_students

#EJERCICIO 6
prim_stud = set(add_students("primario"))
sec_stud = set(add_students("secundario"))

print("\nPRIMARIA:")
show_array(prim_stud)
print("\n\nSECUNDARIA:")
show_array(sec_stud)

print("\n\nNombres REPETIDOS entre estudiantes de primaria y secundaria:")
show_array(prim_stud & sec_stud) #intersección de conjuntos (&): muestra aquellos elementos repetidos en ambos conjuntos

print("\n\nNombres de estudiantes de primaria NO repetidos en estudiantes de secundaria:")
show_array((prim_stud - sec_stud))