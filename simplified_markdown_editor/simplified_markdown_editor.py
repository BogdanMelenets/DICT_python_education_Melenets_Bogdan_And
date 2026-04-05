def help():
    return "Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line Special commands: !help !done"

def plain():
    return input("Text: >")

def bold():
    return "**"+input("Text: >")+"**"

def italic():
    return "*" + input("Text: >") + "*"

def inline_code():
    return "```" + input("Text: >") + "```"

def link():
    return "["+ input("Label: >")+"]("+ input("URL: >")+")"

def header():
    res_header=""
    Lev=0
    while Lev not in range(1,6):
        Lev= int(input("Level: >"))
        if Lev in range(1,6):
           string = input("Text: >")
           for i in range(Lev): res_header=res_header+"#"
           res_header = res_header + " " + string
        else: print("The level should be within the range of 1 to 6.")
    return res_header

def unordered_list():
    res_unordered_list="unordered_list"
    return res_unordered_list

def ordered_list():
    res_ordered_list="ordered_list"
    return res_ordered_list

def new_line():
    return ""

menu=""
string=""
result=[]
resi=0
while menu != "!done" :
    menu = input("Choose a formatter: >")
    if menu == "!help" :
          print(help())
    if menu in ["!done","!help","plain","bold","italic","inline_code","link","header","unordered_list",
                    "ordered_list","new_line"]:
        if menu == "plain":
            result.append(plain())
            resi = resi + 1
        if menu == "bold":
            result.append(bold())
            resi = resi + 1
        if menu == "italic":
            result.append(italic())
            resi = resi + 1
        if menu == "inline_code":
            result.append(inline_code())
            resi = resi + 1
        if menu == "link":
            result.append(link())
            resi = resi + 1
        if menu == "header":
            result.append(header())
            resi=resi+1
        if menu == "unordered_list":
            print(unordered_list())
        if menu == "ordered_list":
            print(ordered_list())
        if menu == "new_line":
            result.append(new_line())
            resi = resi + 1
    else: print ("Unknown formatting type or command")
    print(*result,sep = '\n')
