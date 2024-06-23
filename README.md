# synchronize_time
esta app de python se usa para sincronizar automaticamente la hora de windows o linux si la aplicacion api rest te lo pide
1. from sync_time import Synchronize_time
2. except Exception as e:  # Manejar otros errores de forma diferente
            if "Timestamp for this request is outside of the recvWindow" in str(e):
                print( Synchronize_time.synchronize())
        
