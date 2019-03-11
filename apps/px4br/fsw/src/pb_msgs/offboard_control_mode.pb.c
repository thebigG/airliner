/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:15 2016. */

#include "offboard_control_mode.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t px4_offboard_control_mode_pb_fields[8] = {
    PB_FIELD(  1, UINT64  , REQUIRED, STATIC  , FIRST, px4_offboard_control_mode_pb, timestamp, timestamp, 0),
    PB_FIELD(  2, BOOL    , REQUIRED, STATIC  , OTHER, px4_offboard_control_mode_pb, ignore_thrust, timestamp, 0),
    PB_FIELD(  3, BOOL    , REQUIRED, STATIC  , OTHER, px4_offboard_control_mode_pb, ignore_attitude, ignore_thrust, 0),
    PB_FIELD(  4, BOOL    , REQUIRED, STATIC  , OTHER, px4_offboard_control_mode_pb, ignore_bodyrate, ignore_attitude, 0),
    PB_FIELD(  5, BOOL    , REQUIRED, STATIC  , OTHER, px4_offboard_control_mode_pb, ignore_position, ignore_bodyrate, 0),
    PB_FIELD(  6, BOOL    , REQUIRED, STATIC  , OTHER, px4_offboard_control_mode_pb, ignore_velocity, ignore_position, 0),
    PB_FIELD(  7, BOOL    , REQUIRED, STATIC  , OTHER, px4_offboard_control_mode_pb, ignore_acceleration_force, ignore_velocity, 0),
    PB_LAST_FIELD
};


/* @@protoc_insertion_point(eof) */