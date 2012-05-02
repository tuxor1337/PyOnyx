
%Import QtGui/QtGuimod.sip

class OnyxDialog : QDialog {

%TypeHeaderCode
#include "onyx/ui/onyx_dialog.h"
    using namespace ui;
%End

public:
    OnyxDialog(QWidget *parent /TransferThis/, bool show_shadow = true);
    ~OnyxDialog();
};
