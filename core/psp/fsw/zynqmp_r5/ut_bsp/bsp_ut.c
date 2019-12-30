/******************************************************************************
** File:  bsp_ut.c
**
**
**      This is governed by the NASA Open Source Agreement and may be used,
**      distributed and modified only pursuant to the terms of that agreement.
**
**      Copyright (c) 2004-2015, United States government as represented by the
**      administrator of the National Aeronautics Space Administration.
**      All rights reserved.
**
**
** Purpose:
**   BSP unit test implementation functions.
**
** History:
**   Created on: Feb 10, 2015
**
******************************************************************************/


/*
 * NOTE - This entire source file is only relevant for unit testing.
 * It should not be included in a "normal" BSP build.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include "cfe_platform_cfg.h"
#include <FreeRTOS.h>
#include "timers.h"
#include <ff.h>
#include <xil_printf.h>

#include "utbsp.h"
#include "uttest.h"
#include "osapi-os-core.h"


static TaskHandle_t xInitTask;



#define TIMER_ID	1
#define DELAY_10_SECONDS	10000UL
#define DELAY_1_SECOND		1000UL
#define TIMER_CHECK_THRESHOLD	9



/*
**  Local Variables
*/
static uint32 CurrVerbosity = (2 << UTASSERT_CASETYPE_PASS) - 1;

void UT_BSP_ParseCommandLine(int argc, char *argv[])
{
    uint8 UserShift;
    int opt;

    UserShift = UTASSERT_CASETYPE_NONE;
    while ((opt = getopt(argc, argv, "v:qd")) != -1)
    {
        switch (opt) {
        case 'd':
            UserShift = UTASSERT_CASETYPE_DEBUG;
            break;
        case 'q':
            UserShift = UTASSERT_CASETYPE_FAILURE;
            break;
        case 'v':
            UserShift = atoi(optarg);
            break;
        default: /* '?' */
            fprintf(stderr, "Usage: %s [-v verbosity] [-d] [-q]\n",
                    argv[0]);
            exit(EXIT_FAILURE);
        }
        if (UserShift > 0 && UserShift < UTASSERT_CASETYPE_MAX)
        {
            CurrVerbosity = (2 << UserShift) - 1;
        }
    }


}

void UT_BSP_Setup(const char *Name)
{
    UT_BSP_DoText(UTASSERT_CASETYPE_BEGIN, Name);

    /*
    ** Create local directories for "disk" mount points
    **  See bsp_voltab for the values
    */
    xil_printf("Making directories: ram0, ram1, eeprom1 for OSAL mount points\n\r");
    f_mkdir("ram0");
    f_mkdir("ram1");
    f_mkdir("eeprom1");

    /* For unit testing, the ram3/ram4 mount points need to exist as well */
    f_mkdir("ram3");
    f_mkdir("ram4");
}

void UT_BSP_StartTestSegment(uint32 SegmentNumber, const char *SegmentName)
{
    char ReportBuffer[128];

    snprintf(ReportBuffer,sizeof(ReportBuffer), "%02u %s", (unsigned int)SegmentNumber, SegmentName);
    UT_BSP_DoText(UTASSERT_CASETYPE_BEGIN, ReportBuffer);
}

void UT_BSP_DoText(uint8 MessageType, const char *OutputMessage)
{
   const char *Prefix;

   if ((CurrVerbosity >> MessageType) & 1)
   {
      switch(MessageType)
      {
      case UTASSERT_CASETYPE_ABORT:
         Prefix = "ABORT";
         break;
      case UTASSERT_CASETYPE_FAILURE:
         Prefix = "FAIL";
         break;
      case UTASSERT_CASETYPE_MIR:
         Prefix = "MIR";
         break;
      case UTASSERT_CASETYPE_TSF:
         Prefix = "TSF";
         break;
      case UTASSERT_CASETYPE_TTF:
          Prefix = "TTF";
          break;
      case UTASSERT_CASETYPE_NA:
         Prefix = "N/A";
         break;
      case UTASSERT_CASETYPE_BEGIN:
         Prefix = "BEGIN";
         break;
      case UTASSERT_CASETYPE_END:
         Prefix = "END";
         break;
      case UTASSERT_CASETYPE_PASS:
         Prefix = "PASS";
         break;
      case UTASSERT_CASETYPE_INFO:
         Prefix = "INFO";
         break;
      case UTASSERT_CASETYPE_DEBUG:
         Prefix = "DEBUG";
         break;
      default:
         Prefix = "OTHER";
         break;
      }
      xil_printf("[%5s] %s\n\r",Prefix,OutputMessage);
   }

   /*
    * If any ABORT (major failure) message is thrown,
    * then actually call abort() to stop the test and dump a core
    */
   if (MessageType == UTASSERT_CASETYPE_ABORT)
   {
       abort();
   }
}

void UT_BSP_DoReport(const char *File, uint32 LineNum, uint32 SegmentNum, uint32 TestSeq, uint8 MessageType, const char *SubsysName, const char *ShortDesc)
{
    uint32 FileLen;
    const char *BasePtr;
    char ReportBuffer[128];

    FileLen = strlen(File);
    BasePtr = File + FileLen;
    while (FileLen > 0)
    {
        --BasePtr;
        --FileLen;
        if (*BasePtr == '/' || *BasePtr == '\\')
        {
            ++BasePtr;
            break;
        }
    }

    snprintf(ReportBuffer,sizeof(ReportBuffer), "%02u.%03u %s:%u - %s",
            (unsigned int)SegmentNum, (unsigned int)TestSeq,
            BasePtr, (unsigned int)LineNum, ShortDesc);

    UT_BSP_DoText(MessageType, ReportBuffer);
}

void UT_BSP_DoTestSegmentReport(const char *SegmentName, const UtAssert_TestCounter_t *TestCounters)
{
    char ReportBuffer[128];

    snprintf(ReportBuffer,sizeof(ReportBuffer),
            "%02u %-20s TOTAL::%-4u  PASS::%-4u  FAIL::%-4u   MIR::%-4u   TSF::%-4u   N/A::%-4u\n",
            (unsigned int)TestCounters->TestSegmentCount,
            SegmentName,
            (unsigned int)TestCounters->TotalTestCases,
            (unsigned int)TestCounters->CaseCount[UTASSERT_CASETYPE_PASS],
            (unsigned int)TestCounters->CaseCount[UTASSERT_CASETYPE_FAILURE],
            (unsigned int)TestCounters->CaseCount[UTASSERT_CASETYPE_MIR],
            (unsigned int)TestCounters->CaseCount[UTASSERT_CASETYPE_TSF],
            (unsigned int)TestCounters->CaseCount[UTASSERT_CASETYPE_NA]);


    UT_BSP_DoText(UTASSERT_CASETYPE_END, ReportBuffer);
}

void UT_BSP_EndTest(const UtAssert_TestCounter_t *TestCounters)
{
   int status = 0;

   /*
    * Only output a "summary" if there is more than one test Segment.
    * Otherwise it is a duplicate of the report already given.
    */
   if (TestCounters->TestSegmentCount > 1)
   {
       UT_BSP_DoTestSegmentReport("SUMMARY", TestCounters);
   }

   xil_printf("COMPLETE: %u tests Segment(s) executed\n\n\r", (unsigned int)TestCounters->TestSegmentCount);

   /*
    * The Linux UT BSP allows at least a 7 bit status code to be returned to the OS (i.e. the exit status
    * of the process).  This is useful to report pass/fail.  Because we have multiple bits, we can make
    * descriptive exit status codes to indicate what went wrong.  Anything nonzero represents failure.
    *
    * Consider Failures as well as "TSF" (setup failures) to be grounds for returning nonzero (bad) status.
    * Also the lack of ANY test cases should produce a bad status.
    *
    * "MIR" results should not produce a bad status -- these may have worked fine, we do not know.
    *
    * Likewise "N/A" tests are simply not applicable, so we just ignore them.
    */

   if (TestCounters->TotalTestCases == 0)
   {
      status |= 0x01;
   }

   if (TestCounters->CaseCount[UTASSERT_CASETYPE_FAILURE] > 0)
   {
      status |= 0x02;
   }

   if (TestCounters->CaseCount[UTASSERT_CASETYPE_TSF] > 0)
   {
      status |= 0x04;
   }

   exit(status);
}

/******************************************************************************
**  Function:  main()
**
**  Purpose:
**    BSP Unit Test Application entry point.
**
**  Arguments:
**    (none)
**
**  Return:
**    (none)
*/

void init_main(void *pvParameters)
{
   /*
   ** Call application specific entry point.
   */
   OS_Application_Startup();

   /*
   ** In unit test mode, call the UtTest_Run function (part of UT Assert library)
   */
   UtTest_Run();
   UT_BSP_EndTest(UtAssert_GetCounters());
}



int main(int argc, char *argv[])
{
	UT_BSP_Setup("R5-FreeRTOS UNIT TEST");

   xTaskCreate( init_main,
				 ( const char * ) "init",
				 16536,
				 NULL,
				 50,
				 &xInitTask);

   /* Start the tasks and timer running. */
   vTaskStartScheduler();

   /* If all is well, the scheduler will now be running, and the following line
   will never be reached.  If the following line does execute, then there was
   insufficient FreeRTOS heap memory available for the idle and/or timer tasks
   to be created.  See the memory management section on the FreeRTOS web site
   for more details. */
   for( ;; );

   /* Should typically never get here */
   return(EXIT_SUCCESS);
}

