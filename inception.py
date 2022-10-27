# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    inception.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mle-faou <mle-faou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/29 14:56:23 by mle-faou          #+#    #+#              #
#    Updated: 2022/09/29 14:56:33 by mle-faou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json

def inception(data: dict, input: str, mode: str) -> str:
    if type(data["alphabet"]) is str and data["alphabet"] in "<alphabet>" and "<alphabet>" in data["alphabet"]:
        start = input.find("<alphabet=") + 10
        end = input.find(">", start)
        try:
            assert start is not -1, "alphabet set for value in input but no value"
            assert end is not -1, "alphabet set for value in input but no value"
        except AssertionError as error:
            if mode is "print":
                print("Error: " + error.__str__())
            exit(0)
        data["alphabet"] = json.loads(input[start:end])
        input = input[:start - 10] + input[end + 1:]

    if type(data["states"]) is str and data["states"] in "<states>" and "<states>" in data["states"]:
        start = input.find("<states=") + 8
        end = input.find(">", start)
        try:
            assert start is not -1, "states set for value in input but no value"
            assert end is not -1, "states set for value in input but no value"
        except AssertionError as error:
            if mode is "print":
                print("Error: " + error.__str__())
            exit(0)
        data["states"] = json.loads(input[start:end])
        input = input[:start - 8] + input[end + 1:]

    if type(data["transitions"]) is str and data["transitions"] in "<transitions>" and "<transitions>" in data["transitions"]:
        start = input.find("<transitions=") + 13
        end = input.find(">", start)
        try:
            assert start is not -1, "transitions set for value in input but no value"
            assert end is not -1, "transitions set for value in input but no value"
        except AssertionError as error:
            if mode is "print":
                print("Error: " + error.__str__())
            exit(0)
        data["transitions"] = json.loads(input[start:end])
        input = input[:start - 13] + input[end + 1:]
    return input

# python ft_turing.py machines/inception.json '<alphabet=["1", ".", "+", "="]><states=["move_to_plus", "move_to_equal", "end", "HALT"]><transitions={"move_to_plus":[{"read":"1", "to_state":"move_to_plus", "write":"1", "action":"RIGHT"}, {"read":"0", "to_state":"move_to_plus", "write":"0", "action":"RIGHT"}, {"read":"+", "to_state":"move_to_equal", "write":"1", "action":"RIGHT"}], "move_to_equal":[{"read":"1", "to_state":"move_to_equal", "write":"1", "action":"RIGHT"}, {"read":"0", "to_state":"move_to_equal", "write":"0", "action":"RIGHT"}, {"read":"=", "to_state":"end", "write":".", "action":"LEFT"}], "end":[{"read":"1", "to_state":"HALT", "write":".", "action":"LEFT"}]}>1+1='