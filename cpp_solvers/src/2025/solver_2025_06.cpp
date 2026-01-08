#include <solvers.hpp>

namespace puzzle_2025_06 {

using Int = long long unsigned int;

class MathHomework {
public:
  MathHomework(const std::string &input) {
    m_lines = aoc::splitLines(input);
    const auto nb_lines = static_cast<int>(m_lines.size());
    if (nb_lines < 2) {
      throw std::invalid_argument("bad number of lines");
    }
    m_length = nb_lines - 1;
    m_values.reserve(m_length);
    for (auto line : m_lines) {
      aoc::contractWhiteSpaces(line);
      if (static_cast<int>(m_values.size()) < m_length) {
        const auto values = aoc::splitToULongLongInt(line, ' ');
        if (m_width == 0) {
          m_width = values.size();
        } else if (values.size() != m_width) {
          throw std::invalid_argument("width mismatch");
        }
        m_values.emplace_back();
        m_values.back().reserve(m_width);
        for (const auto value : values) {
          m_values.back().emplace_back(value);
        }
      } else {
        aoc::remove(line, ' ');
        m_operators = line;
        if (m_operators.size() != m_width) {
          throw std::invalid_argument("wrong size for operators string");
        }
      }
    }
  }

  std::string solveOne() const {
    auto grand_total = Int{0};
    for (auto j = 0; j < m_width; ++j) {
      auto solution = m_operators[j] == '*' ? Int{1} : Int{0};
      for (auto i = 0; i < m_length; ++i) {
        if (m_operators[j] == '*') {
          solution *= m_values[i][j];
        } else if (m_operators[j] == '+') {
          solution += m_values[i][j];
        } else {
          throw std::invalid_argument("unknown operator");
        }
      }
      grand_total += solution;
    }
    return std::to_string(grand_total);
  }

  std::string solveTwo() const {
    auto grand_total = Int{0};
    auto column = 0;
    for (const auto &op : m_operators) {
      auto solution = op == '*' ? Int{1} : Int{0};
      for (;;) {
        auto value = Int{0};
        auto power = Int{1};
        for (auto i = m_length - 1; i >= 0; --i) {
          if (aoc::isDigit(m_lines[i][column])) {
            value += power * aoc::toULongLongInt(m_lines[i].substr(column, 1u));
            power *= Int{10};
          }
        }
        ++column;
        if (value == Int{0}) {
          break;
        }
        if (op == '*') {
          solution *= value;
        } else if (op == '+') {
          solution += value;
        } else {
          throw std::invalid_argument("unknown operator");
        }
      }
      grand_total += solution;
    }
    return std::to_string(grand_total);
  }

private:
  int m_length{0};
  int m_width{0};
  std::vector<std::vector<Int>> m_values;
  std::string m_operators;
  std::deque<std::string> m_lines;
};

} // namespace puzzle_2025_06

namespace aoc {

Result solver_2025_06(const std::string &input) {
  const auto homework = puzzle_2025_06::MathHomework(input);
  auto res = Result();
  res.part_one_solution = homework.solveOne();
  res.part_two_solution = homework.solveTwo();
  return res;
}

}
