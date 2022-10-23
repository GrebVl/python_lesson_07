import menu as m
import creating as crea
import reading as rea
import adding as ad
import import_t as imp
import export as exp

action_ = True
while action_ == True:
    action_main = m.menu_click()
    if action_main == 1:
        rea.reading_fail()
    elif action_main == 2:
        ad.adding_fail()
    elif action_main == 3:
        crea.new_fail()
    elif action_main == 4:
        imp.import_fail()
    elif action_main == 5:
        exp.export_fail()
    elif action_main == 6:
        action_ = False



