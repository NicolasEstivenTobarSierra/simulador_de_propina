def calcular_propina(total, porcentaje):
    """Calcula la propina en base al total y porcentaje dado."""
    return total * (porcentaje / 100)

def calcular_total_con_propina(total, propina):
    """Calcula el total a pagar sumando la propina al total original."""
    return total + propina

def desing():
    print(f"""
        =============================================
                 Cálculo de Propina
        =============================================""")
    
    while True:
        total = float(input("        Ingrese el monto total de la cuenta: $"))
        porcentaje = int(input("        Ingrese el porcentaje de propina (por ejemplo: 10, 15, 20): ___ %"))
        
        # Calcular la propina y el total a pagar
        propina = calcular_propina(total, porcentaje)
        total_con_propina = calcular_total_con_propina(total, propina)
        
        print(f"""                 
        =============================================
        La propina calculada es: $ {propina:.2f}
        El total a pagar es: $ {total_con_propina:.2f}
        =============================================
        """)
        
        # Preguntar si desea hacer otro cálculo
        respuesta = input("    ¿Deseas calcular nuevamente? (S/N): ").strip().upper()
        if respuesta != 'S':
            break