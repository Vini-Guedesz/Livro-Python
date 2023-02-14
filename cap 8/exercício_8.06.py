"""
Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
"""
def city_country(city, contry):
    formated_string = str(city).title() + ', ' + str(contry).title()
    return(formated_string)

print(city_country('rio de janeiro', 'brasil'))
print(city_country('new york', 'estados unidos'))
print(city_country('buenos aires', 'argentina'))