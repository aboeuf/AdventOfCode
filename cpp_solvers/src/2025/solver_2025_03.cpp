#include <solvers.hpp>

#include <limits>

namespace puzzle_2025_03 {

using Int = unsigned long long;

class BatteryBank {
public:
  BatteryBank(const std::string &input) {
    const auto n = std::size(input);
    m_data.resize(n);
    for (auto i = 0u; i < n; ++i) {
      m_data[i] = aoc::toUShortInt(input.substr(i, 1u));
    }
  }

  Int getMaxJoltage(std::size_t nb_batteries) const {
    return getMaxJoltageRecursive(nb_batteries, 0, 0);
  }

private:
  Int getMaxJoltageRecursive(std::size_t nb_batteries, std::size_t start,
                             Int joltage) const {
    auto max_value = ushort{0};
    auto max_index = std::size_t{0};
    for (auto i = start; i < m_data.size() - nb_batteries + 1u; ++i) {
      if (m_data[i] > max_value) {
        max_value = m_data[i];
        max_index = i;
      }
    }
    joltage = Int{10} * joltage + static_cast<Int>(max_value);
    if (nb_batteries == 1u) {
      return joltage;
    }
    return getMaxJoltageRecursive(nb_batteries - 1, max_index + 1, joltage);
  }

  std::vector<ushort> m_data;
};

class BatteryBanks {
public:
  BatteryBanks(const std::string &input) {
    const auto lines = aoc::splitLines(input);
    m_banks.reserve(lines.size());
    for (const auto &line : lines) {
      m_banks.emplace_back(line);
    }
  }

  ulong getMaxJoltage(std::size_t nb_batteries) const {
    auto max_joltage = ulong{0};
    for (const auto &bank : m_banks) {
      max_joltage += bank.getMaxJoltage(nb_batteries);
    }
    return max_joltage;
  }

private:
  std::vector<BatteryBank> m_banks;
};

} // namespace puzzle_2025_03

namespace aoc {

Result solver_2025_03(const std::string &input) {
  const auto banks = puzzle_2025_03::BatteryBanks(input);
  auto res = Result();
  res.part_one_solution = std::to_string(banks.getMaxJoltage(2));
  res.part_two_solution = std::to_string(banks.getMaxJoltage(12));
  return res;
}

} // namespace aoc
