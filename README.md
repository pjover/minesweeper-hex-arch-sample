# minesweeper-hex-arch-sample

Python MinesWeeper API for hexagonal architecture sample, based on the article [Hexagonal Architecture in Go](https://medium.com/@matiasvarela/hexagonal-architecture-in-go-cfd4e436faa3) ported by [Matías Varela](https://github.com/matiasvarela/minesweeper-hex-arch-sample)

## Core

### Domain
All the domain models will be placed in the directory `./core/domain`.
It contains the go struct definition of each entity that is part of the domain problem and can be used across the application.

### Ports
The ports will be placed in the directory `./core/ports`.
It contains the abstract classes (AKA interfaces definition ;) used to communicate with actors.

### Services
They will be placed in packages inside the directory `./core/services`.
The services are our entry points to the core and each one of them implements the corresponding port.


## Adapters

### Drivers
Drivers (or primary) actors, are those who trigger the communication with the core. They do so to invoke a specific service on the core. A human or a CLI (command line interface) are perfect examples of drivers actors.
All driver adapters will be placed inside `./adapters/driver`

### Drivens
Driven (or secondary) actors, are those who are expecting the core to be the one who trigger the communication. In this case, is the core who needs something that the actor provides, so it sends a request to the actor and invoke a specific action on it. For example, if the core needs to save data into a MySQL database, then the core trigger the communication to execute an INSERT query on the MySQL client.

All driven adapters will be placed inside `./adapters/driven`


## Dependency injection
Dependency injection puts all components together, and will be placed inside `./di`

## Run the game
The game script is placed at `./cmd` 
