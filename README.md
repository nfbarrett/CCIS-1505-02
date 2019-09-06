# CCIS-1505-02
Fundamentals of Programming

> password room #H257: `ccisF2019`

---
## Session 01


---

## Session 02


[Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)

### ASCII


ASCII Table

Dec  = Decimal Value
Char = Character

'5' has the int value 53
if we write '5'-'0' it evaluates to 53-48, or the int 5
if we write char c = 'B'+32; then c stores 'b'

| Dec | Char |   | Dec | Char | Dec | Char | Dec | Char |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | NUL | (null) | 32 | SPACE | 64 | @ | 96 | ` |
| 1 | SOH | (start of heading)  | 33 | ! | 65 | A | 97 | a |
| 2 | STX | (start of text) | 34 | " |   |   |   |   |
| 3 | ETX | (end of text) | 35 | # |   |   |   |   |
| 4 | EOT | (end of transmission) | 36 | $ |   |   |   |   |
| 5 | ENQ | (enquiry) | 37 | % |   |   |   |   |
| 6 | ACK | (acknowledge) | 38 | & |   |   |   |   |
| 7 | BEL | (bell) | 39 | ' |   |   |   |   |
| 8 | BS | (backspace) | 40 | ( |   |   |   |   |
| 9 | TAB | (horizontal tab) | 41 | ) |   |   |   |   |
| 10 | LF | (NL line feed, new line) | 42 | * |   |   |   |   |
| 11 | VT | (vertical tab) | 43 | + | 75 | S | 115 | s |
| 12 | NF | (NP form feed, new page) | 44 | , | 76 | S | 115 | s |
| 13 | CR | (carriage return) | 45 | - | 77 | S | 115 | s |
| 14 | SO | (shift out) | 46 | . | 78 | S | 115 | s |
| 15 | SI | (shift in) | 47| / | 79 | S | 115 | s |
| 16 | DLE | (data link escape) | 48 | 0 | 80 | S | 115 | s |
| 17 | DC1 | (device control 1) | 49 | 1 | 81 | S | 115 | s |
| 18 | DC2 | (device control 2) | 50 | 2 | 82 | S | 115 | s |
| 19 | DC3 | (device control 3) | 51 | 3 | 83 | S | 115 | s |
| 20 | DC4 | (device control 4) | 52 | 4 | 84 | S | 115 | s |
| 21 | NAK | (negative acknowledge) | 53 | 5 | 85 | S | 115 | s |
| 22 | SYN | (synchronous idle) | 54 | 6 | 86 | S | 115 | s |
| 23 | ETB | (end of trans. block) | 55 | 7 | 87 | S | 115 | s |
| 24 | CAN | (cancel) | 56 | 8 | 88 | X | 120 | x |
| 25 | EM | (end of medium) | 57 | 9 | 89 | Y | 121 | y |
| 26 | SUB | (substitute) | 58 | : | 90 | Z | 122 | z |
| 27 | ESC | (escape) | 59 | ; | 91 | [ | 123 | s |
| 28 | FS | (file separator) | 60 | < | 92 | \ | 124 | s |
| 29 | GS | (group separator) | 61 | = | 93 | ] | 125 | } |
| 30 | RS | (record separator) | 62 | > | 94 | ^ | 126 | ~ |
| 31 | US | (unit separator) | 63 | ? | 95 | _ | 127 | DEL |

### EBCDIC (Extended Binary Coded Decimal Interchange Code)



```python
# Programer: Nick Barrett
# Date Written: Sep 03, 2019
# Program Name: P2.py
# Company Name: HTC-CCIS1505

#Step 2
print ("HHH   HHH   TTTTTTTTTTT        CCCCCCCCC")
print ("HHH   HHH   TTTTTTTTTTT     CCCCC")
print ("HHH   HHH      TTTT       CCCCC")
print ("HHHHHHHHH      TTTT       CCCCC")
print ("HHH   HHH      TTTT       CCCCC")
print ("HHH   HHH      TTTT       CCCCC")
print ("HHH   HHH      TTTT         CCCCC")
print ("HHH   HHH      TTTT           CCCCCCCCC")
print ("\n")

input ("\nPress ENTER key to quit")

#Step 3
print \
("""
HHH   HHH   TTTTTTTTTTT        CCCCCCCCC
HHH   HHH   TTTTTTTTTTT     CCCCC
HHH   HHH      TTTT       CCCCC
HHHHHHHHH      TTTT       CCCCC
HHH   HHH      TTTT       CCCCC
HHH   HHH      TTTT       CCCCC
HHH   HHH      TTTT         CCCCC
HHH   HHH      TTTT           CCCCCCCCC
""")

input("\nPress the ENTER key to exit")
```
test sign
