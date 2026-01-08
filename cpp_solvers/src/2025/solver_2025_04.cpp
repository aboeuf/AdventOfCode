#include <solvers.hpp>

namespace puzzle_2025_04 {

class Grid {
public:
  Grid(const std::string &input) {
    const auto lines = aoc::splitLines(input);
    for (auto i = 0; i < static_cast<int>(lines.size()); ++i) {
      const auto &line = lines.at(i);
      for (auto j = 0; j < static_cast<int>(line.size()); ++j) {
        if (lines.at(i).at(j) == '@') {
          m_grid[i][j] = 0;
        }
      }
    }
    for (const auto &[i, row] : m_grid) {
      for (const auto &[j, _] : row) {
        addToNeighbors(i, j, 1);
      }
    }
  }

  std::deque<std::pair<int, int>> getRemovableRolls() const {
    auto removable_rolls = std::deque<std::pair<int, int>>{};
    for (const auto &[i, row] : m_grid) {
      for (const auto &[j, nb_neighbors] : row) {
        if (nb_neighbors < 4) {
          removable_rolls.emplace_back(i, j);
        }
      }
    }
    return removable_rolls;
  }

  void addNeighbor(int i, int j, int increment) {
    auto it_i = m_grid.find(i);
    if (it_i != m_grid.end()) {
      auto it_j = it_i->second.find(j);
      if (it_j != it_i->second.end()) {
        it_j->second += increment;
      }
    }
  }

  void addToNeighbors(int i, int j, int increment) {
    for (auto ni = i - 1; ni < i + 2; ++ni) {
      for (auto nj = j - 1; nj < j + 2; ++nj) {
        if (i != ni or j != nj) {
          addNeighbor(ni, nj, increment);
        }
      }
    }
  }

  void removeRoll(int i, int j) {
    auto it_i = m_grid.find(i);
    if (it_i != m_grid.end()) {
      auto it_j = it_i->second.find(j);
      if (it_j != it_i->second.end()) {
        addToNeighbors(i, j, -1);
        it_i->second.erase(it_j);
        if (it_i->second.empty()) {
          m_grid.erase(it_i);
        }
      }
    }
  }

  bool removeRolls(uint &nb_removed) {
    const auto removable_rolls = getRemovableRolls();
    for (const auto &[i, j] : removable_rolls) {
      removeRoll(i, j);
    }
    nb_removed += std::size(removable_rolls);
    return not removable_rolls.empty();
  }

  uint removeAllRolls() {
    auto total_removed = 0u;
    while (removeRolls(total_removed)) {
    }
    return total_removed;
  }

private:
  std::unordered_map<int, std::unordered_map<int, int>> m_grid;
};

} // namespace puzzle_2025_04

namespace aoc {

Result solver_2025_04(const std::string &input) {
  auto grid = puzzle_2025_04::Grid(input);
  auto res = Result();
  res.part_one_solution = std::to_string(std::size(grid.getRemovableRolls()));
  res.part_two_solution = std::to_string(grid.removeAllRolls());
  return res;
}

} // namespace aoc
