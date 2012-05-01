
namespace ui {

class MessageDialog : ui::OnyxDialog {

%TypeHeaderCode
#include "onyx/ui/message_dialog.h"
%End

public:
    MessageDialog(QMessageBox::Icon icon /TransferThis/,
                  const QString & title /TransferThis/,
                  const QString & text /TransferThis/,
                  QMessageBox::StandardButtons buttons /TransferThis/ = QMessageBox::NoButton,
                  QWidget * parent /TransferThis/ = 0);
    ~MessageDialog();

public:
    int exec() /PyName=exec_/;
    void updateInformation(const QString & text /TransferThis/);
};

};
