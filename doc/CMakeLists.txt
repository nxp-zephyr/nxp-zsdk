# Copyright (c) 2019-2021 Nordic Semiconductor ASA
# Copyright 2025-2026 NXP
# SPDX-License-Identifier: BSD-3-Clause
#
# NXP Zephyr project documentation build system.
#
# Builds combined documentation for all documentation sets (ZSDK, Zephyr).
# Each docset uses its own Sphinx configuration (see doc/zsdk/conf.py and
# doc/zephyr/conf.py).  Intersphinx links the sets together.

cmake_minimum_required(VERSION 3.20.0)
project(nxp_zephyr_doc NONE)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE} COMPONENTS doc)

#-------------------------------------------------------------------------------
# Options

set(SPHINXOPTS "-j auto --keep-going -T" CACHE STRING "Default Sphinx options")
set(SPHINXOPTS_EXTRA "" CACHE STRING "Extra Sphinx options")
set(DTS_BINDINGS OFF CACHE BOOL "Generate devicetree bindings documentation")
set(HW_FEATURES OFF CACHE BOOL "Generate hardware features documentation")

separate_arguments(SPHINXOPTS)
separate_arguments(SPHINXOPTS_EXTRA)

#-------------------------------------------------------------------------------
# Dependencies

find_package(Python 3.8)
set(DOXYGEN_SKIP_DOT True)
find_package(Doxygen 1.8.18 REQUIRED)

find_program(SPHINXBUILD sphinx-build)
if(NOT SPHINXBUILD)
  message(FATAL_ERROR "The 'sphinx-build' command was not found")
endif()

find_program(SPHINXAUTOBUILD sphinx-autobuild)
if(NOT SPHINXAUTOBUILD)
  message(WARNING "sphinx-autobuild not found, HTML hot reloading will not be available.")
endif()

find_program(WEST west)
if(NOT WEST)
  message(FATAL_ERROR "The 'west' command was not found")
endif()

set(KCONFIG_BINARY_DIR ${CMAKE_BINARY_DIR}/kconfig)
list(INSERT MODULE_EXT_ROOT 0 ${ZEPHYR_BASE})
file(MAKE_DIRECTORY ${KCONFIG_BINARY_DIR})

# Build dependency graph: zsdk depends on zephyr, zephyr depends on devicetree
set(DOCSET_DEPENDENCIES_zsdk "zephyr-all")
set(DOCSET_DEPENDENCIES_zephyr "zephyr-devicetree")

message(STATUS "Generation branch: ${DOCGEN_BRANCH}")
message(STATUS "Generation revision: ${DOCGEN_REV}")

#-------------------------------------------------------------------------------
# Functions

# add_doxygen_docset(<name> <sources> <version> [STANDALONE])
#
# Add a Doxygen documentation target.
#   STANDALONE  — docset is Doxygen-only (no Sphinx wrapper).
#
# Targets created:
#   ${name}[-doxygen]        Build Doxygen output.
#   ${name}[-doxygen]-clean  Remove build artifacts.
#
function(add_doxygen_docset name sources version)
  cmake_parse_arguments(DOXYGEN "STANDALONE" "" "" ${ARGN})
  set(DOCSET_BUILD_DIR ${CMAKE_BINARY_DIR}/html/${name})
  set(DOCSET_SOURCE_BASE ${sources})
  set(DOCSET_VERSION ${version})

  if(NOT DOXYGEN_STANDALONE)
    set(SUFFIX "-doxygen")
    set(DOCSET_BUILD_DIR ${DOCSET_BUILD_DIR}/doxygen)
  endif()

  configure_file(${CMAKE_CURRENT_LIST_DIR}/${name}/${name}.doxyfile.in ${CMAKE_BINARY_DIR}/${name}.doxyfile)

  add_custom_target(
    ${name}${SUFFIX}
    COMMAND ${CMAKE_COMMAND} -E make_directory ${DOCSET_BUILD_DIR}
    COMMAND ${DOXYGEN_EXECUTABLE} ${CMAKE_BINARY_DIR}/${name}.doxyfile
    USES_TERMINAL
    COMMENT "Building ${name} Doxygen docset..."
  )

  add_custom_target(
    ${name}${SUFFIX}-clean
    COMMAND ${CMAKE_COMMAND} -E rm -rf ${DOCSET_BUILD_DIR}
  )
endfunction()

# add_docset(<name> <version> [DODGY] [SPHINXOPTS <opts>])
#
# Add a Sphinx documentation set.  Configuration is read from
# ${name}/conf.py (relative to doc/).  Sources come from ${name}/src
# (relative to the build directory) via the external_content extension.
#
#   DODGY      — suppress -W (warnings-as-errors); useful for upstream
#                docsets that generate warnings we do not control.
#   SPHINXOPTS — additional Sphinx options for this docset only.
#
# Targets created:
#   ${name}              Sphinx HTML build.
#   ${name}-inventory    Sphinx inventory-only build (for intersphinx).
#   ${name}-live         Live-reload build (requires sphinx-autobuild).
#   ${name}-linkcheck    Check external links.
#   ${name}-clean        Remove build artifacts.
#
function(add_docset name version)
  cmake_parse_arguments(DOCSET "DODGY" "" "SPHINXOPTS" ${ARGN})

  set(DOCSET_CFG_DIR ${CMAKE_CURRENT_LIST_DIR}/${name})
  set(DOCSET_BUILD_DIR ${CMAKE_BINARY_DIR}/${name})
  set(DOCSET_SRC_DIR ${CMAKE_BINARY_DIR}/${name}/src)
  set(DOCSET_DOCTREE_DIR ${CMAKE_BINARY_DIR}/${name}/doctree)
  set(DOCSET_HTML_DIR ${CMAKE_BINARY_DIR}/html/${name})
  set(DOCSET_LINKCHECK_DIR ${CMAKE_BINARY_DIR}/linkcheck/${name})
  set(DOCSET_MAKE_DIRS ${DOCSET_BUILD_DIR};${DOCSET_SRC_DIR};${DOCSET_HTML_DIR})
  set(DOCSET_CLEAN_DIRS ${DOCSET_BUILD_DIR};${DOCSET_HTML_DIR})
  set(DOCSET_ENV DOXYGEN_EXECUTABLE=${DOXYGEN_EXECUTABLE};DOCSET_VERSION=${version};DOCS_HTML_DIR=${DOCSET_HTML_DIR}; DOCGEN_BRANCH=${DOCGEN_BRANCH};DOCGEN_REV=${DOCGEN_REV})

  if(${DOCSET_DODGY})
    list(REMOVE_ITEM SPHINXOPTS "-W" "--keep-going")
  endif()

  add_doc_target(
    ${name}-inventory
    COMMAND ${CMAKE_COMMAND} -E make_directory ${DOCSET_MAKE_DIRS}
    COMMAND ${CMAKE_COMMAND} -E env ${DOCSET_ENV}
    ${SPHINXBUILD}
      -b inventory
      -c ${DOCSET_CFG_DIR}
      -d ${DOCSET_DOCTREE_DIR}
      -w ${DOCSET_BUILD_DIR}/inventory.log
      ${SPHINXOPTS}
      ${SPHINXOPTS_EXTRA}
      ${DOCSET_SPHINXOPTS}
      ${DOCSET_SRC_DIR}
      ${DOCSET_HTML_DIR}
    USES_TERMINAL
    COMMENT "Building ${name} inventory..."
  )

  add_doc_target(
    ${name}
    COMMAND ${CMAKE_COMMAND} -E make_directory ${DOCSET_MAKE_DIRS}
    COMMAND ${CMAKE_COMMAND} -E env ${DOCSET_ENV}
    ${SPHINXBUILD}
      -b html
      -c ${DOCSET_CFG_DIR}
      -d ${DOCSET_DOCTREE_DIR}
      -w ${DOCSET_BUILD_DIR}/html.log
      ${SPHINXOPTS}
      ${SPHINXOPTS_EXTRA}
      ${DOCSET_SPHINXOPTS}
      ${EXTRA_ARGS}
      ${DOCSET_SRC_DIR}
      ${DOCSET_HTML_DIR}
    USES_TERMINAL
    COMMENT "Building ${name} docset..."
  )

  if(SPHINXAUTOBUILD)
    add_doc_target(
      ${name}-live
      COMMAND ${CMAKE_COMMAND} -E make_directory ${DOCSET_MAKE_DIRS}
      COMMAND ${CMAKE_COMMAND} -E env ${DOCSET_ENV}
      ${SPHINXAUTOBUILD}
        --watch ${DOCSET_CFG_DIR}
        --ignore ${DOCSET_BUILD_DIR}
        -b html
        -c ${DOCSET_CFG_DIR}
        -d ${DOCSET_DOCTREE_DIR}
        -w ${DOCSET_BUILD_DIR}/html-live.log
        ${SPHINXOPTS}
        ${SPHINXOPTS_EXTRA}
        ${DOCSET_SPHINXOPTS}
        ${EXTRA_ARGS}
        ${DOCSET_SRC_DIR}
        ${DOCSET_HTML_DIR}
      USES_TERMINAL
      COMMENT "Building ${name}-live docset..."
    )
  endif()

  add_custom_target(
    ${name}-linkcheck
    COMMAND ${CMAKE_COMMAND} -E make_directory ${DOCSET_MAKE_DIRS}
    COMMAND ${CMAKE_COMMAND} -E env ${DOCSET_ENV}
    ${SPHINXBUILD}
      -b linkcheck
      -c ${DOCSET_CFG_DIR}
      -d ${DOCSET_DOCTREE_DIR}
      -w ${DOCSET_BUILD_DIR}/linkcheck.log
      ${SPHINXOPTS}
      ${SPHINXOPTS_EXTRA}
      ${DOCSET_SPHINXOPTS}
      ${EXTRA_ARGS}
      ${DOCSET_SRC_DIR}
      ${DOCSET_LINKCHECK_DIR}
    USES_TERMINAL
    COMMENT "Checking links for ${name} docset..."
  )

  set_target_properties(
    ${name}-inventory ${name}-inventory-all
    ${name} ${name}-all
    ${name}-linkcheck
    PROPERTIES
      ADDITIONAL_CLEAN_FILES "${DOCSET_CLEAN_DIRS}"
  )

  if(SPHINXAUTOBUILD)
    set_target_properties(
      ${name}-live ${name}-live-all
      PROPERTIES
        ADDITIONAL_CLEAN_FILES "${DOCSET_CLEAN_DIRS}"
    )
  endif()

  add_custom_target(
    ${name}-clean
    COMMAND ${CMAKE_COMMAND} -E rm -rf ${DOCSET_CLEAN_DIRS}
  )

  # Add inventory dependencies
  if(DEFINED DOCSET_DEPENDENCIES_${name} AND DOCSET_DEPENDENCIES_${name})
    add_dependencies(${name} ${DOCSET_DEPENDENCIES_${name}})
    add_dependencies(${name}-all ${DOCSET_DEPENDENCIES_${name}})
    if(SPHINXAUTOBUILD)
      add_dependencies(${name}-live-all ${DOCSET_DEPENDENCIES_${name}})
    endif()
  endif()

endfunction()

# add_doc_target(<name> ...)
#
# Wrapper around add_custom_target() that creates two identical targets:
#   ${name}      — standalone build (missing cross-references are warnings).
#   ${name}-all  — full build with controlled dependency ordering.
#
function(add_doc_target name)
  add_custom_target(${name} ${ARGN})
  add_custom_target(${name}-all ${ARGN})
endfunction()

#-------------------------------------------------------------------------------
# Paths

get_filename_component(ZSDK_BASE ${CMAKE_CURRENT_LIST_DIR}../ DIRECTORY)

set(ZSDK_BINARY_DIR ${CMAKE_BINARY_DIR}/zsdk)
set(ZEPHYR_BINARY_DIR ${CMAKE_BINARY_DIR}/zephyr)

set(HTML_DIR ${CMAKE_BINARY_DIR}/html)
file(MAKE_DIRECTORY ${HTML_DIR})

#-------------------------------------------------------------------------------
# Zephyr docset

set(DTS_ARGS)
if(NOT DTS_BINDINGS)
  list(APPEND DTS_ARGS --turbo-mode)
endif()

add_custom_target(
  zephyr-devicetree
  COMMAND ${CMAKE_COMMAND} -E env
    PYTHONPATH=${ZEPHYR_BASE}/scripts/dts/python-devicetree/src
    ZEPHYR_BASE=${ZEPHYR_BASE}
    ${PYTHON_EXECUTABLE}
      ${ZEPHYR_BASE}/doc/_scripts/gen_devicetree_rest.py
      --vendor-prefixes ${ZEPHYR_BASE}/dts/bindings/vendor-prefixes.txt
      --dts-root ${ZEPHYR_BASE}
      ${ZEPHYR_BINARY_DIR}/src/build/dts/api
      ${DTS_ARGS}
  VERBATIM
  USES_TERMINAL
  COMMENT "Generating devicetree bindings documentation..."
)

if(NOT HW_FEATURES)
  set(ZEPHYR_SPHINXOPTS -t hw_features_turbo)
endif()

if(HW_FEATURES_VENDOR_FILTER)
  list(JOIN HW_FEATURES_VENDOR_FILTER "," vendor_filter)
  list(APPEND ZEPHYR_SPHINXOPTS "-D" "zephyr_hw_features_vendor_filter=${vendor_filter}")
endif()

add_docset(zephyr ${Zephyr_VERSION} SPHINXOPTS ${ZEPHYR_SPHINXOPTS})

#-------------------------------------------------------------------------------
# ZSDK docset

add_docset(zsdk "nxp-v4.4.0")

#-------------------------------------------------------------------------------
# Global targets

# Merge per-docset search indexes into a unified cross-docset index.
# Runs after all docsets are built so every searchindex.js is available.
add_custom_target(
  merge-search-indexes
  COMMAND ${PYTHON_EXECUTABLE}
    -m mcux_book_theme.extensions.merge_search
    -b ${CMAKE_BINARY_DIR}
  COMMENT "Merging cross-docset search indexes..."
)
add_dependencies(merge-search-indexes zsdk-all zephyr-all)

# Default build — fast iteration, skips devicetree bindings and HW features.
add_custom_target(build-quick ALL)
add_dependencies(build-quick merge-search-indexes zsdk-all zephyr-all)

# Full build — enables NXP devicetree bindings and hardware features.
# Reconfigures then rebuilds so a single `cmake --build . --target build-complete`
# is sufficient.
add_custom_target(
  build-complete
  COMMAND ${CMAKE_COMMAND}
    -DHW_FEATURES=ON
    -DDTS_BINDINGS=ON
    -DHW_FEATURES_VENDOR_FILTER=nxp
    -S ${CMAKE_SOURCE_DIR}
    -B ${CMAKE_BINARY_DIR}
  COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target build-quick
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  COMMENT "Full build with NXP hardware features and devicetree bindings..."
  USES_TERMINAL
)

# Remove all build artifacts.
add_custom_target(
  clean-build
  COMMAND ${CMAKE_COMMAND} -E rm -rf ${CMAKE_BINARY_DIR}
  COMMENT "Cleaning all build artifacts..."
)
