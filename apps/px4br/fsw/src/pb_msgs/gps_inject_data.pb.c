/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:12 2016. */

#include "gps_inject_data.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t px4_gps_inject_data_pb_fields[5] = {
    PB_FIELD(  1, UINT64  , REQUIRED, STATIC  , FIRST, px4_gps_inject_data_pb, timestamp, timestamp, 0),
    PB_FIELD(  2, UINT32  , REQUIRED, STATIC  , OTHER, px4_gps_inject_data_pb, len, timestamp, 0),
    PB_FIELD(  3, UINT32  , REQUIRED, STATIC  , OTHER, px4_gps_inject_data_pb, flags, len, 0),
    PB_FIELD(  4, STRING  , REQUIRED, STATIC  , OTHER, px4_gps_inject_data_pb, data, flags, 0),
    PB_LAST_FIELD
};


/* @@protoc_insertion_point(eof) */
