# Dockerized Flask Multiplication Table App

## Overview

This project is a simple Flask web application that generates the multiplication table of a user-provided number. The application is containerized using Docker.

Purpose of this project is to practice Docker fundamentals, including:

* Creating a Dockerfile
* Building Docker images
* Running Docker containers
* Exposing ports
* Managing Python dependencies with requirements.txt

## Tech Stack

* Python
* Flask
* Docker

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Build the Docker Image

```bash
docker build -t table-app .
```

## Run the Container

```bash
docker run -p 5000:5000 table-app
```

## Access the Application

Open the browser and visit:

```text
http://localhost:5000
```

Enter a number and the application will generate its multiplication table from 1 to 10.

## Learned docker skills:

Through this project I learned:

* Difference between Docker images and containers
* How to create a Dockerfile
* How to build Docker images
* How to run containers

