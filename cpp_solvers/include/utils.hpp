#pragma once

#include <parsers.hpp>

namespace aoc {

bool contains(const std::string &str, char c);
bool contains(const std::string &str, const std::string &pattern);

void contractWhiteSpaces(std::string &str);

bool isDigit(char c);

void remove(std::string &str, char pattern);
void remove(std::string &str, const std::string &pattern);

std::string repeatedString(const std::string &str, std::size_t n);

} // namespace aoc
