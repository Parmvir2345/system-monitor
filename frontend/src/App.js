import { useState, useEffect } from 'react';
import MetricCard from './MetricCard';
import './App.css';

function App() {
  // useState stores the data from our API
  const [data, setData] = useState(null);
  // this tracks if we are connected to the backend
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5003/api/metrics');
        const json = await response.json();
        setData(json);
        setConnected(true);
      } catch (error) {
        // if Flask is not running, show disconnected
        setConnected(false);
      }
    };

    fetchData();
    // fetch new data every 3 seconds
    const interval = setInterval(fetchData, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard">
      <div className="header">
        <h1>System Monitor</h1>
        <span className={connected ? 'badge-online' : 'badge-offline'}>
          {connected ? 'Live' : 'Disconnected'}
        </span>
      </div>

      {!data ? (
        <p className="loading">Connecting to backend...</p>
      ) : (
        <>
          <div className="grid">
            <MetricCard
              label="CPU Usage"
              value={data.cpu_percent}
              unit="%"
              color={data.cpu_percent > 80 ? 'red' : data.cpu_percent > 60 ? 'amber' : 'green'}
            />
            <MetricCard
              label="Memory Used"
              value={data.memory_used_gb}
              unit="GB"
              subtitle={`${data.disk_free_gb} GB free`}
              color={data.memory_percent > 80 ? 'red' : 'green'}
            />
            <MetricCard
              label="Disk Used"
              value={data.disk_percent}
              unit="%"
              subtitle={`${data.disk_used_gb} GB of ${data.disk_total_gb} GB`}
              color={data.disk_percent > 80 ? 'red' : 'green'}
            />
            <MetricCard
              label="Data Sent"
              value={(data.net_bytes_sent / (1024 ** 3)).toFixed(2)}
              unit="GB"
              color="blue"
            />
          </div>
        </>
      )}
    </div>
  );
}

export default App;
