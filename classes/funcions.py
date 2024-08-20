from .configuration import *
from tkinter import messagebox
import os
import time

hum = None
temp = None

def on_sh():
    print("ON SH")
    
    os.system(f"sudo {ON_SH}")
    
def on_c():
    print("ON C")
    
    os.system(f"sudo {ON_C}")
    
def on_asm():
    print("ON ASM - Ensamblador")
    os.system(f"sudo {ON_ASM}")
    os.system(f"sudo {ON_SH}")
    
def off_sh():
    print("OFF SH")
    
    os.system(f"sudo {OFF_SH}")
    
def off_c():
    print("OFF C")
    
    os.system(f"sudo {OFF_C}")
    
def off_asm():
    print("OFF ASM - Ensamblador")
    
    os.system(f"sudo {OFF_ASM}")
    os.system(f"sudo {OFF_SH}")
    
def eval_radiobutton_sh(value):
    on_sh() if value == 1 else off_sh()
    
def eval_radiobutton_c(value):
    on_c() if value == 1 else off_c()
    
def eval_radiobutton_asm(value):
    on_asm() if value == 1 else off_asm()
    
def eval_checkbutton_sh(value):
    on_sh() if value == "1" else off_sh()
    
def eval_checkbutton_c(value):
    on_c() if value == "1" else off_c()
    
def eval_checkbutton_asm(value):
    on_asm() if value == "1" else off_asm()
    
def eval_combobox_sh(value):
    on_sh() if value == "ON" else off_sh()
    
def save_time(initial_hour, initial_minute, final_hour, final_minute):
    if initial_hour == "" or initial_minute == "" or final_hour == "" or final_minute == "":
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        init_hour = int(initial_hour)
        init_minute = int(initial_minute)
        fin_hour = int(final_hour)
        fin_minute = int(final_minute)
    except ValueError:
        messagebox.showerror("Error", "Todos los campos deben ser números")
        return

    if (init_hour < 0 or init_hour > 23 or 
        init_minute < 0 or init_minute > 59 or 
        fin_hour < 0 or fin_hour > 23 or 
        fin_minute < 0 or fin_minute > 59):
        messagebox.showerror("Error", "Las horas deben estar entre 0 y 23 y los minutos entre 0 y 59")
        return

    if (init_hour > fin_hour or 
        (init_hour == fin_hour and init_minute > fin_minute)):
        messagebox.showerror("Error", "La hora inicial debe ser menor o igual a la hora final")
        return
    
    create_task(init_hour, init_minute, fin_hour, fin_minute)
    
def create_task(init_hour, init_minute, fin_hour, fin_minute):
    str_task_on = f"{init_minute} {init_hour} * * * {ROOT} sudo {ON_SH}"
    str_task_off = f"{fin_minute} {fin_hour} * * * {ROOT} sudo {OFF_SH}"

    os.system("sudo rm -f /etc/cron.d/taskon")
    os.system("sudo rm -f /etc/cron.d/taskoff")
    
    os.system("sudo touch /etc/cron.d/taskon")
    os.system("sudo touch /etc/cron.d/taskoff")

    os.system("sudo chmod 666 /etc/cron.d/taskon")
    os.system("sudo chmod 666 /etc/cron.d/taskoff")
    
    with open("/etc/cron.d/taskon", "w") as task_on:
        task_on.write(str_task_on + "\n")

    with open("/etc/cron.d/taskoff", "w") as task_off:
        task_off.write(str_task_off + "\n")
    
    time.sleep(0.1)
    
    os.system("sudo chmod 644 /etc/cron.d/taskon")
    os.system("sudo chmod 644 /etc/cron.d/taskoff")
    
    os.system("sudo service cron restart")

def read_mail():
    os.system(f"sudo {EMAIL_SH}")
