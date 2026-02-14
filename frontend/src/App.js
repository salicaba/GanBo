import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState({ activos: [], pasivos: [] });
  const [balanceKey, setBalanceKey] = useState('catalogo');
  // Estado para controlar si mostramos la factura o no
  const [mostrarFactura, setMostrarFactura] = useState(false);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/balance/${balanceKey}`)
      .then(res => setData(res.data))
      .catch(err => console.error("Error:", err));
  }, [balanceKey]);

  const formatoMoneda = (val) => new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(val);
  const sumar = (lista) => (lista || []).reduce((acc, item) => acc + item.valor, 0);

  return (
    <div className="dashboard">
      <header className="main-header">
        <div>
          <h1>GanBo, S.A.S.</h1>
          <span className="subtitle">Sistema de Control Financiero</span>
        </div>
        
        <div className="header-actions">
          {/* BOTÓN DE FACTURA (Solo aparece si el balance trae datos de factura) */}
          {data.factura && (
            <button className="btn-factura" onClick={() => setMostrarFactura(true)}>
              📄 Ver Factura
            </button>
          )}

          <div className="selector-container">
            <select value={balanceKey} onChange={(e) => setBalanceKey(e.target.value)}>
              <option value="catalogo">1. Catálogo de Cuentas</option>
              <option value="bgi">2. Balance General Inicial (BGI)</option>
              <option value="bgce">3. Balance General Compra Efectivo (BGCE)</option>
              <option value="bgcc">4. Balance General Compra a Crédito</option>
              <option value="bgec">5. Balance General Compra Efectivo - Crédito</option>
              <option value="bgac">6. Balance General con Anticipo de Clientes</option>
            </select>
          </div>
        </div>
      </header>

      {/* --- MODAL DE FACTURA --- */}
      {mostrarFactura && data.factura && (
        <div className="modal-overlay" onClick={() => setMostrarFactura(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="close-button" onClick={() => setMostrarFactura(false)}>×</button>
            
            <div className="factura-header">
              <h2>{data.factura.titulo}</h2>
              <p>{data.factura.concepto}</p>
            </div>
            
            <div className="factura-body">
              <div className="factura-row">
                <span>Subtotal:</span>
                <span>{formatoMoneda(data.factura.subtotal)}</span>
              </div>
              <div className="factura-row">
                <span>IVA (16%):</span>
                <span>{formatoMoneda(data.factura.iva)}</span>
              </div>
              <div className="factura-row total">
                <span>TOTAL:</span>
                <span>{formatoMoneda(data.factura.total)}</span>
              </div>

              {data.factura.notas && (
                <div className="factura-notas">
                  <strong>Notas:</strong>
                  <ul>
                    {data.factura.notas.map((nota, i) => <li key={i}>{nota}</li>)}
                  </ul>
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* RENDERIZADO PRINCIPAL (Tablas) */}
      {data.es_catalogo ? (
        <div className="grid" style={{ display: 'block' }}>
          <div className="card" style={{ maxWidth: '800px', margin: '0 auto' }}>
            <h2 className="section-title">Catálogo de Cuentas Oficial</h2>
            <div className="table-container">
              <table className="balance-table">
                <thead><tr><th>Código</th><th>Cuenta</th></tr></thead>
                <tbody>
                  {data.lista?.map((c, i) => (
                    <tr key={i}>
                      <td style={{ fontWeight: 'bold', color: '#1a237e' }}>{c.codigo}</td>
                      <td style={{ whiteSpace: 'pre-wrap' }}>{c.nombre}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      ) : (
        <div className="grid">
          <div className="card">
            <h2 className="section-title">ACTIVOS</h2>
            <div className="table-container">
              <table className="balance-table">
                <thead><tr><th>Cuenta</th><th style={{textAlign: 'right'}}>Importe</th></tr></thead>
                <tbody>
                  {data.activos?.map((a, i) => (
                    <tr key={i}>
                      <td>{a.nombre}</td>
                      <td className="monto positive">{formatoMoneda(a.valor)}</td>
                    </tr>
                  ))}
                  <tr className="total-row"><td>TOTAL ACTIVO</td><td>{formatoMoneda(sumar(data.activos))}</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div className="card">
            <h2 className="section-title">PASIVO Y CAPITAL</h2>
            <div className="table-container">
              <table className="balance-table">
                <thead><tr><th>Cuenta</th><th style={{textAlign: 'right'}}>Importe</th></tr></thead>
                <tbody>
                  {data.pasivos?.map((p, i) => (
                    <tr key={i}>
                      <td>{p.nombre}</td>
                      <td className="monto negative">{formatoMoneda(p.valor)}</td>
                    </tr>
                  ))}
                  <tr className="total-row"><td>TOTAL PASIVO + CAP</td><td>{formatoMoneda(sumar(data.pasivos))}</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      <footer className="footer-signatures">
        <div className="signature-block">
          <div className="signature-line"></div>
          <p className="role">Autorizado por:</p>
          <p className="name">Lic. Gonzáles Zúñiga Nuria</p>
        </div>
        <div className="signature-block">
          <div className="signature-line"></div>
          <p className="role">Elaborado por:</p>
          <p className="name">Ing. Salinas Caballero Emmanuel</p>
        </div>
      </footer>
    </div>
  );
}

export default App;