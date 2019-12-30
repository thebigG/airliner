#include <untar.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "common_types.h"
#include "osapi.h"
#include "utassert.h"
#include "uttest.h"
#include "utbsp.h"
#include <nuttx/binfmt/binfmt.h>
#include <nuttx/symtab.h>


void TestUntar(void);
void TestDynamicLoader(void);

os_fs_err_name_t errname;

extern unsigned char testDir1[];
extern unsigned int testDir1Size;

extern unsigned char CFS_LIB[];
extern unsigned int CFS_LIBSize;

extern int load_module(struct binary_s *bin);

extern symtab_s OS_DL_Exports[OS_DL_EXPORT_MAX_COUNT];


/* *************************************** MAIN ************************************** */

void OS_Application_Startup(void)
{
    errname[0] = 0;

    if (OS_API_Init() != OS_SUCCESS)
    {
        UtAssert_Abort("OS_API_Init() failed");
    }

    /*
     * Register the test setup and check routines in UT assert
     *
     * It is done this way so that the output is logically grouped,
     * otherwise the entire thing would be lumped together
     * as a single test case.
     */
    UtTest_Add(TestUntar, NULL, NULL, "TestUntar");
    UtTest_Add(TestDynamicLoader, NULL, NULL, "TestDynamicLoader");
}

void TestUntar(void)
{
    int       status;
    os_dirp_t dirp0;
    char      dir0[OS_MAX_PATH_LEN];
    os_dirent_t   *dirent_ptr0;
    int size = 0;
    int fd = 0;
    char buffer [30] = "";

    strcpy(dir0,"/drive0");

    /* Make the file system */
    status = OS_mkfs(0,"/ramdev0","RAM",512,200);
    UtAssert_True(status == OS_SUCCESS, "status after mkfs = %d",(int)status);

    status = OS_mount("/ramdev0","/drive0");
    UtAssert_True(status == OS_SUCCESS, "status after mount = %d",(int)status);

	untar((char*)testDir1, testDir1Size, "0:/");

    dirp0 = OS_opendir(dir0);
    UtAssert_True(dirp0 != NULL, "OS_opendir not null");

    /* try to read the two folders that are in the "/" */
    /* Have to make it a loop to see if we can find the directories in question */

    dirent_ptr0 = OS_readdir (dirp0);
    while (dirent_ptr0 != NULL)
    {
        if ( strncmp(dirent_ptr0 -> d_name,"DIR_ONE",strlen("DIR_ONE")) == 0)
        {
            break;
        }
        else
            dirent_ptr0 = OS_readdir(dirp0);
    }
    UtAssert_True(dirent_ptr0 != NULL, "DIR_ONE found");

    dirent_ptr0 = OS_readdir (dirp0);
    while (dirent_ptr0 != NULL)
    {
        if ( strncmp(dirent_ptr0 -> d_name,"helloWorld.txt",strlen("helloWorld.txt")) == 0)
        {
            break;
        }
        else
            dirent_ptr0 = OS_readdir(dirp0);
    }
    UtAssert_True(dirent_ptr0 != NULL, "helloWorld.txt found");

    status = OS_open("/drive0/helloWorld.txt", OS_READ_ONLY, 0);
    UtAssert_True(status == OS_SUCCESS, "status after reopen = %d",(int)status);

    fd = status;

    size = sizeof(buffer);
    status = OS_read(fd,(void*)buffer, size);
    UtAssert_True(status > OS_SUCCESS, "status after read = %d",(int)status);
    UtAssert_StrCmp(buffer, "Hello world.\n", "File contents are incorrect");
}


void TestDynamicLoader(void)
{

    int       status;
    os_dirp_t dirp0;
    char      dir0[OS_MAX_PATH_LEN];
    os_dirent_t   *dirent_ptr0;
    int size = 0;
    int fd = 0;
    char buffer [30] = "";
    int loaderResult;
    struct binary_s binFile;

    strcpy(dir0,"/drive0");

	untar((char*)CFS_LIB, CFS_LIBSize, "0:/");

	{
	    int status;
		static FIL fil;
		char buff[100];
		UINT bytesToRead = 8;
		UINT bytesRead = 1;

	    status = f_open(&fil, "0:/CFS_LIB.so", FA_READ);
        if(status == FR_OK)
        {
        	unsigned int addr = 0;

        	while(bytesRead > 0)
        	{
            	f_read(&fil, buff, bytesToRead, &bytesRead);
        		xil_printf("%08x   ", addr);
        		char text[10] = {0};

            	for(unsigned int i = 0; i < bytesRead; ++i)
            	{
            		addr += 1;

            		if(buff[i] >= 32 && buff[i] <= 126)
            		{
            			text[i] = buff[i];
            		}
            		else
            		{
            			text[i] = '.';
            		}

            		xil_printf("%02x ", buff[i]);
            		if(i == 3)
            		{
            			xil_printf(" ");
            		}
            	}
    			xil_printf("  %s\n", text);
        	}
        }


        f_close(&fil);
	}

    dirp0 = OS_opendir(dir0);
    UtAssert_True(dirp0 != NULL, "OS_opendir not null");

    status = OS_open("/drive0/CFS_LIB.so", OS_READ_ONLY, 0);
    UtAssert_True(status >= OS_SUCCESS, "status after reopen = %d",(int)status);

    fd = status;

    size = sizeof(buffer);
    status = OS_read(fd,(void*)buffer, size);
    UtAssert_True(status > OS_SUCCESS, "status after read = %d",(int)status);

    status = OS_close(fd);
    UtAssert_True(status == OS_SUCCESS, "status after close = %d",(int)status);

    strcpy((char*)binFile.filename, "0:/CFS_LIB.so");
    binFile.exports = OS_DL_Exports;
    binFile.nexports = 0;
    binFile.max_exports = OS_DL_EXPORT_MAX_COUNT;

    /* int load_module(FAR struct binary_s *bin); */
    binfmt_initialize();
    loaderResult = load_module(&binFile);

    status = OS_SymbolTableDump("/drive0/symbols.log", 10000);
    UtAssert_True(status == OS_SUCCESS, "status after symbol dump = %d",(int)status);

    struct symtab_s *newSymTab = symtab_findbyname(binFile.exports, "getAnswer", binFile.nexports);
    UtAssert_True(status >= OS_SUCCESS, "status after reopen = %d",(int)status);



    newSymTab = symtab_findorderedbyname(binFile.exports, "getAnswer", binFile.nexports);
    UtAssert_True(status >= OS_SUCCESS, "status after reopen = %d",(int)status);



}

