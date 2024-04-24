from openpyxl import load_workbook
import config


def find_name(name):
    wb = load_workbook(filename=config.path_to_main)
    ws = wb['main']
    found = []

    for row in ws.iter_rows(max_row=1000, min_col=8, max_col=8):
        for cell in row:
            try:
                if name in cell.value:
                    data = {'name': ws.cell(row=cell.row, column=8).value,
                            'company': ws.cell(row=cell.row, column=5).value,
                            'localization': ws.cell(row=cell.row, column=2).value,
                            'phase': ws.cell(row=cell.row, column=10).value}
                    found.append(data)
            except:
                continue
    return found


