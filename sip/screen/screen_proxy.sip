
%Import QtGui/QtGuimod.sip
%Import QtNetwork/QtNetworkmod.sip

struct ScreenCommand {

%TypeHeaderCode
#include "onyx/screen/screen_proxy.h"
using namespace onyx;
using namespace screen;
%End

    enum Type {
        WAIT_FOR_FINISHED,
        SYNC,
        UPDATE,
        SYNC_AND_UPDATE,
        DRAW_LINE,
        DRAW_LINES,
        FILL_SCREEN,
    };

    enum WaitMode {
        WAIT_NONE,
        WAIT_BEFORE_UPDATE,
        WAIT_COMMAND_FINISH,
        WAIT_NORMAL,
        WAIT_ALL,
    };

    enum UpdateMode {
        FULL_UPDATE,
        PARTIAL_UPDATE,
    };

    static const int MAX_POINTS;
    Type type;
    int waveform;
    UpdateMode update_flags;
    int top;
    int left;
    int width;
    int height;
    int point_count;
    int color;
    int size;
    WaitMode wait_flags;
};

class ScreenProxy {

%TypeHeaderCode
#include "onyx/screen/screen_proxy.h"
using namespace onyx;
using namespace screen;
%End

public:
    enum Waveform {
        INVALID, 
        DW,    
        A2,     
        GU,          
        GC,         
        GC4,   
        GC8,   
        GC16,
    };

    enum WaveformPolicy {
        INVALID_POLICY,
        PERFORMANCE_FIRST,
        QUALITY_FIRST,
    };

    static ScreenProxy & instance();
    ~ScreenProxy();

    bool isUpdateEnabled();
    void enableUpdate(bool enable);

    void ensureUpdateFinished();

    void setDefaultWaveform(Waveform w = ScreenProxy::GC);
    Waveform defaultWaveform() const;
    Waveform toggleWaveform();
    Waveform saveWaveform();
    Waveform restoreWaveform();

    void setWaveformPolicy(WaveformPolicy policy = QUALITY_FIRST);
    WaveformPolicy waveformPolicy();

    void flush(const QWidget *widget,
               Waveform w = INVALID,
               bool whole = true,
               ScreenCommand::WaitMode wait = ScreenCommand::WAIT_BEFORE_UPDATE);
    void flush(int timeout = 3000);

    QRect & sync(const QWidget *widget, const QRect * region = 0);
    void updateWidget(const QWidget *widget,
                      Waveform w = INVALID,
                      bool whole = true,
                      ScreenCommand::WaitMode wait = ScreenCommand::WAIT_BEFORE_UPDATE);
    void updateWidgetRegion(const QWidget *,
                            const QRect&,
                            Waveform w = INVALID,
                            bool whole = true,
                            ScreenCommand::WaitMode wait = ScreenCommand::WAIT_BEFORE_UPDATE);
    void updateScreen(Waveform w = INVALID,
                      ScreenCommand::WaitMode wait = ScreenCommand::WAIT_BEFORE_UPDATE);

    void drawLine(int x1, int y1, int x2, int y2, unsigned char color, int size);
    void drawLines(QPoint * points, const int size, unsigned char color, int width);
    void fillScreen(unsigned char color);

    void setGCInterval(const int interval);
    void resetGUCount();
    void updateWidgetWithGCInterval(const QWidget *widget,
                                   const QRect * rect = 0,
                                   Waveform w = INVALID,
                                   bool whole = true,
                                   ScreenCommand::WaitMode wait = ScreenCommand::WAIT_BEFORE_UPDATE);

private:
    ScreenProxy();
    ScreenProxy(ScreenProxy & ref);

};
