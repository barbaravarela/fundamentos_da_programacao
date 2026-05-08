# Relatório de Temperatura Diária

temperaturas = []

for i in range(24):
    temperatura = int(input("Digite a temperatura (em °C): "))
    temperaturas.append(temperatura)

temp_max = temperaturas[0]
temp_min = temperaturas[0]
temp_total = 0
acima_trinta = 0

for temperatura in temperaturas:
    temp_total += temperatura
    if temperatura > temp_max:
        temp_max = temperatura
    if temperatura < temp_min:
        temp_min = temperatura
    if temperatura > 30:
        acima_trinta += 1

temp_media = temp_total / 24
if temp_media < 15:
    classificacao = "Frio"
elif temp_media <= 25:
    classificacao = "Agradável"
else:
    classificacao = "Quente"

print("---------- RELTÓRIO DO DIA ----------")
print(f"Tempertura máxima: {temp_max}°C")
print(f"Tempertura mínima: {temp_min}°C")
print(f"Tempertura média: {int(temp_media)}°C")
print(f"Classificação do dia: {classificacao}")
print(f"Quantidade de horas com a temperatura acima de 30°C: {acima_trinta}h")