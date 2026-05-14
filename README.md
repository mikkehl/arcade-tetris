# ArcadeTetris
Link: https://github.com/mikkehl/arcade-tetris

# How to build
In desired location, run:
```ps
git clone https://github.com/mikkehl/arcade-tetris
cd arcade-tetris
git submodule update --init --recursive
dotnet build
```
# How to run
To run the game: `dotnet run --project Tetris`

To run the tests: `dotnet test TetrisTests`