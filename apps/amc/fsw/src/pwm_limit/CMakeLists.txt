set(PX4LIB_SOURCES
    ${PX4LIB_SOURCES}
    ${CMAKE_CURRENT_SOURCE_DIR}/pwm_limit.c
)

set(PX4LIB_PUBLIC_INCLUDES
    ${PX4LIB_PUBLIC_INCLUDES}
    ${CMAKE_CURRENT_SOURCE_DIR}
)

set(PX4LIB_INCLUDES
    ${PX4LIB_INCLUDES}
)

set(PX4LIB_SOURCES  ${PX4LIB_SOURCES} PARENT_SCOPE)
set(PX4LIB_INCLUDES ${PX4LIB_INCLUDES} PARENT_SCOPE)
set(PX4LIB_PUBLIC_INCLUDES ${PX4LIB_PUBLIC_INCLUDES} PARENT_SCOPE)
