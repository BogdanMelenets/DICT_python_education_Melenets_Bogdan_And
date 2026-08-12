from mypyc.primitives.int_ops import int_to_str_op


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

def list(list, type):
    N = 0
    res_list = ["" for i in range(len(list))]
    for item in list:
        if type == "ordered_list": res_list[N] = f'{N+1}'+". "+item
        if type == "unordered_list": res_list[N] = "* " + item
        N = N + 1
    return res_list

def new_line():
    return ""

def spisok():
    Lev=-1
    while Lev<=0:
        Lev = int(input("Number of rows: >"))
        if Lev>0:
            sp = ["" for i in range (Lev)]
            for i in range(Lev):
                sp[i]=input(f"Row # {i+1} : >")
        else: print ("The number of rows should be greater than zero.")
    return sp


menu=""
string=""
result=[]
while menu != "!done" :
    menu = input("Choose a formatter: >")
    if menu == "!help" :
          print(help())
    if menu in ["!done","!help","plain","bold","italic","inline_code","link","header","unordered_list",
                    "ordered_list","new_line"]:
        if menu == "plain":
            result.append(plain())

        if menu == "bold":
            result.append(bold())

        if menu == "italic":
            result.append(italic())

        if menu == "inline_code":
            result.append(inline_code())

        if menu == "link":
            result.append(link())

        if menu == "header":
            result.append(header())

        if menu == "unordered_list":
            ul=list(spisok(), "unordered_list")
            for item in ul: result.append(item)

        if menu == "ordered_list":
            ul = list(spisok(), "ordered_list")
            for item in ul: result.append(item)

        if menu == "new_line":
            result.append(new_line())

    else: print ("Unknown formatting type or command")
    print(*result,sep="\n")

with open('output.md', 'w') as f:
    for item in result:  f.write(f'{item}\n')
    f.close()
