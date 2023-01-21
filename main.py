# import the libraries we need for these console project
import sys
import time
import random

# delay printing for the text in console
def delayText(x):
    for i in x:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
        
def delayTextTime(x):
    for i in x:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.08)

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    YELLOW = '\033[33m'
    LRED ='\033[91m'

# class for the characters
class Character:
    def __init__(self, anime, name, classes, moves, evs, damagetaken='', health="============="):
        self.name = name
        self.anime = anime
        self.classes = classes
        self.moves = moves
        self.power = evs['Power']
        self.attack = evs['Attack']
        self.defense = evs['Defense']
        self.damage_taken = damagetaken
        self.health = health
        self.bar = 5000
        
    # interface for the gameplay
    def fight(self, opponent):
            
            print(f"{Colors.BOLD}{Colors.HEADER}\n↼ [BATTLE INFORMATION] ⇀\n{Colors.ENDC}")
            print(f"{Colors.OKBLUE}[PLAYER 1 PICKS] {player1}{Colors.ENDC}")
            print(f"{Colors.BOLD}{self.name}")
            print(f"{Colors.BOLD}Character is from {self.anime}\n")
            print(f"{Colors.FAIL}[PLAYER 2 PICKS] {player2}{Colors.ENDC}")
            print(f"{Colors.BOLD}{opponent.name}")
            print(f"{Colors.BOLD}Character is from {opponent.anime}\n")
            
            delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing Character Information...\n\n{Colors.ENDC}")  
            delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing...\n\n{Colors.ENDC}")  
            time.sleep(2)

            delayText(f"{Colors.BOLD}{Colors.HEADER}\n↼ [CHARACTER INFORMATION] ⇀\n{Colors.ENDC}")
            print(f"\n{Colors.OKBLUE}[PLAYER 1]{Colors.ENDC}")
            print(f"IGN: {player1}")
            print(f"{Colors.BOLD}{self.name}")
            print(f"{Colors.BOLD}Class ➣ {Colors.ENDC}", self.classes)
            print(f"{Colors.BOLD}Power ➣ {Colors.ENDC}", self.power)
            print(f"{Colors.BOLD}Damage ➣ {Colors.ENDC}", self.attack)
            print(f"{Colors.BOLD}Defense ➣ {Colors.ENDC}", self.defense)
            
            print("\nVS\n")
            
            print(f"{Colors.FAIL}[PLAYER 2]{Colors.ENDC}")
            print(f"IGN: {player2}")
            print(f"{Colors.BOLD}{opponent.name}")
            print(f"{Colors.BOLD}Class ➣ {Colors.ENDC}", opponent.classes)
            print(f"{Colors.BOLD}Power ➣ {Colors.ENDC}", opponent.power)
            print(f"{Colors.BOLD}Damage ➣ {Colors.ENDC}", opponent.attack)
            print(f"{Colors.BOLD}Defense ➣ {Colors.ENDC}", opponent.defense)
            
            delayText(f"\n{Colors.OKGREEN} ↻"+f" Loading...\n\n{Colors.ENDC}")     
            delayText(f"\n{Colors.WARNING} ↺"+f" Configuring Gameplay Conditions...\n\n{Colors.ENDC}")   
            delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing Hero...\n\n{Colors.ENDC}")      
            delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing Arena...\n\n{Colors.ENDC}")  
            delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing...\n\n{Colors.ENDC}")  
            time.sleep(2)    
            delayText(f"\n\n{Colors.BOLD}{Colors.HEADER}Lets Get Ready To Battle In...{Colors.ENDC}\n\n")
            delayTextTime(f"\n\n{Colors.BOLD}{Colors.OKBLUE}3\n\n{Colors.ENDC}")       
            delayTextTime(f"\n\n{Colors.BOLD}{Colors.FAIL}2\n\n{Colors.ENDC}")       
            delayTextTime(f"\n\n{Colors.BOLD}{Colors.OKGREEN}1\n\n{Colors.ENDC}")       
            delayText(f"\n\n{Colors.BOLD}{Colors.BOLD}Fight!!!\n\n{Colors.ENDC}")       
            time.sleep(1)
            
            # develop the fighting gameplay
            # check if the characters is still alive
            while self.bar > 0 and opponent.bar > 0:
                # print the fight ui
                # print the health of the characters
                # player 1
                print(f"{Colors.BOLD}{Colors.OKBLUE}[PLAYER 1 TURN] {player1}{Colors.ENDC}\n")
                print(f"\n→ {Colors.BOLD}{self.name} {Colors.ENDC}")
                print(f"{opponent.name}{Colors.ENDC} \n")
                
                # pick the skills you want to use
                for i, x in enumerate(self.moves):
                    print(f"❅  {i+1}.", x)
                    # randomize the damage of every skills to ensure the fairness of the game
                    dmg = random.randint(200, 5000)
                    if dmg == 5000:
                        self.damage_taken = (f'{Colors.FAIL}!!!!!!!!!!1 HIT DELETE!!!!!!!!!!{Colors.ENDC}')
                    elif dmg >= 3000 and dmg <= 4000:
                        self.damage_taken = (f'{Colors.WARNING}!!!!!!CRITICAL HIT!!!!!!{Colors.ENDC}')
                    elif dmg >= 2000 and dmg <= 3000:
                        self.damage_taken = (f'{Colors.OKCYAN}!!!AWESOME HIT!!!{Colors.ENDC}')
                    elif dmg < 1000:
                        self.damage_taken = (f'{Colors.OKGREEN}NICE MOVE!!!{Colors.ENDC}')
                        
                skill = int(input(f"\n{Colors.BOLD}Pick your skill: {Colors.ENDC}"))
                delayText(f"\n{self.name}{Colors.ENDC}")
                delayText(f"\n{Colors.BOLD}➣  Used {self.moves[skill-1]}!\n")
                delayText(f"\n{Colors.BOLD}{self.damage_taken}\n")
                delayText(f"{Colors.BOLD}{Colors.LRED}➣  The {self.moves[skill-1]}{Colors.LRED} deal {dmg}{Colors.LRED} on opponent life!\n{Colors.ENDC}")
                time.sleep(1)
            
                # determine the damage of the character
                opponent.bar -= dmg
                
                # determine the current status of players
                time.sleep(1)
                print(f"\n{Colors.BOLD}{Colors.OKBLUE}[PLAYER 1] {player1}{Colors.ENDC}")
                print(f"{self.name}\t\t\t\tHP {self.health} {self.bar}\n")
                print(f"{Colors.BOLD}{Colors.FAIL}[PLAYER 2] {player2}{Colors.ENDC}")
                print(f"{opponent.name}\t\t\t\tHP {opponent.health} {opponent.bar}\n")
                time.sleep(.5)
                
                # conditions if the characters still have life bars
                if opponent.bar <= 0:
                    delayTextTime(f"\n\n\n\n{Colors.BOLD}{Colors.WARNING} [GAME FINISH!!!]{Colors.ENDC}\n\n\n\n")
                    print(f"{Colors.OKBLUE}∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎[PLAYER 1] - LOSE∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎{Colors.FAIL}\n")
                    print(f"{Colors.BOLD}{Colors.OKBLUE}∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎[PLAYER 2] - WIN∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎{Colors.FAIL}\n\n\n\n\n")
                    break
            
                # opponent turn
                print(f"\n{Colors.BOLD}{Colors.FAIL}[PLAYER 2 TURN] {player2}{Colors.ENDC}\n")
                print(f"\n→ {Colors.BOLD}{opponent.name} {Colors.ENDC}")
                print(f"{self.name}\n {Colors.ENDC}")
                    
                # pick the skills you want to use
                for i, x in enumerate(opponent.moves):
                    print(f"❅  {i+1}.", x)
                    # randomize the damage of every skills to ensure the fairness of the game
                    dmg = random.randint(200, 5000)
                    if dmg == 5000:
                        opponent.damage_taken = (f'{Colors.FAIL}!!!!!!!!!!1 HIT DELETE!!!!!!!!!!{Colors.ENDC}')
                    elif dmg >= 3000 and dmg <= 4000:
                        opponent.damage_taken = (f'{Colors.WARNING}!!!!!!CRITICAL HIT!!!!!!{Colors.ENDC}')
                    elif dmg >= 2000 and dmg <= 3000:
                        opponent.damage_taken = (f'{Colors.OKCYAN}!!!AWESOME HIT!!!{Colors.ENDC}')
                    elif dmg < 1000:
                        opponent.damage_taken = (f'{Colors.OKGREEN}NICE MOVE!!!{Colors.ENDC}')
       
                skill = int(input(f"\n{Colors.BOLD}Pick your skill: {Colors.ENDC}"))
                delayText(f"\n{opponent.name}{Colors.ENDC}")
                delayText(f"\n{Colors.BOLD}➣  Used {opponent.moves[skill-1]}!\n")
                delayText(f"\n{Colors.BOLD}{opponent.damage_taken}\n")
                delayText(f"{Colors.BOLD}{Colors.LRED}➣  The {opponent.moves[skill-1]}{Colors.LRED} deal {dmg}{Colors.LRED} on opponent life!\n{Colors.ENDC}")
                time.sleep(1)
                
                # determine the damage of the character
                self.bar -= dmg
                    
                # determine the current status of players
                time.sleep(1)
                print(f"\n{Colors.BOLD}{Colors.OKBLUE}[PLAYER 1] {player1}{Colors.ENDC}")
                print(f"{self.name}\t\t\t\tHP {self.health} {self.bar}\n")
                print(f"{Colors.BOLD}{Colors.OKBLUE}[PLAYER 2] {player2}{Colors.ENDC}")
                print(f"{opponent.name}\t\t\t\tHP {opponent.health} {opponent.bar}\n")
                time.sleep(.5)
                    
                # conditions if the characters still have life bars
                if self.bar <= 0:
                    delayTextTime(f"\n\n\n\n{Colors.BOLD}{Colors.WARNING} [GAME FINISH!!!]{Colors.ENDC}\n\n\n\n")
                    print(f"{Colors.BOLD}{Colors.OKBLUE}∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎[PLAYER 1] - WIN∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎{Colors.FAIL}\n")
                    print(f"{Colors.OKBLUE}∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎[PLAYER 2] - LOSE∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎{Colors.FAIL}\n\n\n\n\n")
                    break
                         
if __name__ == '__main__':
    # [FUN FACT] - You can add the character you want! or create your own character!
    # Create the characters
    Ichigo = Character(f'{Colors.WARNING}Bleach{Colors.ENDC}', f'{Colors.WARNING}Kurosaki Ichigo{Colors.ENDC}', f'{Colors.WARNING}Shinigami{Colors.ENDC}', [f'{Colors.WARNING}Zanpakto{Colors.ENDC}', f'{Colors.WARNING}Bankai', f'{Colors.WARNING}Hollow Bankai{Colors.ENDC}', f'{Colors.WARNING}Final Getsuga{Colors.ENDC}'], {'Power':1500, 'Attack':320, 'Defense': 150})
    Luffy = Character(f'{Colors.FAIL}One-Piece{Colors.ENDC}', f'{Colors.FAIL}Monkey D. Luffy {Colors.ENDC}', f'{Colors.FAIL}Pirate King{Colors.ENDC}', [f'{Colors.FAIL}Goma Goma{Colors.ENDC}', f'{Colors.FAIL}Goma Goma Piston{Colors.ENDC}', f'{Colors.FAIL}Immune{Colors.ENDC}', f'{Colors.FAIL}Black Haki{Colors.ENDC}'], {'Power':1400, 'Attack':320, 'Defense': 150})
    Goku = Character(f'{Colors.YELLOW}Dragon Ball{Colors.ENDC}', f'{Colors.YELLOW}Goku           {Colors.ENDC}', f'{Colors.YELLOW}Saiyan{Colors.ENDC}', [f'{Colors.YELLOW}Kaioken{Colors.ENDC}', f'{Colors.YELLOW}Kamehameha{Colors.ENDC}', f'{Colors.YELLOW}Dragon Fist{Colors.ENDC}', f'{Colors.YELLOW}Spirit Bomb{Colors.ENDC}'], {'Power':1400, 'Attack':370, 'Defense': 190})
    Kaneki = Character(f'{Colors.HEADER}Tokyo Ghoul{Colors.ENDC}', f'{Colors.HEADER}Ken Kaneki     {Colors.ENDC}', f'{Colors.HEADER}Ghoul{Colors.ENDC}', [f'{Colors.HEADER}Spectral Knock{Colors.ENDC}', f'{Colors.HEADER}Stealth Tail{Colors.ENDC}', f'{Colors.HEADER}Kakuja Fist{Colors.ENDC}', f'{Colors.HEADER}Blazing Decimate{Colors.ENDC}'], {'Power':1500, 'Attack':360, 'Defense': 130})
    Deku = Character(f'{Colors.OKGREEN}My Hero Academia{Colors.ENDC}', f'{Colors.OKGREEN}Deku           {Colors.ENDC}', f'{Colors.OKGREEN}Hero{Colors.ENDC}', [f'{Colors.OKGREEN}Blackwhip{Colors.ENDC}', f'{Colors.OKGREEN}Fa Jin{Colors.ENDC}', f'{Colors.OKGREEN}Gear Shift{Colors.ENDC}', f'{Colors.OKGREEN}One For All{Colors.ENDC}'], {'Power':1500, 'Attack':360, 'Defense': 130})
    
    # welcome ui
    delayText(f"\n{Colors.OKGREEN} ↻"+f" Loading...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.WARNING} ↺"+f" Initializing Player Configurations...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.WARNING} ↻"+f" Initializing Hero Configurations...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.WARNING} ↺"+f" Initializing Hero Moves...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.WARNING} ↻"+f" Initializing Hero Stats...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing....\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.OKGREEN} ↻"+f" Please Wait... \n{Colors.ENDC}")    
        
    time.sleep(2)
    
    print(f"\n\n\n\n\n{Colors.HEADER}↼✧  "+f"{Colors.FAIL}Welcome to the Jump Force! Console Version"+f"{Colors.HEADER} ✧⇀{Colors.ENDC}\n\n\n\n\n")
    input(f"\n\n{Colors.BOLD} [Please Hit The Enter Button!]{Colors.ENDC}\n\n")
    player1 = input(f"{Colors.OKBLUE} [PLAYER - 1] Enter your username: {Colors.ENDC}").upper()
    player2 = input(f"{Colors.FAIL} [PLAYER - 2] Enter your username: {Colors.ENDC}").upper()
    print(f"\n\n\n\n\n{Colors.HEADER}↼✧  "+f"{Colors.FAIL}Welcome to the Jump Force! Console Version"+f"{Colors.HEADER} ✧⇀\n\n{Colors.ENDC}")
    
    delayText(f"\n{Colors.BOLD}\tWelcome to the World of Jump Force {Colors.OKBLUE} {player1}!\n{Colors.ENDC}")
    delayText(f"\n{Colors.BOLD}\tWelcome to the Wordl of Jump Force{Colors.FAIL} {player2}!\n{Colors.ENDC}\n\n\n\n")
    
    delayText(f"\n{Colors.OKGREEN} ↻"+f" Loading Hero...\n\n{Colors.ENDC}")  
    delayText(f"\n{Colors.OKGREEN} ↻"+f" Loading Hero Selection...\n\n{Colors.ENDC}")   
    delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing....\n\n{Colors.ENDC}")  
    time.sleep(2)

    # hero menu
    print(f"\n\n\n\n\n\n{Colors.OKBLUE}|-----------------------------------------------------------|{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKBLUE}|                      HERO SELECTION                       |{Colors.ENDC}")
    print(f"{Colors.OKBLUE}|-----------------------------------------------------------|{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.WARNING}| [1] ICHIGO |{Colors.BOLD}{Colors.FAIL} [2] LUFFY | {Colors.BOLD}{Colors.YELLOW}[3] GOKU |{Colors.BOLD}{Colors.HEADER} [4] KANEKI |{Colors.BOLD}{Colors.OKGREEN} [5] DEKU |{Colors.ENDC}")
    print(f"{Colors.OKBLUE}|------------|-----------|----------|------------|----------|{Colors.ENDC}")
  
    
    # hero selection
    p1 = int(input(f"\n{Colors.BOLD}{Colors.OKBLUE}[PLAYER - 1] Select your hero: "))
    if p1 == 1:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.WARNING}[-{player1} Picks Ichigo!-]{Colors.ENDC}\n")
        p1_hero = Ichigo
    elif p1 == 2 :
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.FAIL}[-{player1} Picks Luffy!-]{Colors.ENDC}\n")
        p1_hero = Luffy
    elif p1 == 3:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.YELLOW}[-{player1} Picks Goku!-]{Colors.ENDC}\n")
        p1_hero = Goku
    elif p1 == 4:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.HEADER}[-{player1} Picks Kaneki!-]{Colors.ENDC}\n")
        p1_hero = Kaneki
    elif p1 == 5:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.OKGREEN}[-{player1} Picks Deku!-]{Colors.ENDC}\n")
        p1_hero = Deku
        
    p2 = int(input(f"\n{Colors.BOLD}{Colors.FAIL}[PLAYER - 2] Select your hero: "))
    if p2 == 1:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.WARNING}[-{player2} Picks Ichigo!-]{Colors.ENDC}\n")
        p2_hero = Ichigo
    elif p2 == 2 :
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.FAIL}[-{player2} Picks Luffy!-]{Colors.ENDC}\n")
        p2_hero = Luffy
    elif p2 == 3:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.YELLOW}[-{player2} Picks Goku!-]{Colors.ENDC}\n")
        p2_hero = Goku
    elif p2 == 4:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.HEADER}[-{player2} Picks Kaneki!-]{Colors.ENDC}\n")
        p2_hero = Kaneki
    elif p2 == 5:
        print(f"{Colors.BOLD}[HERO LOCK]{Colors.ENDC}")
        delayText(f"\n{Colors.BOLD}{Colors.OKGREEN}[-{player2} Picks Deku!-]{Colors.ENDC}\n")
        p2_hero = Deku
        
    delayText(f"\n{Colors.OKGREEN} ↻"+f" Loading...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.WARNING} ↺"+f" Initializing Battle Information...\n\n{Colors.ENDC}")    
    delayText(f"\n{Colors.OKCYAN} ↺"+f" Initializing....\n\n{Colors.ENDC}")  
    time.sleep(2)

    # fight
    (p1_hero).fight(p2_hero)
    
        
    
                
