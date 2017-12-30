#!/usr/bin/python3
import runpy
from os import path, getcwd
from sys import argv

def m_init():
	global global_var, work_dir
	global_var = {}
	global_var['__user_dir__'] = getcwd()
	work_dir = path.dirname(path.realpath(__file__))
	global_var['__work_dir__'] = path.dirname(path.realpath(__file__))
	pass

def main():
	if len(argv)>1 and argv[1]=='plugin':
		global_var['argv'] = argv[2:]
		runpy.run_path(path.join(work_dir, 'manager/plugin-manager.pyc'), 
						global_var, '__main__')
		pass
	else:
		global_var['argv'] = argv
		runpy.run_path(path.join(work_dir, 'manager/manager.pyc'), 
						global_var, '__main__')
		pass
	pass

if __name__ == '__main__':
	m_init()
	try: #cope with Interrupt Signal
		main()
	except Exception as e:
		print(e) #fro debug
	finally:
		exit()