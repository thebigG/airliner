/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:13 2016. */

#include "mc_att_ctrl_status.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t px4_mc_att_ctrl_status_pb_fields[5] = {
    PB_FIELD(  1, UINT64  , REQUIRED, STATIC  , FIRST, px4_mc_att_ctrl_status_pb, timestamp, timestamp, 0),
    PB_FIELD(  2, FLOAT   , REQUIRED, STATIC  , OTHER, px4_mc_att_ctrl_status_pb, roll_rate_integ, timestamp, 0),
    PB_FIELD(  3, FLOAT   , REQUIRED, STATIC  , OTHER, px4_mc_att_ctrl_status_pb, pitch_rate_integ, roll_rate_integ, 0),
    PB_FIELD(  4, FLOAT   , REQUIRED, STATIC  , OTHER, px4_mc_att_ctrl_status_pb, yaw_rate_integ, pitch_rate_integ, 0),
    PB_LAST_FIELD
};


/* @@protoc_insertion_point(eof) */
