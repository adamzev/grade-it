from worksheet_gen import WorksheetGen


specs = {
    "problem_type": "add",
    "problem_count": 16,
}
my_gen = WorksheetGen("add", "add", specs)

sheet = my_gen.create_sheet()