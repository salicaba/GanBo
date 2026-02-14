class ContabilidadModel:
    @staticmethod
    def obtener_datos(tipo_balance):
        datos_ganbo = {
            # --- 0. CATÁLOGO ---
            "catalogo": {
                "es_catalogo": True,
                "lista": [
                    {"codigo": "A", "nombre": "ACTIVOS"},
                    {"codigo": "AC", "nombre": "  Circulantes"},
                    {"codigo": "ACc", "nombre": "    Caja"},
                    {"codigo": "ACb", "nombre": "    Bancos"},
                    {"codigo": "ACi", "nombre": "    Inventarios"},
                    {"codigo": "ACia", "nombre": "    IVA Acreditable"},
                    {"codigo": "ACixa", "nombre": "    IVA por Acreditar"},
                    {"codigo": "ANC", "nombre": "  No Circulantes"},
                    {"codigo": "ANCt", "nombre": "    Terrenos"},
                    {"codigo": "ANCe", "nombre": "    Edificios"},
                    {"codigo": "ANCme", "nombre": "    Mobiliario y Equipo"},
                    {"codigo": "ANCece", "nombre": "    Equipo de Cómputo"},
                    {"codigo": "ANCeer", "nombre": "    Equipo de Reparto"},
                    {"codigo": "ANCgi", "nombre": "    Gastos de Instalación"},
                    {"codigo": "ANCpu", "nombre": "    Papelería y Útiles"},
                    {"codigo": "ANCrpa", "nombre": "    Rentas Pagadas x Ant."},
                    {"codigo": "P", "nombre": "PASIVOS"},
                    {"codigo": "PC", "nombre": "  Circulantes"},
                    {"codigo": "PCp", "nombre": "    Proveedores"},
                    {"codigo": "PCa", "nombre": "    Acreedores"},
                    {"codigo": "PCac", "nombre": "    Anticipo de Clientes"},
                    {"codigo": "PCit", "nombre": "    IVA Trasladado"},
                    {"codigo": "C", "nombre": "CAPITAL"},
                    {"codigo": "CC", "nombre": "  Contable"},
                    {"codigo": "CCcs", "nombre": "    Capital Social"},
                ]
            },

            # --- 1. BALANCE INICIAL (Sin Factura) ---
            "bgi": {
                "factura": None,
                "activos": [
                    {"nombre": "Caja", "valor": 70000},
                    {"nombre": "Bancos", "valor": 200000},
                    {"nombre": "Inventarios", "valor": 150000},
                    {"nombre": "Terrenos", "valor": 2500000},
                    {"nombre": "Edificios", "valor": 1000000},
                    {"nombre": "Mobiliario y Equipo", "valor": 145000},
                    {"nombre": "Equipo de Cómputo", "valor": 60000},
                    {"nombre": "Equipo de Reparto", "valor": 1000000},
                    {"nombre": "Gastos de Instalación", "valor": 150000},
                    {"nombre": "Papelería y Útiles", "valor": 8000},
                    {"nombre": "Rentas Pagadas x Ant.", "valor": 50000},
                ],
                "pasivos": [{"nombre": "Capital Social", "valor": 5333000}]
            },
            
            # --- 2. COMPRA EFECTIVO (BGCE) ---
            "bgce": {
                "factura": {
                    "titulo": "Factura de Compra (Contado)",
                    "concepto": "Compra de Ganado Bovino",
                    "subtotal": 100000,
                    "iva": 16000,
                    "total": 116000,
                    "notas": ["Pago realizado en una sola exhibición."]
                },
                "activos": [
                    {"nombre": "Caja", "valor": 70000},
                    {"nombre": "Bancos", "valor": 84000},
                    {"nombre": "Inventarios", "valor": 250000}, 
                    {"nombre": "IVA Acreditable", "valor": 16000},
                    {"nombre": "Terrenos", "valor": 2500000},
                    {"nombre": "Edificios", "valor": 1000000},
                    {"nombre": "Mobiliario y Equipo", "valor": 145000},
                    {"nombre": "Equipo de Cómputo", "valor": 60000},
                    {"nombre": "Equipo de Reparto", "valor": 1000000},
                    {"nombre": "Gastos de Instalación", "valor": 150000},
                    {"nombre": "Papelería y Útiles", "valor": 8000},
                    {"nombre": "Rentas Pagadas x Ant.", "valor": 50000},
                ],
                "pasivos": [{"nombre": "Capital Social", "valor": 5333000}]
            },

            # --- 3. COMPRA A CRÉDITO (BGCC) ---
            "bgcc": {
                "factura": {
                    "titulo": "Factura de Compra (Crédito)",
                    "concepto": "Compra de Ganado (Lote 2)",
                    "subtotal": 50000,
                    "iva": 8000,
                    "total": 58000,
                    "notas": ["IVA pendiente de acreditar hasta el pago."]
                },
                "activos": [
                    {"nombre": "Caja", "valor": 70000},
                    {"nombre": "Bancos", "valor": 84000},
                    {"nombre": "Inventarios", "valor": 300000},
                    {"nombre": "IVA Acreditable", "valor": 16000},
                    {"nombre": "IVA x Acreditar", "valor": 8000},
                    {"nombre": "Terrenos", "valor": 2500000},
                    {"nombre": "Edificios", "valor": 1000000},
                    {"nombre": "Mobiliario y Equipo", "valor": 145000},
                    {"nombre": "Equipo de Cómputo", "valor": 60000},
                    {"nombre": "Equipo de Reparto", "valor": 1000000},
                    {"nombre": "Gastos de Instalación", "valor": 150000},
                    {"nombre": "Papelería y Útiles", "valor": 8000},
                    {"nombre": "Rentas Pagadas x Ant.", "valor": 50000},
                ],
                "pasivos": [{"nombre": "Proveedores", "valor": 58000}, {"nombre": "Capital Social", "valor": 5333000}]
            },

            # --- 4. COMPRA CAMIÓN (BGEC) ---
            "bgec": {
                "factura": {
                    "titulo": "Factura de Activo Fijo",
                    "concepto": "Compra de Camión de Reparto",
                    "subtotal": 1000000,
                    "iva": 160000,
                    "total": 1160000,
                    "notas": [
                        "Contado (5%): $50,000 + IVA",
                        "Crédito (95%): $950,000 + IVA"
                    ]
                },
                "activos": [
                    {"nombre": "Caja", "valor": 70000},
                    {"nombre": "Bancos", "valor": 26000},
                    {"nombre": "Inventarios", "valor": 300000},
                    {"nombre": "IVA Acreditable", "valor": 24000},
                    {"nombre": "IVA x Acreditar", "valor": 160000},
                    {"nombre": "Terrenos", "valor": 2500000},
                    {"nombre": "Edificios", "valor": 1000000},
                    {"nombre": "Mobiliario y Equipo", "valor": 145000},
                    {"nombre": "Equipo de Cómputo", "valor": 60000},
                    {"nombre": "Equipo de Reparto", "valor": 2000000},
                    {"nombre": "Gastos de Instalación", "valor": 150000},
                    {"nombre": "Papelería y Útiles", "valor": 8000},
                    {"nombre": "Rentas Pagadas x Ant.", "valor": 50000},
                ],
                "pasivos": [{"nombre": "Proveedores", "valor": 58000}, {"nombre": "Acreedores", "valor": 1102000}, {"nombre": "Capital Social", "valor": 5333000}]
            },

            # --- 5. VENTA (BGAC) ---
            "bgac": {
                "factura": {
                    "titulo": "Factura de Venta",
                    "concepto": "Venta de Carne (Lote Especial)",
                    "subtotal": 1500000,
                    "iva": 240000,
                    "total": 1740000,
                    "notas": ["Anticipo recibido (80%): $1,392,000", "Saldo pendiente: 20%"]
                },
                "activos": [
                    {"nombre": "Caja", "valor": 70000},
                    {"nombre": "Bancos", "valor": 1418000},
                    {"nombre": "Inventarios", "valor": 300000},
                    {"nombre": "IVA Acreditable", "valor": 24000},
                    {"nombre": "IVA x Acreditar", "valor": 160000},
                    {"nombre": "Terrenos", "valor": 2500000},
                    {"nombre": "Edificios", "valor": 1000000},
                    {"nombre": "Mobiliario y Equipo", "valor": 145000},
                    {"nombre": "Equipo de Cómputo", "valor": 60000},
                    {"nombre": "Equipo de Reparto", "valor": 2000000},
                    {"nombre": "Gastos de Instalación", "valor": 150000},
                    {"nombre": "Papelería y Útiles", "valor": 8000},
                    {"nombre": "Rentas Pagadas x Ant.", "valor": 50000},
                ],
                "pasivos": [
                    {"nombre": "Proveedores", "valor": 58000},
                    {"nombre": "Acreedores", "valor": 1102000},
                    {"nombre": "Anticipo de Cliente", "valor": 1200000},
                    {"nombre": "IVA Trasladado", "valor": 192000},
                    {"nombre": "Capital Social", "valor": 5333000},
                ]
            }
        }
        
        return datos_ganbo.get(tipo_balance, {"error": "Balance no encontrado"})