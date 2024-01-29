from pathlib import Path


# Dette er start-koden til den første programmeringsoppgave i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name):
    #Åpner filen
    with open( file_name , 'r', encoding= 'utf-8') as f:
        leser = f.readlines()
        liste = list(leser)
        print(liste)
        return liste
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open

(read_file("C:/GIT/Test2/tests/small.txt"))



def lines_to_words(lines):
    wordlist = []

    for line in lines:
        # Splitter opp setningene til ord
        words = line.split()

        for word in words:
            # Fjerner ulike tegn i listen og setter alle bokstaver fra store til små bokstaver
            clean_word = word.strip('.,;:?!)(').lower()

            # Sjekker etter tomme strenger etter å ha tatt vekk de ulike tegnene
            if clean_word:
                wordlist.append(clean_word)

    return wordlist
    """
    Denne funksjonen får en liste med strenger som input (dvs. linjene av tekstfilen som har nettopp blitt lest inn)
    og deler linjene opp i enkelte ord. Enhver linje blir delt opp der det er blanktegn (= whitespaces).
    Desto videre er vi bare interessert i faktiske ord, dvs. alle punktum (.), kolon (:), semikolon (;),
    kommaer (,), spørsmåls- (?) og utråbstegn (!) skal fjernes underveis.
    Til sist skal alle ord i den resulterende listen være skrevet i små bokstav slik at "Odin" og "odin"
    blir behandlet likt.
    OBS! Pass også på at du ikke legger til tomme ord (dvs. "" eller '' skal ikke være med) i resultatlisten!

    F. eks: Inn: ["Det er", "bare", "noen få ord"], Ut: ["Det", "er", "bare", "noen", "få", "ord"]
    """
    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig

lines = read_file('C:/GIT/Test2/tests/voluspaa.txt')
print(lines_to_words(lines))


test_data = ['the', 'quick', 'brown', 'fox', 'the', 'jumps', 'over', 'the', 'brown', 'wall']
def compute_frequency(words):
    frequencies = {}
    # Går i en løkke gjennom alle ord i listen til den er ferdig med oppgaven den er satt til å gjøre
    for word in words:
        # Legger til ord fra listen og en standardverdi (0) for ordet og plusser på 1 til løkken er ferdig
        frequencies[word]=frequencies.get(word, 0) + 1
    return frequencies

    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige input listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
print(compute_frequency(test_data))

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']

def remove_filler_words(frequency_table):
    updated_frequency_table = {word: count for word, count in frequency_table.items() if word.lower() not in FILL_WORDS}
    return updated_frequency_table

data = {
            'det': 42,
            'odin': 10,
            'og': 9,
            'ulv': 1,
            'til': 1,
            'gud': 3
        }
"""
       Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
       analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
       Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
       Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
       som finnes i FILL_WORDS. """
print(remove_filler_words(data))


def largest_pair(par_1, par_2):
    if par_1[1] > par_2[1]:
        return par_1
    else:
        return par_2
    """
    Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    tallet er størst.
    """
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!



def find_most_frequent(frequency_table):
    #Ser gjennom listen ved bruk av max for å finne ordet med høyest frekvens.
    most_frequent_word = max(frequency_table, key=frequency_table.get)
    return most_frequent_word
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget


data = {
    'hei': 23,
    'sjelden': 1,
    'oftest': 9000,
    'answer': 42
}
print(find_most_frequent(data))

############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


def main():
    file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()
