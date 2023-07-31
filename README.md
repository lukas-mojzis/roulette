# Roulette
Simple text-based simulator of the gambling game roulette written in Python.

## Getting Started
You need to install [Python](https://www.python.org/) (version 3.9 or above) to run the game.

The game can then be started from the command line by navigating into the directory where the file `roulette.py` is placed and running the command `python roulette.py`.

## Controls
The entire game runs in the command line environment and is controlled by entering numerical commands whenever prompted.

In most cases, a list of all available options is displayed. Each option is assigned a number at the beginning of the line, e.g. (1), (4) or (11). To pick an option, enter its assigned number.

In some cases (such as when asked how much money you would like to bet), no list of options is displayed. To answer, simply enter a number of your choice.

## Rules Overview
For an explanation of the rules, please refer to the Wikipedia article on roulette (mainly the [top section](https://en.wikipedia.org/wiki/Roulette), [rules of play against a casino](https://en.wikipedia.org/wiki/Roulette#Rules_of_play_against_a_casino), [types of bets](https://en.wikipedia.org/wiki/Roulette#Types_of_bets) and [bet odds table](https://en.wikipedia.org/wiki/Roulette#Bet_odds_table)). In addition to that, please consider the following:
- The game uses a single-zero (European-style) wheel.
- You can place only one bet on each spin.
- The minimum bet is $1. No maximum bet limit is imposed.
- If you bet on low/high, red/black or even/odd numbers, you lose only half of your bet if a zero is drawn.
- You start the game with $1,000.

After each spin, your bet is evaluated. If you lose and have no more money left, the game ends. Otherwise, you are asked whether you want to play another spin. Leave the casino with enough money and you will earn a highscore record!

## Demo
![Roulette Demo](https://github.com/lukas-mojzis/roulette/blob/main/demo.gif "Roulette Demo")

## Contributing
Any feedback, suggestions and pull requests are welcome!

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[Lukas Mojzis](https://github.com/lukas-mojzis)

You can also contact me via [e-mail](mailto:mojzis.lukas@gmail.com) or [LinkedIn](https://www.linkedin.com/in/lukas-mojzis/).
