# minesweeper-hex-arch-sample

Python MinesWeeper API for hexagonal architecture sample, based on the article [Hexagonal Architecture in Go](https://medium.com/@matiasvarela/hexagonal-architecture-in-go-cfd4e436faa3) ported by [Matías Varela](https://github.com/matiasvarela/minesweeper-hex-arch-sample)

## Domain
All the domain models will be placed in the directory `./domain`.
It contains the go struct definition of each entity that is part of the domain problem and can be used across the application.

## Ports
The ports will be placed in the directory `./ports`.
It contains the abstract classes (AKA interfaces definition ;) used to communicate with actors.

## Services
The services are our entry points to the core and each one of them implements the corresponding port.

They will be placed in packages inside the directory `./services`.


## Adapters
All driven adapters will be placed inside `./adapters/driven`