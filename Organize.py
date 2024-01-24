def run_macro(macro_name):
    notepad.runMenuCommand('Macro', '1 Numbers remain')
    notepad.runMenuCommand('Macro', '2 Remove spaces')
    notepad.runMenuCommand('Macro', '3 Add quotes')
    notepad.runMenuCommand('Macro', '4 Pretty')
    notepad.runMenuCommand('Macro', '5 Add 20000')
    editor = notepad.getCurrentEditor()
    editor.addText(macro_name)
    editor.clearAll()

for macro_name in macro_names:
    run_macro(macro_name)