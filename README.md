# FT-TURING

The main goal of the project was to produce 5 JSON turing machines and a functional interpreter.
In addition, we could determine the complexity of each machine as a bonus.

With a working mate, we decided to choose the python language and use the matplotlib librairy to realize the bonus.

## Setup Project

- Clone the project
```bash
git clone https://github.com/vvaucoul/Ft_Turing && cd FT_Turing
```
- Use Conda environment
```bash
sh install_python.sh
```
- Then, open a new shell

## Usage

- **unary_add.json**
```bash
python3 ft_turing.py machines/unary_add.json <Args> (Ex: "111+11=")
```

- **unary_sub.json**
```bash
python3 ft_turing.py machines/unary_sub.json <Args> (Ex: "111-11=")
```

- **is_pair.json**
```bash
python3 ft_turing.py machines/is_pair.json <Args> (Ex: "0000=")
```

- **equal.json**
```bash
python3 ft_turing.py machines/equal.json <Args> (Ex: "000111")
```

- **palindrome.json**
```bash
python3 ft_turing.py machines/palindrome.json <Args> (Ex: "1001001")
```

- **inception.json**
```bash
python3 ft_turing.py machines/inception.json '<alphabet=["1", ".", "+", "="]><states=["move_to_plus", "move_to_equal", "end", "HALT"]><transitions={"move_to_plus":[{"read":"1", "to_state":"move_to_plus", "write":"1", "action":"RIGHT"}, {"read":"0", "to_state":"move_to_plus", "write":"0", "action":"RIGHT"}, {"read":"+", "to_state":"move_to_equal", "write":"1", "action":"RIGHT"}], "move_to_equal":[{"read":"1", "to_state":"move_to_equal", "write":"1", "action":"RIGHT"}, {"read":"0", "to_state":"move_to_equal", "write":"0", "action":"RIGHT"}, {"read":"=", "to_state":"end", "write":".", "action":"LEFT"}], "end":[{"read":"1", "to_state":"HALT", "write":".", "action":"LEFT"}]}>1+1='
```

-----

## A few examples

<img align="left" src="https://user-images.githubusercontent.com/66129673/198415388-e508e947-6d1d-4fe4-b2f8-4b09c617b6da.png" width="48%">
<img align="left" src="https://user-images.githubusercontent.com/66129673/198416107-21f970d1-ade7-4303-b3f1-35e6fc323fd7.png" width="48%">
<img align="left" src="https://user-images.githubusercontent.com/66129673/198415520-6eca21d3-898e-40a5-b5bc-aaa7968eae3e.png" width="48%">
<img align="left" src="https://user-images.githubusercontent.com/66129673/198416030-036daefa-22cb-4a58-bdbc-03542915fae3.png" width="48%">

-----

## Complexity

<img align="left" src="https://user-images.githubusercontent.com/66129673/198416782-3fb05646-0504-418f-ad6a-4884c01b4da6.png" width="60%">
