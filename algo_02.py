# stavba domu
agent.teleport()
#materialy
'''
Přidělujeme agentovi materiály potřebné pro stavbu domu.
'''
agent.give("brick_block", 64, 1)
agent.give("stone_bricks", 64, 2)
agent.give("stone_slab", 64, 3)
agent.give("stone_brick_stairs", 64, 4)
agent.give("brick_stairs", 64, 5)
agent.give("brick_slab", 64, 6)

#definice funkci
'''
Tyto dvě funkce definují postup pro stavbu jednotlivých řad stěn. Funkce postav_rady_stena_1a3 staví první a třetí řadu stěn, zatímco funkce postav_radu_stena_2 staví druhou řadu stěn.
'''
agent.move("up")
def postav_rady_stena_1a3():
    '''
    Staví první a třetí řadu stěn
    '''
    for count in range(4):
        agent.place("down", 2)
        agent.move("forward")
        for count in range(3):
            agent.place("down")
            agent.move("forward")
        agent.turn("left")
    agent.move("up")

def postav_radu_stena_2():
    '''
    Staví druhou řadu stěny
    '''
    for count in range(4):
        for count in range(4):
            agent.place("down", 1)
            agent.move("forward")
        agent.turn("left")
    agent.move("up")


#strecha
'''
Tyto dvě funkce se týkají stavby střechy. Funkce presun_na_lichou_strechu přesune agenta na správnou pozici pro stavbu liché střechy. Funkce postav_lichou_strechu staví samotnou lichou střechu pomocí několika posunů agenta a umisťování materiálů.
'''
def presun_na_lichou_strechu():
    '''
    Přesunuje agenta na správne misto pro stavbu liché střechy
    '''
    for count in range(2):
        agent.move("back")
        agent.move("down")
    agent.move("right")

def postav_lichou_strechu():
    '''
    Staví samotnou lichou střechu
    '''
    for count in range(3):
        agent.place("forward", 4)
        agent.move("up")
        agent.move("forward")

    agent.move("right")
    agent.move("forward")
    agent.turn("left")
    agent.move("down")
    agent.place("forward", 4)

    for count in range(2):
        agent.move("right")
    agent.move("forward")
    agent.turn("left")

    for count in range(3):
        agent.place("forward", 4)
        agent.move("down")
        agent.move("back")

def presun_na_sudou_strechu():
    '''
    Přesunuje agenta na správne misto pro stavbu sudé střechy
    '''
    agent.move("forward")
    agent.move("right")
    agent.move("up")

def postav_sudou_strechu():
    '''
    Staví samotnou sudou střechu
    '''
    for count in range(5):
        agent.place("forward", 4)
        agent.move("right")


def presun_na_vyplneni_sude_strechy():
    '''
    Přesunuje agenta na misto pro vyplnění střechy
    '''
    agent.move("up")
    agent.move("left")
    agent.move("forward")

def vypln_sudou_strechu_rada1_z_prava_do_leva():
    '''
    Vyplňuje první řadu střechy zprava doleva
    '''
    for count in range(2):
        agent.place("forward", 5)
        agent.move("left")
    agent.place("forward", 4)
    agent.move("left")
    for count in range(2):
        agent.place("forward", 5)
        agent.move("left")
    agent.move("up")

def presun_na_vyplneni_sude_strechy_2():
    '''
    Přesunuje agenta na misto pro druhou část vyplňování střechy
    '''
    agent.move("right")
    agent.move("forward")

def vypln_sudou_strechu_rada2_z_leva_do_prava():
    '''
    Vyplňuje druhou řadu střechy zleva doprava
    '''
    for count in range(2):
        agent.place("forward", 5)
        agent.move("right")
    agent.place("forward", 4)
    agent.move("right")
    for count in range(2):
        agent.place("forward", 5)
        agent.move("right")
    agent.move("up")

def presun_na_vyplneni_horni_strechy_3():
    '''
    Přesunuje agenta na pozici pro třetí část vyplňování střechy
    '''
    for count in range(2):
        agent.move("forward")

def vyplneni_horni_strechy():
    '''
    Vyplňuje horní část střechy
    '''
    for count in range(5):
        agent.move("left")
        agent.place("down", 3)

def presun_pro_vyplneni_liche_strechy_z_prava_do_leva():
    agent.move("forward")
    agent.turn("left")
    agent.move("back")
    for count in range(2):
        agent.move("down")

def vyplneni_liche_strechy_z_prava_do_leva():
    for count in range(3):
        agent.place("forward")
        agent.move("left")

def vnitrni_presun_pro_vyplneni_liche_strechy_z_prava_do_leva():
    for count in range(2):
        agent.move("back")
    for count in range(2):
        agent.turn("left")

def presun_na_vyplneni_sude_strechy_rada1_z_prava_do_leva():
    for count in range(3):
        agent.move("back")
    agent.turn("right")
    agent.move("back")




# Volání funkcí pro postavení domu

postav_rady_stena_1a3()
postav_radu_stena_2()
postav_rady_stena_1a3()
presun_na_lichou_strechu()
postav_lichou_strechu()
presun_na_sudou_strechu()
postav_sudou_strechu()
postav_lichou_strechu()
presun_na_sudou_strechu()
postav_sudou_strechu()
presun_na_vyplneni_sude_strechy()
vypln_sudou_strechu_rada1_z_prava_do_leva()
presun_na_vyplneni_sude_strechy_2()
vypln_sudou_strechu_rada2_z_leva_do_prava()
presun_na_vyplneni_horni_strechy_3()
vyplneni_horni_strechy()
presun_pro_vyplneni_liche_strechy_z_prava_do_leva()
vyplneni_liche_strechy_z_prava_do_leva()
vnitrni_presun_pro_vyplneni_liche_strechy_z_prava_do_leva()
vyplneni_liche_strechy_z_prava_do_leva()
presun_na_vyplneni_sude_strechy_rada1_z_prava_do_leva()
vypln_sudou_strechu_rada1_z_prava_do_leva()
presun_na_vyplneni_sude_strechy_2()
vypln_sudou_strechu_rada2_z_leva_do_prava()






