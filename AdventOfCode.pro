QT += core gui network sql
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
CONFIG += c++17
DEFINES += QT_DEPRECATED_WARNINGS

INCLUDEPATH += D:/boost_1_78_0
LIBS += "-LD:/boost_1_53_0/stage/lib/"

RC_ICONS = icon.ico

SOURCES += \
    2015/puzzle_2015_01.cpp \
    2015/puzzle_2015_02.cpp \
    2015/puzzle_2015_03.cpp \
    2015/puzzle_2015_04.cpp \
    2015/puzzle_2015_05.cpp \
    2015/puzzle_2015_06.cpp \
    2015/puzzle_2015_07.cpp \
    2015/puzzle_2015_08.cpp \
    2015/puzzle_2015_09.cpp \
    2016/puzzle_2016_01.cpp \
    2017/puzzle_2017_01.cpp \
    2018/puzzle_2018_01.cpp \
    2018/puzzle_2018_02.cpp \
    2018/puzzle_2018_03.cpp \
    2018/puzzle_2018_04.cpp \
    2018/puzzle_2018_05.cpp \
    2018/puzzle_2018_06.cpp \
    2018/puzzle_2018_07.cpp \
    2019/intcodecomputer.cpp \
    2019/puzzle_2019_01.cpp \
    2019/puzzle_2019_02.cpp \
    2019/puzzle_2019_03.cpp \
    2019/puzzle_2019_04.cpp \
    2019/puzzle_2019_05.cpp \
    2019/puzzle_2019_06.cpp \
    2019/puzzle_2019_07.cpp \
    2019/puzzle_2019_08.cpp \
    2019/puzzle_2019_09.cpp \
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
    2021/puzzle_2021_01.cpp \
    2021/puzzle_2021_02.cpp \
    2021/puzzle_2021_03.cpp \
    2021/puzzle_2021_04.cpp \
    2021/puzzle_2021_05.cpp \
    2021/puzzle_2021_06.cpp \
    2021/puzzle_2021_07.cpp \
    2021/puzzle_2021_08.cpp \
    2021/puzzle_2021_09.cpp \
    2021/puzzle_2021_10.cpp \
    2021/puzzle_2021_11.cpp \
    2021/puzzle_2021_12.cpp \
    2021/puzzle_2021_13.cpp \
    2021/puzzle_2021_14.cpp \
    2021/puzzle_2021_15.cpp \
    2021/puzzle_2021_16.cpp \
    2021/puzzle_2021_17.cpp \
    2021/puzzle_2021_18.cpp \
    2021/puzzle_2021_19.cpp \
    2021/puzzle_2021_20.cpp \
    2021/puzzle_2021_21.cpp \
    2021/puzzle_2021_22.cpp \
    2021/puzzle_2021_23.cpp \
    2022/puzzle_2022_01.cpp \
    2022/puzzle_2022_02.cpp \
    2022/puzzle_2022_03.cpp \
    2022/puzzle_2022_04.cpp \
    2022/puzzle_2022_05.cpp \
    2022/puzzle_2022_06.cpp \
    2022/puzzle_2022_07.cpp \
    2022/puzzle_2022_08.cpp \
    2022/puzzle_2022_09.cpp \
    2022/puzzle_2022_10.cpp \
    2022/puzzle_2022_11.cpp \
    2022/puzzle_2022_12.cpp \
    2022/puzzle_2022_13.cpp \
    2022/puzzle_2022_14.cpp \
    2022/puzzle_2022_15.cpp \
    2022/puzzle_2022_16.cpp \
    2023/puzzle_2023_01.cpp \
    2023/puzzle_2023_02.cpp \
    2023/puzzle_2023_03.cpp \
    2023/puzzle_2023_04.cpp \
    2023/puzzle_2023_05.cpp \
    2023/puzzle_2023_06.cpp \
    2023/puzzle_2023_07.cpp \
    2023/puzzle_2023_08.cpp \
    2023/puzzle_2023_09.cpp \
    2023/puzzle_2023_10.cpp \
    2023/puzzle_2023_11.cpp \
    2023/puzzle_2023_12.cpp \
    2023/puzzle_2023_13.cpp \
    2023/puzzle_2023_14.cpp \
    2023/puzzle_2023_15.cpp \
    2023/puzzle_2023_16.cpp \
    2023/puzzle_2023_17.cpp \
    2023/puzzle_2023_18.cpp \
    2023/puzzle_2023_19.cpp \
    2023/puzzle_2023_20.cpp \
    2023/puzzle_2023_21.cpp \
    2023/puzzle_2023_22.cpp \
    2023/puzzle_2023_23.cpp \
    2023/puzzle_2023_24.cpp \
    2023/puzzle_2023_25.cpp \
    common.cpp \
    display/display.cpp \
    display/view.cpp \
    leaderboard.cpp \
    main.cpp \
    mainwindow.cpp \
    solvers.cpp

HEADERS += \
    2015/event_2015.h \
    2015/puzzle_2015_01.h \
    2015/puzzle_2015_02.h \
    2015/puzzle_2015_03.h \
    2015/puzzle_2015_04.h \
    2015/puzzle_2015_05.h \
    2015/puzzle_2015_06.h \
    2015/puzzle_2015_07.h \
    2015/puzzle_2015_08.h \
    2015/puzzle_2015_09.h \
    2016/puzzle_2016_01.h \
    2017/puzzle_2017_01.h \
    2018/event_2018.h \
    2018/puzzle_2018_01.h \
    2018/puzzle_2018_02.h \
    2018/puzzle_2018_03.h \
    2018/puzzle_2018_04.h \
    2018/puzzle_2018_05.h \
    2018/puzzle_2018_06.h \
    2018/puzzle_2018_07.h \
    2019/event_2019.h \
    2019/intcodecomputer.h \
    2019/puzzle_2019_01.h \
    2019/puzzle_2019_02.h \
    2019/puzzle_2019_03.h \
    2019/puzzle_2019_04.h \
    2019/puzzle_2019_05.h \
    2019/puzzle_2019_06.h \
    2019/puzzle_2019_07.h \
    2019/puzzle_2019_08.h \
    2019/puzzle_2019_09.h \
    2020/display/puzzle_2020_24/puzzle_2020_24_display.h \
    2020/display/puzzle_2020_24/puzzle_2020_24_view.h \
    2020/event_2020.h \
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
    2021/event_2021.h \
    2021/puzzle_2021_01.h \
    2021/puzzle_2021_02.h \
    2021/puzzle_2021_03.h \
    2021/puzzle_2021_04.h \
    2021/puzzle_2021_05.h \
    2021/puzzle_2021_06.h \
    2021/puzzle_2021_07.h \
    2021/puzzle_2021_08.h \
    2021/puzzle_2021_09.h \
    2021/puzzle_2021_10.h \
    2021/puzzle_2021_11.h \
    2021/puzzle_2021_12.h \
    2021/puzzle_2021_13.h \
    2021/puzzle_2021_14.h \
    2021/puzzle_2021_15.h \
    2021/puzzle_2021_16.h \
    2021/puzzle_2021_17.h \
    2021/puzzle_2021_18.h \
    2021/puzzle_2021_19.h \
    2021/puzzle_2021_20.h \
    2021/puzzle_2021_21.h \
    2021/puzzle_2021_22.h \
    2021/puzzle_2021_23.h \
    2022/event_2022.h \
    2022/puzzle_2022_01.h \
    2022/puzzle_2022_02.h \
    2022/puzzle_2022_03.h \
    2022/puzzle_2022_04.h \
    2022/puzzle_2022_05.h \
    2022/puzzle_2022_06.h \
    2022/puzzle_2022_07.h \
    2022/puzzle_2022_08.h \
    2022/puzzle_2022_09.h \
    2022/puzzle_2022_10.h \
    2022/puzzle_2022_11.h \
    2022/puzzle_2022_12.h \
    2022/puzzle_2022_13.h \
    2022/puzzle_2022_14.h \
    2022/puzzle_2022_15.h \
    2022/puzzle_2022_16.h \
    2023/puzzle_2023_01.h \
    2023/puzzle_2023_02.h \
    2023/puzzle_2023_03.h \
    2023/puzzle_2023_04.h \
    2023/puzzle_2023_05.h \
    2023/puzzle_2023_06.h \
    2023/puzzle_2023_07.h \
    2023/puzzle_2023_08.h \
    2023/puzzle_2023_09.h \
    2023/puzzle_2023_10.h \
    2023/puzzle_2023_11.h \
    2023/puzzle_2023_12.h \
    2023/puzzle_2023_13.h \
    2023/puzzle_2023_14.h \
    2023/puzzle_2023_15.h \
    2023/puzzle_2023_16.h \
    2023/puzzle_2023_17.h \
    2023/puzzle_2023_18.h \
    2023/puzzle_2023_19.h \
    2023/puzzle_2023_20.h \
    2023/puzzle_2023_21.h \
    2023/puzzle_2023_22.h \
    2023/puzzle_2023_23.h \
    2023/puzzle_2023_24.h \
    2023/puzzle_2023_25.h \
    common.h \
    display/display.h \
    display/view.h \
    jsonhelper.h \
    leaderboard.h \
    mainwindow.h \
    solvers.h

FORMS += \
    2020/display/puzzle_2020_24/puzzle_2020_24_display.ui \
    display/display.ui \
    mainwindow.ui
