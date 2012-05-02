
%Import QtCore/QtCoremod.sip

class SysStatus : QObject {

%TypeHeaderCode
#include "onyx/sys/sys_status.h"
using namespace sys;
%End

  public:
    static SysStatus & instance();
    ~SysStatus();

  public slots:
    void setSystemBusy(bool busy = true, bool show_indicator = true);

  private:
    SysStatus();
    SysStatus(SysStatus & ref);
};
