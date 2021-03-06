/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:15 2016. */

#ifndef PB_POSITION_SETPOINT_PB_H_INCLUDED
#define PB_POSITION_SETPOINT_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _px4_position_setpoint_pb_SETPOINT_TYPE {
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_POSITION = 0,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_VELOCITY = 1,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_LOITER = 2,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_TAKEOFF = 3,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_LAND = 4,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_IDLE = 5,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_OFFBOARD = 6,
    px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_FOLLOW_TARGET = 7
} px4_position_setpoint_pb_SETPOINT_TYPE;
#define _px4_position_setpoint_pb_SETPOINT_TYPE_MIN px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_POSITION
#define _px4_position_setpoint_pb_SETPOINT_TYPE_MAX px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_FOLLOW_TARGET
#define _px4_position_setpoint_pb_SETPOINT_TYPE_ARRAYSIZE ((px4_position_setpoint_pb_SETPOINT_TYPE)(px4_position_setpoint_pb_SETPOINT_TYPE_SETPOINT_TYPE_FOLLOW_TARGET+1))

/* Struct definitions */
typedef struct _px4_position_setpoint_pb {
    uint64_t timestamp;
    double lat;
    double lon;
    float x;
    float y;
    float z;
    float vx;
    float vy;
    float vz;
    float alt;
    float yaw;
    float yawspeed;
    float loiter_radius;
    float pitch_min;
    float a_x;
    float a_y;
    float a_z;
    float acceptance_radius;
    float cruising_speed;
    float cruising_throttle;
    bool valid;
    uint32_t type;
    bool position_valid;
    bool velocity_valid;
    bool yaw_valid;
    bool disable_mc_yaw_control;
    bool yawspeed_valid;
    int32_t loiter_direction;
    bool acceleration_valid;
    bool acceleration_is_force;
/* @@protoc_insertion_point(struct:px4_position_setpoint_pb) */
} px4_position_setpoint_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_position_setpoint_pb_init_default    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
#define px4_position_setpoint_pb_init_zero       {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_position_setpoint_pb_timestamp_tag   1
#define px4_position_setpoint_pb_lat_tag         2
#define px4_position_setpoint_pb_lon_tag         3
#define px4_position_setpoint_pb_x_tag           4
#define px4_position_setpoint_pb_y_tag           5
#define px4_position_setpoint_pb_z_tag           6
#define px4_position_setpoint_pb_vx_tag          7
#define px4_position_setpoint_pb_vy_tag          8
#define px4_position_setpoint_pb_vz_tag          9
#define px4_position_setpoint_pb_alt_tag         10
#define px4_position_setpoint_pb_yaw_tag         11
#define px4_position_setpoint_pb_yawspeed_tag    12
#define px4_position_setpoint_pb_loiter_radius_tag 13
#define px4_position_setpoint_pb_pitch_min_tag   14
#define px4_position_setpoint_pb_a_x_tag         15
#define px4_position_setpoint_pb_a_y_tag         16
#define px4_position_setpoint_pb_a_z_tag         17
#define px4_position_setpoint_pb_acceptance_radius_tag 18
#define px4_position_setpoint_pb_cruising_speed_tag 19
#define px4_position_setpoint_pb_cruising_throttle_tag 20
#define px4_position_setpoint_pb_valid_tag       21
#define px4_position_setpoint_pb_type_tag        22
#define px4_position_setpoint_pb_position_valid_tag 23
#define px4_position_setpoint_pb_velocity_valid_tag 24
#define px4_position_setpoint_pb_yaw_valid_tag   25
#define px4_position_setpoint_pb_disable_mc_yaw_control_tag 26
#define px4_position_setpoint_pb_yawspeed_valid_tag 27
#define px4_position_setpoint_pb_loiter_direction_tag 28
#define px4_position_setpoint_pb_acceleration_valid_tag 29
#define px4_position_setpoint_pb_acceleration_is_force_tag 30

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_position_setpoint_pb_fields[31];

/* Maximum encoded size of messages (where known) */
#define px4_position_setpoint_pb_size            162

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define POSITION_SETPOINT_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
