print("______                         _  _____         _       ")
print("|  _  \                       | |/  __ \       | |      ")
print("| | | | _ __   ___   __ _   __| || /  \/  __ _ | |  ___ ")
print("| | | || '__| / _ \ / _` | / _` || |     / _` || | / __|")
print("| |/ / | |   |  __/| (_| || (_| || \__/\| (_| || || (__ ")
print("|___/  |_|    \___| \__,_| \__,_| \____/ \__,_||_| \___|")
print()                                                    
print() 
print("DreadCalc Version 0.1")
print() 
print() 
DamageScore = input("Wat is de damage-score? (0-10) ")
ReproducibilityScore = input("Wat is de Reproducibility-score? (0-10) ")
ExploitabilityScore = input("Wat is de Exploitability-score? (0-10) ")
AffecteduserScore = input("Wat is de Affected user-score? (0-10) ")
DiscoverabilityScore = input("Wat is de Discoverability-score? (0-10) ")

DreadScore = ((int(DamageScore) + int(ReproducibilityScore) + int(ExploitabilityScore) + int(AffecteduserScore) + int(DiscoverabilityScore)) / 5)

print() 
print() 
print("De DREAD-score is:")
print(DreadScore)
print() 