import random
caleFisierOrase = "berlin52.txt"

def citesteInfoOraseFisier(caleFisierOrase):
    with open(caleFisierOrase) as f:
        linii = f.readlines()
        informatiiOrase = []
        for linie in linii:
            linie = linie.strip()
            if linie != "":
                parti = linie.split(" ")
                informatiiOras = (int(parti[0]) - 1, float(parti[1]), float(parti[2]))
                informatiiOrase.append(informatiiOras)
        return informatiiOrase

informatiiOrase = citesteInfoOraseFisier(caleFisierOrase)
# print(informatiiOrase)

def calculeazaDistantaEuclideana(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
def calculeazaDistanteEuclidieneOrase(informatiiOrase):
    distanteEucliedene = {}
    for i in range(len(informatiiOrase)):
        for j in range(len(informatiiOrase)):
            if i != j:
                distantaEucliedena = calculeazaDistantaEuclideana(informatiiOrase[i][1], informatiiOrase[i][2], informatiiOrase[j][1], informatiiOrase[j][2])
                distanteEucliedene[(i, j)] = distantaEucliedena
                distanteEucliedene[(j, i)] = distantaEucliedena
    return distanteEucliedene

distanteEucliedene = calculeazaDistanteEuclidieneOrase(informatiiOrase)
# print(distanteEucliedene)

def calculeazaFitnessCandidat(candidat, distanteEucliedene):
    suma = 0
    for i in range(len(candidat) - 1):
        suma += distanteEucliedene[(candidat[i], candidat[i + 1])]
    suma += distanteEucliedene[(candidat[-1], candidat[0])]
    return suma

def genereazaPopulatieInitiala(distanteEuclidiene, nrOrase, dimensiunePopulatie):
    populatie = []
    for i in range(dimensiunePopulatie):
        candidat = [i for i in range(nrOrase)]
        random.shuffle(candidat)
        fitnessCandidat = calculeazaFitnessCandidat(candidat, distanteEucliedene)
        populatie.append((candidat, fitnessCandidat))
    return populatie

def selectieParinte(populatie, marimeTurnir):
    turnir = random.sample(populatie, marimeTurnir)
    return min(turnir, key = lambda x: x[1])[0]

def crossover(parinte1, parinte2):
    copil = [-1 for i in range(len(parinte1))]
    for i in range(len(parinte1)):
        copil[parinte2[i]] = parinte1[i]
    return copil 

def genereazaUrmasi(populatie, marimeTurnir):
    urmasi = []
    for i in range(len(populatie)):
        parinte1 = selectieParinte(populatie, marimeTurnir)
        parinte2 = selectieParinte(populatie, marimeTurnir)
        copil = crossover(parinte1, parinte2)
        fitnessCopil = calculeazaFitnessCandidat(copil, distanteEucliedene)
        urmasi.append((copil, fitnessCopil))
    return urmasi

def suferaMutatie(candidat):
    # k = random.randint(0, len(candidat[0]) - 1)
    k = 3
    for _ in range(k):
        i = random.randint(0, len(candidat[0]) - 1)
        j = random.randint(0, len(candidat[0]) - 1)
        candidat[0][i], candidat[0][j] = candidat[0][j], candidat[0][i]

def mutatie(populatie, probabilitateMutatie):
    for i in range(len(populatie)):
        if random.random() < probabilitateMutatie:
            suferaMutatie(populatie[i])

def algoritmGenetic(distanteEucliedene, nrOrase, dimensiunePopulatie, probabilitateMutatie, nrGeneratii, marimeTurnir):
    for i in range(nrGeneratii):
        populatie = genereazaPopulatieInitiala(distanteEucliedene, nrOrase, dimensiunePopulatie)
        urmasi = genereazaUrmasi(populatie, marimeTurnir)
        populatie += urmasi
        mutatie(populatie, probabilitateMutatie)
        populatie.sort(key = lambda x: x[1])
        populatie = populatie[:dimensiunePopulatie]
        print(populatie[0])

algoritmGenetic(distanteEucliedene, 52, 1000, 0.6, 1000, 50)

def temperature(timp):
    return 1 / timp

def hillClimbing(distanteEuclidiene, nrOrase, taboo, deltaTimp):
    timp = 1
    candidat = [i for i in range(nrOrase)]
    random.shuffle(candidat)
    taboo.add(tuple(candidat))
    fitnessCandidat = calculeazaFitnessCandidat(candidat, distanteEucliedene)

    while True:
        ok = False
        for i in range(nrOrase):
            for j in range(nrOrase):
                if i != j:
                    vecin = candidat.copy()
                    vecin[i], vecin[j] = vecin[j], vecin[i]
                    if tuple(vecin) not in taboo:
                        taboo.add(tuple(vecin))
                        fitnessVecin = calculeazaFitnessCandidat(vecin, distanteEucliedene)
                        if fitnessVecin < fitnessCandidat:
                            ok = True
                            candidat = vecin
                            fitnessCandidat = fitnessVecin
                            # print(fitnessCandidat, candidat)
        if not ok:
            datCuBanu = random.random()
            if datCuBanu < temperature(timp):
                return candidat, fitnessCandidat
            else:
                random.shuffle(candidat)
                fitnessCandidat = calculeazaFitnessCandidat(candidat, distanteEucliedene)
        timp += deltaTimp

# hillClimbing(distanteEucliedene, 52)

def hillClimbingFlota(distanteEuclidiene, nrOrase, cataratori, deltaTimp):
    
    taboo = set([])
    candidat, fitnessCandidat = hillClimbing(distanteEuclidiene, nrOrase, taboo, deltaTimp)
    for i in range(cataratori - 1):
        vecin, fitnessVecin = hillClimbing(distanteEuclidiene, nrOrase, taboo, deltaTimp)
        if fitnessVecin < fitnessCandidat:
            candidat = vecin
            fitnessCandidat = fitnessVecin
            print(fitnessCandidat, candidat)
    return candidat, fitnessCandidat

# hillClimbingFlota(distanteEucliedene, 52, 1000, 0.15)