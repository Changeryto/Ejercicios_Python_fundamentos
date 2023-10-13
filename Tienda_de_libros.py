print("Proporcione los siguientes datos del libro")
nombre = input("Proporciona el nombre: ")
id = int(input("roporciona el ID del libro: "))
precio = float(input("Proporciona el precio del libro: "))
envio_gratuito = input("Indica si el envio es gratuito (True/False): ")

if(envio_gratuito == "True"):
    envio_gratuito = True
elif(envio_gratuito == "False"):
    envio_gratuito = False
else:
    envio_gratuito = "Valor incorrecto, use True/False"
    #El uso de comas añade espacios automáticamente
print("Nombre:", nombre)
print("ID:", id)
print("Precio:", precio)
print("Envío gratuito?:", envio_gratuito)

print(type(envio_gratuito))
