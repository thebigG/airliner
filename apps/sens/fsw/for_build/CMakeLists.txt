
add_airliner_app_def(sens
    FILE SENS
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_app.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_config_utils.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_events.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_msg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_symbols.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_tbldefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_version.h

    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/

    USER_DOCS   ${CMAKE_CURRENT_SOURCE_DIR}/user_doxy.in
    DESIGN_DOCS ${CMAKE_CURRENT_SOURCE_DIR}/detail_doxy.in

    MSG_OVERRIDES ${CMAKE_CURRENT_SOURCE_DIR}/sens_msg_overrides.json

    COMMANDER_PLUGIN
        ${CMAKE_CURRENT_SOURCE_DIR}/../../cdr
    
    REFERENCE_CONFIG
        ${PROJECT_SOURCE_DIR}/apps/sens/fsw/mission_inc
        ${PROJECT_SOURCE_DIR}/apps/sens/fsw/platform_inc
)

add_airliner_app_unit_test(sens-ut
    UTASSERT
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_app_test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_app_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_cmds_test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_cmds_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_config_tbl_test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_config_tbl_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_testrunner.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_test_utils.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/sens_test_utils.h
        #${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/stubs/ut_LowPassFilter2p_hooks.cpp
        #${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/stubs/ut_LowPassFilter2p_hooks.h
        #${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/stubs/ut_LowPassFilter2p_stubs.cpp
        #${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/stubs/ut_LowPassFilter2p_stubs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_app.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_config_utils.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_events.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_msg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_tbldefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/sens_version.h
        ${PX4LIB_LIB_SOURCES}

    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/

    VALGRIND_SUPPRESSION_FILE
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/valgrind.supp
)
