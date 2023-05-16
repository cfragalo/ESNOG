
# Configuracion generada por CHATGPT

# Cambio del hostname en un equipo Juniper (funciona)
# Usando NETCONF
# Juniper vmx  -- Model: vmx Junos: 14.1R1.10


from ncclient import manager

hostname = "ROU-01"
host = "200.0.0.4"
username = "root"
password = "esnog29"

# Crea una sesión NETCONF con el dispositivo Juniper
with manager.connect(host=host, port=830, username=username, password=password, hostkey_verify=False) as m:
    # Crea una configuración XML para cambiar el hostname
    xml_config = """
        <config>
            <configuration>
                <system>
                    <host-name>{}</host-name>
                </system>
            </configuration>
        </config>
    """.format(hostname)

    # Envía la configuración al dispositivo
    response = m.edit_config(target='candidate', config=xml_config)

    # Verifica si la edición de configuración tuvo éxito
    if response.ok:
        # Aplica la configuración editada
        m.commit()
        print("Hostname cambiado correctamente.")
    else:
        print("Error al cambiar el hostname:", response)
