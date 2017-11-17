
add_airliner_app_def(ld
    FILE LD
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_app.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_config_utils.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_events.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_msg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_tbldefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_version.h
   
    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/

    USER_DOCS   ${CMAKE_CURRENT_SOURCE_DIR}/user_doxy.in
    DESIGN_DOCS ${CMAKE_CURRENT_SOURCE_DIR}/detail_doxy.in
)

add_airliner_app_unit_test(ld-ut
    UTASSERT
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_app_test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_app_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_cmds_test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_cmds_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_config_tbl_test.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_config_tbl_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_testrunner.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_test_utils.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ld_test_utils.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_app.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_config_utils.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_events.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_msg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_tbldefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ld_version.h
        
    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/
        
    VALGRIND_SUPPRESSION_FILE
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/valgrind.supp
)