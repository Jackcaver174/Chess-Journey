##### Chat GPT assisted game #####
##### Stats #####
class Player:
    def __init__(self, name, elo=1100, love=50, friends=3, reputation=0):
        self.elo = elo
        self.láska = love
        self.priatelia = friends
        self.reputácia = reputation
        self.name = name

    def display_stats(self):
        print(f"Štatistiky:\nElo: {self.elo}\nLáska: {self.láska}\nPriatelia: {self.priatelia}\nReputácia: {self.reputácia}\n")

def story_scenario(player):
    print("Vitaj! Už čoskoro sa vydáš na dobrodružstvo, najskôr však potrebujem vedieť, tvoje meno.")
    player.name = input("Ako sa voláš? \n> ")

    print(f"\nAhoj, {player.name}! Už viem všetko potrebné. Môžme začať...")
    
    choice = input("Pre spustenie hry stlač. 1 \n> ")

    if choice == "1":
        print("\n*1 nová správa od používateľa Matej Krištál*")
    else:
        print("\nNesprávna voľba. Skús znovu.")
        choice = input("Pre spustenie hry stlač. 1 \n> ")
        if choice == "1":
            print("\n*1 nová správa od používateľa Matej Krištál*")

    choice = input("1. Otvoriť správu. \n> ")
    if choice == "1":
        print(f"Ahoj {player.name}, \ndlho sme sa nevideli, ako máš? Stále si sa nevrátil k šachu? Našiel som jeden zaujímavý diagram, posielam ti ho v prílohe. Na Tvojom mieste by som sa naň pozrel. \n1. vyriešiť diagram \n2. odpísať")
    else:
        print("\nNesprávna voľba. Skús znovu. \n> ")

    choice = input("niektoré akcie ti zlepšia štatistiky, ktoré neskôr môžu odomknúť nové pokračovania príbehu\n> ")
    if choice == "1":
        print("Biely na ťahu.")
        showChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        move = input("Napíš najlepší ťah.\n> ")
        # Check if the move is correct (case-insensitive)
        if move.lower() in ['va8', 'va8+']:
            print("Správne! Získavaš 10 ELO bodov.")
            player.elo += 10
        else:
            print("Nesprávny ťah. Strácaš 10 ELO bodov.")
            player.elo -= 10
    elif choice == "2":
        print("*Ahoj, \nprepáč momentálne nemám náladu na šach.* \nStrácaš 25 ELO bodov.")
        player.elo -= 25
    else:
        print("\nNesprávna voľba. Skús znovu.")
        choice = input("niektoré akcie ti zlepšia štatistiky, ktoré neskôr môžu odomknúť nové pokračovania príbehu")

    player.display_stats()

    print("*1 nová správa od používateľa Matej Krištál*")
    choicechoice = input("1. Otvoriť správu. \n> ")
    if choice == "1":
        print()

chrs = {
    'p': u'\u265F',
    'r': u'\u265C',
    'n': u'\u265E',
    'b': u'\u265D',
    'k': u'\u265A',
    'q': u'\u265B',
    'P': u'\u2659',
    'R': u'\u2656',
    'N': u'\u2658',
    'B': u'\u2657',
    'K': u'\u2654',
    'Q': u'\u2655'
}

def drawField(position, piece):

    if position == 0:
        print('|', end="")

    print(' ' + piece + ' |', end="")

def drawFloor():
    print('+---' * 8, end="")
    print('+')

def showChessBoard(FEN):

    rows = FEN.split('/')

    drawFloor()
    position = 0
    for row in rows[::-1]:
        for pismeno in row:
            if ord(pismeno) in range(ord('0'), ord('9') + 1):
                for _ in range(int(pismeno)):
                    drawField(position, " ")
                    position += 1
            else:
                drawField(position, chrs[pismeno])
                position += 1

        position = 0
        print()
        drawFloor()



# Main game loop
player = Player(name="")
story_scenario(player)