add_rules("mode.debug", "mode.release")

set_languages("c++20")

target("ecgen")
    set_kind("static")
    -- Headers
    add_headerfiles("include/(ecgen/**.hpp)")

    -- Sources
    add_files("src/**.cpp")

    -- Include directories
    add_includedirs("include", "include/cppcoro", {public = true})

    -- C++ features
    add_cxxflags("/std:c++latest", {tools = {"msvc"}})
    add_cxxflags("-std=c++23", "-fcoroutines", {tools = {"gcc", "clang"}})

    if is_mode("debug") then
        add_defines("DEBUG")
        add_cxxflags("-g", "-O0")
    else
        add_cxxflags("-O3")
    end

-- target("test_ecgen")
--     set_kind("binary")
--     add_deps("ecgen")
--     add_files("tests/**.cpp")
--     add_includedirs("include")
--
--     -- Check if doctest exists, warn if not but don't download
--     before_build(function (target)
--         local doctest_path = path.join(target:scriptdir(), "tests", "doctest.h")
--         if not os.isfile(doctest_path) then
--             print("Warning: doctest.h not found. Tests will not compile.")
--             print("You can download it manually from:")
--             print("https://raw.githubusercontent.com/doctest/doctest/v2.4.11/doctest/doctest.h")
--         end
--     end)


target("combin_example")
    set_kind("binary")
    add_deps("ecgen")
    add_files("examples/combin_example.cpp")
    add_includedirs("include")

target("permutations_example")
    set_kind("binary")
    add_deps("ecgen")
    add_files("examples/permutations_example.cpp")
    add_includedirs("include")

-- Package configuration
package("ecgen")
    set_description("Low-Discrepancy Sequence Generator C++ Library")
    set_license("MIT")

    add_urls("https://github.com/luk036/ec-gen.git")
    add_versions("1.0.0", "dcda260be4010b1509c1dcb9d5f3edcddba9cc51")

    on_install(function (package)
        import("package.tools.cmake").install(package)
    end)
