import os,sys,glob
import sipconfig
from PyQt4 import pyqtconfig
from distutils import dir_util,file_util

config = pyqtconfig.Configuration()
pyqt_sip_flags = config.pyqt_sip_flags

src_dir = os.path.dirname(os.path.abspath(__file__))
pyonyx_installdir = os.path.join(config.default_sip_dir,"PyOnyx")
pyonyx_modroot = os.path.join(config.default_mod_dir, "PyOnyx")
mlist = ["screen","ui","onyx"]

install_sips = False

def generate_code(mname):
   os.makedirs(mname)

   argv = [config.sip_bin, "-c", os.path.abspath(mname)]
   build_file = os.path.join(mname, mname + ".sbf")
   argv.extend(["-b",build_file])
   argv.extend(["-I", config.pyqt_sip_dir])
   argv.extend(["-I", os.path.join(src_dir,"sip")])
   argv.append(pyqt_sip_flags)
   sip_file = os.path.join(mname,mname+ "mod.sip")
   argv.append(sip_file)

   cmd = " ".join(argv)
   print cmd
   os.system(cmd)

   installs = []
   if install_sips == True:
      sipfiles = []
      sipdir = os.path.join("sip", mname)
      if mname != "onyx":
         sipdir = os.path.join(src_dir, sipdir)
         rel_sipdir = sipdir
      else:
         rel_sipdir = os.path.join("..", sipdir)

      for s in glob.glob(os.path.join(sipdir, "*.sip")):
         sipfiles.append(os.path.join(rel_sipdir, os.path.basename(s)))

      installs.append([sipfiles, os.path.join(opts.pyqtsipdir, mname)])

   makefile = pyqtconfig.QtGuiModuleMakefile(
       configuration=config,
       build_file=mname + ".sbf",
       installs=installs,
       install_dir=pyonyx_modroot,
       dir=mname
   )
   if mname != "onyx":
      makefile.extra_libs = ["onyx_"+mname]
   makefile.generate()

if __name__ == "__main__":
   for mname in mlist: 
      generate_code(mname)

   makefile_out = []
   for sect in ["all","install","clean"]:
      makefile_out.append("\n" + sect + ":")
      for mname in mlist: 
         makefile_out.append("\t@(cd %s; $(MAKE) %s)" % (mname,sect))
      if sect == "install":
         makefile_out.append("\t@test -d $(DESTDIR)%s || mkdir -p $(DESTDIR)%s" % (pyonyx_modroot,pyonyx_modroot))
         makefile_out.append("\ttouch $(DESTDIR)%s" % (os.path.join(pyonyx_modroot,"__init__.py")))
         makefile_out.append("\tcp -f pyonyxconfig.py $(DESTDIR)%s" % (os.path.join(pyonyx_modroot,"pyonyxconfig.py")))

   mkfile = open("Makefile","w")
   mkfile.writelines([s + "\n" for s in makefile_out])
   
   content = {
       "pyonyx_sip_dir":    config.default_sip_dir,
       "pyonyx_sip_flags":  pyqt_sip_flags
   }
   confname = "pyonyxconfig.py"
   sipconfig.create_config_module(confname, os.path.join(src_dir,confname + ".in"), content)
