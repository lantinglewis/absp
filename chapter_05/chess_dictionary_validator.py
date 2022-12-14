chess_board_no_king = {'6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
chess_board_correct = {'1a': 'bking', '2a': 'bqueen', '3a': 'brook', '4a': 'brook',
                       '5a': 'bknight', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
                       '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn',
                       '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn',
                       '1c': 'wking', '2c': 'wqueen', '3c': 'wrook', '4c': 'wrook',
                       '5c': 'wbishop', '6c': 'wbishop', '7c': 'wknight', '8c': 'wknight',
                       '1e': 'wpawn', '2e': 'wpawn', '3e': 'wpawn', '4e': 'wpawn',
                       '5e': 'wpawn', '6e': 'wpawn', '7e': 'wpawn', '8e': 'wpawn'}


def is_valid_chess_board(board):
    w_king_check = 0
    b_king_check = 0
    w_pawn_check = 0
    b_pawn_check = 0
    w_piece_check = 0
    b_piece_check = 0

    valid_spaces = ['1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
                    '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '1d', '2d', '3c', '4c', '5c', '6c', '7c', '8c',
                    '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
                    '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f', '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g',
                    '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h']

    valid_w_pieces = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking']
    valid_b_pieces = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']
    valid_pieces = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking', 'wpawn', 'wknight', 'wbishop', 'wrook',
                    'wqueen', 'wking']

    for k, v in board.items():
        if v == 'wking':
            w_king_check += 1

        if v == 'bking':
            b_king_check += 1

        if v == 'wpawn':
            w_pawn_check += 1

        if v == 'bpawn':
            b_pawn_check += 1

        if k not in valid_spaces:
            return False

        if v in valid_w_pieces:
            w_piece_check += 1

        if v in valid_b_pieces:
            b_piece_check += 1

        if v not in valid_pieces:
            return False

    if w_king_check != 1 or b_king_check != 1 or w_pawn_check > 8 or b_pawn_check > 8 or w_piece_check > 16 \
            or b_piece_check > 16:
        return False

    return True


print(is_valid_chess_board(chess_board_no_king))
print(is_valid_chess_board(chess_board_correct))
