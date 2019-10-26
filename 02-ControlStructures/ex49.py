nrDniaTygodnia = 2

i = 1
kalendarz = "│ PN │ WT │ SR │ CZ │ PT │ SB │ ND │"
kalendarz += (nrDniaTygodnia) * "│    "
    
for k in range(i, 8 - nrDniaTygodnia):
    kalendarz += f"│ {str(i):>2} "
    i += 1
else:
    kalendarz += "│"

for j in range(4 if nrDniaTygodnia == 6 else 3):
    kalendarz += "│"
    for m in range(7):
         kalendarz += f" {str(i):>2} │"
         i += 1

kalendarz += "│"
for j in range(i, 31):
    kalendarz += f" {str(j):>2} │"

kalendarz += 6 * "    │" if nrDniaTygodnia == 6 else (5 - nrDniaTygodnia) * "    │"

for j in range(0, len(kalendarz), 36):
    print(kalendarz[j : j + 36])