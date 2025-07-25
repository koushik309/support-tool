Health Monitor Simulation System
This Docker-based simulation replicates a real-world health monitoring system setup where:

sys1 runs a health check client

sys2 hosts a support tool server

Both systems connect through a simulated network

File Structure
text
health_monitor_simulation/
├── docker-compose.yml
├── scripts/
│   ├── server.py
│   └── health_check.py
└── README.md
System Components
1. Support Tool Server (sys2)
File: scripts/server.py

Flask-based REST API server

Exposes /health endpoint

Configurable via environment variables

2. Health Check Client (sys1)
File: scripts/health_check.py

Checks server status on sys2

Uses environment variables for configuration

Provides detailed logging

Returns ONLINE/OFFLINE status with exit codes

3. Docker Configuration
File: docker-compose.yml

Defines two services: sys1 and sys2

Sets up shared volume for scripts

Configures environment variables

Handles dependencies automatically



Operation Commands
1. Start the simulation
bash
docker-compose up --build -d
2. View server logs (sys2)
bash
docker logs sys2
3. View health check results (sys1)
bash
docker logs sys1
4. Run health check manually
bash
docker exec sys1 python /app/health_check.py5. Stop the server (simulate failure)
bash
docker-compose stop sys2
6. Restart the server
bash
docker-compose start sys2
7. Stop and clean up
bash
docker-compose down
Custom Configuration
Create .env file to override defaults:

ini
# .env
API_PORT=7000
APP_VERSION=2.5.0
CONNECTION_TIMEOUT=5.0
Start with custom configuration:

bash
docker-compose --env-file .env up --build -d
