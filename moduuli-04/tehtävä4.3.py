"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

"""
luvut = []
luku = input("Anna luku: ")

while luku!="":
    luvut.append(luku)
    print(luvut)
    luku = (input("Anna seuraava luku tai lopeta painamalla Enter: "))

if luku=="":
    if luvut==[]:
        print("Toiminto lopetettu. ")
    else:
        print(f"Suurin luku on " + max(luvut))
        print(f"Pienin luku on " + min(luvut))
        print("Toiminto lopetettu. ")