/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:14 2016. */

#ifndef PB_MC_VIRTUAL_ATTITUDE_SETPOINT_PB_H_INCLUDED
#define PB_MC_VIRTUAL_ATTITUDE_SETPOINT_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_mc_virtual_attitude_setpoint_pb {
    uint64_t timestamp;
    float roll_body;
    float pitch_body;
    float yaw_body;
    float yaw_sp_move_rate;
    pb_size_t R_body_count;
    float R_body[9];
    pb_size_t q_d_count;
    float q_d[4];
    pb_size_t q_e_count;
    float q_e[4];
    float thrust;
    bool R_valid;
    bool q_d_valid;
    bool q_e_valid;
    bool roll_reset_integral;
    bool pitch_reset_integral;
    bool yaw_reset_integral;
    bool fw_control_yaw;
    bool disable_mc_yaw_control;
    bool apply_flaps;
/* @@protoc_insertion_point(struct:px4_mc_virtual_attitude_setpoint_pb) */
} px4_mc_virtual_attitude_setpoint_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_mc_virtual_attitude_setpoint_pb_init_default {0, 0, 0, 0, 0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0}, 0, {0, 0, 0, 0}, 0, {0, 0, 0, 0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
#define px4_mc_virtual_attitude_setpoint_pb_init_zero {0, 0, 0, 0, 0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0}, 0, {0, 0, 0, 0}, 0, {0, 0, 0, 0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_mc_virtual_attitude_setpoint_pb_timestamp_tag 1
#define px4_mc_virtual_attitude_setpoint_pb_roll_body_tag 2
#define px4_mc_virtual_attitude_setpoint_pb_pitch_body_tag 3
#define px4_mc_virtual_attitude_setpoint_pb_yaw_body_tag 4
#define px4_mc_virtual_attitude_setpoint_pb_yaw_sp_move_rate_tag 5
#define px4_mc_virtual_attitude_setpoint_pb_R_body_tag 6
#define px4_mc_virtual_attitude_setpoint_pb_q_d_tag 7
#define px4_mc_virtual_attitude_setpoint_pb_q_e_tag 8
#define px4_mc_virtual_attitude_setpoint_pb_thrust_tag 9
#define px4_mc_virtual_attitude_setpoint_pb_R_valid_tag 10
#define px4_mc_virtual_attitude_setpoint_pb_q_d_valid_tag 11
#define px4_mc_virtual_attitude_setpoint_pb_q_e_valid_tag 12
#define px4_mc_virtual_attitude_setpoint_pb_roll_reset_integral_tag 13
#define px4_mc_virtual_attitude_setpoint_pb_pitch_reset_integral_tag 14
#define px4_mc_virtual_attitude_setpoint_pb_yaw_reset_integral_tag 15
#define px4_mc_virtual_attitude_setpoint_pb_fw_control_yaw_tag 16
#define px4_mc_virtual_attitude_setpoint_pb_disable_mc_yaw_control_tag 17
#define px4_mc_virtual_attitude_setpoint_pb_apply_flaps_tag 18

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_mc_virtual_attitude_setpoint_pb_fields[19];

/* Maximum encoded size of messages (where known) */
#define px4_mc_virtual_attitude_setpoint_pb_size 142

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define MC_VIRTUAL_ATTITUDE_SETPOINT_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
