from weather import weather_update

def output_return(tag, address):
    if tag=="weather_value":
         address = address[3:]
         return weather_update(address)
    else:
        return " "