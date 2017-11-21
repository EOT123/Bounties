# Plural And Single
# Works But not as well...Cactus = Cactuses instead of Cacti
# By Efrain
import inflect
p = inflect.engine()
while True:
    plu = input("Enter A Plural Or Singular Word: ")
    print("The Plural/Singular Of ", plu, " Is ", p.plural(plu))

    """
    print("The singular of ", plu, " is ", p.singular_noun(plu))
    """