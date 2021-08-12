
# https://newjazz.dk/Compendiums/scales_of_harmonies.pdf

# https://www.youtube.com/watch?v=Vq2xt2D3e3E

notes = {0:'do',2:'ré',4:'mi',5:'fa',7:'sol',9:'la',11:'si'}
ordre_notes = {0:'do',1:'ré',2:'mi',3:'fa',4:'sol',5:'la',6:'si'}
notes_ordre = {'do':0,'ré':1,'mi':2,'fa':3,'sol':4,'la':5,'si':6}
hauteur_notes = {'do':0,'ré':2,'mi':4,'fa':5,'sol':7,'la':9,'si':11}
alt = {-2:'bb',-1:'b',0:'',1:'#',2:'##'}

class Note:

    def __init__(self,hauteur_relative,alt =0, echelle=0):
        self.hauteur_relative = hauteur_relative % 12
        self.echelle = echelle
        self.alt = alt

    def __repr__(self):
        hauteur = self.hauteur_relative - self.alt
        return notes[hauteur % 12]+alt[self.alt]

class Gamme:

    def __init__(self):
        self.famille = None;
        self.intervalles = None;


    def note_suivante(self,note,intervalle):
        alt = note.alt
        hauteur = note.hauteur_relative
        hauteur_nom_note = (hauteur - alt) %12
        ordre_nom_note = notes_ordre[notes[hauteur_nom_note]]
        nouveau_nom_note = ordre_notes[(ordre_nom_note+1)%7]
        if nouveau_nom_note == 'si':
            nouv_alt = (hauteur + intervalle) - hauteur_notes[nouveau_nom_note]
        elif nouveau_nom_note == 'do' and alt != 1:
            nouv_alt = (hauteur + intervalle - 12)
        else:
            nouv_alt = (hauteur + intervalle) % 12 - hauteur_notes[nouveau_nom_note]
        return Note(hauteur + intervalle,nouv_alt)


    def gen_gamme(self,note):
        gamme = []
        note_suivante = note
        for inter in self.intervalles:
            gamme.append(note_suivante)
            note_suivante = self.note_suivante(note_suivante,inter)
        return gamme

    
majeur = Gamme()
mineur_mel = Gamme()
mineur_harmo = Gamme()

majeur.intervalles = [2,2,1,2,2,2,1]
mineur_mel.intervalles = [1,2,1,2,2,2,2]


def essai(i,j,gamme):
    ma_note = Note(i, j)
    ma_gamme = gamme.gen_gamme(ma_note)
    print(ma_gamme)

def genere_multi_tonalitees(gamme):
    for i in [0,2,4,5,7,9,11]:
        essai(i,0,gamme)
        if not(i in [4,11]):
            essai(i+1, -1,gamme)
        if not (i in [0,5]):
            essai(i - 1, 1,gamme)

genere_multi_tonalitees(majeur)
print("--------")
genere_multi_tonalitees(mineur_mel)
