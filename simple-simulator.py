# This code base will simulate a group of X characters, traveling throughout Y homes and Z public buildings. The simulation will test how disease spreads among a population

num_characters = 40
num_homes = 30
pub_buildings = 13

class Home(object):
    # Values of the home will be residents and primary resident, who should be a member of resident
    def __init__(self,residents=None,primary_resident=None):
        self.residents = residents
        if primary_resident in self.residents:
            self.primary_resident = primary_resident
        else:
            self.primary_resident = None
        for resident in self.residents:
            resident.home = self
    def __str__(self):
        home_str = self.primary_resident.name + "'s House\nThe residents of this home are:\n"
        for resident in self.residents:
            home_str += str(resident)
        return home_str




class Character(object):
    # Values of a character will be social level, immune strength, and home
    def __init__(self, name=None, social_level=0.5, immune_strength=0.8, home=None):
        self.name = name
        self.social_level = social_level
        self.immune_strength = immune_strength
        self.home = home
    def __str__(self,social=True,immune=True,home=True):
        char_str = self.name + ":\n"
        char_str += "Social Level: " + str(self.social_level) +"\n"
        char_str += "Immune Strength: " + str(self.immune_strength) + "\n"
        if self.home != None:
            char_str += "Home: " + self.home.primary_resident.name + "'s home\n"
        else:
            char_str += "No home\n"
        return char_str

if __name__ == "__main__":
    bob = Character(name="Bob")
    print(bob)
    sarah = Character(name="Sarah",immune_strength=0.2)
    
    bob_home = Home(residents=[bob,sarah],primary_resident=bob)
    print(bob_home)
