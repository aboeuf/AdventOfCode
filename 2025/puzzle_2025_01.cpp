#include <2025/puzzle_2025_01.h>
#include <common.h>

namespace puzzle_2025_01 {

class Line
{
public:
    Line(const QString& input) : m_line{input} {}

private:
    QString m_line;
};

class Lines
{
public:
    Lines(const QString& input) {
        const auto lines = common::splitLines(input);
        m_lines.reserve(lines.size());
        for (const auto& line : lines) {
            m_lines.emplace_back(line);
        }
    }

    QString solveOne() const { return "Default"; }
    QString solveTwo() const { return "Default"; }

private:
    std::vector<Line> m_lines;
};

}

void Solver_2025_01_1::solve(const QString& input)
{
    const auto lines = puzzle_2025_01::Lines(input);
    emit finished(lines.solveOne());
}

void Solver_2025_01_2::solve(const QString& input)
{
    const auto lines = puzzle_2025_01::Lines(input);
    emit finished(lines.solveTwo());
}
