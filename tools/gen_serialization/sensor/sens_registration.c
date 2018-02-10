/* This file was autogenerated from template version 0.0.0.1 and autogenerator version 0.0.0.1 */

#include "sens_registration.h"

#ifdef __cplusplus
extern "C" {
#endif

uint32 SENS_RegisterSerializationFuncs()
{
	int32 Status = CFE_SUCCESS;

	/* Register each message with PBL */
	Status = PBLIB_RegisterTlmMessage(0x0c55, "SENS_HkTlm_t");
	if (Status != CFE_SUCCESS)
	{
		goto SENS_RegisterSerializationFuncs_Exit_Tag;
	}
	
SENS_RegisterSerializationFuncs_Exit_Tag:
    return Status;
}

#ifdef __cplusplus
} /* extern "C" */
#endif

