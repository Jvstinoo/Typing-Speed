"""Typing Test in terminal:

have a timer of 30 seconds.
three sentences will pop up, and words will change in color indiciating which you should type.

Have an array with filler sentences, and if there's a connection available make a call to
random word api. Use a try catch for this, to not disrupt user.
"""
import time
import curses
from curses import wrapper

sentences = [
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
    "This is a six word sentence.",
]


def display_sentences():
    """In charge of displaying three lines worth of sentences in the terminal."""


def scroll_sentences():
    return 1


def calculateScore(characters_typed, typos):
    speed = characters_typed / 1.25
    accuracy = characters_typed * (characters_typed - typos)
    return speed, accuracy


def main(stdscr):
    characters_typed = 0
    typos = 0
    curses.curs_set(1)
    stdscr.clear()
    stdscr.refresh()
    run = True
    typeWord = "".join(sentences) + "\n\n"
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.addstr(typeWord)  # check if i can edit previously printed strings.if
    sentence_y, sentence_x = stdscr.getyx()

    sentenceIterator = 0
    while run:
        c = stdscr.getch()
        if sentenceIterator != len(typeWord) - 3:
            if c == ord(typeWord[sentenceIterator]):
                stdscr.addch(c, curses.color_pair(1))
                characters_typed += 1
            elif c == curses.KEY_BACKSPACE:
                y, x = stdscr.getyx()
                stdscr.delch(y, x - 1)
                sentenceIterator -= 2
            elif c == curses.KEY_BTAB:
                break
            else:
                stdscr.addch(c, curses.color_pair(2))
                typos += 1
            sentenceIterator += 1
        else:
            score = calculateScore(characters_typed, typos)
            stdscr.addstr("\n\nTyping speed: " + str(score[0]), curses.color_pair(3))
            stdscr.addstr("\nTyping accuracy: " + str(score[1]), curses.color_pair(3))


wrapper(main)
