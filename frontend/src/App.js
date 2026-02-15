import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState({ activos: [], pasivos: [] });
  const [balanceKey, setBalanceKey] = useState('bgi');
  const [asientos, setAsientos] = useState([]);
  const [nuevoAsiento, setNuevoAsiento] = useState({ cuenta: '', tipo: 'cargo', monto: '' });

  useEffect(() => {
    if (balanceKey !== 'catalogo') {
      axios.post(`http://localhost:5000/api/balance/${balanceKey}`, { asientos })
        .then(res => setData(res.data))
        .catch(err => console.error("Error:", err));
    } else {
      axios.get(`http://localhost:5000/api/balance/catalogo`)
        .then(res => setData(res.data))
        .catch(err => console.error(err));
    }
  }, [balanceKey, asientos]);

  const formatoMoneda = (val) => new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(val);
  const sumar = (lista) => (lista || []).reduce((acc, item) => acc + item.valor, 0);

  const agregarAsiento = () => {
    if (!nuevoAsiento.cuenta || !nuevoAsiento.monto) return;
    setAsientos([...asientos, { ...nuevoAsiento, id: Date.now() }]);
    setNuevoAsiento({ cuenta: '', tipo: 'cargo', monto: '' });
  };

  const totalActivo = sumar(data.activos);
  const totalPasivoCap = sumar(data.pasivos);
  const diferencia = Math.abs(totalActivo - totalPasivoCap);
  const estaCuadrado = diferencia < 0.01;

  return (
    <div className="dashboard">
      <header className="main-header">
        <div>
          <h1>GanBo, S.A.S.</h1>
          <span className="subtitle">Gestión Financiera de Ingeniería</span>
        </div>
        
        <div className="header-actions">
          <div className="selector-container">
            <select value={balanceKey} onChange={(e) => {setBalanceKey(e.target.value); setAsientos([]);}}>
              <option value="catalogo">1. Catálogo de Cuentas</option>
              <option value="bgi">2. Balance Inicial (BGI)</option>
              <option value="bgce">3. Compra Efectivo (BGCE)</option>
              <option value="bgcc">4. Compra a Crédito (BGCC)</option>
              <option value="bgec">5. Compra Mixta (BGEC)</option>
              <option value="bgac">6. Anticipo de Clientes (BGAC)</option>
            </select>
          </div>
        </div>
      </header>

      {!estaCuadrado && !data.es_catalogo && (
        <div className="alert-error" style={{ background: '#ffebee', color: '#c62828', padding: '10px', textAlign: 'center', fontWeight: 'bold', borderBottom: '2px solid #c62828' }}>
          ⚠️ BALANCE DESCUADRADO: Diferencia de {formatoMoneda(diferencia)}
        </div>
      )}

      <div className="layout-container">
        {!data.es_catalogo && (
          <aside className="sidebar-captura">
            <h3 style={{color: '#1a237e', marginBottom: '15px'}}>➕ Registro de Movimientos</h3>
            <input 
              className="input-contable" 
              placeholder="Nombre de Cuenta" 
              style={{width: '100%', marginBottom: '10px', padding: '10px', boxSizing: 'border-box'}}
              value={nuevoAsiento.cuenta} 
              onChange={e => setNuevoAsiento({...nuevoAsiento, cuenta: e.target.value})} 
            />
            <select 
              style={{width: '100%', marginBottom: '10px', padding: '10px'}}
              value={nuevoAsiento.tipo} 
              onChange={e => setNuevoAsiento({...nuevoAsiento, tipo: e.target.value})}
            >
              <option value="cargo">Debe (Cargo)</option>
              <option value="abono">Haber (Abono)</option>
            </select>
            <input 
              type="number" 
              placeholder="Monto $" 
              style={{width: '100%', marginBottom: '10px', padding: '10px', boxSizing: 'border-box'}}
              value={nuevoAsiento.monto} 
              onChange={e => setNuevoAsiento({...nuevoAsiento, monto: e.target.value})} 
            />
            <button className="btn-registrar" onClick={agregarAsiento}>Registrar Asiento</button>
            <button onClick={() => setAsientos([])} style={{ marginTop: '10px', width: '100%', background: '#757575', color: 'white', border: 'none', padding: '8px', borderRadius: '4px', cursor: 'pointer' }}>
              Limpiar Ajustes
            </button>
            <div style={{marginTop: '20px', borderTop: '1px solid #eee', paddingTop: '10px'}}>
              <strong style={{fontSize: '0.8rem'}}>Historial:</strong>
              {asientos.map(a => (
                <div key={a.id} className="asiento-card">
                  {a.cuenta}: {a.tipo === 'cargo' ? '+' : '-'}{formatoMoneda(a.monto)}
                </div>
              ))}
            </div>
          </aside>
        )}

        <main style={{flex: 1}}>
          {data.es_catalogo ? (
             <div className="card"><h2 className="section-title">Catálogo Oficial</h2><table className="balance-table"><tbody>{data.lista.map((c, i) => <tr key={i}><td>{c.codigo}</td><td>{c.nombre}</td></tr>)}</tbody></table></div>
          ) : (
            <div className="grid">
              <div className="card">
                <h2 className="section-title">ACTIVOS</h2>
                <table className="balance-table">
                  <tbody>
                    {data.activos?.map((a, i) => (
                      <tr key={i}><td>{a.nombre}</td><td className="monto positive">{formatoMoneda(a.valor)}</td></tr>
                    ))}
                    <tr className="total-row"><td>TOTAL ACTIVO</td><td>{formatoMoneda(totalActivo)}</td></tr>
                  </tbody>
                </table>
              </div>
              <div className="card">
                <h2 className="section-title">PASIVO Y CAPITAL</h2>
                <table className="balance-table">
                  <tbody>
                    {data.pasivos?.map((p, i) => (
                      <tr key={i}><td>{p.nombre}</td><td className="monto negative">{formatoMoneda(p.valor)}</td></tr>
                    ))}
                    <tr className="total-row"><td>TOTAL PASIVO + CAP</td><td>{formatoMoneda(totalPasivoCap)}</td></tr>
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </main>
      </div>

      <footer className="footer-signatures">
        <div className="signature-block"><div className="signature-line"></div><p>Autorizado: Lic. Gonzáles Zúñiga Nuria</p></div>
        <div className="signature-block"><div className="signature-line"></div><p>Elaborado: Ing. Salinas Caballero Emmanuel</p></div>
      </footer>
    </div>
  );
}

export default App;