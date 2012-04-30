
%Import QtCore/QtCoremod.sip

namespace sys {

class SysStatus : QObject {

%TypeHeaderCode
#include "onyx/sys/sys_status.h"
%End

  public:
    static SysStatus & instance();
    ~SysStatus();

  public slots:
    void setSystemBusy(bool busy = true, bool show_indicator = true);
};

};
