# Weightlog

Weightlog is a simple weightlogger. It stores the data encrypted and can draw and save a plot of you history.

## Usage

`weightlog` currently accepts five possible commands: `--edit`, `--add`, `--print`, `--plot`, `--save`. `--edit` is mostly for debugging and allow you to play with the stored weights. `--print` just prints all stored data. `--add` adds a new weight to the log. `--plot` shows a plot of the stored weights and `--save` saved it.

You can pass six options to weightlog. Two of them are used in every command: `--weightfile` and `--password`. `--weightfile` speficies the filepath to which the weightlog should be saved. Its default is `weight.aes` in the current directory. `--password` specifies the password with which the weightfile will be encrypted. The other four options are only needed for some commands (will be ignored in all other cases). `--weight` and `--date` are used in `--add`. They tell the programm the weight which should be added to the log and at which date it should be added. `--date` has format DD-MM-YYYY HH:MM and defaults to the current date and time. `--height` is used in `--plot` and `--save` and tell the programm your current height for calculating the Body-Mass-Index. `--outfile` is only used in `--save` and tells the program where to save the plot to.

You can save some defaults into `settings.py`, see `settings.py.example` for the format and possible options which can be set.