import json
from getpass import getpass
import os
from functions import *
import time
import argparse
from plot import plot
import datetime
try:
	import settings
except ImportError:
	settings = None
	print("You can store password and height in settings.py (see settings.py.example) if you don't want to enter it all the time.")


parser = argparse.ArgumentParser(description='Log weights')
group_options = parser.add_argument_group('general options')

group_options.add_argument('--weightfile', type=str, dest="weightfile", default="weight.aes",
                   help='the path to the weightfile, default: weight.aes')
group_options.add_argument('--password', type=str, dest="password",
                   help='password, if not specified, it will be asked')


group_commands = parser.add_argument_group('commands', "multiple commands can be executed at once.")
group_commands.add_argument('--edit', dest="manual_edit", help='open pdb after loading weight, saves weight log afterwards', action='store_true')
group_commands.add_argument('--add', dest="add_weight", help='add weight to weight log', action='store_true')
group_commands.add_argument('--print', dest="print_weight", help='print weight log', action='store_true')
group_commands.add_argument('--plot', dest="plot_weight", help='plot weights', action='store_true')
group_commands.add_argument('--save', dest="save_weight", help='save weight-plot', action='store_true')



parser.add_argument('--weight', type=float, dest="weight",
                   help='weight, if not specified, it will be asked')
parser.add_argument('--height', type=float, dest="height",
                   help='height in meter, if not specified, it will be asked')
parser.add_argument('--date', type=str, dest="date",
                   help='date in format DD-MM-YYYY HH:MM, current date is default')
parser.add_argument('--outfile', type=str, dest="outfile", default="weightlog.png",
                   help='file to save plot in (default: weightlog.png)')


args = parser.parse_args()


if not args.password:
	if settings and hasattr(settings, "password"):
		password = settings.password
	else:
		password = input("Password: ")
else:
	password = args.password

weights = load_weights(args.weightfile, password)

if args.manual_edit:
	import pdb;pdb.set_trace()
	save_weights(weights, args.weightfile, password)

if args.add_weight:
	if not args.weight:
		weight = float(input("Weight in kg: "))
	else:
		weight = args.weight
	if not args.date:
		date = time.time()
	else:
		time_tuple = time.strptime(args.date, "%d-%m-%Y %H:%M")

		date = time.mktime(time_tuple)
	weight_data = {"time":date, "weight":weight}
	weights.append(weight_data)
	save_weights(weights, args.weightfile, password)

if args.print_weight:
	print(weights)

if args.plot_weight or args.save_weight:
	if not args.height:
		if settings and hasattr(settings, "height"):
			height = settings.height
		else:
			height = input("Height: ")
	else:
		height = args.height
	if settings and hasattr(settings, "plot_kwargs"):		
		plot_kwargs = settings.plot_kwargs
	else:
		plot_kwargs = {}

	plot(weights, height, plot=args.plot_weight, save=args.save_weight, outfile=args.outfile, **plot_kwargs)
