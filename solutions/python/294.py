class PokeScan:
    def __init__(self, name, level, pokemonType):
        self.name = name
        self.level = level
        self.pokemonType = pokemonType
        
    def info(self):
        return '{}, a {} and {} Pokemon.'.format(
            self.name,
            self.getPokemonTypeDescription(),
            self.getStrengthDescription()
        )
        
    def getStrengthDescription(self):
        return ('strong' if self.level > 50 
             else 'fair' if self.level > 20 
             else 'weak')
            
    def getPokemonTypeDescription(self):
        return { 
            'water' : 'wet', 
            'fire'  : 'fiery', 
            'grass' : 'grassy' 
        }[self.pokemonType]
