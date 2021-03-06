 #############################################################################
 #
 #   Copyright (c) 2017 Windhover Labs, L.L.C. All rights reserved.
 #
 # Redistribution and use in source and binary forms, with or without
 # modification, are permitted provided that the following conditions
 # are met:
 #
 # 1. Redistributions of source code must retain the above copyright
 #    notice, this list of conditions and the following disclaimer.
 # 2. Redistributions in binary form must reproduce the above copyright
 #    notice, this list of conditions and the following disclaimer in
 #    the documentation and/or other materials provided with the
 #    distribution.
 # 3. Neither the name Windhover Labs nor the names of its contributors 
 #    may be used to endorse or promote products derived from this software
 #    without specific prior written permission.
 #
 # THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 # "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 # LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 # FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 # COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 # INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 # BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 # OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 # AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 # LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 # ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 # POSSIBILITY OF SUCH DAMAGE.
 #
 #############################################################################
 
add_airliner_app_def(ds
    FILE DS
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_app.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_appdefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_cmds.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_cmds.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_file.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_file.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_msg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_msgdefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_symbols.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_table.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_table.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_verify.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_version.h
    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/

    USER_DOCS   ${CMAKE_CURRENT_SOURCE_DIR}/user_doxy.in
    DESIGN_DOCS ${CMAKE_CURRENT_SOURCE_DIR}/detail_doxy.in  
    
    MSG_OVERRIDES   ${CMAKE_CURRENT_SOURCE_DIR}/ds_msg_overrides.json 

    COMMANDER_PLUGIN
        ${CMAKE_CURRENT_SOURCE_DIR}/../../cdr
    
    REFERENCE_CONFIG
        ${PROJECT_SOURCE_DIR}/apps/ds/fsw/mission_inc
        ${PROJECT_SOURCE_DIR}/apps/ds/fsw/platform_inc
)


add_airliner_app_unit_test(ds-ut
    UTASSERT
    SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_app_test.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_app_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_cmds_test.c 
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_cmds_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_file_test.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_file_test.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_msgids.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_platform_cfg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_table_test.c 
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_table_test.h 
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_test_utils.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_test_utils.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds_testrunner.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_app.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_app.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_appdefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_cmds.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_cmds.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_file.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_file.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_msg.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_msgdefs.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_table.c
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_table.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_verify.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/ds_version.h
        ${CMAKE_CURRENT_SOURCE_DIR}/../../../cfs_lib/fsw/src/cfs_utils.c
        
    INCLUDES
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/
        ${CMAKE_CURRENT_SOURCE_DIR}/../src/

    VALGRIND_SUPPRESSION_FILE
        ${CMAKE_CURRENT_SOURCE_DIR}/../unit_test/ds-ut.supp
)
