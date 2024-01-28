def run_macro(macro_name):
    notepad.runMenuCommand('Macro', macro_name)

macro_names = ['1 Numbers remain', '2 Remove spaces', '3 Add quotes', '4 Pretty', '5 Add 20000']

# Run each macro
for macro_name in macro_names:
    run_macro(macro_name)
