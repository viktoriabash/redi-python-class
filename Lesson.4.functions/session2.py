   
def initialize(temperature: int):
    print("Water Kettle Simulation")
    print(f"Starting Temperature: {temperature} C")

def shut_down():
    print("your water is ready!")
    
def determine_status(temperature):

def heat_up(starting_temperature, heating_increment):
    current_temperature = starting_temperature
    while current_temperature < 100:
        temperature += heating_increment
        
        if current_temperature <=25:
            status = "Cool"
        elif temperature <=40:
             status = "Getting warmer"
        elif temperature <=65:
             status = "Hot"
        elif temperature < 100:
             status = "Almous boiling"
        else:
             status = "boiling!"

    print(f"heating.... current temperature: {current_temperature} - {status}") 


initialize(10)
shut_down()
heat_up(20,10)