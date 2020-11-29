from openpyxl import load_workbook
wb = load_workbook('./db.xlsx')
sheet = wb.get_sheet_by_name("Лист1")
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
arr = []
for i in range(2, 31):
		x = []
		for j in char_range("A", "K"):
			x.append(sheet[f"{j}{i}"].value)
		arr.append(x)
j = 0
for i in arr:
	k = f'INSERT INTO "Apps" ("Name","Category","Views","Price","Rating","SourceCode","Functions","Tags","Size","Age", "Desc") VALUES ("{i[0]}","{i[1]}",0,"{i[4]}","{i[5]}","{i[6]}","{i[7]}","{i[8]}","{i[10]}","{i[9]}", "{i[2]}");'
	print(k)
	j += 1
"""INSERT INTO "main"."Apps"("id","Name","Category","Views","Price","Rating","SourceCode","Functions","Tags","Size","Age") VALUES (NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);"""