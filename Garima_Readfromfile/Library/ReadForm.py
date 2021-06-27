import xlrd

class ReadForm():
    def readList(self,row,path):
        rownum=1
        wb=xlrd.open_workbook_xls(path)
        sheet=wb.sheet_by_index(0)

        for i in range(sheet.nrows):
            if(sheet.cell_value(i,0)) == int(row):
                rownum=i
                break;

        return [sheet.cell_value(rownum,1),sheet.cell_value(rownum,2),sheet.cell_value(rownum,3),sheet.cell_value(rownum,4)]

