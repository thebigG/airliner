/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:15 2016. */

#ifndef PB_POSITION_SETPOINT_TRIPLET_PB_H_INCLUDED
#define PB_POSITION_SETPOINT_TRIPLET_PB_H_INCLUDED
#include <pb.h>

#include "position_setpoint.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_position_setpoint_triplet_pb {
    uint64_t timestamp;
    uint32_t nav_state;
    px4_position_setpoint_pb previous;
    px4_position_setpoint_pb current;
    px4_position_setpoint_pb next;
/* @@protoc_insertion_point(struct:px4_position_setpoint_triplet_pb) */
} px4_position_setpoint_triplet_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_position_setpoint_triplet_pb_init_default {0, 0, px4_position_setpoint_pb_init_default, px4_position_setpoint_pb_init_default, px4_position_setpoint_pb_init_default}
#define px4_position_setpoint_triplet_pb_init_zero {0, 0, px4_position_setpoint_pb_init_zero, px4_position_setpoint_pb_init_zero, px4_position_setpoint_pb_init_zero}

/* Field tags (for use in manual encoding/decoding) */
#define px4_position_setpoint_triplet_pb_timestamp_tag 1
#define px4_position_setpoint_triplet_pb_nav_state_tag 2
#define px4_position_setpoint_triplet_pb_previous_tag 3
#define px4_position_setpoint_triplet_pb_current_tag 4
#define px4_position_setpoint_triplet_pb_next_tag 5

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_position_setpoint_triplet_pb_fields[6];

/* Maximum encoded size of messages (where known) */
#define px4_position_setpoint_triplet_pb_size    (35 + px4_position_setpoint_pb_size + px4_position_setpoint_pb_size + px4_position_setpoint_pb_size)

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define POSITION_SETPOINT_TRIPLET_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
