# 📊 GanBo, S.A.S. - Sistema de Gestión Financiera y Contable

Un sistema contable web (ERP) diseñado para **GanBo, S.A.S.** que digitaliza y automatiza el ciclo contable completo. El sistema permite la captura dinámica de transacciones bajo el principio de partida doble y genera automáticamente la trazabilidad hasta los estados financieros finales.

## 🚀 Características Principales

* **Libro Diario Dinámico:** Motor de captura de asientos contables con múltiples cuentas. Incluye validación matemática en tiempo real que bloquea el registro si el Debe y el Haber no cuadran (Partida Doble).
* **Libro Mayor Automatizado (Cuentas T):** Motor de recálculo que lee los asientos del Libro Diario, genera Cuentas T al vuelo, agrupa movimientos y calcula saldos deudores y acreedores automáticamente.
* **Reportes de Cierre Exactos:** Visualización de Balanza de Comprobación Ajustada (BCA), Estado de Resultados (ER) y Estado de Situación Financiera (EF) con cuadre perfecto.
* **Trazabilidad Histórica:** Registro de la evolución financiera desde el Balance General Inicial (BGI) pasando por compras en efectivo, a crédito, mixtas y anticipos de clientes.

## 🛠️ Stack Tecnológico

* **Frontend:** React.js (Hooks, State Management, Renderizado Dinámico).
* **Backend:** Python con Flask (API RESTful para procesamiento de lógica contable).
* **Comunicación:** Axios para peticiones HTTP cliente-servidor.

## ⚙️ Instalación y Uso Local

Sigue estos pasos para correr el proyecto en tu máquina local:

### 1. Clonar el repositorio
\`\`\`bash
git clone https://github.com/TU_USUARIO/GanBo.git
cd GanBo
\`\`\`

### 2. Iniciar el Backend (Python)
Abre una terminal en la carpeta `backend`:
\`\`\`bash
cd backend
# Instalar dependencias si es necesario (ej. pip install flask flask-cors)
python app.py
\`\`\`
El servidor de Flask se ejecutará en `http://localhost:5000`.

### 3. Iniciar el Frontend (React)
Abre una nueva terminal en la carpeta `frontend`:
\`\`\`bash
cd frontend
npm install
npm start
\`\`\`
La aplicación web se abrirá automáticamente en tu navegador en `http://localhost:3000`.

## 📖 Flujo Contable del Sistema

Este sistema respeta el flujo estricto de la contabilidad financiera:
1.  **Origen:** Los datos inician en el **Balance General Inicial**.
2.  **Registro:** Las operaciones diarias se capturan en el **Libro Diario**.
3.  **Clasificación:** El sistema transfiere y calcula los montos en el **Libro Mayor** (Cuentas T).
4.  **Comprobación:** Se verifica el cuadre perfecto de movimientos y saldos en la **Balanza de Comprobación Ajustada**.
5.  **Resultados:** Se calcula la Utilidad Neta en el **Estado de Resultados**.
6.  **Cierre:** La utilidad se inyecta en el Capital Contable dentro del **Estado de Situación Financiera**, asegurando que Activo = Pasivo + Capital.

---
**Créditos del Proyecto:**
* Autorizado por: Lic. Gonzáles Zúñiga Nuria
* Elaborado por: Ing. Salinas Caballero Emmanuel