from bert import Ner

model = Ner("out_base/")

output = model.predict("""
Estados Unidos sigue siendo el foco rojo de la Covid-19 y ya supera los 580.000 contagios con más de 23.600 muertes, la cifra de fallecimientos más alta del mundo hasta ahora. El Estado de Nueva York, el foco rojo mundial de la pandemia, ha registrado 778 fallecimientos nuevos en las últimas 24 horas. El epicentro latinoamericano está en Brasil, que ya registra 1.532 muertos y donde dos gobernadores han dado positivo. Argentina ha alcanzado los 105 decesos y tiene 2.443 casos confirmados. En México, el número de contagios escaló hasta los 5.399 casos confirmados y las 406 muertes. Ecuador suma ya 7.603 diagnósticos positivos y reconoce 369 fallecimientos, pero esa cifra asciende a 805 decesos si se suman los pacientes que murieron por covid-19 como causa probable. Hay más de dos millones de infectados en el mundo, de acuerdo con la Universidad Johns Hopkins.
""")

print(output)