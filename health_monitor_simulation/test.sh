#!/bin/bash

# Start simulation
echo "Starting containers..."
docker-compose up -d

# Wait for services to initialize
sleep 2

echo -e "\n=== TEST 1: Server Online ==="
docker exec sys1 python /app/health_check.py

echo -e "\n=== TEST 2: Server Offline ==="
docker-compose stop sys2
docker exec sys1 python /app/health_check.py

echo -e "\n=== TEST 3: Network Failure ==="
docker network disconnect health_monitor_simulation_monitor-net sys1
docker exec sys1 python /app/health_check.py

# Reconnect network for cleanup
docker network connect health_monitor_simulation_monitor-net sys1

# Cleanup
echo -e "\nCleaning up..."
docker-compose down -v