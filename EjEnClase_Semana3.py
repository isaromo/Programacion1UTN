print("Ingrese la fecha actual en formato 'día, DD/MM'")
full_date = input().upper()

day = full_date[0 : full_date.find(",")]
date = int(full_date[full_date.find(" ")+1 : full_date.find("/")])
month = int(full_date[full_date.find("/")+1 : ])

week_days = ["LUNES", "MARTES", "MIERCOLES", "MIÉRCOLES", "JUEVES", "VIERNES"]

if day not in week_days:
    print("ERROR")
elif date < 1 or date > 31:
    print("ERROR")
elif month < 1 or month > 12:
    print("ERROR")
elif day in week_days[0:3]:
    if day == "LUNES":
        print("Nivel inicial")
    elif day == "MARTES":
        print("Nivel intermedio")
    else:
        print("Nivel avanzado")

    print("¿Se tomaron los exámenes? 1. SÍ  2. NO")
    exams = int(input())
    if exams == 1:
        print("Ingrese los alumnos aprobados y desaprobados")
        passed = int(input())
        failed = int(input())
        print("El promedio de los alumnos aprobados es del ", passed * (passed+failed) / 100, "%")
elif day in week_days[4:5]:
    print("Ingrese el porcentaje de asistencia a la clase")
    attendance = int(input())
    if attendance > 50:
        print("Asistió la mayoría")
    else:
        print("No asistió la mayoría")
elif day in week_days[5:6]:
    if date == 1 and month == 1 or month == 7:
        print("Comienzo de nuevo ciclo")
        print("Ingrese la cantidad de alumnos nuevos")
        students = int(input())
        print("Ingrese el arancel")
        fee = float(input())
        print("Ingreso total: ", fee * students)
    
