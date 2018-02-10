#ifndef CS_PLATFORM_CFG_H
#define CS_PLATFORM_CFG_H

/*************************************************************************
 ** Macro Definitions
 *************************************************************************/

/**
**  \cscfg EEPROM File Table -- default table filename
**
**  \par Description:
**       This parameter defines the default filename for the
**       EEPROM addresses File Table.
**
**  \par Limits:
**       The string length (including string terminator) cannot exceed
**       #OS_MAX_PATH_LEN.  (limit is not verified)
*/
#define CS_DEF_EEPROM_TABLE_FILENAME                "/cf/apps/cs_eepromtbl.tbl"

/**
**  \cscfg Memory Address File Table -- default table filename
**
**  \par Description:
**       This parameter defines the default filename for the
**       Memory addresses File Table.
**
**  \par Limits:
**       The string length (including string terminator) cannot exceed
**       #OS_MAX_PATH_LEN.  (limit is not verified)
*/
#define CS_DEF_MEMORY_TABLE_FILENAME                "/cf/apps/cs_memorytbl.tbl"

/**
**  \cscfg Tables File Table -- default table filename
**
**  \par Description:
**       This parameter defines the default filename for the
**       Tables List File Table.
**
**  \par Limits:
**       The string length (including string terminator) cannot exceed
**       #OS_MAX_PATH_LEN.  (limit is not verified)
*/
#define CS_DEF_TABLES_TABLE_FILENAME                "/cf/apps/cs_tablestbl.tbl"

/**
**  \cscfg Application File Table -- default table filename
**
**  \par Description:
**       This parameter defines the default filename for the
**       Application List File Table.
**
**  \par Limits:
**       The string length (including string terminator) cannot exceed
**       #OS_MAX_PATH_LEN.  (limit is not verified)
*/
#define CS_DEF_APP_TABLE_FILENAME                   "/cf/apps/cs_apptbl.tbl"

/**
**  \cscfg Application Pipe Depth
**
**  \par Description:
**       This parameter defines the depth of the CS input pipe.  The
**       depth should be deep enough to accommodate all of the DS
**       command packets and all of the subscribed telemetry packets
**       that might be generated by applications with a priority
**       higher than the CS application.
**
**  \par Limits:
**		 The value must be greater than zero and cannot exceed the
**       definition of #CFE_SB_MAX_PIPE_DEPTH.
*/
#define CS_PIPE_DEPTH                   12

/** \cscfg  Maximum number of entries in the Eeprom table to checksum
 **  
 **  \par  Description:
 **        Maximum number of entries that can be in the table of
 **        Eeprom areas to checksum.
 **
 **  \par Limits:
 **     This parameter is limited by the  uint16 datatype that defines it.
 **     This parameter is limited to 65535. 
 **
 */
#define CS_MAX_NUM_EEPROM_TABLE_ENTRIES     16

/** \cscfg  Maximum number of entries in the Memory table to checksum
 **  
 **  \par  Description:
 **        Maximum number of entries that can be in the table of
 **        Memory areas to checksum.
 **
 **  \par Limits:
 **     This parameter is limited by the  uint16 datatype that defines it.
 **     This parameter is limited to 65535. 
 **
 */
#define CS_MAX_NUM_MEMORY_TABLE_ENTRIES     16

/** \cscfg Maximum number of tables to checksum
 **  
 **  \par  Description:
 **        Maximum number of entries in the table of tables to checksum 
 **
 **  \par Limits:
 **       This parameter is limited by the maximum number of tables allowed
 **       in the system. This parameter is limited to #CFE_TBL_MAX_NUM_TABLES
 **
 */
#define CS_MAX_NUM_TABLES_TABLE_ENTRIES     24

/** \cscfg Maximum number of applications to checksum
 **  
 **  \par  Description:
 **        Maximum number of entries in the table of applications to checksum 
 **
 **  \par Limits:
 **       This parameter is limited by the maximum number of applications allowed
 **       in the system. This parameter is limited to #CFE_ES_MAX_APPLICATIONS
 **
 */
#define CS_MAX_NUM_APP_TABLE_ENTRIES        24

/** \cscfg Default number of bytes to checksum per cycle
 **  
 **  \par  Description:
 **        The default number of bytes that are checksummed in a single CS cycle
 **
 **  \par Limits:
 **       This parameter is limited by the maximum value allowed by the data type.
 **       In this case, the data type is an unsigned 32-bit integer, so the valid 
 **       range is 0 to 0xFFFFFFFF.  Note that "0" is a valid value, and will 
 **       result in a checksum of 0.
 **
 */
#define CS_DEFAULT_BYTES_PER_CYCLE          (1024 *16) 

/** \cscfg CS Child Task Priority
 **  
 **  \par  Description:
 **        Priority of child tasks created by CS.  Lower numbers are higher priority,
 **        with 1 being the highest priority in the case of a child task.
 **
 **  \par Limits:
 **       Valid range for a child task is 1 to 255, but the priority cannot be 
 **       higher (lower number) than the CS App priority. 
 **
 */
#define CS_CHILD_TASK_PRIORITY              200


/** \cscfg Delay between checksumming cycles for child task
 **  
 **  \par  Description:
 **        CS child tasks perform checksum cycles like the main App.
 **        Since the child tasks aren't scheduled, there needs to be 
 **        some other mechanism to prevent it from hogging the CPU.
 **        This parameter specifies the number of milliseconds to delay
 **        in between cycles.
 **
 **  \par Limits:
 **       CS does not place limits on this parameter. It is intended to
 **       be configurable to prevent the child task from hogging the CPU
 **
 */
#define CS_CHILD_TASK_DELAY                 1000


/** \cscfg Timeout for waiting for other apps to start
 **  
 **  \par  Description:
 **        CS waits for all of the other applications that are listed in
 **        the startup script to start before entering its main loop. If
 **        not all of those apps start, CS can pend indefinitely without
 **        a timeout. Once CS waits this amount of time ( in milliseconds)
 **        it will start regardless of the status of the rest of the apps
 **        in the startup script.  
 **
 **  \par Limits:
 **       CS does not place limits on this parameter. It is intended to
 **       be configurable to allow enough time for all apps to start.
 **
 */
#define CS_STARTUP_TIMEOUT                  60000



/** \cscfg Desired state of the checksumming of OS code segment at power on
**
**  \par Description:
**       This determines the default state the checksumming of
**       OS code segment should be in at power on
**
**  \par Limits:
**       This can either be CS_STATE_ENABLED or CS_STATE_DISABLED
*/
#define CS_OSCS_CHECKSUM_STATE CS_STATE_ENABLED

/** \cscfg Desired state of the checksumming of CFE core checksum at power on
**
**  \par Description:
**       This determines the default state the checksumming of
**       CFE core should be in at power on
**
**  \par Limits:
**       This can either be CS_STATE_ENABLED or CS_STATE_DISABLED
*/
#define CS_CFECORE_CHECKSUM_STATE CS_STATE_ENABLED

/** \cscfg Desired state of the EEPROM table at power on
**
**  \par Description:
**       This determines the default state the EEPROM table should
**       be in at power on
**
**  \par Limits:
**       This can either be CS_STATE_ENABLED or CS_STATE_DISABLED
*/
#define CS_EEPROM_TBL_POWERON_STATE CS_STATE_ENABLED

/** \cscfg Desired state of the EEPROM table at power on
**
**  \par Description:
**       This determines the default state the Memory table should
**       be in at power on
**
**  \par Limits:
**       This can either be CS_STATE_ENABLED or CS_STATE_DISABLED
*/
#define CS_MEMORY_TBL_POWERON_STATE CS_STATE_ENABLED

/** \cscfg Desired state of the Applications table at power on
**
**  \par Description:
**       This determines the default state the EEPROM table should
**       be in at power on
**
**  \par Limits:
**       This can either be CS_STATE_ENABLED or CS_STATE_DISABLED
*/
#define CS_APPS_TBL_POWERON_STATE   CS_STATE_ENABLED

/** \cscfg Desired state of the Tables table at power on
**
**  \par Description:
**       This determines the default state the EEPROM table should
**       be in at power on
**
**  \par Limits:
**       This can either be CS_STATE_ENABLED or CS_STATE_DISABLED
*/
#define CS_TABLES_TBL_POWERON_STATE CS_STATE_ENABLED

/** \cscfg Whether to preserve checksum states on processor reset
**
**  \par Description:
**       This determines whether to preserve checksum
**       enabled/disabled states on processor reset
**
**  \par Limits:
**       None
*/
#define CS_PRESERVE_STATES_ON_PROCESSOR_RESET TRUE


/** \cscfg Name of the Critical Data Store Used for CS
**
**  \par Description:
**       Name of the Critical Data Store for CS
**       This CDS is used to preserve the checksum
**       enabled states for EERPOM, Memory, Apps, Tables tables
**       as well as OS code segment and cFE core states
**
**  \par Limits:
**       Must be a unique string with regards to CDS
*/
#define CS_CDS_NAME  "CS_CDS"

/** \cscfg Mission specific version number for CS application
**  
**  \par Description:
**       An application version number consists of four parts:
**       major version number, minor version number, revision
**       number and mission specific revision number. The mission
**       specific revision number is defined here and the other
**       parts are defined in "cs_version.h".
**
**  \par Limits:
**       Must be defined as a numeric value that is greater than
**       or equal to zero.
*/
#define CS_MISSION_REV            0

#endif /*_cs_platform_cfg_*/

/************************/
/*  End of File Comment */
/************************/

