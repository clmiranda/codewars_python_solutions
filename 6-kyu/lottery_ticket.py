# Lottery Ticket => https://www.codewars.com/kata/57f625992f4d53c24200070e


def bingo(ticket, win) -> str:
    return (
        "Winner!"
        if sum([1 for i in ticket for j in i[0] if ord(j) == i[1]]) >= win
        else "Loser!"
    )
