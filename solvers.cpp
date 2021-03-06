#include <solvers.h>
#include <mainwindow.h>

#include <2019/puzzle_2019_01.h>
#include <2019/puzzle_2019_02.h>
#include <2019/puzzle_2019_03.h>
#include <2019/puzzle_2019_04.h>
#include <2019/puzzle_2019_05.h>
#include <2019/puzzle_2019_06.h>
#include <2019/puzzle_2019_07.h>
#include <2019/puzzle_2019_08.h>

#include <2020/puzzle_2020_01.h>
#include <2020/puzzle_2020_02.h>
#include <2020/puzzle_2020_03.h>
#include <2020/puzzle_2020_04.h>
#include <2020/puzzle_2020_05.h>
#include <2020/puzzle_2020_06.h>
#include <2020/puzzle_2020_07.h>
#include <2020/puzzle_2020_08.h>
#include <2020/puzzle_2020_09.h>
#include <2020/puzzle_2020_10.h>
#include <2020/puzzle_2020_11.h>
#include <2020/puzzle_2020_12.h>
#include <2020/puzzle_2020_13.h>
#include <2020/puzzle_2020_14.h>
#include <2020/puzzle_2020_15.h>
#include <2020/puzzle_2020_16.h>
#include <2020/puzzle_2020_17.h>
#include <2020/puzzle_2020_18.h>
#include <2020/puzzle_2020_19.h>
#include <2020/puzzle_2020_20.h>
#include <2020/puzzle_2020_21.h>
#include <2020/puzzle_2020_22.h>
#include <2020/puzzle_2020_23.h>
#include <2020/puzzle_2020_24.h>
#include <2020/puzzle_2020_25.h>

void Solver::onInputReceived(const QString&) {}

IntcodeComputerUsingSolver::~IntcodeComputerUsingSolver() { delete m_computer; }

void IntcodeComputerUsingSolver::onInputReceived(const QString& input)
{
  if (input.isEmpty()) {
    emit askInput("Intcode computer is asking for an integer input");
    return;
  }
  bool ok;
  int integer = input.toInt(&ok);
  if (!ok) {
    emit askInput("Intcode computer is asking for an integer input");
    return;
  }
  emit integerInputReceived(integer);
}

Solvers::Solvers()
{
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

  m_solvers[2020][1][1] = new Solver_2020_01_1();
  m_solvers[2020][1][2] = new Solver_2020_01_2();
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
}

Solvers::~Solvers()
{
  for (auto year : m_solvers.values())
    for (auto day : year.values())
      for (auto solver : day.values())
        delete solver;
}

Solver* Solvers::operator()(int year, int day, int puzzle) const
{
  if (m_solvers.contains(year))
    if (m_solvers[year].contains(day))
      if (m_solvers[year][day].contains(puzzle))
        return m_solvers[year][day][puzzle];
  return nullptr;
}

