
%Import QtGui/QtGuimod.sip
%Include onyx_dialog.sip

namespace ui
{

class MessageDialog : OnyxDialog
{

%TypeHeaderCode
#include "onyx/ui/message_dialog.h"
%End

public:
    MessageDialog(QMessageBox::Icon icon,
                  const QString & title,
                  const QString & text,
                  QMessageBox::StandardButtons buttons = QMessageBox::NoButton,
                  QWidget * parent = 0);
    ~MessageDialog();

public:
    int exec();
    void updateInformation(const QString & text);
};

};
