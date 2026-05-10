function MetricCard({ label, value, unit, subtitle, color }) {
  return (
    <div className={`card card-${color}`}>
      <p className="card-label">{label}</p>
      <p className="card-value">
        {value}<span className="card-unit">{unit}</span>
      </p>
      {subtitle && <p className="card-subtitle">{subtitle}</p>}
    </div>
  );
}

export default MetricCard;
