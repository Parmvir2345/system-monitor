# System Monitor Dashboard

A full-stack system monitoring tool that displays real-time CPU, memory, disk, and network metrics from a Linux/Mac machine.

## Tech Stack

- **Backend:** Python, Flask, psutil
- **Frontend:** React, Chart.js
- **DevOps:** GitHub Actions, CI/CD pipeline

## Features

- Real-time CPU, memory, disk and network monitoring
- Auto-refreshes every 3 seconds
- REST API built with Flask
- Automated tests with pytest
- CI/CD pipeline with GitHub Actions

## Project Structure
## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python3 app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

Open http://localhost:3000 in your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/metrics | Returns current system metrics as JSON |

## What I Learned

- Building REST APIs with Flask
- Reading system metrics using psutil
- React hooks (useState, useEffect) for live data fetching
- Writing unit tests with pytest
- Setting up CI/CD pipelines with GitHub Actions
