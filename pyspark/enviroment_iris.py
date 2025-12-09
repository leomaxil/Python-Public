from pyspark.sql.types import *
import os

def get_environment(env: IntegerType):
    """
    This function retrieves the environment and ambient settings based on the provided integer value.
    
    Parameters:
    env (IntegerType): An integer representing the ambient setting (0 for commandcenter, 1 for analytical, others for unknown).
    
    Returns:
    tuple: A tuple containing the environment (ENVIRONMENT) and ambient (AMBIENT) settings.
    """
    ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev').upper()
    if env == 0:
        AMBIENT = "commandcenter"
    elif env == 1:
        AMBIENT = "analytical"
    else:
        AMBIENT = "unknown"

    if AMBIENT == "commandcenter":
        if ENVIRONMENT == 'DEV': 
            cz = 'consumezoneprod'
            hz = 'historyzoneprod'
            tz = 'trustedzone'
        else: 
            cz = 'consumezone'
            hz = 'historyzone'
            tz = 'trustedzone'
    elif AMBIENT == "analytical":
        if ENVIRONMENT == 'DEV': 
            cz = 'prod/consumezone'
            hz = 'prod/historyzone'
            tz = 'trustedzone'
        else: 
            cz = 'consumezone'
            hz = 'historyzone'
            tz = 'trustedzone'
    else:
        cz = 'unknown'
        hz = 'unknown'
        tz = 'unknown'

    hz_write = 'historyzone'
    cz_write = 'consumezone'
        
    return ENVIRONMENT, AMBIENT, cz, hz, tz, hz_write, cz_write


ENVIRONMENT, AMBIENT, cz, hz, tz, hz_write, cz_write = get_environment(1)


print(ENVIRONMENT + " " + AMBIENT)
print(ENVIRONMENT + " " + AMBIENT)
