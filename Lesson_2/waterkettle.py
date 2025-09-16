boiling_point = 100
starting_temperature = 20
heating_increment = 10
current_temperature = 20

print("Water Kettle Simulation")
print(f"Starting Temperature:{starting_temperature}")

for current_temperature in range (current_temperature, boiling_point, heating_increment):
 print(f"current temperature: {current_temperature}") 

# while current_temperature < boiling_point:
    current_temperature += heating_increment
    print(f"current temperature: {current_temperature}") 
    
if current_temperature <=25:
    print("Cool")
elif current_temperature <=40:
    print("Getting warmer")
elif current_temperature <=65:
    print("Hot")
elif current_temperature < 100:
    print("Almous boiling")
else:
    print("boiling!")