/*
    This file is part of joystick_remote.

    joystick_remote is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or any later version.

    joystick_remote is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with joystick_remote.  
    If not, see <http://www.gnu.org/licenses/>.
*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <poll.h>
#include <getopt.h>
#include <stdint.h>
#include <time.h>
#include <stdarg.h>
#include <string.h>
#include <inttypes.h>

#include "joystick.h"
#include "remote.h"
#include "joystick_remote.h"

static struct timespec start_time;

static struct option long_options[] = {
    {"list",      no_argument, 0,           'l' },
    {"device",    required_argument, 0,     'd' },
    {"mode",      required_argument, 0,     'm' },
    {"verbose",   no_argument, 0,           'v' },
    {"remote",    required_argument, 0,     'r' },
    {"type",      required_argument, 0,     't' },
    {"help",      no_argument, 0,           'h' },
    {0, 0, 0, 0 }
};

static struct joystick joystick;
static struct remote remote;

static const char usage[] = "usage:\n\tjoystick_remote -d your_device "
                            "-t joystick_type -r remote_address:remote_port\n\n"
                            "\tjoystick types: xbox360, skycontroller, ps3, and frsky\n\n";
static uint8_t verbose = 0;

void debug_printf(const char *fmt, ...)
{
    va_list arglist;

    if (verbose == 1) {
        va_start(arglist, fmt);
        vprintf(fmt, arglist);
        va_end(arglist);
    }
}

static void microsleep(uint32_t usec) {
    struct timespec ts;

    ts.tv_sec = 0;
    ts.tv_nsec = usec * 1000UL;
    while (nanosleep(&ts, &ts) == -1 && errno == EINTR);
}

static uint64_t get_micro64()
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return 1.0e6*((ts.tv_sec + (ts.tv_nsec*1.0e-9)) - 
                  (start_time.tv_sec +
                   (start_time.tv_nsec*1.0e-9)));
}

int main(int argc, char **argv)
{
    int c;
    char *device_path = NULL;
    char *joystick_type = NULL;
    uint64_t next_run_usec;
    char *remote_host = NULL;
    uint16_t pwms[RCINPUT_UDP_NUM_CHANNELS];

    if (argc < 2)
        printf(usage);

    while (1) {

        c = getopt_long(argc, argv, "vld:m:r:cht:", long_options, NULL);
        if (c == -1)
            break;

        switch (c) {
        case 'l':
            debug_printf("get the list of joysticks\n");
            break;
        case 'd':
            debug_printf("device : %s\n", optarg);
            device_path = optarg;
            break;
        case 'm':
            debug_printf("mode : %s\n", optarg);
            break;
        case 'v':
            verbose = 1;
            break;
        case 'r':
            debug_printf("set remote to %s\n", optarg);
            remote_host = optarg;
            break;
        case 't':
            debug_printf("set joystick_type to %s\n", optarg);
            joystick_type = optarg;
            break;
        case 'h':
            printf(usage);
            goto end;
        case '?':
            printf(usage);
            goto end;
        default:
            fprintf(stderr, "bad option parsed by getopt : %d\n", c);
            goto end;
        }
    }

    if (optind < argc) {
        fprintf(stderr, "wrong option in arguments: ");
        while (optind < argc)
            printf("%s", argv[optind++]);
        printf("\n");
    }

    if (device_path == NULL) {
        fprintf(stderr, "you must specify a device with -d option\n");
        goto end;
    }

    if (joystick_start(device_path, &joystick) == -1) {
        fprintf(stderr, "joystick start failed\n");
        goto end;
    }

    if (remote_host == NULL) {
        fprintf(stderr, "no ip address specified\n");
        goto end;
    }

    if (remote_start(remote_host, &remote) == -1) {
        fprintf(stderr, "remote start failed\n");
        goto end;
    }

    /* Calibration procedure to be added */
    if (joystick_type == NULL) {
        fprintf(stderr, "no joystick type specified\n");
        goto end;
    }
    joystick_set_type(&joystick, joystick_type);

    /* get start time, necessary for get_micro64) */
    clock_gettime(CLOCK_MONOTONIC, &start_time);

    next_run_usec = get_micro64() + 10000;
    while (1) {
        uint64_t dt = next_run_usec - get_micro64();
        uint64_t micro64;
        uint8_t len;

        if (dt > 20000) {
            // we've lost sync - restart
            next_run_usec = get_micro64();
        } else {
            microsleep(dt);
        }
        next_run_usec += 10000;
        joystick_get_pwms(&joystick, pwms, &len);
        remote_send_pwms(&remote, pwms, len, (micro64 = get_micro64()));
        printf("Micros : %" PRIu64", Roll : %d, Pitch : %d, Throttle : %d, Yaw : %d, Mode : %d\n",
                micro64, pwms[0], pwms[1], pwms[2], pwms[3], pwms[4]);
    }

end:
    exit(EXIT_SUCCESS);
}
