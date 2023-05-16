
# Configuracion generada por CHATGPT

# Cambio del hostname en un equipo ARista (no funciona)
# Arista vEOS-lab -- Software image version: 4.26.5M


import paramiko

def change_hostname(hostname, host, username, password):
    # Crea una instancia del cliente SSH
    client = paramiko.SSHClient()

    # Agrega la clave del host automáticamente (solo para pruebas, NO recomendado en producción)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectarse al equipo Arista
        client.connect(host, username=username, password=password)

        # Abre un canal SSH
        ssh_channel = client.invoke_shell()

        # Envía el comando de configuración y cambio de nombre de host
        ssh_channel.send('configure terminal\n')
        ssh_channel.send(f'hostname {hostname}\n')

        # Espera a que se complete la ejecución de los comandos
        while not ssh_channel.recv_ready():
            pass

        # Recibe la salida del comando ejecutado
        output = ssh_channel.recv(65535).decode()

        # Cierra la conexión SSH
        client.close()

        # Imprime la salida del comando ejecutado
        print(output)
    except paramiko.AuthenticationException:
        print("Error de autenticación. Verifica las credenciales de SSH.")
    except paramiko.SSHException as ssh_ex:
        print(f"Error SSH: {str(ssh_ex)}")
    except Exception as ex:
        print(f"Error: {str(ex)}")

# Parámetros de conexión SSH y configuración del hostname
hostname = "nuevo_nombre"
host = "255.0.0.2"  # Dirección IP de tu dispositivo Arista
username = "admin"
password = "esnog29"  # Contraseña de acceso al dispositivo Arista

# Llamada a la función para cambiar el nombre de host
change_hostname(hostname, host, username, password)

