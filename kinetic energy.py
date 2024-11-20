#function to calulate kinetic energy

mass = float(input("What is the mass (in kg)?"))

velocity = float(input("What is the velocity (in m/s)?"))

kinetic_energy = 0.5*mass*(velocity**2)

print(kinetic_energy)