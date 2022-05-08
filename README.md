# Geno.me-Challenge-DevOps

System Administration and DevOps code challenge.

## Architecture

![Challenge Architecture](/document/png/challenge-architecture.png "Challenge Architecture")

## Pre-requisites

1. [Virtualbox](https://www.virtualbox.org/wiki/Downloads) must be installed in your host machine.
2. [Vagrant](https://www.vagrantup.com/downloads) must be installed on your host machine. 
3. Optional: [Visual Studio Code](https://code.visualstudio.com/) or any Code Editor.

- **Note:** This app has been tested in Ubuntu (Linux).

## How to run

- ```vagrant up```

## How to test

From your host machine:

- ```curl -v http://localhost:8080/api/greeting```
- ```curl -v http://localhost:8080/api/cryptocurrencies/1```
- ```curl -d '{"cryptocurrency_id":8, "cryptocurrency_name":"Lite Coin", "cryptocurrency_symbol":"LTC"}' -H 'Content-Type: application/json' http://localhost:8080/api/messages```