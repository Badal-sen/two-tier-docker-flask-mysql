# Two-Tier Docker Flask MySQL Application

This project demonstrates a **two-tier Docker architecture** using **Flask** and **MySQL**.

## Architecture
- **Flask**: Application layer
- **MySQL**: Database layer
- **Docker Compose**: Container orchestration and networking

## Docker Networking Explained
Docker Compose automatically creates an internal bridge network.
The Flask container connects to the MySQL container using the **service name `mysql`** instead of `localhost` or IP address.

## How to Run
```bash
docker compose up --build

