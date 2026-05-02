import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import ArqueoCaja from './components/ArqueoCaja'; 

function App() {
  const [data, setData] = useState({ activos: [], pasivos: [] });
  const [balanceKey, setBalanceKey] = useState('bgi');
  const [isBotOpen, setIsBotOpen] = useState(false);
  
  // === ESTADO PARA EL NUEVO MODAL DE ARQUEO ===
  const [isArqueoOpen, setIsArqueoOpen] = useState(false);

  const [asientos, setAsientos] = useState([]);
  const [nuevoAsiento, setNuevoAsiento] = useState({ cuenta: '', tipo: 'cargo', monto: '' });

  const [asientosDiario, setAsientosDiario] = useState([]);
  const [nuevoDiario, setNuevoDiario] = useState({
    fecha: '', concepto: '',
    movimientos: [{ cuenta: '', debe: '', haber: '' }, { cuenta: '', debe: '', haber: '' }]
  });

  useEffect(() => {
    axios.post(`http://localhost:5000/api/balance/${balanceKey}`, { asientos })
      .then(res => setData(res.data))
      .catch(err => console.error("Error:", err));
  }, [balanceKey, asientos]);

  const formatoMoneda = (val) => val === "" || val === null || val === undefined ? "" : new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(val);
  const sumar = (lista) => (lista || []).reduce((acc, item) => acc + item.valor, 0);

  const agregarAsiento = () => {
    if (!nuevoAsiento.cuenta || !nuevoAsiento.monto) return;
    setAsientos([...asientos, { ...nuevoAsiento, id: Date.now() }]);
    setNuevoAsiento({ cuenta: '', tipo: 'cargo', monto: '' });
  };

  const agregarFilaDiario = () => {
    setNuevoDiario({ ...nuevoDiario, movimientos: [...nuevoDiario.movimientos, { cuenta: '', debe: '', haber: '' }] });
  };

  const actualizarFilaDiario = (index, field, value) => {
    const nuevosMovs = [...nuevoDiario.movimientos];
    nuevosMovs[index][field] = value;
    if (field === 'debe' && value !== '') nuevosMovs[index]['haber'] = '';
    if (field === 'haber' && value !== '') nuevosMovs[index]['debe'] = '';
    setNuevoDiario({ ...nuevoDiario, movimientos: nuevosMovs });
  };

  const totalDebe = nuevoDiario.movimientos.reduce((acc, mov) => acc + Number(mov.debe || 0), 0);
  const totalHaber = nuevoDiario.movimientos.reduce((acc, mov) => acc + Number(mov.haber || 0), 0);
  const cuadraDiario = totalDebe === totalHaber && totalDebe > 0;

  const registrarAsientoDiario = () => {
    if (!cuadraDiario || !nuevoDiario.fecha || !nuevoDiario.concepto) return;
    const movsLimpios = nuevoDiario.movimientos.filter(m => m.cuenta.trim() !== '' && (m.debe !== '' || m.haber !== ''));
    
    setAsientosDiario([...asientosDiario, { fecha: nuevoDiario.fecha, concepto: nuevoDiario.concepto, movimientos: movsLimpios }]);
    setNuevoDiario({ fecha: '', concepto: '', movimientos: [{ cuenta: '', debe: '', haber: '' }, { cuenta: '', debe: '', haber: '' }] });
  };

  const totalActivo = sumar(data.activos);
  const totalPasivoCap = sumar(data.pasivos);
  const todosLosAsientosLD = [...(data.asientos || []), ...asientosDiario];

  const obtenerCuentasMayorCalculadas = () => {
    const cuentasMap = {};
    (data.cuentas || []).forEach(c => {
      cuentasMap[c.nombre.toLowerCase()] = {
        nombre: c.nombre,
        cargos: [...c.cargos], abonos: [...c.abonos],
        md: c.md, ma: c.ma, sd: c.sd, sa: c.sa
      };
    });

    asientosDiario.forEach((asiento, index) => {
      const refActual = `N-${index + 1})`; 
      
      asiento.movimientos.forEach(mov => {
        const nombreClave = mov.cuenta.toLowerCase().trim();
        if (!cuentasMap[nombreClave]) {
          cuentasMap[nombreClave] = { nombre: mov.cuenta.trim(), cargos: [], abonos: [], md: 0, ma: 0, sd: 0, sa: 0 };
        }
        const cuentaObj = cuentasMap[nombreClave];

        if (mov.debe !== '') {
          const monto = Number(mov.debe);
          cuentaObj.cargos.push({ ref: refActual, monto: monto });
          cuentaObj.md += monto;
        }
        if (mov.haber !== '') {
          const monto = Number(mov.haber);
          cuentaObj.abonos.push({ ref: refActual, monto: monto });
          cuentaObj.ma += monto;
        }
      });
    });

    return Object.values(cuentasMap).map(c => {
      let sd = 0;
      let sa = 0;
      if (c.md > c.ma) sd = c.md - c.ma;
      if (c.ma > c.md) sa = c.ma - c.md;
      return { ...c, sd, sa };
    });
  };

  const cuentasMayorDinamicas = obtenerCuentasMayorCalculadas();

  return (
    <div className="dashboard relative">
      
      {/* RENDERIZADO DEL MODAL (Condicionado y flotante) */}
      {isArqueoOpen && <ArqueoCaja onClose={() => setIsArqueoOpen(false)} />}

      <header className="main-header">
        <div>
          <h1>GanBo, S.A.S.</h1>
          <span className="subtitle">Gestión Financiera de Ingeniería</span>
        </div>
        
        <div className="header-actions" style={{display: 'flex', gap: '15px', alignItems: 'center'}}>
          
          {/* === BOTÓN PARA ABRIR EL ARQUEO === */}
          <button 
            onClick={() => setIsArqueoOpen(true)}
            style={{
              background: '#2563eb', color: 'white', padding: '10px 16px', borderRadius: '8px', 
              border: 'none', cursor: 'pointer', fontWeight: 'bold', fontSize: '0.95em',
              boxShadow: '0 4px 6px -1px rgba(37, 99, 235, 0.2)'
            }}
          >
            💰 Corte de Caja
          </button>

          <div className="selector-container">
            <select value={balanceKey} onChange={(e) => {setBalanceKey(e.target.value); setAsientos([]);}}>
              <option value="catalogo">1. Catálogo de Cuentas</option>
              <option value="bgi">2. Balance Inicial (BGI)</option>
              <option value="bgce">3. Compra Efectivo (BGCE)</option>
              <option value="bgcc">4. Compra a Crédito (BGCC)</option>
              <option value="bgec">5. Compra Mixta (BGEC)</option>
              <option value="bgac">6. Anticipo de Clientes (BGAC)</option>
              <option value="ld">7. Libro Diario (LD)</option>
              <option value="lm">8. Libro Mayor (Cuentas T)</option>
              <option value="bca">9. Balanza de Comprobación (BCA)</option>
              <option value="er">10. Estado de Resultados (ER)</option>
              <option value="ef">11. Estado de Sit. Financiera (EF)</option>
            </select>
          </div>
        </div>
      </header>

      {/* REVERTIDO A TU ESTRUCTURA ORIGINAL SIN CLASES DE TAILWIND */}
      <div className="layout-container">
        
        {(!data.es_catalogo && !data.es_bca && !data.es_er && !data.es_ef && !data.es_ld && !data.es_lm) && (
          <aside className="sidebar-captura">
            <h3 style={{color: '#1a237e', marginBottom: '15px'}}>➕ Registro Rápido</h3>
            <input className="input-contable" placeholder="Nombre de Cuenta" style={{width: '100%', marginBottom: '10px', padding: '10px'}} value={nuevoAsiento.cuenta} onChange={e => setNuevoAsiento({...nuevoAsiento, cuenta: e.target.value})} />
            <select style={{width: '100%', marginBottom: '10px', padding: '10px'}} value={nuevoAsiento.tipo} onChange={e => setNuevoAsiento({...nuevoAsiento, tipo: e.target.value})}>
              <option value="cargo">Debe (Cargo)</option>
              <option value="abono">Haber (Abono)</option>
            </select>
            <input type="number" placeholder="Monto $" style={{width: '90%', marginBottom: '10px', padding: '10px'}} value={nuevoAsiento.monto} onChange={e => setNuevoAsiento({...nuevoAsiento, monto: e.target.value})} />
            <button className="btn-registrar" onClick={agregarAsiento}>Registrar</button>
            <button onClick={() => setAsientos([])} style={{ marginTop: '10px', width: '100%', background: '#757575', color: 'white', border: 'none', padding: '8px', cursor: 'pointer' }}>Limpiar Ajustes</button>
          </aside>
        )}

        {(data.es_ld || data.es_lm) && (
          <aside className="sidebar-captura" style={{minWidth: '320px'}}>
            <h3 style={{color: '#1a237e', marginBottom: '15px'}}>📝 Nuevo Asiento Diario</h3>
            <p style={{fontSize: '0.85em', color: '#666', marginBottom: '15px'}}>Los asientos se reflejarán automáticamente en el Diario y en las Cuentas T.</p>
            <input type="date" style={{width: '100%', marginBottom: '10px', padding: '8px'}} value={nuevoDiario.fecha} onChange={e => setNuevoDiario({...nuevoDiario, fecha: e.target.value})} />
            <input type="text" placeholder="Concepto (Ej. Pago de luz)" style={{width: '100%', marginBottom: '15px', padding: '8px'}} value={nuevoDiario.concepto} onChange={e => setNuevoDiario({...nuevoDiario, concepto: e.target.value})} />
            
            {nuevoDiario.movimientos.map((mov, index) => (
              <div key={index} style={{background: '#f5f5f5', padding: '10px', marginBottom: '10px', borderRadius: '4px', border: '1px solid #e0e0e0'}}>
                <input type="text" placeholder="Cuenta (Sensible a mayúsculas)" style={{width: '100%', marginBottom: '5px', padding: '6px'}} value={mov.cuenta} onChange={e => actualizarFilaDiario(index, 'cuenta', e.target.value)} />
                <div style={{display: 'flex', gap: '5px'}}>
                  <input type="number" placeholder="Debe $" style={{width: '50%', padding: '6px'}} value={mov.debe} disabled={mov.haber !== ''} onChange={e => actualizarFilaDiario(index, 'debe', e.target.value)} />
                  <input type="number" placeholder="Haber $" style={{width: '50%', padding: '6px'}} value={mov.haber} disabled={mov.debe !== ''} onChange={e => actualizarFilaDiario(index, 'haber', e.target.value)} />
                </div>
              </div>
            ))}
            
            <button onClick={agregarFilaDiario} style={{width: '100%', padding: '6px', background: '#e0e0e0', border: 'none', borderRadius: '4px', cursor: 'pointer', marginBottom: '15px'}}>+ Agregar cuenta</button>
            
            <div style={{display: 'flex', justifyContent: 'space-between', fontWeight: 'bold', fontSize: '0.9em', color: cuadraDiario ? '#2e7d32' : '#c62828', marginBottom: '15px'}}>
              <span>Totales:</span>
              <span>{formatoMoneda(totalDebe)} | {formatoMoneda(totalHaber)}</span>
            </div>

            <button className="btn-registrar" onClick={registrarAsientoDiario} disabled={!cuadraDiario || !nuevoDiario.fecha || !nuevoDiario.concepto} style={{ opacity: (!cuadraDiario || !nuevoDiario.fecha || !nuevoDiario.concepto) ? 0.5 : 1 }}>Guardar Asiento</button>
            <button onClick={() => setAsientosDiario([])} style={{ marginTop: '10px', width: '100%', background: '#757575', color: 'white', border: 'none', padding: '8px', cursor: 'pointer' }}>Limpiar Nuevos Asientos</button>
          </aside>
        )}

        <main style={{flex: 1}}>
          {data.es_catalogo && (
            <div className="card"><h2 className="section-title">Catálogo Oficial</h2><table className="balance-table"><tbody>{data.lista.map((c, i) => <tr key={i}><td>{c.codigo}</td><td>{c.nombre}</td></tr>)}</tbody></table></div>
          )}

          {data.es_bca && (
            <div className="card"><h2 className="section-title">{data.titulo}</h2><table className="balance-table"><thead><tr><th>Cuenta</th><th>Debe</th><th>Haber</th><th>Deudor</th><th>Acreedor</th></tr></thead><tbody>{data.lista.map((c, i) => (<tr key={i}><td>{c.cuenta}</td><td>{formatoMoneda(c.debe)}</td><td>{formatoMoneda(c.haber)}</td><td>{formatoMoneda(c.deudor)}</td><td>{formatoMoneda(c.acreedor)}</td></tr>))}</tbody></table></div>
          )}

          {data.es_er && (
            <div className="card">
              <h2 className="section-title">{data.titulo}</h2>
              <table className="balance-table">
                <thead>
                  <tr>
                    <th>Cuenta / Concepto</th>
                    <th style={{textAlign: 'right'}}>Columna 1</th>
                    <th style={{textAlign: 'right'}}>Columna 2</th>
                    <th style={{textAlign: 'right'}}>Columna 3</th>
                    <th style={{textAlign: 'right'}}>Columna 4</th>
                  </tr>
                </thead>
                <tbody>
                  {data.resultados.map((c, i) => (
                    <tr key={i}>
                      <td style={{paddingLeft: '10px'}}>{c.concepto}</td>
                      <td className="monto">{formatoMoneda(c.c1)}</td>
                      <td className="monto">{formatoMoneda(c.c2)}</td>
                      <td className="monto">{formatoMoneda(c.c3)}</td>
                      <td className="monto"><strong>{formatoMoneda(c.c4)}</strong></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {data.es_ef && (
            <div className="card"><h2 className="section-title">{data.titulo}</h2><table className="balance-table"><thead><tr><th>Cuenta / Concepto</th><th style={{textAlign: 'right'}}>Columna 1</th><th style={{textAlign: 'right'}}>Columna 2</th><th style={{textAlign: 'right'}}>Columna 3</th></tr></thead><tbody>{data.secciones.map((sec, i) => (<React.Fragment key={i}>{sec.nombre && (<tr style={{background: '#f5f5f5'}}><td colSpan="4"><strong>{sec.nombre}</strong></td></tr>)}{sec.cuentas?.map((c, j) => (<tr key={j}><td style={{paddingLeft: '20px'}}>{c.n}</td><td className="monto">{formatoMoneda(c.c1)}</td><td className="monto">{formatoMoneda(c.c2)}</td><td className="monto"><strong>{formatoMoneda(c.c3)}</strong></td></tr>))}{sec.is_total && (<tr className="total-row"><td colSpan="3"><strong>{sec.n}</strong></td><td className="monto"><strong>{formatoMoneda(sec.c3)}</strong></td></tr>)}</React.Fragment>))}</tbody></table></div>
          )}

          {data.es_ld && (
            <div className="card">
              <h2 className="section-title">{data.titulo}</h2>
              <table className="balance-table">
                <thead><tr><th>Fecha</th><th>Cuenta y Concepto</th><th style={{textAlign: 'right'}}>Debe</th><th style={{textAlign: 'right'}}>Haber</th></tr></thead>
                <tbody>
                  {todosLosAsientosLD.map((asiento, i) => (
                    <React.Fragment key={i}>
                      {asiento.movimientos.map((mov, j) => (
                        <tr key={`${i}-${j}`}>
                          <td style={{width: '120px'}}>{j === 0 ? asiento.fecha : ''}</td>
                          <td style={{paddingLeft: mov.haber !== "" ? '40px' : '10px'}}>{mov.cuenta}</td>
                          <td className="monto">{formatoMoneda(mov.debe)}</td>
                          <td className="monto">{formatoMoneda(mov.haber)}</td>
                        </tr>
                      ))}
                      <tr style={{background: '#f8f9fa'}}><td colSpan="4" style={{textAlign: 'center', fontStyle: 'italic', color: '#555', padding: '8px'}}>{asiento.concepto}</td></tr>
                    </React.Fragment>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {data.es_lm && (
            <div className="card">
              <h2 className="section-title">{data.titulo}</h2>
              <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '20px', marginTop: '20px'}}>
                {cuentasMayorDinamicas.map((cuenta, i) => (
                  <div key={i} style={{border: '1px solid #ccc', borderRadius: '6px', overflow: 'hidden', backgroundColor: 'white', boxShadow: '0 2px 4px rgba(0,0,0,0.05)'}}>
                    <div style={{textAlign: 'center', fontWeight: 'bold', padding: '8px', borderBottom: '2px solid #2c3e50', backgroundColor: '#e8eaf6', color: '#1a237e'}}>
                      {cuenta.nombre}
                    </div>
                    <div style={{display: 'flex', minHeight: '100px'}}>
                      <div style={{flex: 1, borderRight: '2px solid #2c3e50', padding: '10px'}}>
                        {cuenta.cargos.map((c, j) => <div key={j} style={{display: 'flex', justifyContent: 'space-between', marginBottom: '4px'}}><span style={{color: '#666', fontSize: '0.9em'}}>{c.ref}</span><span>{formatoMoneda(c.monto)}</span></div>)}
                      </div>
                      <div style={{flex: 1, padding: '10px'}}>
                        {cuenta.abonos.map((a, j) => <div key={j} style={{display: 'flex', justifyContent: 'space-between', marginBottom: '4px'}}><span style={{color: '#666', fontSize: '0.9em'}}>{a.ref}</span><span>{formatoMoneda(a.monto)}</span></div>)}
                      </div>
                    </div>
                    <div style={{display: 'flex', borderTop: '1px solid #ccc', backgroundColor: '#f5f5f5', fontSize: '0.9em', padding: '8px'}}>
                      <div style={{flex: 1, textAlign: 'right', paddingRight: '10px', borderRight: '2px solid #2c3e50'}}>MD: {formatoMoneda(cuenta.md)}</div>
                      <div style={{flex: 1, textAlign: 'right', paddingRight: '10px'}}>MA: {formatoMoneda(cuenta.ma)}</div>
                    </div>
                    <div style={{display: 'flex', backgroundColor: '#e3f2fd', fontSize: '0.9em', padding: '8px', fontWeight: 'bold'}}>
                      <div style={{flex: 1, textAlign: 'right', paddingRight: '10px', borderRight: '2px solid #2c3e50', color: '#2e7d32'}}>{cuenta.sd > 0 ? `SD: ${formatoMoneda(cuenta.sd)}` : ''}</div>
                      <div style={{flex: 1, textAlign: 'right', paddingRight: '10px', color: '#c62828'}}>{cuenta.sa > 0 ? `SA: ${formatoMoneda(cuenta.sa)}` : ''}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {(!data.es_catalogo && !data.es_bca && !data.es_er && !data.es_ef && !data.es_ld && !data.es_lm) && (
            <div className="grid">
              <div className="card"><h2 className="section-title">ACTIVOS</h2><table className="balance-table"><tbody>{data.activos?.map((a, i) => <tr key={i}><td>{a.nombre}</td><td className="monto positive">{formatoMoneda(a.valor)}</td></tr>)}<tr className="total-row"><td>TOTAL ACTIVO</td><td>{formatoMoneda(totalActivo)}</td></tr></tbody></table></div>
              <div className="card"><h2 className="section-title">PASIVO Y CAPITAL</h2><table className="balance-table"><tbody>{data.pasivos?.map((p, i) => <tr key={i}><td>{p.nombre}</td><td className="monto negative">{formatoMoneda(p.valor)}</td></tr>)}<tr className="total-row"><td>TOTAL PASIVO + CAP</td><td>{formatoMoneda(totalPasivoCap)}</td></tr></tbody></table></div>
            </div>
          )}
        </main>
      </div>

      <footer className="footer-signatures">
        <div className="signature-block"><div className="signature-line"></div><p>Autorizado: Lic. Gonzáles Zúñiga Nuria</p></div>
        <div className="signature-block"><div className="signature-line"></div><p>Elaborado: Ing. Salinas Caballero Emmanuel</p></div>
      </footer>

      {/* --- BOTÓN FLOTANTE DEL CHATBOT --- */}
      <button className="chatbot-toggle" onClick={() => setIsBotOpen(!isBotOpen)}>
        {isBotOpen ? '✖' : '💬'}
      </button>

      {/* --- WIDGET DEL CHATBOT --- */}
      <div className={`chatbot-widget ${isBotOpen ? 'open' : 'closed'}`}>
        <div className="chatbot-header">Asistente NIF</div>
        <iframe title="Chatbot Contable" allow="microphone" className="chatbot-iframe" src="https://console.dialogflow.com/api-client/demo/embedded/5b6fa7bc-3b66-4d28-b2a4-bf307bd273a0"></iframe>
      </div>

    </div>
  );
}

export default App;