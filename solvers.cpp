#include <mainwindow.h>
#include <solvers.h>

#include <2015/event_2015.h>
#include <2016/event_2016.h>
#include <2017/event_2017.h>
#include <2018/event_2018.h>
#include <2019/event_2019.h>
#include <2020/event_2020.h>
#include <2021/event_2021.h>
#include <2022/event_2022.h>
#include <2023/event_2023.h>
#include <2024/event_2024.h>

Solvers::Solvers() {
  m_solvers[2015][1][1] = new Solver_2015_01_1();
  m_solvers[2015][1][2] = new Solver_2015_01_2();
  m_solvers[2015][2][1] = new Solver_2015_02_1();
  m_solvers[2015][2][2] = new Solver_2015_02_2();
  m_solvers[2015][3][1] = new Solver_2015_03_1();
  m_solvers[2015][3][2] = new Solver_2015_03_2();
  m_solvers[2015][4][1] = new Solver_2015_04_1();
  m_solvers[2015][4][2] = new Solver_2015_04_2();
  m_solvers[2015][5][1] = new Solver_2015_05_1();
  m_solvers[2015][5][2] = new Solver_2015_05_2();
  m_solvers[2015][6][1] = new Solver_2015_06_1();
  m_solvers[2015][6][2] = new Solver_2015_06_2();
  m_solvers[2015][7][1] = new Solver_2015_07_1();
  m_solvers[2015][7][2] = new Solver_2015_07_2();
  m_solvers[2015][8][1] = new Solver_2015_08_1();
  m_solvers[2015][8][2] = new Solver_2015_08_2();
  m_solvers[2015][9][1] = new Solver_2015_09_1();
  m_solvers[2015][9][2] = new Solver_2015_09_2();
  m_solvers[2016][1][1] = new Solver_2016_01_1();
  m_solvers[2016][1][2] = new Solver_2016_01_2();
  m_solvers[2016][2][1] = new Solver_2016_02_1();
  m_solvers[2016][2][2] = new Solver_2016_02_2();
  m_solvers[2016][3][1] = new Solver_2016_03_1();
  m_solvers[2016][3][2] = new Solver_2016_03_2();
  m_solvers[2016][5][1] = new Solver_2016_05_1();
  m_solvers[2016][5][2] = new Solver_2016_05_2();
  m_solvers[2016][6][1] = new Solver_2016_06_1();
  m_solvers[2016][6][2] = new Solver_2016_06_2();
  m_solvers[2016][7][1] = new Solver_2016_07_1();
  m_solvers[2016][7][2] = new Solver_2016_07_2();
  m_solvers[2016][8][1] = new Solver_2016_08_1();
  m_solvers[2016][8][2] = new Solver_2016_08_2();
  m_solvers[2016][9][1] = new Solver_2016_09_1();
  m_solvers[2016][9][2] = new Solver_2016_09_2();
  m_solvers[2017][1][1] = new Solver_2017_01_1();
  m_solvers[2017][1][2] = new Solver_2017_01_2();
  m_solvers[2017][2][1] = new Solver_2017_02_1();
  m_solvers[2017][2][2] = new Solver_2017_02_2();
  m_solvers[2017][3][1] = new Solver_2017_03_1();
  m_solvers[2017][3][2] = new Solver_2017_03_2();
  m_solvers[2017][4][1] = new Solver_2017_04_1();
  m_solvers[2017][4][2] = new Solver_2017_04_2();
  m_solvers[2017][5][1] = new Solver_2017_05_1();
  m_solvers[2017][5][2] = new Solver_2017_05_2();
  m_solvers[2017][6][1] = new Solver_2017_06_1();
  m_solvers[2017][6][2] = new Solver_2017_06_2();
  m_solvers[2017][7][1] = new Solver_2017_07_1();
  m_solvers[2017][7][2] = new Solver_2017_07_2();
  m_solvers[2017][8][1] = new Solver_2017_08_1();
  m_solvers[2017][8][2] = new Solver_2017_08_2();
  m_solvers[2017][9][1] = new Solver_2017_09_1();
  m_solvers[2017][9][2] = new Solver_2017_09_2();
  m_solvers[2018][1][1] = new Solver_2018_01_1();
  m_solvers[2018][1][2] = new Solver_2018_01_2();
  m_solvers[2018][2][1] = new Solver_2018_02_1();
  m_solvers[2018][2][2] = new Solver_2018_02_2();
  m_solvers[2018][3][1] = new Solver_2018_03_1();
  m_solvers[2018][3][2] = new Solver_2018_03_2();
  m_solvers[2018][4][1] = new Solver_2018_04_1();
  m_solvers[2018][4][2] = new Solver_2018_04_2();
  m_solvers[2018][5][1] = new Solver_2018_05_1();
  m_solvers[2018][5][2] = new Solver_2018_05_2();
  m_solvers[2018][6][1] = new Solver_2018_06_1();
  m_solvers[2018][6][2] = new Solver_2018_06_2();
  m_solvers[2018][7][1] = new Solver_2018_07_1();
  m_solvers[2018][7][2] = new Solver_2018_07_2();
  m_solvers[2018][8][1] = new Solver_2018_08_1();
  m_solvers[2018][8][2] = new Solver_2018_08_2();
  m_solvers[2018][9][1] = new Solver_2018_09_1();
  m_solvers[2018][9][2] = new Solver_2018_09_2();
  m_solvers[2019][1][1] = new Solver_2019_01_1();
  m_solvers[2019][1][2] = new Solver_2019_01_2();
  m_solvers[2019][2][1] = new Solver_2019_02_1();
  m_solvers[2019][2][2] = new Solver_2019_02_2();
  m_solvers[2019][3][1] = new Solver_2019_03_1();
  m_solvers[2019][3][2] = new Solver_2019_03_2();
  m_solvers[2019][4][1] = new Solver_2019_04_1();
  m_solvers[2019][4][2] = new Solver_2019_04_2();
  m_solvers[2019][5][1] = new Solver_2019_05_1();
  m_solvers[2019][5][2] = new Solver_2019_05_2();
  m_solvers[2019][6][1] = new Solver_2019_06_1();
  m_solvers[2019][6][2] = new Solver_2019_06_2();
  m_solvers[2019][7][1] = new Solver_2019_07_1();
  m_solvers[2019][7][2] = new Solver_2019_07_2();
  m_solvers[2019][8][1] = new Solver_2019_08_1();
  m_solvers[2019][8][2] = new Solver_2019_08_2();
  m_solvers[2019][9][1] = new Solver_2019_09_1();
  m_solvers[2019][9][2] = new Solver_2019_09_2();
  m_solvers[2020][10][1] = new Solver_2020_10_1();
  m_solvers[2020][10][2] = new Solver_2020_10_2();
  m_solvers[2020][11][1] = new Solver_2020_11_1();
  m_solvers[2020][11][2] = new Solver_2020_11_2();
  m_solvers[2020][12][1] = new Solver_2020_12_1();
  m_solvers[2020][12][2] = new Solver_2020_12_2();
  m_solvers[2020][13][1] = new Solver_2020_13_1();
  m_solvers[2020][13][2] = new Solver_2020_13_2();
  m_solvers[2020][14][1] = new Solver_2020_14_1();
  m_solvers[2020][14][2] = new Solver_2020_14_2();
  m_solvers[2020][15][1] = new Solver_2020_15_1();
  m_solvers[2020][15][2] = new Solver_2020_15_2();
  m_solvers[2020][16][1] = new Solver_2020_16_1();
  m_solvers[2020][16][2] = new Solver_2020_16_2();
  m_solvers[2020][17][1] = new Solver_2020_17_1();
  m_solvers[2020][17][2] = new Solver_2020_17_2();
  m_solvers[2020][18][1] = new Solver_2020_18_1();
  m_solvers[2020][18][2] = new Solver_2020_18_2();
  m_solvers[2020][19][1] = new Solver_2020_19_1();
  m_solvers[2020][19][2] = new Solver_2020_19_2();
  m_solvers[2020][1][1] = new Solver_2020_01_1();
  m_solvers[2020][1][2] = new Solver_2020_01_2();
  m_solvers[2020][20][1] = new Solver_2020_20_1();
  m_solvers[2020][20][2] = new Solver_2020_20_2();
  m_solvers[2020][21][1] = new Solver_2020_21_1();
  m_solvers[2020][21][2] = new Solver_2020_21_2();
  m_solvers[2020][22][1] = new Solver_2020_22_1();
  m_solvers[2020][22][2] = new Solver_2020_22_2();
  m_solvers[2020][23][1] = new Solver_2020_23_1();
  m_solvers[2020][23][2] = new Solver_2020_23_2();
  m_solvers[2020][24][1] = new Solver_2020_24_1();
  m_solvers[2020][24][2] = new Solver_2020_24_2();
  m_solvers[2020][25][1] = new Solver_2020_25_1();
  m_solvers[2020][25][2] = new Solver_2020_25_2();
  m_solvers[2020][2][1] = new Solver_2020_02_1();
  m_solvers[2020][2][2] = new Solver_2020_02_2();
  m_solvers[2020][3][1] = new Solver_2020_03_1();
  m_solvers[2020][3][2] = new Solver_2020_03_2();
  m_solvers[2020][4][1] = new Solver_2020_04_1();
  m_solvers[2020][4][2] = new Solver_2020_04_2();
  m_solvers[2020][5][1] = new Solver_2020_05_1();
  m_solvers[2020][5][2] = new Solver_2020_05_2();
  m_solvers[2020][6][1] = new Solver_2020_06_1();
  m_solvers[2020][6][2] = new Solver_2020_06_2();
  m_solvers[2020][7][1] = new Solver_2020_07_1();
  m_solvers[2020][7][2] = new Solver_2020_07_2();
  m_solvers[2020][8][1] = new Solver_2020_08_1();
  m_solvers[2020][8][2] = new Solver_2020_08_2();
  m_solvers[2020][9][1] = new Solver_2020_09_1();
  m_solvers[2020][9][2] = new Solver_2020_09_2();
  m_solvers[2021][10][1] = new Solver_2021_10_1();
  m_solvers[2021][10][2] = new Solver_2021_10_2();
  m_solvers[2021][11][1] = new Solver_2021_11_1();
  m_solvers[2021][11][2] = new Solver_2021_11_2();
  m_solvers[2021][12][1] = new Solver_2021_12_1();
  m_solvers[2021][12][2] = new Solver_2021_12_2();
  m_solvers[2021][13][1] = new Solver_2021_13_1();
  m_solvers[2021][13][2] = new Solver_2021_13_2();
  m_solvers[2021][14][1] = new Solver_2021_14_1();
  m_solvers[2021][14][2] = new Solver_2021_14_2();
  m_solvers[2021][15][1] = new Solver_2021_15_1();
  m_solvers[2021][15][2] = new Solver_2021_15_2();
  m_solvers[2021][16][1] = new Solver_2021_16_1();
  m_solvers[2021][16][2] = new Solver_2021_16_2();
  m_solvers[2021][17][1] = new Solver_2021_17_1();
  m_solvers[2021][17][2] = new Solver_2021_17_2();
  m_solvers[2021][18][1] = new Solver_2021_18_1();
  m_solvers[2021][18][2] = new Solver_2021_18_2();
  m_solvers[2021][19][1] = new Solver_2021_19_1();
  m_solvers[2021][19][2] = new Solver_2021_19_2();
  m_solvers[2021][1][1] = new Solver_2021_01_1();
  m_solvers[2021][1][2] = new Solver_2021_01_2();
  m_solvers[2021][20][1] = new Solver_2021_20_1();
  m_solvers[2021][20][2] = new Solver_2021_20_2();
  m_solvers[2021][21][1] = new Solver_2021_21_1();
  m_solvers[2021][21][2] = new Solver_2021_21_2();
  m_solvers[2021][22][1] = new Solver_2021_22_1();
  m_solvers[2021][22][2] = new Solver_2021_22_2();
  m_solvers[2021][23][1] = new Solver_2021_23_1();
  m_solvers[2021][23][2] = new Solver_2021_23_2();
  m_solvers[2021][2][1] = new Solver_2021_02_1();
  m_solvers[2021][2][2] = new Solver_2021_02_2();
  m_solvers[2021][3][1] = new Solver_2021_03_1();
  m_solvers[2021][3][2] = new Solver_2021_03_2();
  m_solvers[2021][4][1] = new Solver_2021_04_1();
  m_solvers[2021][4][2] = new Solver_2021_04_2();
  m_solvers[2021][5][1] = new Solver_2021_05_1();
  m_solvers[2021][5][2] = new Solver_2021_05_2();
  m_solvers[2021][6][1] = new Solver_2021_06_1();
  m_solvers[2021][6][2] = new Solver_2021_06_2();
  m_solvers[2021][7][1] = new Solver_2021_07_1();
  m_solvers[2021][7][2] = new Solver_2021_07_2();
  m_solvers[2021][8][1] = new Solver_2021_08_1();
  m_solvers[2021][8][2] = new Solver_2021_08_2();
  m_solvers[2021][9][1] = new Solver_2021_09_1();
  m_solvers[2021][9][2] = new Solver_2021_09_2();
  m_solvers[2022][10][1] = new Solver_2022_10_1();
  m_solvers[2022][10][2] = new Solver_2022_10_2();
  m_solvers[2022][11][1] = new Solver_2022_11_1();
  m_solvers[2022][11][2] = new Solver_2022_11_2();
  m_solvers[2022][12][1] = new Solver_2022_12_1();
  m_solvers[2022][12][2] = new Solver_2022_12_2();
  m_solvers[2022][13][1] = new Solver_2022_13_1();
  m_solvers[2022][13][2] = new Solver_2022_13_2();
  m_solvers[2022][14][1] = new Solver_2022_14_1();
  m_solvers[2022][14][2] = new Solver_2022_14_2();
  m_solvers[2022][15][1] = new Solver_2022_15_1();
  m_solvers[2022][15][2] = new Solver_2022_15_2();
  m_solvers[2022][16][1] = new Solver_2022_16_1();
  m_solvers[2022][16][2] = new Solver_2022_16_2();
  m_solvers[2022][1][1] = new Solver_2022_01_1();
  m_solvers[2022][1][2] = new Solver_2022_01_2();
  m_solvers[2022][2][1] = new Solver_2022_02_1();
  m_solvers[2022][2][2] = new Solver_2022_02_2();
  m_solvers[2022][3][1] = new Solver_2022_03_1();
  m_solvers[2022][3][2] = new Solver_2022_03_2();
  m_solvers[2022][4][1] = new Solver_2022_04_1();
  m_solvers[2022][4][2] = new Solver_2022_04_2();
  m_solvers[2022][5][1] = new Solver_2022_05_1();
  m_solvers[2022][5][2] = new Solver_2022_05_2();
  m_solvers[2022][6][1] = new Solver_2022_06_1();
  m_solvers[2022][6][2] = new Solver_2022_06_2();
  m_solvers[2022][7][1] = new Solver_2022_07_1();
  m_solvers[2022][7][2] = new Solver_2022_07_2();
  m_solvers[2022][8][1] = new Solver_2022_08_1();
  m_solvers[2022][8][2] = new Solver_2022_08_2();
  m_solvers[2022][9][1] = new Solver_2022_09_1();
  m_solvers[2022][9][2] = new Solver_2022_09_2();
  m_solvers[2023][10][1] = new Solver_2023_10_1();
  m_solvers[2023][10][2] = new Solver_2023_10_2();
  m_solvers[2023][11][1] = new Solver_2023_11_1();
  m_solvers[2023][11][2] = new Solver_2023_11_2();
  m_solvers[2023][12][1] = new Solver_2023_12_1();
  m_solvers[2023][12][2] = new Solver_2023_12_2();
  m_solvers[2023][13][1] = new Solver_2023_13_1();
  m_solvers[2023][13][2] = new Solver_2023_13_2();
  m_solvers[2023][14][1] = new Solver_2023_14_1();
  m_solvers[2023][14][2] = new Solver_2023_14_2();
  m_solvers[2023][15][1] = new Solver_2023_15_1();
  m_solvers[2023][15][2] = new Solver_2023_15_2();
  m_solvers[2023][16][1] = new Solver_2023_16_1();
  m_solvers[2023][16][2] = new Solver_2023_16_2();
  m_solvers[2023][17][1] = new Solver_2023_17_1();
  m_solvers[2023][17][2] = new Solver_2023_17_2();
  m_solvers[2023][18][1] = new Solver_2023_18_1();
  m_solvers[2023][18][2] = new Solver_2023_18_2();
  m_solvers[2023][19][1] = new Solver_2023_19_1();
  m_solvers[2023][19][2] = new Solver_2023_19_2();
  m_solvers[2023][1][1] = new Solver_2023_01_1();
  m_solvers[2023][1][2] = new Solver_2023_01_2();
  m_solvers[2023][20][1] = new Solver_2023_20_1();
  m_solvers[2023][20][2] = new Solver_2023_20_2();
  m_solvers[2023][21][1] = new Solver_2023_21_1();
  m_solvers[2023][21][2] = new Solver_2023_21_2();
  m_solvers[2023][22][1] = new Solver_2023_22_1();
  m_solvers[2023][22][2] = new Solver_2023_22_2();
  m_solvers[2023][23][1] = new Solver_2023_23_1();
  m_solvers[2023][23][2] = new Solver_2023_23_2();
  m_solvers[2023][24][1] = new Solver_2023_24_1();
  m_solvers[2023][24][2] = new Solver_2023_24_2();
  m_solvers[2023][25][1] = new Solver_2023_25_1();
  m_solvers[2023][25][2] = new Solver_2023_25_2();
  m_solvers[2023][2][1] = new Solver_2023_02_1();
  m_solvers[2023][2][2] = new Solver_2023_02_2();
  m_solvers[2023][3][1] = new Solver_2023_03_1();
  m_solvers[2023][3][2] = new Solver_2023_03_2();
  m_solvers[2023][4][1] = new Solver_2023_04_1();
  m_solvers[2023][4][2] = new Solver_2023_04_2();
  m_solvers[2023][5][1] = new Solver_2023_05_1();
  m_solvers[2023][5][2] = new Solver_2023_05_2();
  m_solvers[2023][6][1] = new Solver_2023_06_1();
  m_solvers[2023][6][2] = new Solver_2023_06_2();
  m_solvers[2023][7][1] = new Solver_2023_07_1();
  m_solvers[2023][7][2] = new Solver_2023_07_2();
  m_solvers[2023][8][1] = new Solver_2023_08_1();
  m_solvers[2023][8][2] = new Solver_2023_08_2();
  m_solvers[2023][9][1] = new Solver_2023_09_1();
  m_solvers[2023][9][2] = new Solver_2023_09_2();
  m_solvers[2024][10][1] = new Solver_2024_10_1();
  m_solvers[2024][10][2] = new Solver_2024_10_2();
  m_solvers[2024][11][1] = new Solver_2024_11_1();
  m_solvers[2024][11][2] = new Solver_2024_11_2();
  m_solvers[2024][12][1] = new Solver_2024_12_1();
  m_solvers[2024][12][2] = new Solver_2024_12_2();
  m_solvers[2024][13][1] = new Solver_2024_13_1();
  m_solvers[2024][13][2] = new Solver_2024_13_2();
  m_solvers[2024][14][1] = new Solver_2024_14_1();
  m_solvers[2024][14][2] = new Solver_2024_14_2();
  m_solvers[2024][15][1] = new Solver_2024_15_1();
  m_solvers[2024][15][2] = new Solver_2024_15_2();
  m_solvers[2024][16][1] = new Solver_2024_16_1();
  m_solvers[2024][16][2] = new Solver_2024_16_2();
  m_solvers[2024][17][1] = new Solver_2024_17_1();
  m_solvers[2024][17][2] = new Solver_2024_17_2();
  m_solvers[2024][18][1] = new Solver_2024_18_1();
  m_solvers[2024][18][2] = new Solver_2024_18_2();
  m_solvers[2024][19][1] = new Solver_2024_19_1();
  m_solvers[2024][19][2] = new Solver_2024_19_2();
  m_solvers[2024][1][1] = new Solver_2024_01_1();
  m_solvers[2024][1][2] = new Solver_2024_01_2();
  m_solvers[2024][20][1] = new Solver_2024_20_1();
  m_solvers[2024][20][2] = new Solver_2024_20_2();
  m_solvers[2024][21][1] = new Solver_2024_21_1();
  m_solvers[2024][21][2] = new Solver_2024_21_2();
  m_solvers[2024][22][1] = new Solver_2024_22_1();
  m_solvers[2024][22][2] = new Solver_2024_22_2();
  m_solvers[2024][23][1] = new Solver_2024_23_1();
  m_solvers[2024][23][2] = new Solver_2024_23_2();
  m_solvers[2024][24][1] = new Solver_2024_24_1();
  m_solvers[2024][24][2] = new Solver_2024_24_2();
  m_solvers[2024][25][1] = new Solver_2024_25_1();
  m_solvers[2024][25][2] = new Solver_2024_25_2();
  m_solvers[2024][2][1] = new Solver_2024_02_1();
  m_solvers[2024][2][2] = new Solver_2024_02_2();
  m_solvers[2024][3][1] = new Solver_2024_03_1();
  m_solvers[2024][3][2] = new Solver_2024_03_2();
  m_solvers[2024][4][1] = new Solver_2024_04_1();
  m_solvers[2024][4][2] = new Solver_2024_04_2();
  m_solvers[2024][5][1] = new Solver_2024_05_1();
  m_solvers[2024][5][2] = new Solver_2024_05_2();
  m_solvers[2024][6][1] = new Solver_2024_06_1();
  m_solvers[2024][6][2] = new Solver_2024_06_2();
  m_solvers[2024][7][1] = new Solver_2024_07_1();
  m_solvers[2024][7][2] = new Solver_2024_07_2();
  m_solvers[2024][8][1] = new Solver_2024_08_1();
  m_solvers[2024][8][2] = new Solver_2024_08_2();
  m_solvers[2024][9][1] = new Solver_2024_09_1();
  m_solvers[2024][9][2] = new Solver_2024_09_2();
}

Solvers::~Solvers() {
  for (auto year : m_solvers.values())
    for (auto day : year.values())
      for (auto solver : day.values())
        delete solver;
}

Solver *Solvers::operator()(int year, int day, int puzzle) const {
  if (m_solvers.contains(year))
    if (m_solvers[year].contains(day))
      if (m_solvers[year][day].contains(puzzle))
        return m_solvers[year][day][puzzle];
  return nullptr;
}
