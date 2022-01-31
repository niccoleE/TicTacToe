player_1 = "Player_1(X)"
player_2 = "Player_2(0)"
cross = "X"
null = "0"
start = input("Do you want to play TicTacToe game?\nType 'y' or 'n': ")


def show_field(field):
    """display playing field"""
    for field_row in field:
        row_string = ' '.join([str(elem) for elem in field_row])
        print(row_string)
    print("\n")


def move(player, sign):
    """take a position for X or 0 from the players and update the field"""
    position_ok = False
    while not position_ok:
        position = input(f"{player}: choose your position by typing a relative number on the field: ")
        if position in positions:
            for row in game_field:
                if position in row:
                    pos_index = row.index(position)
                    row[pos_index] = sign
                    positions.remove(position)
                    position_ok = True
        else:
            print(f"You've entered {position}. Please choose a free position: ")
            continue
        show_field(game_field)


def winner():
    """check horizontal, vertical and diagonal rows for three identical marks """
    columns = [[row[a] for row in game_field if row != ['----------']] for a in range(0, 6, 2)]
    work_rows = [value for index, value in enumerate(game_field) if index % 2 == 0]
    # horizontal winning position
    for row in work_rows:
        if row[0] == row[2] == row[4]:
            return True
    # vertical winning position
    for col in columns:
        if len(set(col)) == 1:
            return True
    # diagonal winning position
    diagonal1 = []
    diagonal2 = []
    a = -2
    b = 6
    for row in work_rows:
        a += 2
        d_1 = row[a]
        diagonal1.append(d_1)
        b -= 2
        d_2 = row[b]
        diagonal2.append(d_2)
    if len(set(diagonal1)) == 1 or len(set(diagonal2)) == 1:
        return True


def winning_message(player):
    """print winning message"""
    print(f"Congratulations! {player} wins!")


def play():
    """determine the course of the game"""
    """alternate moves of each of the players; check the winner"""
    moves = 0
    game_over = False
    while not game_over:
        move(player_1, cross)
        winner()
        moves += 1
        if moves == 9:
            print("It's a draw.")
            game_over = True
        elif winner():
            winning_message(player_1)
            game_over = True
        else:
            move(player_2, null)
            moves += 1
            winner()
            if winner():
                winning_message(player_2)
                game_over = True


while start.lower() == "y":
    positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    START_FIELD = [["1", "|", "2", "|", "3"], ["----------"],
                   ["4", "|", "5", "|", "6"], ["----------"],
                   ["7", "|", "8", "|", "9"]]
    game_field = START_FIELD[:]
    print("LET'S START")
    show_field(START_FIELD)
    play()
    start = input("Do you want to play TicTacToe game again?\nType 'y' or 'n': ")
