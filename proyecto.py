from proyecto_simulacion import validateQueens
from proyecto_simulacion_random import validateQueensRandom
from random import randint
from threading import Thread

#Attributes
# Numero de retadores
opponents = 50
#********************
# Intervalo de iteraciones para la llegada de un retador
interval_challenge = 800
#********************
# Desviacion estadar dada por un octavo de el intervalo de iteraciones, se usa como tope para la generacion aleatoria
deviation = int(interval_challenge/8)
# ***************************************

data = {}
data['timer'] = 0
attended_last = 0 

stadisticals = []
stadisticals.append(
    (
        '0',
        'person_0_arrival_time',0,
        'person_0_attended_time',0,
        'person_0_waiting_time',0
    )
)

counter = 0
#******************

def challengeMaster(to_use):
    if to_use == 0:
        data['standard_uses'] = data.get('standard_uses',0) + 1
        return validateQueens(0,0,data)
    elif to_use == 1:
        data['las_vegas_uses'] = data.get('las_vegas_uses',0) + 1
        return validateQueensRandom(0,0,data)

while opponents > counter:
    counter += 1

    data['timer'] += interval_challenge + (randint(0,(2*deviation))-deviation)

    time_start = data.get('iterations',0)
    #to_use = randint(0,1) - Usar para evualar con metodo las vegas y determinista con 50% de probabilidad
    #to_use = 0            - Usar para evualar con metodo las vegas y determinista con 50% de probabilidad
    #to_use = 1            - Usar para evualar con metodo las vegas y determinista con 50% de probabilidad
    challengeMaster(randint(0,1))
    time_game = data.get('iterations',0) - time_start

    time_attended = (time_start+time_game) if (time_start+time_game) > data.get('timer',0) else data.get('timer',0)
    time_waiting = time_attended - data['timer']
    
    if opponents > counter:
        stadisticals.append(
            (
                str(counter),
                'person_'+str(counter)+'_arrival_time',data.get('timer',0),
                'person_'+str(counter)+'_attended_time',time_attended,
                'person_'+str(counter)+'_waiting_time', time_waiting,
                'person_'+str(counter-1)+'_game_time',time_game,
                'person_'+str(counter-1)+'_leave_time',attended_last+time_game,
                'idle_time', time_attended - (attended_last+time_game) if time_attended - (attended_last+time_game) > 0 else 0
            )
        )
    else:
        stadisticals.append(
            (
                str(counter),
                'person_'+str(counter-1)+'_time_game',time_game,
                'person_'+str(counter-1)+'_leave_time',attended_last+time_game
            )
        )

    attended_last = time_attended

for e,row in enumerate(stadisticals):
    if e==0:
        data['waiting_time_avg'] = data.get('waiting_time_avg',0) + row[6]
    elif e>0 and e < (len(stadisticals)-2):
        data['waiting_time_avg'] = data.get('waiting_time_avg',0) + row[6]
        data['idle_time_avg'] = data.get('idle_time_avg',0) + row[12]

    #print(row)

data['waiting_time_total'] = data['waiting_time_avg']
data['idle_time_total'] = data['idle_time_avg']
data['waiting_time_avg'] = data['waiting_time_avg']/len(stadisticals)
data['idle_time_avg'] = data['idle_time_avg']/len(stadisticals)

print('Using Stadistics ---->',data)