/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:15 2016. */

#include "optical_flow.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t px4_optical_flow_pb_fields[14] = {
    PB_FIELD(  1, UINT64  , REQUIRED, STATIC  , FIRST, px4_optical_flow_pb, timestamp, timestamp, 0),
    PB_FIELD(  2, FLOAT   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, pixel_flow_x_integral, timestamp, 0),
    PB_FIELD(  3, FLOAT   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, pixel_flow_y_integral, pixel_flow_x_integral, 0),
    PB_FIELD(  4, FLOAT   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, gyro_x_rate_integral, pixel_flow_y_integral, 0),
    PB_FIELD(  5, FLOAT   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, gyro_y_rate_integral, gyro_x_rate_integral, 0),
    PB_FIELD(  6, FLOAT   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, gyro_z_rate_integral, gyro_y_rate_integral, 0),
    PB_FIELD(  7, FLOAT   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, ground_distance_m, gyro_z_rate_integral, 0),
    PB_FIELD(  8, UINT32  , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, integration_timespan, ground_distance_m, 0),
    PB_FIELD(  9, UINT32  , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, time_since_last_sonar_update, integration_timespan, 0),
    PB_FIELD( 10, UINT32  , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, frame_count_since_last_readout, time_since_last_sonar_update, 0),
    PB_FIELD( 11, INT32   , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, gyro_temperature, frame_count_since_last_readout, 0),
    PB_FIELD( 12, UINT32  , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, sensor_id, gyro_temperature, 0),
    PB_FIELD( 13, UINT32  , REQUIRED, STATIC  , OTHER, px4_optical_flow_pb, quality, sensor_id, 0),
    PB_LAST_FIELD
};


/* @@protoc_insertion_point(eof) */
