def help():
    res="Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line Special commands: !help !done"
    return res

def plain():
    res_plain="plain"
    return res_plain

def bold():
    res_bold="bold"
    return res_bold

def italic():
    res_italic="italic"
    return res_italic

def inline_code():
    res_inline_code="inline_code"
    return res_inline_code

def link():
    res_link="link"
    return res_link

def header():
    res_header="header"
    return res_header

def unordered_list():
    res_unordered_list="unordered_list"
    return res_unordered_list

def ordered_list():
    res_ordered_list="ordered_list"
    return res_ordered_list

def new_line():
    res_new_line="new_line"
    return res_new_line

menu=""
while menu != "!done" :
    menu = input("Choose a formatter: >")
    if menu == "!help" :
          print(help())
    if menu == "plain" :
        print(plain())
    if menu == "bold" :
          print(bold())
    if menu == "italic" :
          print(italic())
    if menu == "inline_code" :
          print(inline_code())
    if menu == "link" :
          print(link())
    if menu == "header" :
          print(header())
    if menu == "unordered_list" :
          print(unordered_list())
    if menu == "ordered_list" :
          print(ordered_list())
    if menu == "new_line" :
        print(new_line())
    if menu not in ["!done","!help","plain","bold","italic","inline_code","link","header","unordered_list",
                    "ordered_list","new_line"]: print ("Unknown formatting type or command")
