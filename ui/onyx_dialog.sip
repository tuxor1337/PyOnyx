
%Import QtGui/QtGuimod.sip

namespace ui
{

class OnyxDialog : QDialog
{

%TypeHeaderCode
#include "onyx/ui/onyx_dialog.h"
%End

public:
    OnyxDialog(QWidget *parent, bool show_shadow = true);
    ~OnyxDialog();
};

};
