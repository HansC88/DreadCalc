print("______                         _  _____         _       ")
print("|  _  \                       | |/  __ \       | |      ")
print("| | | | _ __   ___   __ _   __| || /  \/  __ _ | |  ___ ")
print("| | | || '__| / _ \ / _` | / _` || |     / _` || | / __|")
print("| |/ / | |   |  __/| (_| || (_| || \__/\| (_| || || (__ ")
print("|___/  |_|    \___| \__,_| \__,_| \____/ \__,_||_| \___|")
print()                                                    
print() 
print("DreadCalc Version 0.2")
print() 
print() 

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Vul een cijfer in tussen de 0 en 10... ")
            continue
        if value < 0:
            print("Vul een waarde in tussen de 0 en 10... ")
            continue
        if value > 10:
            print("Vul een waarde in tussen de 0 en 10... ")
        else:
            break
    return value

DamageScore = get_int("Wat is de damage-score? (0-10) ")
ReproducibilityScore = get_int("Wat is de Reproducibility-score? (0-10) ")
ExploitabilityScore = get_int("Wat is de Exploitability-score? (0-10) ")
AffecteduserScore = get_int("Wat is de Affected user-score? (0-10) ")
DiscoverabilityScore = get_int("Wat is de Discoverability-score? (0-10) ")

DreadScore = ((int(DamageScore) + int(ReproducibilityScore) + int(ExploitabilityScore) + int(AffecteduserScore) + int(DiscoverabilityScore)) / 5)

print() 
print() 
print("De DREAD-score is:")
print(DreadScore)
print() 