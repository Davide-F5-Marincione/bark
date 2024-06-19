def tables_to_ternary(mg_table, eg_table, mg_add, eg_add):
    for i in range(64):
        mg_table[i] = mg_table[i] + mg_add
        eg_table[i] = eg_table[i] + eg_add

    mg = f"f<4?(f<2?(f==0?(r<4?(r<2?(r==0?{mg_table[56]}:{mg_table[57]}):(r==2?{mg_table[58]}:{mg_table[59]})):(r<6?(r==4?{mg_table[60]}:{mg_table[61]}):(r==6?{mg_table[62]}:{mg_table[63]}))):(r<4?(r<2?(r==0?{mg_table[48]}:{mg_table[49]}):(r==2?{mg_table[50]}:{mg_table[51]})):(r<6?(r==4?{mg_table[52]}:{mg_table[53]}):(r==6?{mg_table[54]}:{mg_table[55]})))):(f==2?(r<4?(r<2?(r==0?{mg_table[40]}:{mg_table[41]}):(r==2?{mg_table[42]}:{mg_table[43]})):(r<6?(r==4?{mg_table[44]}:{mg_table[45]}):(r==6?{mg_table[46]}:{mg_table[47]}))):(r<4?(r<2?(r==0?{mg_table[32]}:{mg_table[33]}):(r==2?{mg_table[34]}:{mg_table[35]})):(r<6?(r==4?{mg_table[36]}:{mg_table[37]}):(r==6?{mg_table[38]}:{mg_table[39]}))))):(f<6?(f==4?(r<4?(r<2?(r==0?{mg_table[24]}:{mg_table[25]}):(r==2?{mg_table[26]}:{mg_table[27]})):(r<6?(r==4?{mg_table[28]}:{mg_table[29]}):(r==6?{mg_table[30]}:{mg_table[31]}))):(r<4?(r<2?(r==0?{mg_table[16]}:{mg_table[17]}):(r==2?{mg_table[18]}:{mg_table[19]})):(r<6?(r==4?{mg_table[20]}:{mg_table[21]}):(r==6?{mg_table[22]}:{mg_table[23]})))):(f==6?(r<4?(r<2?(r==0?{mg_table[8]}:{mg_table[9]}):(r==2?{mg_table[10]}:{mg_table[11]})):(r<6?(r==4?{mg_table[12]}:{mg_table[13]}):(r==6?{mg_table[14]}:{mg_table[15]}))):(r<4?(r<2?(r==0?{mg_table[0]}:{mg_table[1]}):(r==2?{mg_table[2]}:{mg_table[3]})):(r<6?(r==4?{mg_table[4]}:{mg_table[5]}):(r==6?{mg_table[6]}:{mg_table[7]})))))"
    eg = f"f<4?(f<2?(f==0?(r<4?(r<2?(r==0?{eg_table[56]}:{eg_table[57]}):(r==2?{eg_table[58]}:{eg_table[59]})):(r<6?(r==4?{eg_table[60]}:{eg_table[61]}):(r==6?{eg_table[62]}:{eg_table[63]}))):(r<4?(r<2?(r==0?{eg_table[48]}:{eg_table[49]}):(r==2?{eg_table[50]}:{eg_table[51]})):(r<6?(r==4?{eg_table[52]}:{eg_table[53]}):(r==6?{eg_table[54]}:{eg_table[55]})))):(f==2?(r<4?(r<2?(r==0?{eg_table[40]}:{eg_table[41]}):(r==2?{eg_table[42]}:{eg_table[43]})):(r<6?(r==4?{eg_table[44]}:{eg_table[45]}):(r==6?{eg_table[46]}:{eg_table[47]}))):(r<4?(r<2?(r==0?{eg_table[32]}:{eg_table[33]}):(r==2?{eg_table[34]}:{eg_table[35]})):(r<6?(r==4?{eg_table[36]}:{eg_table[37]}):(r==6?{eg_table[38]}:{eg_table[39]}))))):(f<6?(f==4?(r<4?(r<2?(r==0?{eg_table[24]}:{eg_table[25]}):(r==2?{eg_table[26]}:{eg_table[27]})):(r<6?(r==4?{eg_table[28]}:{eg_table[29]}):(r==6?{eg_table[30]}:{eg_table[31]}))):(r<4?(r<2?(r==0?{eg_table[16]}:{eg_table[17]}):(r==2?{eg_table[18]}:{eg_table[19]})):(r<6?(r==4?{eg_table[20]}:{eg_table[21]}):(r==6?{eg_table[22]}:{eg_table[23]})))):(f==6?(r<4?(r<2?(r==0?{eg_table[8]}:{eg_table[9]}):(r==2?{eg_table[10]}:{eg_table[11]})):(r<6?(r==4?{eg_table[12]}:{eg_table[13]}):(r==6?{eg_table[14]}:{eg_table[15]}))):(r<4?(r<2?(r==0?{eg_table[0]}:{eg_table[1]}):(r==2?{eg_table[2]}:{eg_table[3]})):(r<6?(r==4?{eg_table[4]}:{eg_table[5]}):(r==6?{eg_table[6]}:{eg_table[7]})))))"
    
    print("(c?" + mg.replace("f", "file") + ":" + "0)")
    print("(c?" + eg.replace("f", "file") + ":" + "0)")
    print("(c?0:" + mg.replace("f", "7-file") + ")")
    print("(c?0:" + eg.replace("f", "7-file") + ")")


# tables from https://www.chessprogramming.org/PeSTO%27s_Evaluation_Function


tables_to_ternary([-65,  23,  16, -15, -56, -34,   2,  13,
     29,  -1, -20,  -7,  -8,  -4, -38, -29,
     -9,  24,   2, -16, -20,   6,  22, -22,
    -17, -20, -12, -27, -30, -25, -14, -36,
    -49,  -1, -27, -39, -46, -44, -33, -51,
    -14, -14, -22, -46, -44, -30, -15, -27,
      1,   7,  -8, -64, -43, -16,   9,   8,
    -15,  36,  12, -54,   8, -28,  24,  14],
      [-74, -35, -18, -18, -11,  15,   4, -17,
    -12,  17,  14,  17,  17,  38,  23,  11,
     10,  17,  23,  15,  20,  45,  44,  13,
     -8,  22,  24,  27,  26,  33,  26,   3,
    -18,  -4,  21,  24,  27,  23,   9, -11,
    -19,  -3,  11,  21,  23,  16,   7,  -9,
    -27, -11,   4,  13,  14,   4,  -5, -17,
    -53, -34, -21, -11, -28, -14, -24, -43], 0, 0)