#pragma once

#include <QDebug>
#include <QHash>
#include <QStringList>
#include <QVector>
#include <functional>
#include <iso646.h>
#include <optional>

namespace common {

void throwRunTimeError(const QString &message);
void throwInvalidArgumentError(const QString &message);

QStringList splitLines(const QString &input, bool filter_empty_lines = false);
QStringList splitValues(const QString &input, const QChar &split_char = ',');

QVector<short> toShort(const QString &input, const QChar &split_char = ',');
QVector<ushort> toUShort(const QString &input, const QChar &split_char = ',');

QVector<int> toInt(const QString &input, const QChar &split_char = ',');
QVector<uint> toUInt(const QString &input, const QChar &split_char = ',');

QVector<long> toLong(const QString &input, const QChar &split_char = ',');
QVector<ulong> toULong(const QString &input, const QChar &split_char = ',');

QVector<long long> toLongLong(const QString &input,
                              const QChar &split_char = ',');
QVector<unsigned long long> toULongLong(const QString &input,
                                        const QChar &split_char = ',');

template <typename Data, typename Scalar, bool reversed = false> class OpenSet {
public:
  OpenSet() = default;

  bool empty() const { return m_data.isEmpty(); }

  int size() const { return m_data.size(); }

  std::optional<std::pair<Data, Scalar>> pop() {
    if (m_data.isEmpty())
      return std::nullopt;
    auto it = std::min_element(std::cbegin(m_data), std::cend(m_data),
                               [this](const Scalar &lhs, const Scalar &rhs) {
                                 if constexpr (reversed)
                                   return lhs > rhs;
                                 else
                                   return lhs < rhs;
                               });
    if (it == std::end(m_data))
      return std::nullopt;
    auto res = std::make_pair(it.key(), it.value());
    m_data.erase(it);
    return res;
  }

  void push(const Data &data, Scalar cost) {
    if (m_data.contains(data)) {
      auto &old_cost = m_data[data];
      if constexpr (reversed) {
        if (cost > old_cost)
          old_cost = cost;
      } else {
        if (cost < old_cost)
          old_cost = cost;
      }
    } else {
      m_data[data] = cost;
    }
  }

private:
  QHash<Data, Scalar> m_data;
};

} // namespace common
