
namespace ui {

class MessageDialog : ui::OnyxDialog {

%TypeHeaderCode
#include "onyx/ui/message_dialog.h"
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

};
