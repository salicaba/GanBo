import React, { useState, useEffect } from 'react';
import { Calculator, Save, X, DollarSign, Coins, Wallet } from 'lucide-react';

const ArqueoCaja = ({ onClose }) => {
  // AHORA EL FONDO FIJO ES UN ESTADO DINÁMICO (Inicia en 0)
  const [fondoFijo, setFondoFijo] = useState(0);

  const [denominaciones, setDenominaciones] = useState({
    billetes: { b1000: 0, b500: 0, b200: 0, b100: 0, b50: 0, b20: 0 },
    monedas: { m10: 0, m5: 0, m2: 0, m1: 0, m050: 0 }
  });

  const [totales, setTotales] = useState({ fisico: 0, diferencia: 0 });

  useEffect(() => {
    const totalBilletes = 
      (denominaciones.billetes.b1000 * 1000) + (denominaciones.billetes.b500 * 500) +
      (denominaciones.billetes.b200 * 200) + (denominaciones.billetes.b100 * 100) +
      (denominaciones.billetes.b50 * 50) + (denominaciones.billetes.b20 * 20);
    
    const totalMonedas = 
      (denominaciones.monedas.m10 * 10) + (denominaciones.monedas.m5 * 5) +
      (denominaciones.monedas.m2 * 2) + (denominaciones.monedas.m1 * 1) +
      (denominaciones.monedas.m050 * 0.5);

    const granTotal = totalBilletes + totalMonedas;
    
    setTotales({
      fisico: granTotal,
      diferencia: granTotal - fondoFijo // Ahora usa el valor que el usuario escribe
    });
  }, [denominaciones, fondoFijo]);

  const handleInputChange = (categoria, item, valor) => {
    setDenominaciones(prev => ({
      ...prev,
      [categoria]: { ...prev[categoria], [item]: valor === '' ? 0 : parseFloat(valor) }
    }));
  };

  const guardarArqueo = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/tesoreria/arqueo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fondoFijo, denominaciones, totales })
      });
      const data = await response.json();
      alert(data.message);
      if (data.status === "success") onClose(); 
    } catch (error) {
      console.error("Error al guardar:", error);
      alert("Error al conectar con el backend.");
    }
  };

  return (
    <>
      <style>{`
        .modal-overlay {
          position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
          background: rgba(2, 6, 23, 0.85); backdrop-filter: blur(8px);
          display: flex; justify-content: center; align-items: center;
          z-index: 9999; font-family: 'Segoe UI', system-ui, sans-serif;
        }
        .modal-content {
          background: #0f172a; border: 1px solid #334155; border-radius: 16px;
          width: 95%; max-width: 900px; max-height: 90vh; overflow-y: auto;
          box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7); color: #f8fafc;
        }
        .modal-header {
          display: flex; justify-content: space-between; align-items: center;
          padding: 24px; border-bottom: 1px solid #1e293b; background: #0f172a;
          position: sticky; top: 0; z-index: 10;
        }
        .modal-header h2 { margin: 0; color: #f8fafc; font-size: 1.5rem; display: flex; align-items: center; gap: 12px; }
        .modal-header p { margin: 4px 0 0 40px; color: #94a3b8; font-size: 0.9rem; }
        .btn-close {
          background: transparent; border: none; color: #64748b; cursor: pointer;
          padding: 8px; border-radius: 50%; transition: 0.2s;
        }
        .btn-close:hover { background: #334155; color: #f1f5f9; }
        
        .modal-body {
          display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 30px; padding: 30px;
        }
        @media (max-width: 768px) { .modal-body { grid-template-columns: 1fr; } }
        
        .section-box {
          background: #1e293b; border: 1px solid #334155; padding: 20px; border-radius: 12px;
          margin-bottom: 20px;
        }
        .section-title {
          margin-top: 0; color: #60a5fa; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;
          border-bottom: 1px solid #334155; padding-bottom: 12px; margin-bottom: 16px;
        }
        .section-help { font-size: 0.85rem; color: #94a3b8; margin-bottom: 15px; display: block; }
        
        .input-row {
          display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;
        }
        .input-row label { font-weight: 600; color: #cbd5e1; font-size: 1.1rem; }
        .input-row input {
          background: #020617; border: 1px solid #475569; color: #60a5fa;
          padding: 10px 12px; border-radius: 8px; width: 100px; text-align: right;
          font-size: 1.1rem; font-family: monospace; outline: none; transition: 0.2s;
        }
        .input-row input:focus { border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2); }
        
        .summary-box {
          position: sticky; top: 30px; background: #0f172a; border: 2px solid #1e293b;
          padding: 24px; border-radius: 16px;
        }
        .summary-row {
          display: flex; justify-content: space-between; margin-bottom: 16px; font-size: 1.1rem;
        }
        .val-fondo { color: #94a3b8; }
        .val-fisico { color: #60a5fa; font-weight: bold; font-size: 1.2rem; }
        
        .result-box {
          margin-top: 24px; padding: 16px; border-radius: 12px; text-align: center;
        }
        .result-faltante { background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #f87171; }
        .result-sobrante { background: rgba(245, 158, 11, 0.1); border: 1px solid #f59e0b; color: #fbbf24; }
        .result-cuadre { background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; color: #34d399; }
        
        .btn-save {
          width: 100%; background: #2563eb; color: white; border: none; padding: 16px;
          border-radius: 10px; font-size: 1.1rem; font-weight: bold; cursor: pointer;
          display: flex; justify-content: center; align-items: center; gap: 10px;
          margin-top: 24px; transition: 0.3s;
        }
        .btn-save:hover { background: #1d4ed8; transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3); }
      `}</style>

      <div className="modal-overlay">
        <div className="modal-content">
          
          <div className="modal-header">
            <div>
              <h2><Calculator /> Arqueo de Caja</h2>
              <p>Valida el efectivo físico al cierre del turno.</p>
            </div>
            <button className="btn-close" onClick={onClose}><X size={28} /></button>
          </div>

          <div className="modal-body">
            
            {/* --- ZONA DE CAPTURA --- */}
            <div className="capture-zone">
              
              {/* NUEVO CAMPO: FONDO FIJO */}
              <div className="section-box" style={{borderColor: '#3b82f6', background: 'rgba(59, 130, 246, 0.05)'}}>
                <h3 className="section-title" style={{borderBottomColor: '#3b82f6'}}><Wallet /> 1. Fondo Fijo Inicial</h3>
                <span className="section-help">Ingresa con cuánto dinero en efectivo inició la caja este turno.</span>
                <div className="input-row">
                  <label>Monto Base:</label>
                  <input 
                    type="number" min="0" placeholder="0.00"
                    onChange={(e) => setFondoFijo(e.target.value === '' ? 0 : parseFloat(e.target.value))}
                    style={{width: '140px', borderColor: '#3b82f6'}}
                  />
                </div>
              </div>

              <div className="section-box">
                <h3 className="section-title"><DollarSign /> 2. Billetes</h3>
                <span className="section-help">Ingresa la <b>cantidad</b> de billetes (ej. si tienes 3 billetes de $500, escribe "3").</span>
                
                {Object.keys(denominaciones.billetes).map(key => (
                  <div key={key} className="input-row">
                    <label>${key.replace('b', '')}</label>
                    <input 
                      type="number" min="0" placeholder="0"
                      onChange={(e) => handleInputChange('billetes', key, e.target.value)}
                    />
                  </div>
                ))}
              </div>

              <div className="section-box">
                <h3 className="section-title"><Coins /> 3. Monedas</h3>
                <span className="section-help">Ingresa la <b>cantidad</b> de monedas contadas.</span>
                
                {Object.keys(denominaciones.monedas).map(key => (
                  <div key={key} className="input-row">
                    <label>${key === 'm050' ? '0.50' : key.replace('m', '')}</label>
                    <input 
                      type="number" min="0" placeholder="0"
                      onChange={(e) => handleInputChange('monedas', key, e.target.value)}
                    />
                  </div>
                ))}
              </div>
            </div>

            {/* --- ZONA DE RESUMEN --- */}
            <div>
              <div className="summary-box">
                <h3 className="section-title" style={{color: 'white'}}>4. Resumen y Cuadre</h3>
                <span className="section-help">El sistema calculará automáticamente las diferencias contra el fondo fijo de la caja.</span>
                
                <div style={{marginTop: '25px'}}>
                  <div className="summary-row val-fondo">
                    <span>Fondo Fijo (Base):</span>
                    <span style={{fontFamily: 'monospace'}}>${fondoFijo.toFixed(2)}</span>
                  </div>
                  
                  <div className="summary-row val-fisico">
                    <span>Efectivo Contado:</span>
                    <span style={{fontFamily: 'monospace'}}>${totales.fisico.toFixed(2)}</span>
                  </div>
                </div>

                <div className={`result-box ${
                  fondoFijo === 0 && totales.fisico === 0 ? 'result-cuadre' :
                  totales.diferencia < 0 ? 'result-faltante' : 
                  totales.diferencia > 0 ? 'result-sobrante' : 
                  'result-cuadre'
                }`}>
                  <div style={{fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '5px'}}>
                    {fondoFijo === 0 && totales.fisico === 0 ? '✅ Esperando datos...' :
                     totales.diferencia < 0 ? '⚠️ Faltante en Caja' : 
                     totales.diferencia > 0 ? '⚠️ Sobrante en Caja' : 
                     '✅ Cuadre Perfecto'}
                  </div>
                  <div style={{fontSize: '2rem', fontWeight: 'bold', fontFamily: 'monospace'}}>
                    ${Math.abs(totales.diferencia).toFixed(2)}
                  </div>
                </div>

                <button className="btn-save" onClick={guardarArqueo}>
                  <Save /> Registrar Arqueo Definitivo
                </button>
              </div>
            </div>

          </div>
        </div>
      </div>
    </>
  );
};

export default ArqueoCaja;