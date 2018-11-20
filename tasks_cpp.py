import re

f = open('d:/Projects/VS/Project1_cpp/Project1_cpp/tasks.cpp', encoding='cp1251')

tm = open('template.cpp', encoding='cp1251')
template = tm.read()
tm.close()

codebase = f.read()

#res = re.findall(r'void\s+task\d+\(\)\s*{(.+?)\n}', codebase, re.DOTALL)
#print(res)


i = 1
for code in re.findall(r'void\s+task\d+\(\)\s*{\s*(.+?)\n}', codebase, re.DOTALL):
    cpp = open('cpp/task_{}.cpp'.format(i), mode='w', encoding='cp1251')
    cpp.write(template.format(CODE=code))
    cpp.close()
    i += 1
