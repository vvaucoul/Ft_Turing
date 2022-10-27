# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_turing.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mle-faou <mle-faou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/29 14:56:58 by mle-faou          #+#    #+#              #
#    Updated: 2022/09/29 15:05:56 by mle-faou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import json
from inception import inception

def ft_turing(to_open: str, input: str, mode = "print") -> int:
    '''A program able to simulate a single headed and single tape Turing machine from a json machine description given as a parameter to the program.
    '''
    try:
        with open("./" + to_open, 'r') as jsonfile:
            data = json.load(jsonfile)
        assert "name" in data, "name is missing"
        assert "alphabet" in data, "alphabet is missing"
        assert "blank" in data, "blank is missing"
        assert "states" in data, "states is missing"
        assert "initial" in data, "initial is missing"
        assert "finals" in data, "finals is missing"
        assert "transitions" in data, "transitions is missing"
        assert list(data.keys()) == ["name", "alphabet", "blank", "states", "initial", "finals", "transitions"], "unknown key"
        input = inception(data, input, mode)
        for state in data["finals"]:
            assert state in data["states"], "final state is not in states"
        for state in data["states"]:
            if state in data["finals"]:
                assert state not in data["transitions"], "final state must not be in transitions"
                continue
            assert state in data["transitions"], "transitions for a state is missing"
            for step in data["transitions"][state]:
                assert "read" in step, "read is missing"
                assert "to_state" in step, "to_state is missing"
                assert step["to_state"] in data["states"], "to_state is not in states"
                assert "write" in step, "write is missing"
                assert "action" in step, "action is missing"
                assert list(step.keys()) == ["read", "to_state", "write", "action"], "unknown key in state"
        for state in data["transitions"]:
            assert state in data["states"], "state is not in states"
        assert data["blank"] in data["alphabet"], "blank must be in alphabet"
        assert data["blank"] not in input, "blank must not be in input"
        for char in input:
            assert char in data["alphabet"], "input must be in alphabet"
    except AssertionError as error:
        if mode is "print":
            print("Error: " + error.__str__())
        return -1
    except Exception as error:
        if mode is "print":
            print("Error: " + error.__str__())
        return -1

    if mode is "print":
        print("*" * 80)
        print("*" + " " * 78 + "*")
        print("*{:^78}*".format(data["name"]))
        print("*" + " " * 78 + "*")
        print("*" * 80)
        print("Alphabet : " + str(data["alphabet"]).replace("'", "").replace("[", "[ ").replace("]", " ]"))
        print("States : " + str(data["states"]).replace("'", "").replace("[", "[ ").replace("]", " ]"))
        print("Initial : " + data["initial"])
        print("Finals : " + str(data["finals"]).replace("'", "").replace("[", "[ ").replace("]", " ]"))
        for state in data["states"]:
            if state not in data["finals"]:
                for step in data["transitions"][state]:
                    print("({}, {}) -> ({}, {}, {})".format(state, step["read"], step["to_state"], step["write"], step["action"]))
        print("*" * 80)

    tape = list(input)
    for _ in range(10):
        tape.insert(0, data["blank"])
    while(len(tape) < 1000):
        tape.append(data["blank"])
    head = 10
    state = data["initial"]
    bkp = []
    steps = 0

    while (state not in data["finals"]):
        steps += 1
        print_tape = list(tape)
        print_tape.insert(head, "<")
        print_tape.insert(head + 2, ">")
        if ("".join(print_tape) + state) in bkp or head < 9:
            print("Infinite loop detected")
            return -1
        bkp.append("".join(print_tape) + state)
        while (len(print_tape) > head + 12):
            print_tape.pop()
        for _ in range(head - 9):
            print_tape.pop(0)
        if mode is "print":
            print("[{}] ({}, {}:{}) -> ".format("".join(print_tape), state, head - 10, tape[head]), end = "")

        check = next((x for x in data["transitions"][state] if x["read"] == tape[head]), None)
        if check is None:
            print("No transition for this state and this char")
            return -1
        if mode is "print":
            print("({}, {}, {})".format(check["to_state"], check["write"], check["action"]))
        tape[head] = check["write"]
        if check["action"] == "RIGHT":
            head += 1
        elif check["action"] == "LEFT":
            head -= 1
        state = check["to_state"]

    while (tape[0] == data["blank"] and len(tape) > 1):
        tape.pop(0)
    while (tape[-1] == data["blank"] and len(tape) > 1):
        tape.pop()
    if mode is "print":
        print("[{}] in {} steps".format("".join(tape), steps))
    if (mode is "sample"):
        return steps
    return 0

if __name__ == "__main__":
    if (len(sys.argv) is 2 and (sys.argv[1] is "--help" or sys.argv[1] == "-h")):
        print("usage: ft_turing [-h] jsonfile input\n\npositional arguments:\n\tjsonfile\tjson description of the machine\n\n\tinput\t\tinput of the machine\n\noptional arguments:\n\t-h, --help\tshow this help message and exit")
        exit(0)
    try:
        assert len(sys.argv) is 3, "Wrong number of arguments"
        assert isinstance(sys.argv[1], str), "jsonfile must be a string"
        assert isinstance(sys.argv[2], str), "input must be a string"
        assert len(sys.argv[2]) > 0, "input must not be empty"
    except AssertionError as error:
        print("Error: " + error.__str__())
        exit(0)
    ft_turing(sys.argv[1], sys.argv[2], "print")
