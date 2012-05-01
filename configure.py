import os,sys
import sipconfig
from PyQt4 import pyqtconfig
from distutils import dir_util,file_util

config = pyqtconfig.Configuration()
pyonyx_installdir = os.path.join(config.default_sip_dir,"PyOnyx")
pyqt_sip_flags = config.pyqt_sip_flags

def generate_code(mname):
   argv = [config.sip_bin, "-c", "."]
   build_file = os.path.join(mname, mname + ".sbf")
   argv.extend(["-b",build_file])
   argv.extend(["-I", config.pyqt_sip_dir])
   argv.append(pyqt_sip_flags)
   sip_file = os.path.join(mname,mname+ "mod.sip")
   argv.append(sip_file)

   cmd = " ".join(argv)
   print cmd
   os.system(cmd)

   installs = []
   installs.append([os.path.join(mname,mname + "mod.sip"), os.path.join(pyonyx_installdir, mname)])

   makefile = pyqtconfig.QtGuiModuleMakefile(
       configuration=config,
       build_file=build_file,
       installs=installs
   )
   
   makefile.extra_libs = ["onyx_ui","onyx_sys","onyx_base","onyx_screen"]
   makefile.generate()


for mdir in ["Onyx","sys","ui","screen"]: 
   if not os.path.exists(mdir):
      dir_util.copy_tree(os.path.join(os.path.dirname(sys.argv[0]),mdir),"./"+mdir)
generate_code("Onyx")

content = {
    "pyonyx_sip_dir":    config.default_sip_dir,
    "pyonyx_sip_flags":  pyqt_sip_flags
}
confname = "pyonyxconfig.py"
if not os.path.exists(confname + ".in"):
   file_util.copy_file(os.path.join(os.path.dirname(sys.argv[0]),confname + ".in"),".")
sipconfig.create_config_module(confname, confname + ".in", content)
