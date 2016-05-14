### Shuffle card
## Require matplotlib
## logarithmic totient with card shuffle

import matplotlib.pyplot as plt

aCards = 52

deck = []

originalPos = False

def doubler(position):
    positionNew = position + position
    while positionNew > aCards-1:
        positionNew = positionNew - (aCards - 1)
    return positionNew

for i in range(aCards):
    card = []
    card.append(i)
    deck.append(card)

while originalPos == False:
    if aCards%2!=0:
        break
    for i in range(aCards):
        position = deck[i][-1]
        positionNext = doubler(position)
        deck[i].append(positionNext)
        if i == aCards-1:
            cardsInPlace = 0
            for k in range(aCards):
                if deck[k][0]==deck[k][-1]:
                    cardsInPlace += 1
            if cardsInPlace == aCards:
                originalPos = True

## print deck # Card shuffle array after swap

for i in range(aCards): ## plot using plt 
    plt.plot(deck[i])

plt.ylabel("position")
plt.gca().invert_yaxis()
plt.show()
