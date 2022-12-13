#include <2022/puzzle_2022_10.h>
#include <common.h>
#include <functional>

namespace puzzle_2022_10 {

class Instruction
{
public:
    Instruction() = default;

    Instruction(QString code) {
        if (code == "noop") {
            m_remaining_ticks = 1u;
        } else if (code.startsWith("addx ")) {
            code.remove(0, 4);
            bool ok;
            const auto value = code.toInt(&ok);
            if (not ok)
                throw std::invalid_argument(QString("addx: cannot convert \"%1\" to int")
                                            .arg(code).toStdString());
            m_operation =  [value](auto i) { return i + value; };
            m_remaining_ticks = 2u;
        } else {
            throw std::invalid_argument(QString("unrecognized instruction \"%1\"")
                                        .arg(code).toStdString());
        }
    }

    bool finished() const { return m_remaining_ticks == 0u; }

    int apply(int reg) const { return m_operation(reg); }

    void tick() {
        if (m_remaining_ticks == 0u)
            throw std::invalid_argument("no more ticks");
        --m_remaining_ticks;
    }

private:
    std::function<int(int)> m_operation = [](auto i) { return i; };
    uint m_remaining_ticks{0u};
};

class ClockCircuit
{
public:
    ClockCircuit(const QString& program)
    {
        auto lines = common::splitLines(program);
        const auto get_next_instruction = [this, &lines]() {
            if (lines.empty())
                return false;
            m_current_instruction = Instruction{lines.front()};
            lines.pop_front();
            return true;
        };

        for (;;) {
            if (m_current_instruction.finished()) {
                m_register = m_current_instruction.apply(m_register);
                if (not get_next_instruction())
                    break;
            } else {
                tick();
            }
        }
    }

    QString puzzleOne() const { return QString("%1").arg(m_puzzle_one); }
    const QString& CRT() const { return m_CRT; }

    QString m_log;

private:
    void tick() {
        if (m_current_cycle >= 20 and
                m_current_cycle <= 220 and
                    (m_current_cycle - 20) % 40 == 0)
            m_puzzle_one += m_current_cycle * m_register;
        m_current_instruction.tick();
        m_log += QString("C[%1] R[%2] S[%3]\n")
                .arg(m_current_cycle)
                .arg(m_register)
                .arg(m_current_cycle * m_register);

        const auto pixel_position = (m_current_cycle - 1) % 40;
        m_CRT.push_back(std::abs(m_register - pixel_position) < 2 ? '#' : '.');
        if (pixel_position == 39)
            m_CRT.push_back('\n');
        ++m_current_cycle;
    }

    int m_puzzle_one{0};
    Instruction m_current_instruction{};
    int m_register{1};
    int m_current_cycle{1};
    QString m_CRT{};
};

}

void Solver_2022_10_1::solve(const QString& input)
{
    const auto circuit = puzzle_2022_10::ClockCircuit(input);
    emit finished(circuit.puzzleOne());
}

void Solver_2022_10_2::solve(const QString& input)
{
    const auto circuit = puzzle_2022_10::ClockCircuit(input);
    emit output(circuit.CRT());
    emit finished("Done");
}
