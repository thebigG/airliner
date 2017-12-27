/****************************************************************************
*
*   Copyright (c) 2017 Windhover Labs, L.L.C. All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*
* 1. Redistributions of source code must retain the above copyright
*    notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in
*    the documentation and/or other materials provided with the
*    distribution.
* 3. Neither the name Windhover Labs nor the names of its 
*    contributors may be used to endorse or promote products derived 
*    from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
* FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
* COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
* OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
* AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
* ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
* POSSIBILITY OF SUCH DAMAGE.
*
*****************************************************************************/
/************************************************************************
** Pragmas
*************************************************************************/

/************************************************************************
** Includes
*************************************************************************/
#include "gps_custom_shared.h"
#include <time.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include "simlib.h"

/************************************************************************
** Local Defines
*************************************************************************/

/************************************************************************
** Local Structure Declarations
*************************************************************************/

/************************************************************************
** External Global Variables
*************************************************************************/

/************************************************************************
** Global Variables
*************************************************************************/
GPS_AppCustomData_t GPS_AppCustomData;
/************************************************************************
** Local Variables
*************************************************************************/

/************************************************************************
** Local Function Definitions
*************************************************************************/

void GPS_Custom_InitData(void)
{
    /* Set all struct zero values */
    bzero(&GPS_AppCustomData, sizeof(GPS_AppCustomData));
    //GPS_Parser_Reset();
    /* Set all non-zero values */
    GPS_AppCustomData.ContinueFlag          = TRUE;
    GPS_AppCustomData.Priority              = GPS_STREAMING_TASK_PRIORITY;
    GPS_AppCustomData.StreamingTask         = GPS_Stream_Task;
}

boolean GPS_Custom_Init()
{
    boolean returnBool = TRUE;
    int32 returnCode = 0;
    int32 Status = CFE_SUCCESS;
    
    Status = OS_MutSemCreate(&GPS_AppCustomData.MutexPosition, GPS_MUTEX_POS, 0);
    if (Status != CFE_SUCCESS)
    {
        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
            "GPS mutex create failed in custom init");
        returnBool = FALSE;
        goto end_of_function;
    }
    Status = OS_MutSemCreate(&GPS_AppCustomData.MutexSatInfo, GPS_MUTEX_SAT, 0);
    if (Status != CFE_SUCCESS)
    {
        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
            "GPS mutex create failed in custom init");
        returnBool = FALSE;
        goto end_of_function;
    }
    /* Create the streaming task */
    returnCode = CFE_ES_CreateChildTask(
            &GPS_AppCustomData.ChildTaskID,
            GPS_STREAMING_TASK_NAME,
            GPS_AppCustomData.StreamingTask,
            0,
            CFE_ES_DEFAULT_STACK_SIZE,
            GPS_AppCustomData.Priority,
            0);
    if(CFE_SUCCESS != returnCode)
    {
        GPS_AppCustomData.ContinueFlag = FALSE;
        returnBool = FALSE;
        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
            "GPS create streaming task failed");
        goto end_of_function;
    }
    else
    {
        GPS_AppCustomData.Status = GPS_CUSTOM_INITIALIZED;
    }

end_of_function:
    return returnBool;
}


void GPS_Stream_Task(void)
{
    uint32 iStatus = -1;
    boolean returnBool = FALSE;
    
    iStatus = CFE_ES_RegisterChildTask();
    
    if (iStatus == CFE_SUCCESS)
    {
        GPS_AppCustomData.Status = GPS_CUSTOM_STREAMING;
        while (GPS_AppCustomData.ContinueFlag == TRUE)
        {
            returnBool = GPS_Custom_Read_and_Parse(GPS_PACKET_TIMEOUT);
            if(returnBool == FALSE)
            {
                /* TODO remove me*/
                OS_printf("GPS parse and read failed\n");
            }
        }
    }

    /* Streaming task is exiting so set app flag to initialized */
    GPS_AppCustomData.Status = GPS_CUSTOM_INITIALIZED;
    CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
        "GPS receive task exited with task status (0x%08lX)", iStatus);

    /* The child task was successfully registered so exit from it */
    if (iStatus == CFE_SUCCESS)
    {
        CFE_ES_ExitChildTask();
    }
}


boolean GPS_Custom_Uninit(void)
{
    boolean returnBool = TRUE;
    int returnCode = 0;

    //else
    //{
        //GPS_AppCustomData.Status = GPS_CUSTOM_UNINITIALIZED;
    //}
    return returnBool;
}


boolean GPS_Custom_Max_Events_Not_Reached(int32 ind)
{
    if ((ind < CFE_EVS_MAX_EVENT_FILTERS) && (ind > 0))
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}


int32 GPS_Custom_Init_EventFilters(int32 ind, CFE_EVS_BinFilter_t *EventTbl)
{
    int32 customEventCount = ind;
    
    /* Null check */
    if(0 == EventTbl)
    {
        customEventCount = -1;
        goto end_of_function;
    }

    if(TRUE == GPS_Custom_Max_Events_Not_Reached(customEventCount))
    {
        EventTbl[  customEventCount].EventID = GPS_DEVICE_ERR_EID;
        EventTbl[customEventCount++].Mask    = CFE_EVS_FIRST_16_STOP;
    }
    else
    {
        customEventCount = -1;
        goto end_of_function;
    }
    
end_of_function:

    return customEventCount;
}


uint64 GPS_Custom_Get_Time_Uint64(void)
{
    uint64 timeStamp = 0;
    CFE_TIME_SysTime_t cfeTimeStamp = {0, 0};
    
    cfeTimeStamp = GPS_Custom_Get_Time();

    if(cfeTimeStamp.Seconds == 0 && cfeTimeStamp.Subseconds == 0)
    {
        goto end_of_function;
    }
    timeStamp = cfeTimeStamp.Seconds * 1000000;
    timeStamp += cfeTimeStamp.Subseconds / 1000;

end_of_function:

    return timeStamp;
}


CFE_TIME_SysTime_t GPS_Custom_Get_Time(void)
{
    struct timespec ts;
    CFE_TIME_SysTime_t Timestamp = {0, 0};

    clock_gettime(CLOCK_MONOTONIC, &ts);

    Timestamp.Seconds = ts.tv_sec;

    Timestamp.Subseconds = CFE_TIME_Micro2SubSecs(ts.tv_nsec / 1000);

end_of_function:
    return Timestamp;
}


//boolean GPS_Custom_Measure_DumpMsg(PX4_GpsDumpMsg_t *Measure)
//{
    //boolean returnBool = TRUE;
    ///* Null check */
    //if(0 == Measure)
    //{
        //CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                //"GPS measure dump message null pointer");
        //returnBool = FALSE;
        //goto end_of_function;
    //}

    //OS_MutSemTake(GPS_AppCustomData.MutexDump);
    //memcpy(Measure, &GPS_AppCustomData.GpsDumpMsg, 
            //sizeof(GPS_AppCustomData.GpsDumpMsg));
    //OS_MutSemGive(GPS_AppCustomData.MutexDump);

//end_of_function:

    //return returnBool;
//}


boolean GPS_Custom_Measure_PositionMsg(PX4_VehicleGpsPositionMsg_t *Measure)
{
    boolean returnBool = TRUE;
    /* Null check */
    if(0 == Measure)
    {
        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                "GPS measure dump message null pointer");
        returnBool = FALSE;
        goto end_of_function;
    }

    OS_MutSemTake(GPS_AppCustomData.MutexPosition);
    memcpy(Measure, &GPS_AppCustomData.GpsPositionMsg, 
            sizeof(GPS_AppCustomData.GpsPositionMsg));
    OS_MutSemGive(GPS_AppCustomData.MutexPosition);

end_of_function:

    return returnBool;
}


boolean GPS_Custom_Measure_SatInfoMsg(PX4_SatelliteInfoMsg_t *Measure)
{
    boolean returnBool = FALSE;
    ///* Null check */
    //if(0 == Measure)
    //{
        //CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                //"GPS measure dump message null pointer");
        //returnBool = FALSE;
        //goto end_of_function;
    //}

    //OS_MutSemTake(GPS_AppCustomData.MutexSatInfo);
    //memcpy(Measure, &GPS_AppCustomData.GpsSatInfoMsg, 
            //sizeof(GPS_AppCustomData.GpsSatInfoMsg));
    //OS_MutSemGive(GPS_AppCustomData.MutexSatInfo);

end_of_function:

    return returnBool;
}



boolean GPS_Custom_Read_and_Parse(const uint32 timeout)
{
    boolean returnBool = TRUE;
    uint32 i = 0;
    uint32 j = 0;
    uint16 satCount = 0;
    int32 bytesRead = 0;
    uint8 from_gps_data[GPS_READ_BUFFER_SIZE];
    boolean done = FALSE;
    
    bytesRead = GPS_Custom_Receive(&from_gps_data[0], 
            sizeof(from_gps_data), timeout);

    if (bytesRead < 0)
    {
        returnBool = FALSE;
        goto end_of_function;
    }
    for(i = 0;  i < bytesRead; ++i)
    {
        GPS_DeviceMessage_t message;
        GPS_ParserStatus_t status;

        if(GPS_ParseChar(from_gps_data[i], &message, &status, &done))
        {
            /* If parsechar completed a message... */
            if(TRUE == done)
            {

                /* TODO remove after debug*/
                OS_printf("ParseChar completed a message\n");
                /* end todo */

                /* Copy message to the CVT */
                CFE_SB_MsgId_t msgID = CFE_SB_GetMsgId((CFE_SB_Msg_t*)&message);
                switch(msgID)
                {
                    case GPS_NAV_DOP_MID:
                    {
                        OS_printf("IN GPS_NAV_DOP_MID\n");
                        GPS_NAV_DOP_t *msgIn = (GPS_NAV_DOP_t*) CFE_SB_GetUserData((CFE_SB_Msg_t*)&message);
                        OS_MutSemTake(GPS_AppCustomData.MutexPosition);
                        /* from cm to m */
                        GPS_AppCustomData.GpsPositionMsg.HDOP = msgIn->hDOP * 0.01f;
                        /* from cm to m */
                        GPS_AppCustomData.GpsPositionMsg.VDOP = msgIn->vDOP * 0.01f;
                        OS_MutSemGive(GPS_AppCustomData.MutexPosition);
                        break;
                    }
                    case GPS_NAV_NAVPVT_MID:
                    {
                        OS_printf("IN GPS_NAV_NAVPVT_MID\n");
                        GPS_NAV_PVT_t *msgIn = (GPS_NAV_PVT_t*) CFE_SB_GetUserData((CFE_SB_Msg_t*)&message);
                        OS_MutSemTake(GPS_AppCustomData.MutexPosition);
                        /* Check if position fix flag is good */
                        if ((msgIn->flags & GPS_NAV_PVT_FLAGS_GNSSFIXOK) == 1)
                        {
                            uint8 carr_soln = msgIn->flags >> 6;
                            GPS_AppCustomData.GpsPositionMsg.FixType = msgIn->fixType;

                            if (msgIn->flags & GPS_NAV_PVT_FLAGS_DIFFSOLN)
                            {
                                /* DGPS */
                                GPS_AppCustomData.GpsPositionMsg.FixType = 4;
                            }

                            if (carr_soln == 1)
                            {
                                /* Float RTK */
                                GPS_AppCustomData.GpsPositionMsg.FixType = 5;

                            }
                            else if (carr_soln == 2)
                            {
                                /* Fixed RTK */
                                GPS_AppCustomData.GpsPositionMsg.FixType = 6;
                            }

                            GPS_AppCustomData.GpsPositionMsg.VelNedValid = TRUE;
                        }
                        else
                        {
                            GPS_AppCustomData.GpsPositionMsg.FixType = 0;
                            GPS_AppCustomData.GpsPositionMsg.VelNedValid = FALSE;
                        }

                        GPS_AppCustomData.GpsPositionMsg.SatellitesUsed = 
                                msgIn->numSV;

                        GPS_AppCustomData.GpsPositionMsg.Lat = 
                                msgIn->lat;
                        GPS_AppCustomData.GpsPositionMsg.Lon = 
                                msgIn->lon;
                        GPS_AppCustomData.GpsPositionMsg.Alt = 
                                msgIn->hMSL;

                        GPS_AppCustomData.GpsPositionMsg.EpH = 
                                (float)msgIn->hAcc * 1e-3f;
                        GPS_AppCustomData.GpsPositionMsg.EpV = 
                                (float)msgIn->vAcc * 1e-3f;
                        GPS_AppCustomData.GpsPositionMsg.SVariance = 
                                (float)msgIn->sAcc * 1e-3f;

                        GPS_AppCustomData.GpsPositionMsg.Vel_m_s = 
                                (float)msgIn->gSpeed * 1e-3f;

                        GPS_AppCustomData.GpsPositionMsg.Vel_n_m_s = 
                                (float)msgIn->velN * 1e-3f;
                        GPS_AppCustomData.GpsPositionMsg.Vel_e_m_s = 
                                (float)msgIn->velE * 1e-3f;
                        GPS_AppCustomData.GpsPositionMsg.Vel_d_m_s = 
                                (float)msgIn->velD * 1e-3f;

                        GPS_AppCustomData.GpsPositionMsg.COG = 
                                (float)msgIn->headMot * M_DEG_TO_RAD_F * 1e-5f;
                        GPS_AppCustomData.GpsPositionMsg.CVariance = 
                                (float)msgIn->headAcc * M_DEG_TO_RAD_F * 1e-5f;

                        //Check if time and date fix flags are good
                        if ((msgIn->valid & GPS_NAV_PVT_VALID_VALIDDATE)
                            && (msgIn->valid & GPS_NAV_PVT_VALID_VALIDTIME)
                            && (msgIn->valid & GPS_NAV_PVT_VALID_FULLYRESOLVED)) 
                        {
                            /* convert to unix timestamp */
                            struct tm timeinfo;
                            timeinfo.tm_year = msgIn->year - 1900;
                            timeinfo.tm_mon  = msgIn->month - 1;
                            timeinfo.tm_mday = msgIn->day;
                            timeinfo.tm_hour = msgIn->hour;
                            timeinfo.tm_min  = msgIn->min;
                            timeinfo.tm_sec  = msgIn->sec;

                            time_t epoch     = mktime(&timeinfo);

                            if (epoch > GPS_EPOCH_SECS)
                            {
                                // FMUv2+ boards have a hardware RTC, but GPS helps us to configure it
                                // and control its drift. Since we rely on the HRT for our monotonic
                                // clock, updating it from time to time is safe.

                                struct timespec ts;
                                ts.tv_sec = epoch;
                                ts.tv_nsec = msgIn->nano;

                                //setClock(ts);

                                GPS_AppCustomData.GpsPositionMsg.TimeUtcUsec = ((uint64)epoch) * 1000000ULL;
                                GPS_AppCustomData.GpsPositionMsg.TimeUtcUsec += msgIn->nano / 1000;
                            }
                            else
                            {
                                GPS_AppCustomData.GpsPositionMsg.TimeUtcUsec = 0;
                            }
                        }
                        
                        GPS_AppCustomData.GpsPositionMsg.Timestamp = GPS_Custom_Get_Time();
                        //GPS_AppCustomData.LastTimeStamp = GPS_AppCustomData.GpsPositionMsg.Timestamp;

                        /* TODO position and velocity update rate functions
                         * and a reset function */
                        GPS_AppCustomData.RateCountVel++;
                        GPS_AppCustomData.RateCountLatLon++;
                        GPS_AppCustomData.GotPosllh = TRUE;
                        GPS_AppCustomData.GotVelned = TRUE;
                        
                        /* TODO verify this for NAV-PVT */
                        //GPS_AppCustomData.GpsPositionMsg.TimestampTimeRelative = 0;

                        OS_MutSemGive(GPS_AppCustomData.MutexPosition);
                        break;
                    }
                    case GPS_NAV_SVINFO_MID:
                    {
                        OS_printf("IN GPS_NAV_SVINFO_MID\n");
                        GPS_NAV_SVINFO_Combined_t *msgIn = (GPS_NAV_SVINFO_Combined_t*) CFE_SB_GetUserData((CFE_SB_Msg_t*)&message);
                        
                        OS_MutSemTake(GPS_AppCustomData.MutexSatInfo);
                        
                        GPS_AppCustomData.GpsSatInfoMsg.Count = msgIn->svinfo.numCh;
                        satCount = GPS_AppCustomData.GpsSatInfoMsg.Count;

                        if(GPS_AppCustomData.GpsSatInfoMsg.Count > PX4_SAT_INFO_MAX_SATELLITES)
                        {
                            CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                                    "GPS sat count %hhu > max buffer length %hhu", 
                                    GPS_AppCustomData.GpsSatInfoMsg.Count,
                                    PX4_SAT_INFO_MAX_SATELLITES);
                            satCount = PX4_SAT_INFO_MAX_SATELLITES;
                        }
                        for(j = 0; j< satCount; j++)
                        {
                            GPS_AppCustomData.GpsSatInfoMsg.Used[j] = 
                                    (uint8)(msgIn->numCh[j].flags & 0x01);
                            GPS_AppCustomData.GpsSatInfoMsg.SNR[j] = 
                                    (uint8)(msgIn->numCh[j].cno);
                                    
                            GPS_AppCustomData.GpsSatInfoMsg.Elevation[j] =
                                    (uint8)(msgIn->numCh[j].elev);
                            GPS_AppCustomData.GpsSatInfoMsg.Azimuth[j] =
                                    (uint8)((float)msgIn->numCh[j].azim * 255.0f / 360.0f);
                            GPS_AppCustomData.GpsSatInfoMsg.SVID[j] =
                                    (uint8)(msgIn->numCh[j].svid);
                        }
                        
                        GPS_AppCustomData.GpsSatInfoMsg.Timestamp = GPS_Custom_Get_Time();
                        
                        OS_MutSemGive(GPS_AppCustomData.MutexSatInfo);
                        break;
                    }
                    case GPS_ACK_NAK_MID:
                    {
                        break;
                    }
                    case GPS_ACK_ACK_MID:
                    {
                        break;
                    }
                    case GPS_CFG_PRT_MID:
                    {
                        break;
                    }
                    case GPS_CFG_MSG_MID:
                    {
                        break;
                    }
                    case GPS_CFG_RATE_MID:
                    {
                        break;
                    }
                    case GPS_CFG_SBAS_MID:
                    {
                        break;
                    }
                    case GPS_CFG_NAV5_MID:
                    {
                        break;
                    }
                    case GPS_MON_HW_MID:
                    {
                        OS_printf("IN GPS_MON_HW_MID\n");
                        OS_MutSemTake(GPS_AppCustomData.MutexPosition);
                        GPS_MON_HW_t *msgIn = (GPS_MON_HW_t*) CFE_SB_GetUserData((CFE_SB_Msg_t*)&message);

                        GPS_AppCustomData.GpsPositionMsg.NoisePerMs = msgIn->noisePerMS;
                        GPS_AppCustomData.GpsPositionMsg.JammingIndicator = msgIn->jamInd;
                        
                        OS_MutSemGive(GPS_AppCustomData.MutexPosition);
                        break;
                    }
                    default:
                    {
                        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                                "GPS parser received unexpected message");
                    }
                }
            }
        }
    }

end_of_function:
    return returnBool;
}


int32 GPS_Custom_Receive(uint8 *Buffer, uint32 Length, uint32 Timeout)
{
    int32 returnCode = 0;
    int32 bytesRead = 0;
    uint8 *payload;
    //uint8 fake_gps_data[GPS_READ_BUFFER_SIZE];
    payload = fake_gps_data;
    GPS_Header_t   header = { GPS_HEADER_SYNC1_VALUE,
                              GPS_HEADER_SYNC2_VALUE,
                              GPS_MESSAGE_CLASS_NAV,
                              GPS_MESSAGE_ID_NAV_PVT,
                              GPS_MESSAGE_NAV_PVT_LENGTH };
    GPS_Checksum_t checksum = { 0, 0 };
    GPS_NAV_PVT_t fakeNavPvt;

    PX4_GpsFixType_t FixTyp = 0;
    int32 Latitude          = 0;
    int32 Longitude         = 0;
    int32 Altitude          = 0;
    uint16 EPH              = 0;
    uint16 EPV              = 0;
    uint16 Velocity         = 0;
    int16 VN                = 0;
    int16 VE                = 0;
    int16 VD                = 0;
    uint16 COG              = 0;
    uint8 SatellitesVisible = 0;

    /* Null check */
    if(0 == Buffer)
    {
        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                "GPS receive null pointer");
        goto end_of_function;
    }

    memset(fakeNavPvt, 0, sizeof(GPS_NAV_PVT_t));

    returnCode = SIMLIB_GetGPS( &FixType, 
                                &Latitude,
                                &Longitude, 
                                &Altitude,
                                &EPH,
                                &EPV, 
                                &Velocity,
                                &VN,
                                &VE,
                                &VD,
                                &COG,
                                &SatellitesVisible );

    if (SIMLIB_OK_FRESH != returnCode)
    {
        goto end_of_function;
    }

    fakeNavPvt.fixType = (uint8)FixType;
    fakeNavPvt.lat     = Latitude;
    fakeNavPvt.lon     = Longitude;
    fakeNavPvt.hMSL    = Altitude;
    fakeNavPvt.numSV   = SatellitesVisible;
    fakeNavPvt.velN    = (int32)(VN / 1e-4f);
    fakeNavPvt.velE    = (int32)(VE / 1e-4f);
    fakeNavPvt.velD    = (int32)(VD / 1e-4f);
    fakeNavPvt.gSpeed  = (int32)(Velocity / 1e-4f);
    /* bit 0 = 1 = valid fix (i.e within DOP & accuracy masks)*/
    fakeNavPvt.flags   = 1;
    fakeNavPvt.headMot = (int32)((COG * 3.1415f / (100.0f * 180.0f)) / M_DEG_TO_RAD_F / 1e-5f);
    fakeNavPvt.hAcc    = (uint32)(EPH / 1e-1f);
    fakeNavPvt.vAcc    = (uint32)(EPV / 1e-1f);

    /* Calculate header checksum, skip two sync bytes */
    returnBool = GPS_Custom_SetChecksum((uint8 *)&header + 2, 
            sizeof(header) - 2, &checksum); 
    if (FALSE == returnBool)
    {
        returnBool = FALSE;
        goto end_of_function;
    }

    /* Calculate (add) payload checksum */
    returnBool = GPS_Custom_SetChecksum(payload, sizeof(GPS_NAV_PVT_t), &checksum); 
    if (FALSE == returnBool)
    {
        returnBool = FALSE;
        goto end_of_function;
    }

    Buffer[0] = header.sync1;
    Buffer[1] = header.sync2;
    Buffer[2] = header.class;
    Buffer[3] = header.id;
    Buffer[4] = header.length;
    Buffer[5] = header.length >> 8;
    //Buffer[6] = iTOW;
    //Buffer[7] = iTOW;
    //Buffer[8] = iTOW;
    //Buffer[9] = iTOW;
    //Buffer[10] = year;
    //Buffer[11] = year;
    //Buffer[12] = month;
    //Buffer[13] = day;
    //Buffer[14] = hour;
    //Buffer[15] = min;
    //Buffer[16] = sec;
    //Buffer[17] = valid;
    //Buffer[18] = tAcc;
    //Buffer[19] = tAcc;
    //Buffer[20] = tAcc;
    //Buffer[21] = tAcc;
    //Buffer[22] = nano;
    //Buffer[23] = nano;
    //Buffer[24] = nano;
    //Buffer[25] = nano;
    Buffer[26] = fakeNavPvt.fixType;
    Buffer[27] = fakeNavPvt.flags;
    //Buffer[28] = flags2;
    Buffer[29] = fakeNavPvt.numSV;
    Buffer[30] = fakeNavPvt.lon;
    Buffer[31] = fakeNavPvt.lon >> 8;
    Buffer[32] = fakeNavPvt.lon >> 16;
    Buffer[33] = fakeNavPvt.lon >> 24;
    Buffer[34] = fakeNavPvt.lat;
    Buffer[35] = fakeNavPvt.lat >> 8;
    Buffer[36] = fakeNavPvt.lat >> 16;
    Buffer[37] = fakeNavPvt.lat >> 24;
    //Buffer[38] = height;
    //Buffer[39] = height;
    //Buffer[40] = height;
    //Buffer[41] = height;
    //Buffer[42] = hSL;
    //Buffer[43] = hSL;
    //Buffer[44] = hSL;
    //Buffer[45] = hSL;





end_of_function:

    return bytesRead;
}


boolean GPS_Custom_SetChecksum(const uint8 *buffer, const uint16 length, GPS_Checksum_t *checksum)
{
    uint16 i = 0;
    boolean returnBool = TRUE;
    
    /* Null check */
    if(0 == checksum || 0 == buffer)
    {
        CFE_EVS_SendEvent(GPS_DEVICE_ERR_EID, CFE_EVS_ERROR,
                "GPS set checksum null pointer");
        returnBool = FALSE;
        goto end_of_function;
    }
    
    for (i = 0; i < length; i++) 
    {
        checksum->ck_a = checksum->ck_a + buffer[i];
        checksum->ck_b = checksum->ck_b + checksum->ck_a;
    }

end_of_function:
    return returnBool;
}
