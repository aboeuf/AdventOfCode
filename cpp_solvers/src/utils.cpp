#include <utils.hpp>

#include <algorithm>

namespace aoc {

bool contains(const std::string &str, char c) {
  return std::any_of(std::cbegin(str), std::cend(str),
                     [&c](const char &_c) { return _c == c; });
}

bool contains(const std::string &str, const std::string &pattern) {
  return str.find(pattern) != std::string::npos;
}

void contractWhiteSpaces(std::string &str) {
  for (auto start_pos = 0u; start_pos < str.size();) {
    const auto found_pos = str.find("  ", start_pos);
    if (found_pos == std::string::npos) {
      return;
    }
    str.replace(found_pos, 2u, " ");
    start_pos = found_pos;
  }
}

bool isDigit(char c) {
  static constexpr auto digits = "0123456789";
  return contains(digits, c);
}

void remove(std::string &str, char pattern) {
  for (auto pos = 0u; pos < str.size();) {
    if (str[pos] == pattern) {
      str.erase(pos, 1u);
    } else {
      ++pos;
    }
  }
}

void remove(std::string &str, const std::string &pattern) {
  const auto n = pattern.size();
  for (auto start_pos = 0u; start_pos < str.size();) {
    const auto found_pos = str.find(pattern, start_pos);
    if (found_pos == std::string::npos) {
      return;
    }
    str.erase(found_pos, n);
    start_pos = found_pos;
  }
}

std::string repeatedString(const std::string &str, std::size_t n) {
  auto res = std::string{};
  for (auto i = 0u; i < n; ++i) {
    res += str;
  }
  return res;
}

} // namespace aoc
