/************************************************************************
** Includes
*************************************************************************/
#include "cfe.h"
#include "md_tbldefs.h"
#include "md_app.h"
#include "cfs_utils.h"
#include "cfe_tbl_filedef.h"
#include "md_platform_cfg.h"


MD_DwellTableLoad_t     MD_Default_Dwell4_Tbl =
{
/* Enabled State */ MD_DWELL_STREAM_DISABLED,
#if MD_SIGNATURE_OPTION == 1  
/* Signature     */ "Default Table 4",
#endif
/* Entry    Length    Delay    Offset           SymName     */
/*   1 */{{      0,       0,  {     0,               ""  }   },
/*   2 */ {      0,       0,  {     0,               ""  }   },
/*   3 */ {      0,       0,  {     0,               ""  }   },
/*   4 */ {      0,       0,  {     0,               ""  }   },
/*   5 */ {      0,       0,  {     0,               ""  }   },
/*   6 */ {      0,       0,  {     0,               ""  }   },
/*   7 */ {      0,       0,  {     0,               ""  }   },
/*   8 */ {      0,       0,  {     0,               ""  }   },
/*   9 */ {      0,       0,  {     0,               ""  }   },
/*  10 */ {      0,       0,  {     0,               ""  }   },
/*  11 */ {      0,       0,  {     0,               ""  }   },
/*  12 */ {      0,       0,  {     0,               ""  }   },
/*  13 */ {      0,       0,  {     0,               ""  }   },
/*  14 */ {      0,       0,  {     0,               ""  }   },
/*  15 */ {      0,       0,  {     0,               ""  }   },
/*  16 */ {      0,       0,  {     0,               ""  }   },
/*  17 */ {      0,       0,  {     0,               ""  }   },
/*  18 */ {      0,       0,  {     0,               ""  }   },
/*  19 */ {      0,       0,  {     0,               ""  }   },
/*  20 */ {      0,       0,  {     0,               ""  }   },
/*  21 */ {      0,       0,  {     0,               ""  }   },
/*  22 */ {      0,       0,  {     0,               ""  }   },
/*  23 */ {      0,       0,  {     0,               ""  }   },
/*  24 */ {      0,       0,  {     0,               ""  }   },
/*  25 */ {      0,       0,  {     0,               ""  }   },
}
};

CFE_TBL_FILEDEF(MD_Default_Dwell4_Tbl, MD.DWELL_TABLE4, MD Dwell Table 4,md_dw04.tbl)

/************************/
/*  End of File Comment */
/************************/
