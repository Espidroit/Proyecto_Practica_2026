from datetime import datetime

fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")

fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
hoy = datetime.today()

edad = hoy.year - fecha_nac.year

if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
    edad -= 1

print("Tu edad es:", edad)