#pragma once
#include <solvers.h>

class Solver_2019_2_1 : public IncodeComputerUsingSolver
{
public:
  void solve(const QString& input) override;

public slots:
  void onComputerStopped() override;
};

class Solver_2019_2_2 : public IncodeComputerUsingSolver
{
public:
  void solve(const QString& input) override;

public slots:
  void onComputerStopped() override;

private:
  std::vector<int> m_program{};
  int m_noun{0};
  int m_verb{0};
};
