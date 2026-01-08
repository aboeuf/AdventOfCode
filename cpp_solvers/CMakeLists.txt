add_library(cpp_solvers
  STATIC
    src/2025/solver_2025_01.cpp
    src/2025/solver_2025_02.cpp
    src/2025/solver_2025_03.cpp
    src/2025/solver_2025_04.cpp
    src/2025/solver_2025_05.cpp
    src/2025/solver_2025_06.cpp
    src/2025/solver_2025_08.cpp
    src/aoc.cpp
    src/converters.cpp
    src/parsers.cpp
    src/utils.cpp
)

target_include_directories(cpp_solvers PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
set_target_properties(cpp_solvers PROPERTIES POSITION_INDEPENDENT_CODE ON)

set(CMAKE_SHARED_MODULE_PREFIX "")

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(Boost COMPONENTS python REQUIRED)

add_library(aoc_bindings MODULE src/bindings.cpp)

set_target_properties(aoc_bindings PROPERTIES OUTPUT_NAME "aoc")

target_include_directories(aoc_bindings PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/..)

target_link_libraries(aoc_bindings
  cpp_solvers
  Boost::python
  Python3::Module
)
