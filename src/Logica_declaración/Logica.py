class Invalid(Exception):
    pass

def calcular_impuesto_renta(ingresos_laborales, otros_ingresos, retenciones_fuente, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion):
    """
    Calcula el impuesto de renta según los parámetros proporcionados.
    """

    total_ingresos_gravados = ingresos_laborales + otros_ingresos
    total_ingresos_no_gravados = donaciones
    total_costos_deducibles = seguridad_social + aportes_pension + gastos_creditos_hipotecarios + gastos_educacion
    Utilidad = total_ingresos_gravados - total_costos_deducibles

    if Utilidad < 0:
        raise Invalid("La utilidad no pueden ser negativos")

    if ingresos_laborales == 0:
        raise Invalid("El ingreso laboral es incorrecto")

    if Utilidad <= 51301000:
        return "El impuesto de renta a pagar por el contribuyente es 0"

    if Utilidad <= 80010000:
        impuesto_renta_sin_resta = (Utilidad - 51301000) * 0.19
        impuesto_renta = impuesto_renta_sin_resta - retenciones_fuente
        return calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles)

    if Utilidad <= 192966000:
        impuesto_renta_sin_resta = (Utilidad - 80010000) * 0.28
        impuesto_renta = (impuesto_renta_sin_resta + 5459000) - retenciones_fuente
        return calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles)

    if Utilidad <= 408053000:
        impuesto_renta_sin_resta = (Utilidad - 192966000) * 0.33
        impuesto_renta = (impuesto_renta_sin_resta + 37087000) - retenciones_fuente
        return calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles)

    if Utilidad <= 892823000:
        impuesto_renta_sin_resta = (Utilidad - 408053000) * 0.35
        impuesto_renta = (impuesto_renta_sin_resta + 108061000) - retenciones_fuente
        return calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles)

    if Utilidad <= 1459015000:
        impuesto_renta_sin_resta = (Utilidad - 892823000) * 0.37
        impuesto_renta = (impuesto_renta_sin_resta + 277730000) - retenciones_fuente
        return calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles)

    impuesto_renta_sin_resta = (Utilidad - 1459015000) * 0.39
    impuesto_renta = (impuesto_renta_sin_resta + 487217000) - retenciones_fuente
    return calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles)


def calcular_impuesto_final(impuesto_renta, Utilidad, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles):
    """
    Calcula y devuelve el impuesto de renta final y muestra los detalles.
    """
    if impuesto_renta <= 0:
        raise Invalid("Hay un dato mal ingresado")

    print(f"Los ingresos totales son: {total_ingresos_gravados}")
    print(f"Los ingresos no gravados son: {total_ingresos_no_gravados}")
    print(f"Los costos deducibles son: {total_costos_deducibles}")
    print(f"La Utilidad es: {Utilidad}")
    return f"El valor a pagar es: {impuesto_renta}"