cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD 17)

#
# This project creates a package called mps-tlib
# which has a library called tmisc.
#
# Usage:
#
#   find_package(mps-tlib)
#   ...
#   target_link_libraries(app PUBLIC tmisc)
#

# The project generates a static library only.
# To build dynamic/shared libraries uncomment the following.
#
# option(BUILD_SHARED_LIBS "Build the shared library" ON)

# What about namespace stuff?
# https://cliutils.gitlab.io/modern-cmake/chapters/install/exporting.html

# Following are scanned by tools/get_version.py
set(THE_PROJECT_NAME "mps-tlib")
set(THE_PROJECT_MAJOR "2")
set(THE_PROJECT_MINOR "2")
set(THE_PROJECT_MICRO "1")

set(PROJECT_VERSION_STRING "${THE_PROJECT_MAJOR}.${THE_PROJECT_MINOR}.${THE_PROJECT_MICRO}" )
message("VER ${PROJECT_VERSION_STRING}")

project(${THE_PROJECT_NAME}  VERSION "${PROJECT_VERSION_STRING}" )

# Add the library target

set(LIB tmisc)
add_library(${LIB})

set(tmisc_src tmisc/tmisc.cc tmisc/tpriv.h)  # private headers are included here
set(tmisc_hdrs  tmisc/tmisc.h)  # public headers

# Use the same version string for the library as for the project.
set(LIB_VERSION_STRING "${LIB}.${THE_PROJECT_MINOR}.${THE_PROJECT_MICRO}" )
set(LIB_VERSION_MAJOR "${THE_PROJECT_MAJOR}" )

set_target_properties(${LIB} PROPERTIES
    LANGUAGES CXX
    CXX_STANDARD_REQUIRED ON
    CXX_EXTENSIONS OFF
    VERSION ${LIB_VERSION_STRING}
    SOVERSION ${LIB_VERSION_MAJOR}
    PUBLIC_HEADER "${tmisc_hdrs}"
#    CXX_VISIBILITY_PRESET hidden
#    VISIBILITY_INLINES_HIDDEN 1
    )

target_sources(${LIB}
    PRIVATE
        ${tmisc_hdrs}
        ${tmisc_src}
    )

# note extra layer of quotes
target_compile_definitions(${LIB} PRIVATE
   -DPROJECT_NAME="${PROJECT_NAME}"
   -DPROJECT_VERSION_MAJOR="${THE_PROJECT_MAJOR}"
   -DPROJECT_VERSION_MINOR="${THE_PROJECT_MINOR}"
   )

# Specify include directories for build and installed library
target_include_directories(${LIB}
    PUBLIC
       $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
       $<BUILD_INTERFACE:${PROJECT_BINARY_DIR}>
       $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

include(GNUInstallDirs)

set(ConfigPackageLocation "${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}")
message("CMAKE_INSTALL_LIBDIR ${CMAKE_INSTALL_LIBDIR}")
message("ConfigPackageLocation ${ConfigPackageLocation}")

# 'make install' to the correct locations (provided by GNUInstallDirs).
include(GNUInstallDirs)
install(TARGETS ${LIB}
    EXPORT ${PROJECT_NAME}Targets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR} COMPONENT Library
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR} COMPONENT Library
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}  COMPONENT Library # This is for Windows
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${LIB} COMPONENT Development
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    )

install(EXPORT ${PROJECT_NAME}Targets
  FILE
    ${PROJECT_NAME}Targets.cmake
  DESTINATION
    ${ConfigPackageLocation}
  COMPONENT
    Development
)

include(CMakePackageConfigHelpers)

configure_package_config_file(
    cmakeConfig.in
    ${PROJECT_NAME}Config.cmake
    INSTALL_DESTINATION "${ConfigPackageLocation}"
    PATH_VARS CMAKE_INSTALL_PREFIX
    )

write_basic_package_version_file(
    ${PROJECT_NAME}ConfigVersion.cmake
    VERSION ${PROJECT_VERSION_STRING}
    COMPATIBILITY AnyNewerVersion
    )

install(
  FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
  DESTINATION
    ${ConfigPackageLocation}
  COMPONENT
    Development
)
