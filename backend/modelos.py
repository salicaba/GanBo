class ContabilidadModel:
    datos_base = {
        "Caja": 70000, "Bancos": 200000, "Inventarios": 150000, "Terrenos": 2500000, 
        "Edificios": 1000000, "Mobiliario y Equipo": 145000, "Equipo de Cómputo": 60000, 
        "Equipo de Reparto": 1000000, "Gastos de Instalación": 150000, 
        "Papelería y Útiles": 8000, "Rentas Pagadas x Ant.": 50000, "Capital Social": 5333000
    }

    @staticmethod
    def obtener_datos(tipo_balance, asientos=[]):
        if tipo_balance == "catalogo":
            return {"es_catalogo": True, "lista": [{"codigo": "A", "nombre": "ACTIVOS"}, {"codigo": "ACb", "nombre": "Bancos"}]}

        saldos = {k.lower(): v for k, v in ContabilidadModel.datos_base.items()}
        nombres_bonitos = {k.lower(): k for k in ContabilidadModel.datos_base.keys()}
        cuentas_acreedoras = ["proveedores", "acreedores", "anticipo de cliente", "iva trasladado", "capital social"]

        for asiento in asientos:
            cuenta = asiento['cuenta'].strip().lower()
            monto = float(asiento['monto'])
            es_pasivo = cuenta in cuentas_acreedoras
            
            if cuenta not in saldos:
                saldos[cuenta] = 0
                nombres_bonitos[cuenta] = asiento['cuenta'].strip()

            if asiento['tipo'] == 'cargo':
                saldos[cuenta] += monto if not es_pasivo else -monto
            else:
                saldos[cuenta] -= monto if not es_pasivo else +monto

        activos = [{"nombre": nombres_bonitos[k], "valor": v} for k, v in saldos.items() if k not in cuentas_acreedoras and v != 0]
        pasivos = [{"nombre": nombres_bonitos[k], "valor": abs(v)} for k, v in saldos.items() if k in cuentas_acreedoras and v != 0]

        return {"activos": activos, "pasivos": pasivos}