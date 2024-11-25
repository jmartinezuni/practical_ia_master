class Colores:
    """Clase para manejar colores y estilos de texto en la terminal."""
    
    # Colores básicos
    NEGRO = '\033[30m'
    ROJO = '\033[31m'
    VERDE = '\033[32m'
    AMARILLO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIAN = '\033[36m'
    BLANCO = '\033[37m'
    
    # Estilos adicionales
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'
    INVERSO = '\033[7m'
    
    # Colores brillantes
    ROJO_BRILLANTE = '\033[91m'
    VERDE_BRILLANTE = '\033[92m'
    AMARILLO_BRILLANTE = '\033[93m'
    AZUL_BRILLANTE = '\033[94m'
    MAGENTA_BRILLANTE = '\033[95m'
    CIAN_BRILLANTE = '\033[96m'
    BLANCO_BRILLANTE = '\033[97m'
    
    # Reset para volver al color original
    RESET = '\033[0m'
    
    # Métodos estáticos para mensajes predefinidos
    @staticmethod
    def mensaje_error(texto):
        return f"{Colores.ROJO}{Colores.NEGRITA}ERROR: {texto}{Colores.RESET}"
    
    @staticmethod
    def mensaje_advertencia(texto):
        return f"{Colores.AMARILLO}{Colores.NEGRITA}ADVERTENCIA: {texto}{Colores.RESET}"
    
    @staticmethod
    def mensaje_exito(texto):
        return f"{Colores.VERDE}{Colores.NEGRITA}ÉXITO: {texto}{Colores.RESET}"
    
    @staticmethod
    def mensaje_info(texto):
        return f"{Colores.AZUL}{Colores.NEGRITA}INFO: {texto}{Colores.RESET}"
