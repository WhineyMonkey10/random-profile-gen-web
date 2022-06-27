from ..classes.gens import Gens


def gen_results(include_middle_name: str):
    gens = Gens()

    x = 0
    name = gens.nameGenerator(include_middle_name)
    age = gens.ageGenerator()
    addr = gens.addrGenerator()
    nick = gens.nickGen()
    allergie = gens.allergiesGen()
    favfood = gens.favouritefood()
    born = gens.borngen()
    bestfriend = gens.your_best_friend()
    eyecolour = gens.eyecolourgen()
    # Initialising the final product

    return f"""
Your name is: {name} also known as (your nickname) {nick},  
you live in {addr}, and you are: {age} years old! {allergie}. 
{favfood}. You were born in: {born} and your BFF is {bestfriend}. 
Your eye colour is: {eyecolour}
    """
