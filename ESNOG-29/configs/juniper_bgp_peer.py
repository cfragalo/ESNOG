
# Configuracion sesion BGP mediante NETCONF
# Config Generada por CHATGPT para ESNOG-29


from ncclient import manager
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# Datos de conexión
hostname = "ROU-01"
ip_address = "200.0.0.4"  # Dirección IP del enrutador Juniper
username = "root"
password = "esnog29"

# Datos de configuración BGP
bgp_local_as = "15954"
bgp_remote_as = "3333"
bgp_peer_ip = "100.1.3.3"
bgp_password = "ME_GUSTA_EL_CAFE"

# Configuración BGP
config_template = f"""
set system host-name {hostname}
set protocols bgp group mygroup type external
set protocols bgp group mygroup local-as {bgp_local_as}
set protocols bgp group mygroup neighbor {bgp_peer_ip} peer-as {bgp_remote_as}
set protocols bgp group mygroup neighbor {bgp_peer_ip} authentication-key {bgp_password}
"""

# Conexión al enrutador Juniper
with Device(host=ip_address, user=username, password=password) as dev:
    # Crear objeto de configuración
    cu = Config(dev)

    # Abrir una transacción de configuración
    cu.lock()

    try:
        # Cargar la configuración
        cu.load(config_template, format="set")

        # Validar la configuración
        cu.commit_check()

        # Confirmar la configuración
        cu.commit()
    except Exception as e:
        # En caso de error, deshacer cambios y mostrar el mensaje de error
        cu.rollback()
        print(str(e))
    finally:
        # Liberar la transacción de configuración
        cu.unlock()
