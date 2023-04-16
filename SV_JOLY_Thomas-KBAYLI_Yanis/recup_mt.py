MOVES = [">","<","-"]


def create_dic(path):
    with open(path) as f:
        l = f.readlines()
        f.close()

    etats_transitions = {}

    liste_etats = []
    liste_transitions = []

    lecture_etat = True
    lecture_transition = False

    for ligne in l:
        if (len(ligne) > 1 and lecture_etat) or "M'" in ligne:
            etat = []
            car = []
            i = 0
            while ligne[i-1] != ",":
                etat.append(ligne[i])
                i+=1
            while i < len(ligne)-1:
                if ligne[i] == "M" and ligne[i+1] == "'":
                    liste_transitions.append(["M'",ligne[i+3:len(ligne)-1]])
                    i = len(ligne)
                elif ligne[i] != ",":
                    car.append(ligne[i])
                
                i+=1
            if "M'" not in ligne:
                lecture_etat = False
                lecture_transition = True
            else:
                lecture_etat = True
                lecture_transition = False
            liste_etats.append(["".join(etat),"".join(car)])
        elif len(ligne) > 1 and lecture_transition:
            etatnv = []
            carnv = []
            mouv = []
            i = 0
            while ligne[i] != ",":
                etatnv.append(ligne[i])
                i+=1
            i+=1
            while ligne[i+1] not in MOVES:
                if ligne[i] != ",":
                    carnv.append(ligne[i])
                i+=1
            i+=1
            while i < len(ligne)-1 :
                if ligne[i] != ",":
                    mouv.append(ligne[i])
                i+=1
            lecture_etat = True
            lecture_transition = False
            liste_transitions.append(["".join(etatnv),carnv,mouv])

    for k in range(len(liste_etats)):
        etats_transitions["".join(liste_etats[k])] = liste_transitions[k]
    return etats_transitions


