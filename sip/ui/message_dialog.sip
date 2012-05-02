
class MessageDialog : OnyxDialog {

%TypeHeaderCode
#include "onyx/ui/message_dialog.h"
using namespace ui;
%End

public:
    MessageDialog(QMessageBox::Icon icon,
                  const QString & title,
                  const QString & text,
                  QMessageBox::StandardButtons buttons = QMessageBox::NoButton,
                  QWidget * parent /TransferThis/ = 0);
    ~MessageDialog();

public:
    int exec() /PyName=exec_/;
    void updateInformation(const QString & text);
};
