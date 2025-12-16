-- xmake.lua for ecgen C++ library
set_project("ecgen-cpp")
set_version("0.1.0")

-- Set C++ standard
set_languages("c++23")

-- Add rules
add_rules("mode.debug", "mode.release")
add_rules("plugin.vsxmake.autoupdate")

-- Options
option("shared", {description = "Build shared library", default = false})
option("tests", {description = "Build tests", default = true})

-- Library target
target("ecgen")
    set_kind("$(kind)")
    set_default(true)
    
    -- Headers
    add_headerfiles("include/(ecgen/**.hpp)")
    
    -- Sources
    add_files("src/**.cpp")
    
    -- Include directories
    add_includedirs("include", "include/cppcoro", {public = true})
    
    -- C++ features
    add_cxxflags("/std:c++latest", {tools = {"msvc"}})
    add_cxxflags("-std=c++23", "-fcoroutines", {tools = {"gcc", "clang"}})
    
    -- Set kind based on option
    if has_config("shared") then
        set_kind("shared")
    else
        set_kind("static")
    end

-- Test targets
if has_config("tests") then
    -- Download doctest if not present
    if not os.exists("doctest") then
        os.exec("git clone --depth 1 --branch v2.4.11 https://github.com/doctest/doctest.git")
    end
    
    add_includedirs("doctest", {public = false})
    
    -- Test executables
    local test_targets = {
        "test_combin",
        "test_set_partition", 
        "test_sjt",
        "test_gray_code",
        "test_ehr",
        "test_set_bipart"
    }
    
    for _, test_name in ipairs(test_targets) do
        target(test_name)
            set_kind("binary")
            add_files("tests/" .. test_name .. ".cpp")
            add_deps("ecgen")
            add_includedirs("doctest")
            
            -- Run tests after build in debug mode
            if is_mode("debug") then
                after_build(function (target)
                    os.exec(target:targetfile())
                end)
            end
    end
end

-- Example targets
target("example_combin")
    set_kind("binary")
    add_files("examples/combin_example.cpp")
    add_deps("ecgen")

target("example_permutations")
    set_kind("binary")
    add_files("examples/permutations_example.cpp")
    add_deps("ecgen")

-- Package configuration
on_install(function (target)
    -- Install headers
    os.cp("include/ecgen", path.join(target:installdir(), "include"))
    
    -- Install library
    if target:kind() == "shared" then
        os.cp(target:targetfile(), path.join(target:installdir(), "lib"))
    else
        os.cp(target:targetfile(), path.join(target:installdir(), "lib"))
    end
    
    -- Install cmake config
    local cmake_config = [[
# ecgen CMake config
include(CMakeFindDependencyMacro)

if(NOT TARGET ecgen::ecgen)
    add_library(ecgen::ecgen INTERFACE IMPORTED)
    set_target_properties(ecgen::ecgen PROPERTIES
        INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_CURRENT_LIST_DIR}/../../include"
        INTERFACE_COMPILE_FEATURES "cxx_std_23;cxx_concepts;cxx_coroutines"
    )
    
    if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/ecgen.lib")
        set_target_properties(ecgen::ecgen PROPERTIES
            IMPORTED_LOCATION "${CMAKE_CURRENT_LIST_DIR}/ecgen.lib"
        )
    elseif(EXISTS "${CMAKE_CURRENT_LIST_DIR}/libecgen.a")
        set_target_properties(ecgen::ecgen PROPERTIES
            IMPORTED_LOCATION "${CMAKE_CURRENT_LIST_DIR}/libecgen.a"
        )
    endif()
endif()
]]
    
    os.writefile(path.join(target:installdir(), "lib/cmake/ecgen/ecgen-config.cmake"), cmake_config)
end)

-- Clean command
on_clean(function (target)
    os.rm("doctest")
end)