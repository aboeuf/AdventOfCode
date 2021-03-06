QT += core gui network sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# The following define makes your compiler emit warnings if you use
# any Qt feature that has been marked deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    2019/display/puzzle_2019_08/puzzle_2019_08_display.cpp \
    2019/display/puzzle_2019_08/puzzle_2019_08_view.cpp \
    2019/intcodecomputer.cpp \
    2019/puzzle_2019_01.cpp \
    2019/puzzle_2019_02.cpp \
    2019/puzzle_2019_03.cpp \
    2019/puzzle_2019_04.cpp \
    2019/puzzle_2019_05.cpp \
    2019/puzzle_2019_06.cpp \
    2019/puzzle_2019_07.cpp \
    2019/puzzle_2019_08.cpp \
    2020/display/puzzle_2020_24/puzzle_2020_24_display.cpp \
    2020/display/puzzle_2020_24/puzzle_2020_24_view.cpp \
    2020/puzzle_2020_01.cpp \
    2020/puzzle_2020_02.cpp \
    2020/puzzle_2020_03.cpp \
    2020/puzzle_2020_04.cpp \
    2020/puzzle_2020_05.cpp \
    2020/puzzle_2020_06.cpp \
    2020/puzzle_2020_07.cpp \
    2020/puzzle_2020_08.cpp \
    2020/puzzle_2020_09.cpp \
    2020/puzzle_2020_10.cpp \
    2020/puzzle_2020_11.cpp \
    2020/puzzle_2020_12.cpp \
    2020/puzzle_2020_13.cpp \
    2020/puzzle_2020_14.cpp \
    2020/puzzle_2020_15.cpp \
    2020/puzzle_2020_16.cpp \
    2020/puzzle_2020_17.cpp \
    2020/puzzle_2020_18.cpp \
    2020/puzzle_2020_19.cpp \
    2020/puzzle_2020_20.cpp \
    2020/puzzle_2020_21.cpp \
    2020/puzzle_2020_22.cpp \
    2020/puzzle_2020_23.cpp \
    2020/puzzle_2020_24.cpp \
    2020/puzzle_2020_25.cpp \
    common.cpp \
    main.cpp \
    mainwindow.cpp \
    solvers.cpp

HEADERS += \
    2019/display/puzzle_2019_08/puzzle_2019_08_display.h \
    2019/display/puzzle_2019_08/puzzle_2019_08_view.h \
    2019/intcodecomputer.h \
    2019/puzzle_2019_01.h \
    2019/puzzle_2019_02.h \
    2019/puzzle_2019_03.h \
    2019/puzzle_2019_04.h \
    2019/puzzle_2019_05.h \
    2019/puzzle_2019_06.h \
    2019/puzzle_2019_07.h \
    2019/puzzle_2019_08.h \
    2020/display/puzzle_2020_24/puzzle_2020_24_display.h \
    2020/display/puzzle_2020_24/puzzle_2020_24_view.h \
    2020/puzzle_2020_01.h \
    2020/puzzle_2020_02.h \
    2020/puzzle_2020_03.h \
    2020/puzzle_2020_04.h \
    2020/puzzle_2020_05.h \
    2020/puzzle_2020_06.h \
    2020/puzzle_2020_07.h \
    2020/puzzle_2020_08.h \
    2020/puzzle_2020_09.h \
    2020/puzzle_2020_10.h \
    2020/puzzle_2020_11.h \
    2020/puzzle_2020_12.h \
    2020/puzzle_2020_13.h \
    2020/puzzle_2020_14.h \
    2020/puzzle_2020_15.h \
    2020/puzzle_2020_16.h \
    2020/puzzle_2020_17.h \
    2020/puzzle_2020_18.h \
    2020/puzzle_2020_19.h \
    2020/puzzle_2020_20.h \
    2020/puzzle_2020_21.h \
    2020/puzzle_2020_22.h \
    2020/puzzle_2020_23.h \
    2020/puzzle_2020_24.h \
    2020/puzzle_2020_25.h \
    common.h \
    jsonhelper.h \
    mainwindow.h \
    solvers.h

FORMS += \
    2019/display/puzzle_2019_08/puzzle_2019_08_display.ui \
    2020/display/puzzle_2020_24/puzzle_2020_24_display.ui \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
