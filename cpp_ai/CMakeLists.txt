cmake_minimum_required(VERSION 3.20)
project(ecgen-cpp VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Options
option(BUILD_SHARED_LIBS "Build shared library" OFF)
option(BUILD_TESTING "Build tests" ON)
option(USE_SYSTEM_CPPCORO "Use system cppcoro" OFF)
option(USE_SYSTEM_DOCTEST "Use system doctest" OFF)

# Library configuration
set(LIBRARY_NAME ecgen)
set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Add library
add_library(${LIBRARY_NAME})
add_library(ecgen::ecgen ALIAS ${LIBRARY_NAME})

target_include_directories(${LIBRARY_NAME}
    PUBLIC
        $<BUILD_INTERFACE:${INCLUDE_DIR}>
        $<INSTALL_INTERFACE:include>
)

# Source files
target_sources(${LIBRARY_NAME}
    PRIVATE
        src/combin.cpp
        src/set_partition.cpp
        src/sjt.cpp
        src/gray_code.cpp
        src/ehr.cpp
        src/set_bipart.cpp
)

# Dependencies
if(USE_SYSTEM_CPPCORO)
    find_package(cppcoro REQUIRED)
    target_link_libraries(${LIBRARY_NAME} PUBLIC cppcoro::cppcoro)
else()
    # Add cppcoro as subdirectory or fetch
    message(STATUS "Using bundled cppcoro headers")
    target_include_directories(${LIBRARY_NAME}
        PUBLIC
            $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/cppcoro>
            $<INSTALL_INTERFACE:include/cppcoro>
    )
endif()

# Compiler features
target_compile_features(${LIBRARY_NAME}
    PUBLIC
        cxx_std_20
)

# Additional flags for C++23 features
if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    target_compile_options(${LIBRARY_NAME} PUBLIC "/std:c++latest")
else()
    target_compile_options(${LIBRARY_NAME} PUBLIC "-std=c++23" "-fcoroutines")
endif()

# Install configuration
include(GNUInstallDirs)
install(TARGETS ${LIBRARY_NAME}
    EXPORT ${LIBRARY_NAME}-targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY ${INCLUDE_DIR}/ecgen
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

install(EXPORT ${LIBRARY_NAME}-targets
    FILE ${LIBRARY_NAME}-targets.cmake
    NAMESPACE ecgen::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${LIBRARY_NAME}
)

# Tests
if(BUILD_TESTING)
    if(USE_SYSTEM_DOCTEST)
        find_package(doctest REQUIRED)
    else()
        # Download doctest
        include(FetchContent)
        FetchContent_Declare(
            doctest
            GIT_REPOSITORY https://github.com/doctest/doctest.git
            GIT_TAG v2.4.11
        )
        FetchContent_MakeAvailable(doctest)
    endif()

    # Test executables
    add_executable(test_combin tests/test_combin.cpp)
    target_link_libraries(test_combin PRIVATE ${LIBRARY_NAME} doctest::doctest)
    add_test(NAME test_combin COMMAND test_combin)

    add_executable(test_set_partition tests/test_set_partition.cpp)
    target_link_libraries(test_set_partition PRIVATE ${LIBRARY_NAME} doctest::doctest)
    add_test(NAME test_set_partition COMMAND test_set_partition)

    add_executable(test_sjt tests/test_sjt.cpp)
    target_link_libraries(test_sjt PRIVATE ${LIBRARY_NAME} doctest::doctest)
    add_test(NAME test_sjt COMMAND test_sjt)

    add_executable(test_gray_code tests/test_gray_code.cpp)
    target_link_libraries(test_gray_code PRIVATE ${LIBRARY_NAME} doctest::doctest)
    add_test(NAME test_gray_code COMMAND test_gray_code)

    add_executable(test_ehr tests/test_ehr.cpp)
    target_link_libraries(test_ehr PRIVATE ${LIBRARY_NAME} doctest::doctest)
    add_test(NAME test_ehr COMMAND test_ehr)

    add_executable(test_set_bipart tests/test_set_bipart.cpp)
    target_link_libraries(test_set_bipart PRIVATE ${LIBRARY_NAME} doctest::doctest)
    add_test(NAME test_set_bipart COMMAND test_set_bipart)

    # Enable test discovery
    enable_testing()
endif()

# Examples
add_executable(example_combin examples/combin_example.cpp)
target_link_libraries(example_combin PRIVATE ${LIBRARY_NAME})

add_executable(example_permutations examples/permutations_example.cpp)
target_link_libraries(example_permutations PRIVATE ${LIBRARY_NAME})

# Package configuration
include(CMakePackageConfigHelpers)
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/ecgen-config.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/ecgen-config.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${LIBRARY_NAME}
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/ecgen-config-version.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/ecgen-config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/ecgen-config-version.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/${LIBRARY_NAME}
)