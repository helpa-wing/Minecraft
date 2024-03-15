#bulding house

# Importuj knihovny
from time import sleep

#Definuj funkce

def agente_teleportuj():
    agent.teleport()

#materials 
    '''
    Tato část kódu slouží k přidání materiálů do inventáře agenta, které budou použity při stavbě. Jednotlivé řádky přidávají konkrétní typy materiálů a jejich počet.
'''
agent.give("stripped_oak_wood", 64, 1)
agent.give("oak_log", 64, 2)
agent.give("oak_stairs", 64, 3)
agent.give("oak_slab", 64, 4)
agent.give("oak_trapdoor", 64, 5)
agent.give("oak_door", 1, 6)

def postav_sloup():
    '''
    Tato funkce umisťuje blok na zem a posouvá agenta vpřed.
    '''
    agent.place("down", 2)
    agent.move("forward")

#bulding wall 6x6x5
'''
Tato funkce staví zdi. Agent se nejprve posune nahoru, a poté jsou zde tři vnitřní smyčky. Druhá smyčka  prochází čtyřmi sloupy a vnitřní smyčka staví zdi dopředu. Po dokončení vnitřní smyčky se agent otočí doprava a vnitřní smyčka se opakuje. Celý tento proces se opakuje pětkrát a poté se agent posune nahoru.
'''
def postav_steny(delka):
    agent.move("up")
    # Počet vrstev domu
    for count in range(5):
        # Stěny domu
        for count in range(4):
            postav_sloup()
            for count in range(delka-2):
                agent.place("down", 1)
                agent.move("forward")
            agent.turn("right")
        agent.move("up")
    
#bulding roof
'''
funkce postav_strechu_1(), postav_strechu_2(), postav_strechu_3(), postav_strechu_4() a dostav_strechu_4() staví jednotlivé části střechy tyto funkce jsou rozděleny do kroků, které vysvětlují postup stavby.
'''
def postav_strechu_1(delka):
    '''
    presun na strechu stavenou pomoci schodu
    '''
    agent.move("down")
    agent.move("left")
    agent.move("down")
    agent.move("down")
    agent.turn("right")
    '''
    stavba strechy 1
    prvni smycka jsou styri strany pote postavi osumkrat schody nad sebe a posune se do leva.
    '''
    for blok in range(4):
            for blok in range(delka+1):
                agent.place("up", 3)
                agent.move("left")
            agent.turn("right")
            agent.move("left")
            agent.move("forward")

def postav_strechu_2(delka):
    '''
    presun na strechu 2

    '''
    agent.move("back")
    for count in range(3):
        agent.move("up")
    for count in range(2):
        agent.move("forward")
    agent.turn("left")

    '''
    stavba strechy 2
    prvni smycka opakuj ctyrikrat jako ctyri steny pote postav sest bloku.
    '''
    for count in range(4):
            for count in range(delka-1):
                    agent.place("down", 4)
                    agent.move("forward")
            agent.turn("right")

def postav_strechu_3(delka):
    '''
    presun na strechu 3
    '''
    agent.move("forward")
    agent.move("right")
    '''
    stavba strechy 3
    prvni smycka opakuj ctyrikrat mineno jako ctyri steny pote postav ctyri bloky pod sebe.
    '''
    for count in range(4):
        for count in range(delka-3):
            agent.place("down")
            agent.move("forward")
        agent.turn("right")

def postav_strechu_4(delka):
    '''
    presun na strechu 4
    '''
    #agent.move("forward")
    #agent.move("right")
    agent.move("up")
    '''
    stavba strechy 4
    prvni smycka opakuj ctyrikrat mineno jako ctyri steny pote postav dva bloky pod sebe.
    '''
    for count in range(4):
        for count in range(delka-5):
            agent.place("down", 4)
            agent.move("forward")
        agent.turn("right")

def dostav_strechu_4(delka):
    '''
    presun na dokonceni strechy 4
    '''
    agent.move("forward")
    agent.move("right")
    '''
    dostavba strechy 4
    '''
#    agent.place("down", 4)

    for count in range(4):
        for count in range(delka-5):
            agent.place("down", 4)
            agent.move("forward")
        agent.turn("right")


# Definuj event handler když je v chatu zpráva
def on_player_message(message, sender, receiver, message_type):
    '''
    Tato funkce poslouchá herní chat a spouští programy podle kličových slov, která jsou definovaná níže:
    
    stena - agent staví 1 opakování algoritmu stěny. Pro testování.
    otoc - otočí se 1 krát. Pro testování.
    '''
    slova = message.split()
	try:
        delka = int(slova[1])
    except IndexError:
        delka = None

    # Když je první slovo stěna, proveď stavbu stěny
    if slova[0] == "postav_steny":
        sleep(1)
        postav_steny(6)

    elif slova[0] == "agente_teleportuj":
        sleep(1)
        agente_teleportuj()

    elif slova[0] == "postav_strechu_1":
        sleep(1)
        postav_strechu_1(6)

    elif slova[0] == "postav_strechu_2":
        sleep(1)
        postav_strechu_2(6)

    elif slova[0] == "postav_strechu_3":
        sleep(1)
        postav_strechu_3(6)

    elif slova[0] == "postav_strechu_4":
        sleep(1)
        postav_strechu_4(6)

    elif slova[0] == "dostav_strechu":
        sleep(1)
        dostav_strechu_4()
    # Když je první slovo dum
    elif slova[0] == "dum":
        sleep(1)

        #volani funkci
        '''
        Toto jsou volání funkcí, které postupně staví stěny a střechu ve správném pořadí.
        '''
        postav_steny(delka)
        postav_strechu_1(delka)
        postav_strechu_2(delka)
        postav_strechu_3(delka)
        postav_strechu_4(delka)
        dostav_strechu_4(delka)
