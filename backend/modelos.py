class ContabilidadModel:
    # 1. Los balances generales anteriores se mantienen intactos
    saldos_por_balance = {
        "bgi": { "Caja": 70000, "Bancos": 200000, "Inventarios": 150000, "Terrenos": 2500000, "Edificios": 1000000, "Mobilario y Equipo": 145000, "Equipo de Cómputo Electrónico": 60000, "Equipo de Entrega y Reparto": 1000000, "Gastos de Instalación": 150000, "Papelería y Útiles": 8000, "Rentas Pagadas por Anticipado": 50000, "Capital Social": 5333000 },
        "bgce": { "Caja": 70000, "Bancos": 84000, "Inventarios": 250000, "IVA Acreditable": 16000, "Terrenos": 2500000, "Edificios": 1000000, "Mobilario y Equipo": 145000, "Equipo de Cómputo Electrónico": 60000, "Equipo de Entrega y Reparto": 1000000, "Gastos de Instalación": 150000, "Papelería y Útiles": 8000, "Rentas Pagadas por Anticipado": 50000, "Capital Social": 5333000 },
        "bgcc": { "Caja": 70000, "Bancos": 84000, "Inventarios": 300000, "IVA Acreditable": 16000, "IVA x Acreditar": 8000, "Terrenos": 2500000, "Edificios": 1000000, "Mobilario y Equipo": 145000, "Equipo de Cómputo Electrónico": 60000, "Equipo de Entrega y Reparto": 1000000, "Gastos de Instalación": 150000, "Papelería y Útiles": 8000, "Rentas Pagadas por Anticipado": 50000, "Proveedores": 58000, "Capital Social": 5333000 },
        "bgec": { "Caja": 70000, "Bancos": 26000, "Inventarios": 300000, "IVA Acreditable": 24000, "IVA x Acreditar": 160000, "Terrenos": 2500000, "Edificios": 1000000, "Mobilario y Equipo": 145000, "Equipo de Cómputo Electrónico": 60000, "Equipo de Entrega y Reparto": 2000000, "Gastos de Instalación": 150000, "Papelería y Útiles": 8000, "Rentas Pagadas por Anticipado": 50000, "Proveedores": 58000, "Acreedores": 1102000, "Capital Social": 5333000 },
        "bgac": { "Caja": 70000, "Bancos": 1418000, "Inventarios": 300000, "IVA Acreditable": 24000, "IVA x Acreditar": 160000, "Terrenos": 2500000, "Edificios": 1000000, "Mobilario y Equipo": 145000, "Equipo de Cómputo Electrónico": 60000, "Equipo de Entrega y Reparto": 2000000, "Gastos de Instalación": 150000, "Papelería y Útiles": 8000, "Rentas Pagadas por Anticipado": 50000, "Proveedores": 58000, "Acreedores": 1102000, "Anticipo de Cliente": 1200000, "IVA Trasladado": 192000, "Capital Social": 5333000 }
    }

    @staticmethod
    def obtener_datos(tipo_balance, asientos=[]):
        tipo = tipo_balance.lower().strip()

        if tipo == "catalogo":
            return {"es_catalogo": True, "lista": [{"codigo": "A", "nombre": "Activos"}, {"codigo": "AC", "nombre": "Circulantes"}, {"codigo": "ACc", "nombre": "Caja"}, {"codigo": "ACb", "nombre": "Bancos"}, {"codigo": "ACi", "nombre": "Inventarios"}, {"codigo": "ANC", "nombre": "No Circulantes"}, {"codigo": "ANCt", "nombre": "Terrenos"}, {"codigo": "ANCe", "nombre": "Edificios"}, {"codigo": "ANCme", "nombre": "Mobilario y Equipo"}, {"codigo": "ANCece", "nombre": "Equipo de Cómputo Electrónico"}, {"codigo": "ANCeer", "nombre": "Equipo de Entrega y Reparto"}, {"codigo": "ANCgc", "nombre": "Gastos de Constitución"}, {"codigo": "ANCgi", "nombre": "Gastos de Instalación"}, {"codigo": "ANCpu", "nombre": "Papelería y Útiles"}, {"codigo": "ANCrpa", "nombre": "Rentas Pagadas por Anticipado"}]}

        # === NUEVAS SECCIONES EXACTAS AL EXCEL ===
        
        if tipo == "bca":
            return {
                "es_bca": True,
                "titulo": "Balanza de Comprobación Ajustada",
                "lista": [
                    {"cuenta": "Caja", "debe": 70000, "haber": 0, "deudor": 70000, "acreedor": 0},
                    {"cuenta": "Bancos", "debe": 1611720, "haber": 201128, "deudor": 1410592, "acreedor": 0},
                    {"cuenta": "Inventarios", "debe": 300000, "haber": 0, "deudor": 300000, "acreedor": 0},
                    {"cuenta": "IVA Acreditable", "debe": 17728, "haber": 320, "deudor": 17408, "acreedor": 0},
                    {"cuenta": "IVA por Acreditar", "debe": 171200, "haber": 160, "deudor": 171040, "acreedor": 0},
                    {"cuenta": "Terrenos", "debe": 2500000, "haber": 0, "deudor": 2500000, "acreedor": 0},
                    {"cuenta": "Edificios", "debe": 1000000, "haber": 0, "deudor": 1000000, "acreedor": 0},
                    {"cuenta": "Mobiliario y Equipo", "debe": 145000, "haber": 0, "deudor": 145000, "acreedor": 0},
                    {"cuenta": "Equipo de Cómputo", "debe": 60000, "haber": 0, "deudor": 60000, "acreedor": 0},
                    {"cuenta": "Equipo de Entrega", "debe": 2000000, "haber": 0, "deudor": 2000000, "acreedor": 0},
                    {"cuenta": "Gastos de Instalación", "debe": 150000, "haber": 0, "deudor": 150000, "acreedor": 0},
                    {"cuenta": "Papelería y Útiles", "debe": 8000, "haber": 500, "deudor": 7500, "acreedor": 0},
                    {"cuenta": "Rentas Pagadas por Anticipado", "debe": 50000, "haber": 11000, "deudor": 39000, "acreedor": 0},
                    {"cuenta": "Proveedores", "debe": 1160, "haber": 81200, "deudor": 0, "acreedor": 80040},
                    {"cuenta": "Acreedores Diversos", "debe": 0, "haber": 1102000, "deudor": 0, "acreedor": 1102000},
                    {"cuenta": "Anticipo de Clientes", "debe": 1200000, "haber": 1200000, "deudor": 0, "acreedor": 0},
                    {"cuenta": "IVA Trasladado", "debe": 193600, "haber": 194400, "deudor": 0, "acreedor": 800},
                    {"cuenta": "IVA por Trasladar", "debe": 0, "haber": 244800, "deudor": 0, "acreedor": 244800},
                    {"cuenta": "Capital Social", "debe": 0, "haber": 5333000, "deudor": 0, "acreedor": 5333000},
                    {"cuenta": "Clientes", "debe": 382800, "haber": 0, "deudor": 382800, "acreedor": 0},
                    {"cuenta": "Ventas", "debe": 0, "haber": 1545000, "deudor": 0, "acreedor": 1545000},
                    {"cuenta": "Gastos de Venta", "debe": 19666.67, "haber": 0, "deudor": 19666.67, "acreedor": 0},
                    {"cuenta": "Gastos de Administración", "debe": 44625, "haber": 0, "deudor": 44625, "acreedor": 0},
                    {"cuenta": "Depreciación Acum. Edificios", "debe": 0, "haber": 4166.67, "deudor": 0, "acreedor": 4166.67},
                    {"cuenta": "Depreciación Acum. Mobiliario", "debe": 0, "haber": 1208.33, "deudor": 0, "acreedor": 1208.33},
                    {"cuenta": "Depreciación Acum. Eq. Cómputo", "debe": 0, "haber": 1500, "deudor": 0, "acreedor": 1500},
                    {"cuenta": "Depreciación Acum. Eq. Entrega", "debe": 0, "haber": 41666.67, "deudor": 0, "acreedor": 41666.67},
                    {"cuenta": "Amortización Acum. Gtos. Inst.", "debe": 0, "haber": 1250, "deudor": 0, "acreedor": 1250},
                    {"cuenta": "Compras", "debe": 30000, "haber": 0, "deudor": 30000, "acreedor": 0},
                    {"cuenta": "Gastos de Compra", "debe": 800, "haber": 0, "deudor": 800, "acreedor": 0},
                    {"cuenta": "Devoluciones s/ Ventas", "debe": 5000, "haber": 0, "deudor": 5000, "acreedor": 0},
                    {"cuenta": "Descuentos s/ Ventas", "debe": 5000, "haber": 0, "deudor": 5000, "acreedor": 0},
                    {"cuenta": "Devoluciones s/ Compras", "debe": 0, "haber": 2000, "deudor": 0, "acreedor": 2000},
                    {"cuenta": "Descuentos s/ Compras", "debe": 0, "haber": 1000, "deudor": 0, "acreedor": 1000},
                    {"cuenta": "SUMAS IGUALES", "debe": 9966299.67, "haber": 9966299.67, "deudor": 8358431.67, "acreedor": 8358431.67}
                ]
            }

        if tipo == "er":
            return {
                "es_er": True,
                "titulo": "Estado de Resultados",
                "resultados": [
                    {"concepto": "Ventas totales", "c1": "", "c2": "", "c3": "", "c4": 1545000},
                    {"concepto": "Devoluciones s/ventas", "c1": "", "c2": "", "c3": 5000, "c4": ""},
                    {"concepto": "Descuentos s/ventas", "c1": "", "c2": "", "c3": 5000, "c4": 10000},
                    {"concepto": "Ventas netas", "c1": "", "c2": "", "c3": "", "c4": 1535000},
                    {"concepto": "Inventario inicial", "c1": "", "c2": "", "c3": 300000, "c4": ""},
                    {"concepto": "Compras", "c1": "", "c2": 30000, "c3": "", "c4": ""},
                    {"concepto": "Gastos de compras", "c1": "", "c2": 800, "c3": "", "c4": ""},
                    {"concepto": "Compras totales", "c1": "", "c2": 30800, "c3": "", "c4": ""},
                    {"concepto": "Devoluciones s/compras", "c1": 2000, "c2": "", "c3": "", "c4": ""},
                    {"concepto": "Descuentos s/compras", "c1": 1000, "c2": 3000, "c3": "", "c4": ""},
                    {"concepto": "Compras netas", "c1": "", "c2": "", "c3": 27800, "c4": ""},
                    {"concepto": "Mercancías disponibles", "c1": "", "c2": "", "c3": 327800, "c4": ""},
                    {"concepto": "Inventario final", "c1": "", "c2": "", "c3": 30000, "c4": ""},
                    {"concepto": "Costo de ventas", "c1": "", "c2": "", "c3": "", "c4": 297800},
                    {"concepto": "Utilidad bruta", "c1": "", "c2": "", "c3": "", "c4": 1237200},
                    {"concepto": "Gastos de operación", "c1": "", "c2": "", "c3": "", "c4": ""},
                    {"concepto": "Gastos de venta", "c1": "", "c2": "", "c3": 19666.67, "c4": ""},
                    {"concepto": "Gastos de administración", "c1": "", "c2": "", "c3": 44625, "c4": 64291.67},
                    {"concepto": "Utilidad de operación", "c1": "", "c2": "", "c3": "", "c4": 1172908.33},
                    {"concepto": "ISR (30%)", "c1": "", "c2": "", "c3": 351872.5, "c4": ""},
                    {"concepto": "PTU (10%)", "c1": "", "c2": "", "c3": 117290.83, "c4": 469163.33},
                    {"concepto": "Utilidad Neta del Ejercicio", "c1": "", "c2": "", "c3": "", "c4": 703745}
                ]
            }

        if tipo == "ef":
            return {
                "es_ef": True,
                "titulo": "Estado de Situación Financiera",
                "secciones": [
                    {
                        "nombre": "ACTIVO CIRCULANTE",
                        "cuentas": [
                            {"n": "Caja", "c1": "", "c2": 70000, "c3": ""},
                            {"n": "Bancos", "c1": "", "c2": 1410592, "c3": ""},
                            {"n": "Clientes", "c1": "", "c2": 382800, "c3": ""},
                            {"n": "Inventarios", "c1": "", "c2": 30000, "c3": ""},
                            {"n": "IVA Acreditable", "c1": "", "c2": 17408, "c3": ""},
                            {"n": "IVA por Acreditar", "c1": "", "c2": 171040, "c3": 2081840}
                        ]
                    },
                    {
                        "nombre": "ACTIVO FIJO",
                        "cuentas": [
                            {"n": "Terrenos", "c1": "", "c2": 2500000, "c3": ""},
                            {"n": "Edificios", "c1": 1000000, "c2": "", "c3": ""},
                            {"n": "(-) Depreciación Acum. Edificios", "c1": 4166.67, "c2": 995833.33, "c3": ""},
                            {"n": "Mobiliario y Equipo", "n": "Mobiliario y Equipo", "c1": 145000, "c2": "", "c3": ""},
                            {"n": "(-) Depreciación Acum. Mobiliario", "c1": 1208.33, "c2": 143791.67, "c3": ""},
                            {"n": "Equipo de Cómputo", "c1": 60000, "c2": "", "c3": ""},
                            {"n": "(-) Depreciación Acum. Eq. Cómputo", "c1": 1500, "c2": 58500, "c3": ""},
                            {"n": "Equipo de Entrega", "c1": 2000000, "c2": "", "c3": ""},
                            {"n": "(-) Depreciación Acum. Eq. Entrega", "c1": 41666.67, "c2": 1958333.33, "c3": 5656458.33}
                        ]
                    },
                    {
                        "nombre": "ACTIVO DIFERIDO",
                        "cuentas": [
                            {"n": "Gastos de Instalación", "c1": 150000, "c2": "", "c3": ""},
                            {"n": "(-) Amortización Acum. Gtos. Inst.", "c1": 1250, "c2": 148750, "c3": ""},
                            {"n": "Papelería y Útiles", "c1": "", "c2": 7500, "c3": ""},
                            {"n": "Rentas Pagadas por Anticipado", "c1": "", "c2": 39000, "c3": 195250}
                        ]
                    },
                    { "n": "TOTAL ACTIVO", "c3": 7933548.33, "is_total": True },
                    {
                        "nombre": "PASIVO CORTO PLAZO",
                        "cuentas": [
                            {"n": "Proveedores", "c1": "", "c2": 80040, "c3": ""},
                            {"n": "IVA Trasladado", "c1": "", "c2": 800, "c3": ""},
                            {"n": "IVA por Trasladar", "c1": "", "c2": 244800, "c3": ""},
                            {"n": "ISR por Pagar", "c1": "", "c2": 351872.50, "c3": ""},
                            {"n": "PTU por Pagar", "c1": "", "c2": 117290.83, "c3": 794803.33}
                        ]
                    },
                    {
                        "nombre": "PASIVO LARGO PLAZO",
                        "cuentas": [
                            {"n": "Acreedores Diversos", "c1": "", "c2": 1102000, "c3": 1102000}
                        ]
                    },
                    {
                        "nombre": "CAPITAL CONTABLE",
                        "cuentas": [
                            {"n": "Capital Social", "c1": "", "c2": 5333000, "c3": ""},
                            {"n": "Utilidad Neta del Ejercicio", "c1": "", "c2": 703745, "c3": 6036745}
                        ]
                    },
                    { "n": "TOTAL PASIVO + CAPITAL", "c3": 7933548.33, "is_total": True }
                ]
            }
        
        if tipo == "ld":
            return {
                "es_ld": True,
                "titulo": "Libro Diario del 23 de enero al 13 de marzo",
                "asientos": [
                    {
                        "fecha": "2026-01-23", "concepto": "— 1 — Constitución de la empresa con aportaciones en efectivo y bienes.",
                        "movimientos": [
                            {"cuenta": "Caja", "debe": 70000, "haber": ""},
                            {"cuenta": "Bancos", "debe": 200000, "haber": ""},
                            {"cuenta": "Inventarios", "debe": 150000, "haber": ""},
                            {"cuenta": "Terrenos", "debe": 2500000, "haber": ""},
                            {"cuenta": "Edificios", "debe": 1000000, "haber": ""},
                            {"cuenta": "Mobiliario y Equipo", "debe": 145000, "haber": ""},
                            {"cuenta": "Equipo de Cómputo", "debe": 60000, "haber": ""},
                            {"cuenta": "Equipo de Entrega y Reparto", "debe": 1000000, "haber": ""},
                            {"cuenta": "Gastos de Instalación", "debe": 150000, "haber": ""},
                            {"cuenta": "Papelería y Útiles", "debe": 8000, "haber": ""},
                            {"cuenta": "Rentas Pagadas por Anticipado", "debe": 50000, "haber": ""},
                            {"cuenta": "Capital Social", "debe": "", "haber": 5333000}
                        ]
                    },
                    {
                        "fecha": "2026-01-28", "concepto": "— 2 — Compra de materia prima (ganado) pagada de contado.",
                        "movimientos": [
                            {"cuenta": "Inventarios", "debe": 100000, "haber": ""},
                            {"cuenta": "IVA Acreditable", "debe": 16000, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 116000}
                        ]
                    },
                    {
                        "fecha": "2026-01-30", "concepto": "— 3 — Compra de materia prima a crédito.",
                        "movimientos": [
                            {"cuenta": "Inventarios", "debe": 50000, "haber": ""},
                            {"cuenta": "IVA Acreditable", "debe": 8000, "haber": ""},
                            {"cuenta": "Proveedores", "debe": "", "haber": 58000}
                        ]
                    },
                    {
                        "fecha": "2026-01-30", "concepto": "— 4 — Compra de camión con pago parcial y resto a crédito.",
                        "movimientos": [
                            {"cuenta": "Equipo de Entrega y Reparto", "debe": 1000000, "haber": ""},
                            {"cuenta": "IVA Acreditable", "debe": 160000, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 58000},
                            {"cuenta": "Acreedores Diversos", "debe": "", "haber": 1102000}
                        ]
                    },
                    {
                        "fecha": "2026-02-04", "concepto": "— 5 — Cobro de anticipo de clientes con IVA incluido.",
                        "movimientos": [
                            {"cuenta": "Bancos", "debe": 1392000, "haber": ""},
                            {"cuenta": "Anticipo de Clientes", "debe": "", "haber": 1200000},
                            {"cuenta": "IVA Trasladado", "debe": "", "haber": 192000}
                        ]
                    },
                    {
                        "fecha": "2026-02-27", "concepto": "— 6 — Aplicación de renta pagada por anticipado (gasto del mes).",
                        "movimientos": [
                            {"cuenta": "Gastos de Venta", "debe": 11000, "haber": ""},
                            {"cuenta": "Rentas Pagadas por Anticipado", "debe": "", "haber": 11000}
                        ]
                    },
                    {
                        "fecha": "2026-03-04", "concepto": "— 7 — Consumo de papelería del mes.",
                        "movimientos": [
                            {"cuenta": "Gastos de Administración", "debe": 500, "haber": ""},
                            {"cuenta": "Papelería y Útiles", "debe": "", "haber": 500}
                        ]
                    },
                    {
                        "fecha": "2026-03-04", "concepto": "— 8 — Venta aplicando anticipo de cliente.",
                        "movimientos": [
                            {"cuenta": "Clientes", "debe": 348000, "haber": ""},
                            {"cuenta": "Anticipo de Clientes", "debe": 1200000, "haber": ""},
                            {"cuenta": "IVA Trasladado", "debe": 192000, "haber": ""},
                            {"cuenta": "Ventas", "debe": "", "haber": 1500000},
                            {"cuenta": "IVA por Trasladar", "debe": "", "haber": 240000}
                        ]
                    },
                    {
                        "fecha": "2026-03-06", "concepto": "— 9 — Registro de depreciaciones y amortizaciones del periodo.",
                        "movimientos": [
                            {"cuenta": "Gastos de Administración", "debe": 44125, "haber": ""},
                            {"cuenta": "Gastos de Venta", "debe": 5666.67, "haber": ""},
                            {"cuenta": "Deprec. Acum. Mob. y Equipo", "debe": "", "haber": 1208.33},
                            {"cuenta": "Deprec. Acum. Eq. Entrega", "debe": "", "haber": 41666.67},
                            {"cuenta": "Amort. Acum. Gastos Inst.", "debe": "", "haber": 1250},
                            {"cuenta": "Deprec. Acum. Eq. Cómputo", "debe": "", "haber": 1500},
                            {"cuenta": "Deprec. Acum. Edificios", "debe": "", "haber": 4166.67}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 10 — Compra de ganado de contado.",
                        "movimientos": [
                            {"cuenta": "Compras", "debe": 10000, "haber": ""},
                            {"cuenta": "IVA Acreditable", "debe": 1600, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 11600}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 11 — Compra de ganado a crédito.",
                        "movimientos": [
                            {"cuenta": "Compras", "debe": 20000, "haber": ""},
                            {"cuenta": "IVA Acreditable", "debe": 3200, "haber": ""},
                            {"cuenta": "Proveedores", "debe": "", "haber": 23200}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 12 — Venta de contado.",
                        "movimientos": [
                            {"cuenta": "Bancos", "debe": 17400, "haber": ""},
                            {"cuenta": "Ventas", "debe": "", "haber": 15000},
                            {"cuenta": "IVA Trasladado", "debe": "", "haber": 2400}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 13 — Venta a crédito.",
                        "movimientos": [
                            {"cuenta": "Clientes", "debe": 34800, "haber": ""},
                            {"cuenta": "Ventas", "debe": "", "haber": 30000},
                            {"cuenta": "IVA por Trasladar", "debe": "", "haber": 4800}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 14 — Pago de gastos de compra.",
                        "movimientos": [
                            {"cuenta": "Gastos de Compra", "debe": 800, "haber": ""},
                            {"cuenta": "IVA Acreditable", "debe": 128, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 928}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 15 — Devolución sobre ventas (contado).",
                        "movimientos": [
                            {"cuenta": "Devoluciones sobre Ventas", "debe": 5000, "haber": ""},
                            {"cuenta": "IVA Trasladado", "debe": 800, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 5800}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 16 — Descuento sobre ventas.",
                        "movimientos": [
                            {"cuenta": "Descuentos sobre Ventas", "debe": 5000, "haber": ""},
                            {"cuenta": "IVA Trasladado", "debe": 800, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 5800}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 17 — Pago de gasolina del camión.",
                        "movimientos": [
                            {"cuenta": "Gastos de Venta", "debe": 3000, "haber": ""},
                            {"cuenta": "Bancos", "debe": "", "haber": 3000}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 18 — Devolución a proveedor.",
                        "movimientos": [
                            {"cuenta": "Bancos", "debe": 2320, "haber": ""},
                            {"cuenta": "Devoluciones sobre Compras", "debe": "", "haber": 2000},
                            {"cuenta": "IVA Acreditable", "debe": "", "haber": 320}
                        ]
                    },
                    {
                        "fecha": "2026-03-13", "concepto": "— 19 — Descuento otorgado por proveedor.",
                        "movimientos": [
                            {"cuenta": "Proveedores", "debe": 1160, "haber": ""},
                            {"cuenta": "Descuentos sobre Compras", "debe": "", "haber": 1000},
                            {"cuenta": "IVA Acreditable", "debe": "", "haber": 160}
                        ]
                    },
                    {
                        "fecha": "---", "concepto": "TOTALES IGUALES",
                        "movimientos": [
                            {"cuenta": "DEBE", "debe": 9966299.67, "haber": ""},
                            {"cuenta": "HABER", "debe": "", "haber": 9966299.67}
                        ]
                    }
                ]
            }

        if tipo == "lm":
            return {
                "es_lm": True,
                "titulo": "Libro Mayor (Cuentas T)",
                "cuentas": [
                    {"nombre": "Caja", "cargos": [{"ref": "1)", "monto": 70000}], "abonos": [], "md": 70000, "ma": 0, "sd": 70000, "sa": 0},
                    {"nombre": "Bancos", "cargos": [{"ref": "1)", "monto": 200000}, {"ref": "5)", "monto": 1392000}, {"ref": "12)", "monto": 17400}, {"ref": "18)", "monto": 2320}], "abonos": [{"ref": "2)", "monto": 116000}, {"ref": "4)", "monto": 58000}, {"ref": "10)", "monto": 11600}, {"ref": "14)", "monto": 928}, {"ref": "15)", "monto": 5800}, {"ref": "16)", "monto": 5800}, {"ref": "17)", "monto": 3000}], "md": 1611720, "ma": 201128, "sd": 1410592, "sa": 0},
                    {"nombre": "Inventarios", "cargos": [{"ref": "1)", "monto": 150000}, {"ref": "2)", "monto": 100000}, {"ref": "3)", "monto": 50000}], "abonos": [], "md": 300000, "ma": 0, "sd": 300000, "sa": 0},
                    {"nombre": "Terrenos", "cargos": [{"ref": "1)", "monto": 2500000}], "abonos": [], "md": 2500000, "ma": 0, "sd": 2500000, "sa": 0},
                    {"nombre": "Edificios", "cargos": [{"ref": "1)", "monto": 1000000}], "abonos": [], "md": 1000000, "ma": 0, "sd": 1000000, "sa": 0},
                    {"nombre": "Mobiliario y Equipo", "cargos": [{"ref": "1)", "monto": 145000}], "abonos": [], "md": 145000, "ma": 0, "sd": 145000, "sa": 0},
                    {"nombre": "Equipo de Cómputo", "cargos": [{"ref": "1)", "monto": 60000}], "abonos": [], "md": 60000, "ma": 0, "sd": 60000, "sa": 0},
                    {"nombre": "Equipo de Entrega y Reparto", "cargos": [{"ref": "1)", "monto": 1000000}, {"ref": "4)", "monto": 1000000}], "abonos": [], "md": 2000000, "ma": 0, "sd": 2000000, "sa": 0},
                    {"nombre": "Gastos de Instalación", "cargos": [{"ref": "1)", "monto": 150000}], "abonos": [], "md": 150000, "ma": 0, "sd": 150000, "sa": 0},
                    {"nombre": "Papelería y Útiles", "cargos": [{"ref": "1)", "monto": 8000}], "abonos": [{"ref": "7)", "monto": 500}], "md": 8000, "ma": 500, "sd": 7500, "sa": 0},
                    {"nombre": "Rentas Pagadas por Ant.", "cargos": [{"ref": "1)", "monto": 50000}], "abonos": [{"ref": "6)", "monto": 11000}], "md": 50000, "ma": 11000, "sd": 39000, "sa": 0},
                    {"nombre": "Capital Social", "cargos": [], "abonos": [{"ref": "1)", "monto": 5333000}], "md": 0, "ma": 5333000, "sd": 0, "sa": 5333000},
                    {"nombre": "IVA Acreditable", "cargos": [{"ref": "2)", "monto": 16000}, {"ref": "3)", "monto": 8000}, {"ref": "4)", "monto": 160000}, {"ref": "10)", "monto": 1600}, {"ref": "11)", "monto": 3200}, {"ref": "14)", "monto": 128}], "abonos": [{"ref": "18)", "monto": 320}, {"ref": "19)", "monto": 160}], "md": 188928, "ma": 480, "sd": 188448, "sa": 0},
                    {"nombre": "Proveedores", "cargos": [{"ref": "19)", "monto": 1160}], "abonos": [{"ref": "3)", "monto": 58000}, {"ref": "11)", "monto": 23200}], "md": 1160, "ma": 81200, "sd": 0, "sa": 80040},
                    {"nombre": "Acreedores Diversos", "cargos": [], "abonos": [{"ref": "4)", "monto": 1102000}], "md": 0, "ma": 1102000, "sd": 0, "sa": 1102000},
                    {"nombre": "Anticipo de Clientes", "cargos": [{"ref": "8)", "monto": 1200000}], "abonos": [{"ref": "5)", "monto": 1200000}], "md": 1200000, "ma": 1200000, "sd": 0, "sa": 0},
                    {"nombre": "IVA Trasladado", "cargos": [{"ref": "8)", "monto": 192000}, {"ref": "15)", "monto": 800}, {"ref": "16)", "monto": 800}], "abonos": [{"ref": "5)", "monto": 192000}, {"ref": "12)", "monto": 2400}], "md": 193600, "ma": 194400, "sd": 0, "sa": 800},
                    {"nombre": "Gastos de Venta", "cargos": [{"ref": "6)", "monto": 11000}, {"ref": "9)", "monto": 5666.67}, {"ref": "17)", "monto": 3000}], "abonos": [], "md": 19666.67, "ma": 0, "sd": 19666.67, "sa": 0},
                    {"nombre": "Gastos de Administración", "cargos": [{"ref": "7)", "monto": 500}, {"ref": "9)", "monto": 44125}], "abonos": [], "md": 44625, "ma": 0, "sd": 44625, "sa": 0},
                    {"nombre": "Clientes", "cargos": [{"ref": "8)", "monto": 348000}, {"ref": "13)", "monto": 34800}], "abonos": [], "md": 382800, "ma": 0, "sd": 382800, "sa": 0},
                    {"nombre": "Ventas", "cargos": [], "abonos": [{"ref": "8)", "monto": 1500000}, {"ref": "12)", "monto": 15000}, {"ref": "13)", "monto": 30000}], "md": 0, "ma": 1545000, "sd": 0, "sa": 1545000},
                    {"nombre": "IVA por Trasladar", "cargos": [], "abonos": [{"ref": "8)", "monto": 240000}, {"ref": "13)", "monto": 4800}], "md": 0, "ma": 244800, "sd": 0, "sa": 244800},
                    {"nombre": "Deprec. Acum. Mob y Eq.", "cargos": [], "abonos": [{"ref": "9)", "monto": 1208.33}], "md": 0, "ma": 1208.33, "sd": 0, "sa": 1208.33},
                    {"nombre": "Deprec. Acum. Eq. Entrega", "cargos": [], "abonos": [{"ref": "9)", "monto": 41666.67}], "md": 0, "ma": 41666.67, "sd": 0, "sa": 41666.67},
                    {"nombre": "Amort. Acum. Gastos Inst.", "cargos": [], "abonos": [{"ref": "9)", "monto": 1250}], "md": 0, "ma": 1250, "sd": 0, "sa": 1250},
                    {"nombre": "Deprec. Acum. Eq. Cómputo", "cargos": [], "abonos": [{"ref": "9)", "monto": 1500}], "md": 0, "ma": 1500, "sd": 0, "sa": 1500},
                    {"nombre": "Deprec. Acum. Edificios", "cargos": [], "abonos": [{"ref": "9)", "monto": 4166.67}], "md": 0, "ma": 4166.67, "sd": 0, "sa": 4166.67},
                    {"nombre": "Compras", "cargos": [{"ref": "10)", "monto": 10000}, {"ref": "11)", "monto": 20000}], "abonos": [], "md": 30000, "ma": 0, "sd": 30000, "sa": 0},
                    {"nombre": "Gastos de Compra", "cargos": [{"ref": "14)", "monto": 800}], "abonos": [], "md": 800, "ma": 0, "sd": 800, "sa": 0},
                    {"nombre": "Devoluciones sobre Ventas", "cargos": [{"ref": "15)", "monto": 5000}], "abonos": [], "md": 5000, "ma": 0, "sd": 5000, "sa": 0},
                    {"nombre": "Descuentos sobre Ventas", "cargos": [{"ref": "16)", "monto": 5000}], "abonos": [], "md": 5000, "ma": 0, "sd": 5000, "sa": 0},
                    {"nombre": "Devoluciones s/ Compras", "cargos": [], "abonos": [{"ref": "18)", "monto": 2000}], "md": 0, "ma": 2000, "sd": 0, "sa": 2000},
                    {"nombre": "Descuentos s/ Compras", "cargos": [], "abonos": [{"ref": "19)", "monto": 1000}], "md": 0, "ma": 1000, "sd": 0, "sa": 1000}
                ]
            }

        # === BALANCES BÁSICOS (Lógica anterior) ===
        snapshot_actual = ContabilidadModel.saldos_por_balance.get(tipo, ContabilidadModel.saldos_por_balance["bgac"])
        saldos = {k.lower(): v for k, v in snapshot_actual.items()}
        nombres_bonitos = {k.lower(): k for k in snapshot_actual.keys()}
        cuentas_acreedoras = ["proveedores", "acreedores", "anticipo de cliente", "anticipo de clientes", "iva trasladado", "capital social", "utilidad", "pérdida"]

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

        activos = []
        pasivos = []
        todas_las_cuentas = list(snapshot_actual.keys()) + [nombres_bonitos[k] for k in saldos.keys() if nombres_bonitos[k] not in snapshot_actual]
        cuentas_vistas = set()

        for nombre_original in todas_las_cuentas:
            c_lower = nombre_original.lower()
            if c_lower in cuentas_vistas: continue
            cuentas_vistas.add(c_lower)
            valor = saldos.get(c_lower, 0)
            if c_lower not in cuentas_acreedoras:
                activos.append({"nombre": nombre_original, "valor": valor})
            else:
                pasivos.append({"nombre": nombre_original, "valor": abs(valor)})

        return {"activos": activos, "pasivos": pasivos}