import xlrd

class CommonUtility():
    def Read_excel_Value(self,rowvalue,filePath):
        rownum =1
        xls=xlrd.open_workbook_xls(filePath)
        sheet=xls.sheet_by_index(0)

        for i in range(sheet.nrows):
            if (sheet.cell_value(i,0))== int(rowvalue):
                rownum=i
                break;

        return sheet.cell(rownum,1)




