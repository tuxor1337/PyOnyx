import os
import sipconfig
from PyQt4 import pyqtconfig

pyonyxdir = os.path.join(pyqtconfig.Configuration().default_sip_dir,"PyOnyx")

def generate_code(mname):
   config = pyqtconfig.Configuration()
   argv = [config.sip_bin, "-c", "."]
   build_file = os.path.join(mname, mname + ".sbf")
   argv.extend(["-b",build_file])
   argv.extend(["-I", config.pyqt_sip_dir])
   pyqt_sip_flags = config.pyqt_sip_flags
   argv.append(pyqt_sip_flags)
   sip_file = "%s/%smod.sip" % (mname,mname)
   argv.append(sip_file)

   cmd = " ".join(argv)
   print cmd
   os.system(cmd)

   installs = []
   installs.append([mname + "mod.sip", os.path.join(pyonyxdir, mname)])

   makefile = pyqtconfig.QtGuiModuleMakefile(
       configuration=config,
       build_file=build_file,
       installs=installs
   )
   
   makefile.extra_libs = ["onyx_" + mname]
   makefile.generate()

generate_code("ui")

content = {
    "pyonyx_sip_dir":    config.default_sip_dir,
    "pyonyx_sip_flags":  pyqt_sip_flags
}
sipconfig.create_config_module("pyonyxconfig.py", "pyonyxconfig.py.in", content)
