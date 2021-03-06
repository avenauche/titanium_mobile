import os, sys, simplejson

project_dir = None
def compile(config):
	global project_dir
	project_dir = config['project_dir']
	# remove unserializable data
	config['android_builder'] = None
	config['tiapp'] = None
	config['logger'] = None
	outfile = os.path.join(project_dir, 'plugin_compile.json')
	open(outfile, "w").write(simplejson.dumps(config))

def postbuild():
	global project_dir
	outfile = os.path.join(project_dir, 'plugin_postbuild.txt')
	open(outfile, "w").write("#")

