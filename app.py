from classes.funcions import *
from classes.configuration import *
from classes.vars import *
from tkinter import *
from tkinter import font
from tkinter import ttk
import subprocess

window = Tk()
window.title("Control GPIO 2024")
window.geometry('650x750+0+0')

TITLE_FONT = font.Font(family='Times New Roman', size=20, weight='bold')
TEXT_FONT = font.Font(family='Arial', size=12)

ON_IMG = PhotoImage(file=ON_IMG)
OFF_IMG = PhotoImage(file=OFF_IMG)

initial_hour = StringVar()
initial_minute = StringVar()
final_hour = StringVar()
final_minute = StringVar()
temp_pro = None
pir_pro = None

Label(window, text="SCADA GPIO", font=TITLE_FONT).place(x=250, y=20)
Label(window, text="Temperatura", font=TEXT_FONT).place(x=50, y=80)
Label(window, text="Humedad", font=TEXT_FONT).place(x=480, y=80)

def leer_valores():
    try:
        with open("/home/sps/examen/status/temp.txt", "r") as temp_file:
            temperatura = temp_file.readline().strip()
        
        with open("/home/sps/examen/status/hum.txt", "r") as hum_file:
            humedad = hum_file.readline().strip()
        
        return temperatura, humedad
    except FileNotFoundError:
        return "N/A", "N/A"
    

def update():
    temperatura, humedad = leer_valores()

    if (check_email.get() == "1" ):
        read_mail()

    Button(window, image=ON_IMG if get_status() == "1" else OFF_IMG).place(x=290, y=80)
    Label(window, text=f"{temperatura if (temperatura != None) else 0} C", font=TITLE_FONT).place(x=70, y=100)
    Label(window, text=f"{humedad if (humedad != None) else 0} %", font=TITLE_FONT).place(x=500, y=100)

    window.after(1000, update)

def get_status():
    return open(STATUS, "r").read().split('\n')[0]

def modal():
    time_modal = Toplevel(window)
    time_modal.title("Configurar tiempo")
    time_modal.geometry('300x300+325+225')
    
    Label(time_modal, text="Hora inicial", font=TEXT_FONT).place(x=50, y=50)
    Label(time_modal, text="Hora final", font=TEXT_FONT).place(x=50, y=100)
    Label(time_modal, text="Minuto inicial", font=TEXT_FONT).place(x=50, y=150)
    Label(time_modal, text="Minuto final", font=TEXT_FONT).place(x=50, y=200)
    
    Entry(time_modal, textvariable=initial_hour, width=12).place(x=150, y=50)
    Entry(time_modal, textvariable=initial_minute, width=12).place(x=150, y=150)
    Entry(time_modal, textvariable=final_hour, width=12).place(x=150, y=100)
    Entry(time_modal, textvariable=final_minute, width=12).place(x=150, y=200)
    
    Button(time_modal, text="Guardar configuración", font=TEXT_FONT, command=lambda: save_time(initial_hour.get(), initial_minute.get(), final_hour.get(), final_minute.get())).place(x=60, y=250)
    
    time_modal.mainloop()

def activete_sensors():
    global temp_pro, pir_pro

    if check_sensor.get() == "1":
        if temp_pro is None or temp_pro.poll() is not None:
            try:
                temp_pro = subprocess.Popen(["python3", "/home/sps/examen/scripts/py/temp.py"])
                print("Sensor TEMP activado.")
            except Exception as e:
                print(f"Error al iniciar el sensor: {e}")
        else:
            print("El sensor ya está activo.")
            
        if pir_pro is None or pir_pro.poll() is not None:
            try:
                pir_pro = subprocess.Popen(["python3", "/home/sps/examen/scripts/py/pir.py"])
                print("Sensor PIR activado.")
            except Exception as e:
                print(f"Error al iniciar el sensor: {e}")
        else:
            print("El sensor ya está activo.")
    else:
        if temp_pro is not None and temp_pro.poll() is None:
            temp_pro.terminate()
            try:
                temp_pro.wait(timeout=10)
                print("Sensor TEMP desactivado.")
            except subprocess.TimeoutExpired:
                temp_pro.kill()
                print("El sensor no respondió y fue forzado a detenerse.")
        else:
            print("El sensor ya está desactivado o no fue iniciado.")

        if pir_pro is not None and pir_pro.poll() is None:
            pir_pro.terminate()
            try:
                pir_pro.wait(timeout=10)
                print("Sensor PIR desactivado.")
            except subprocess.TimeoutExpired:
                pir_pro.kill()
                print("El sensor no respondió y fue forzado a detenerse.")
        else:
            print("El sensor ya está desactivado o no fue iniciado.")


# Creando controles SH
Label(window, text="Controles con SH", font=TITLE_FONT).place(x=50, y=180)
Button(window, text="Configurar tiempo", font=TEXT_FONT, command=modal).place(x=420, y=180)
Canvas(window, width=550, height=2, bg="black").place(x=50, y=220)

# Botones
Button(window, text="ON", font=TEXT_FONT, command=on_sh).place(x=50, y=240)
Button(window, text="OFF", font=TEXT_FONT, command=off_sh).place(x=150, y=240)

# Radio buttons
radio_sh = IntVar()
Radiobutton(window, text="ON", font=TEXT_FONT, value="1", variable=radio_sh, command=lambda: eval_radiobutton_sh(radio_sh.get())).place(x=50, y=290)
Radiobutton(window, text="OFF", font=TEXT_FONT, value="0", variable=radio_sh, command=lambda: eval_radiobutton_sh(radio_sh.get())).place(x=150, y=290)

# Checkbox
check_sh = StringVar()
Checkbutton(window, text="ON / Off", font=TEXT_FONT, variable=check_sh, command=lambda: eval_checkbutton_sh(check_sh.get())).place(x=50, y=330)

# Combobox
combo_sh = StringVar()
ttk.Combobox(window, textvariable=combo_sh, values=["ON", "OFF"], font=TEXT_FONT).place(x=50, y=370)
Button(window, text=">", font=TEXT_FONT, command=lambda: eval_combobox_sh(combo_sh.get())).place(x=250, y=370)

# Creando controles C 
Label(window, text="Controles con C", font=TITLE_FONT).place(x=50, y=420)
Canvas(window, width=220, height=2, bg="black").place(x=50, y=460)

# Botones
Button(window, text="ON", font=TEXT_FONT, command=on_c).place(x=50, y=480)
Button(window, text="OFF", font=TEXT_FONT, command=off_c).place(x=150, y=480)

# Radio buttons
radio_c = IntVar()
Radiobutton(window, text="ON", font=TEXT_FONT, value="1", variable=radio_c, command=lambda: eval_radiobutton_c(radio_c.get())).place(x=50, y=540)
Radiobutton(window, text="OFF", font=TEXT_FONT, value="0", variable=radio_c, command=lambda: eval_radiobutton_c(radio_c.get())).place(x=150, y=540)

# Checkbox
check_c = StringVar()
Checkbutton(window, text="ON / Off", font=TEXT_FONT, variable=check_c, command=lambda: eval_checkbutton_c(check_c.get())).place(x=50, y=580)

# Creando controles ASM - Ensamblador
Label(window, text="Controles con ASM", font=TITLE_FONT).place(x=350, y=420)
Canvas(window, width=220, height=2, bg="black").place(x=350, y=460)

# Botones
Button(window, text="ON", font=TEXT_FONT, command=on_asm).place(x=350, y=480)
Button(window, text="OFF", font=TEXT_FONT, command=off_asm).place(x=450, y=480)

# Radio buttons
radio_asm = IntVar()
Radiobutton(window, text="ON", font=TEXT_FONT, value="1", variable=radio_asm, command=lambda: eval_radiobutton_asm(radio_asm.get())).place(x=350, y=540)
Radiobutton(window, text="OFF", font=TEXT_FONT, value="0", variable=radio_asm, command=lambda: eval_radiobutton_asm(radio_asm.get())).place(x=450, y=540)

# Checkbox
check_asm = StringVar()
Checkbutton(window, text="ON / Off", font=TEXT_FONT, variable=check_asm, command=lambda: eval_checkbutton_asm(check_asm.get())).place(x=350, y=580)

# Creando controles Email
Label(window, text="Controles controles", font=TITLE_FONT).place(x=50, y=640)
Canvas(window, width=550, height=2, bg="black").place(x=50, y=680)

# Checkbox
check_email = StringVar()
check_sensor = StringVar()
Checkbutton(window, text="Activar servicio de correo", font=TEXT_FONT, variable=check_email).place(x=50, y=700)
Checkbutton(window, text="Activar servicio de sensores", font=TEXT_FONT, variable=check_sensor, command=activete_sensors).place(x=280, y=700)

update()

window.mainloop()