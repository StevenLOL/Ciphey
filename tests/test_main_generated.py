from ciphey.__main__ import main, make_default_config
def test_MorseCode_LTSZmeVJ():
    # {'PlainText Sentences': 'We believe that this regulatory power, as defined in this bill, is much too broad and that letting a government rule by order in council in a critical situation like an emergency is definitely not in the public interest.', 'Encrypted Texts': {'PlainText': 'We believe that this regulatory power, as defined in this bill, is much too broad and that letting a government rule by order in council in a critical situation like an emergency is definitely not in the public interest.', 'EncryptedText': '.-- . \n -... . .-.. .. . ...- . \n - .... .- - \n - .... .. ... \n .-. . --. ..- .-.. .- - --- .-. -.-- \n .--. --- .-- . .-. --..-- \n .- ... \n -.. . ..-. .. -. . -.. \n .. -. \n - .... .. ... \n -... .. .-.. .-.. --..-- \n .. ... \n -- ..- -.-. .... \n - --- --- \n -... .-. --- .- -.. \n .- -. -.. \n - .... .- - \n .-.. . - - .. -. --. \n .- \n --. --- ...- . .-. -. -- . -. - \n .-. ..- .-.. . \n -... -.-- \n --- .-. -.. . .-. \n .. -. \n -.-. --- ..- -. -.-. .. .-.. \n .. -. \n .- \n -.-. .-. .. - .. -.-. .- .-.. \n ... .. - ..- .- - .. --- -. \n .-.. .. -.- . \n .- -. \n . -- . .-. --. . -. -.-. -.-- \n .. ... \n -.. . ..-. .. -. .. - . .-.. -.-- \n -. --- - \n .. -. \n - .... . \n .--. ..- -... .-.. .. -.-. \n .. -. - . .-. . ... - .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".-- . 
 -... . .-.. .. . ...- . 
 - .... .- - 
 - .... .. ... 
 .-. . --. ..- .-.. .- - --- .-. -.-- 
 .--. --- .-- . .-. --..-- 
 .- ... 
 -.. . ..-. .. -. . -.. 
 .. -. 
 - .... .. ... 
 -... .. .-.. .-.. --..-- 
 .. ... 
 -- ..- -.-. .... 
 - --- --- 
 -... .-. --- .- -.. 
 .- -. -.. 
 - .... .- - 
 .-.. . - - .. -. --. 
 .- 
 --. --- ...- . .-. -. -- . -. - 
 .-. ..- .-.. . 
 -... -.-- 
 --- .-. -.. . .-. 
 .. -. 
 -.-. --- ..- -. -.-. .. .-.. 
 .. -. 
 .- 
 -.-. .-. .. - .. -.-. .- .-.. 
 ... .. - ..- .- - .. --- -. 
 .-.. .. -.- . 
 .- -. 
 . -- . .-. --. . -. -.-. -.-- 
 .. ... 
 -.. . ..-. .. -. .. - . .-.. -.-- 
 -. --- - 
 .. -. 
 - .... . 
 .--. ..- -... .-.. .. -.-. 
 .. -. - . .-. . ... - .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_YurPvSul():
    # {'PlainText Sentences': '(The House divided on the motion, which was agreed to on the following division:) \nDivision No.', 'Encrypted Texts': {'PlainText': '(The House divided on the motion, which was agreed to on the following division:) \nDivision No.', 'EncryptedText': b'KFRoZSBIb3VzZSBkaXZpZGVkIG9uIHRoZSBtb3Rpb24sIHdoaWNoIHdhcyBhZ3JlZWQgdG8gb24gdGhlIGZvbGxvd2luZyBkaXZpc2lvbjopIApEaXZpc2lvbiBOby4=', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'KFRoZSBIb3VzZSBkaXZpZGVkIG9uIHRoZSBtb3Rpb24sIHdoaWNoIHdhcyBhZ3JlZWQgdG8gb24gdGhlIGZvbGxvd2luZyBkaXZpc2lvbjopIApEaXZpc2lvbiBOby4='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_rrXqlstR():
    # {'PlainText Sentences': 'Rates of recovery regularly exceeded 100% of targets.', 'Encrypted Texts': {'PlainText': 'Rates of recovery regularly exceeded 100% of targets.', 'EncryptedText': b'UmF0ZXMgb2YgcmVjb3ZlcnkgcmVndWxhcmx5IGV4Y2VlZGVkIDEwMCUgb2YgdGFyZ2V0cy4=', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'UmF0ZXMgb2YgcmVjb3ZlcnkgcmVndWxhcmx5IGV4Y2VlZGVkIDEwMCUgb2YgdGFyZ2V0cy4='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_PYcgHCXL():
    # {'PlainText Sentences': 'They will do whatever they have to do to stay in power.', 'Encrypted Texts': {'PlainText': 'They will do whatever they have to do to stay in power.', 'EncryptedText': '84 104 101 121 32 119 105 108 108 32 100 111 32 119 104 97 116 101 118 101 114 32 116 104 101 121 32 104 97 118 101 32 116 111 32 100 111 32 116 111 32 115 116 97 121 32 105 110 32 112 111 119 101 114 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("84 104 101 121 32 119 105 108 108 32 100 111 32 119 104 97 116 101 118 101 114 32 116 104 101 121 32 104 97 118 101 32 116 111 32 100 111 32 116 111 32 115 116 97 121 32 105 110 32 112 111 119 101 114 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_gDekvcai():
    # {'PlainText Sentences': 'The public at large and experts will not have the opportunity to go through this with a fine toothed comb and add their professional opinion as to any potential flaws which might be in Bill C-10 with all of its amendments to the individual treaties.', 'Encrypted Texts': {'PlainText': 'The public at large and experts will not have the opportunity to go through this with a fine toothed comb and add their professional opinion as to any potential flaws which might be in Bill C-10 with all of its amendments to the individual treaties.', 'EncryptedText': b'KRUGKIDQOVRGY2LDEBQXIIDMMFZGOZJAMFXGIIDFPBYGK4TUOMQHO2LMNQQG433UEBUGC5TFEB2GQZJAN5YHA33SOR2W42LUPEQHI3ZAM5XSA5DIOJXXKZ3IEB2GQ2LTEB3WS5DIEBQSAZTJNZSSA5DPN52GQZLEEBRW63LCEBQW4ZBAMFSGIIDUNBSWS4RAOBZG6ZTFONZWS33OMFWCA33QNFXGS33OEBQXGIDUN4QGC3TZEBYG65DFNZ2GSYLMEBTGYYLXOMQHO2DJMNUCA3LJM5UHIIDCMUQGS3RAIJUWY3BAIMWTCMBAO5UXI2BAMFWGYIDPMYQGS5DTEBQW2ZLOMRWWK3TUOMQHI3ZAORUGKIDJNZSGS5TJMR2WC3BAORZGKYLUNFSXGLQ=', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'KRUGKIDQOVRGY2LDEBQXIIDMMFZGOZJAMFXGIIDFPBYGK4TUOMQHO2LMNQQG433UEBUGC5TFEB2GQZJAN5YHA33SOR2W42LUPEQHI3ZAM5XSA5DIOJXXKZ3IEB2GQ2LTEB3WS5DIEBQSAZTJNZSSA5DPN52GQZLEEBRW63LCEBQW4ZBAMFSGIIDUNBSWS4RAOBZG6ZTFONZWS33OMFWCA33QNFXGS33OEBQXGIDUN4QGC3TZEBYG65DFNZ2GSYLMEBTGYYLXOMQHO2DJMNUCA3LJM5UHIIDCMUQGS3RAIJUWY3BAIMWTCMBAO5UXI2BAMFWGYIDPMYQGS5DTEBQW2ZLOMRWWK3TUOMQHI3ZAORUGKIDJNZSGS5TJMR2WC3BAORZGKYLUNFSXGLQ='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_zzoFulpZ():
    # {'PlainText Sentences': 'Personally, I have chosen to help the companies, I have chosen to help the citizens.', 'Encrypted Texts': {'PlainText': 'Personally, I have chosen to help the companies, I have chosen to help the citizens.', 'EncryptedText': b'506572736F6E616C6C792C204920686176652063686F73656E20746F2068656C702074686520636F6D70616E6965732C204920686176652063686F73656E20746F2068656C702074686520636974697A656E732E', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'506572736F6E616C6C792C204920686176652063686F73656E20746F2068656C702074686520636F6D70616E6965732C204920686176652063686F73656E20746F2068656C702074686520636974697A656E732E'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_zxYqhDRO():
    # {'PlainText Sentences': 'Right here in Ottawa, in Kanata, and in Cambridge we have been able to build a highly skilled, highly paid workforce that is producing value added products.', 'Encrypted Texts': {'PlainText': 'Right here in Ottawa, in Kanata, and in Cambridge we have been able to build a highly skilled, highly paid workforce that is producing value added products.', 'EncryptedText': b'5269676874206865726520696E204F74746177612C20696E204B616E6174612C20616E6420696E2043616D6272696467652077652068617665206265656E2061626C6520746F206275696C64206120686967686C7920736B696C6C65642C20686967686C79207061696420776F726B666F72636520746861742069732070726F647563696E672076616C75652061646465642070726F64756374732E', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'5269676874206865726520696E204F74746177612C20696E204B616E6174612C20616E6420696E2043616D6272696467652077652068617665206265656E2061626C6520746F206275696C64206120686967686C7920736B696C6C65642C20686967686C79207061696420776F726B666F72636520746861742069732070726F647563696E672076616C75652061646465642070726F64756374732E'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_WQvsRSbX():
    # {'PlainText Sentences': 'Herb Gray (Deputy Prime Minister, Lib.', 'Encrypted Texts': {'PlainText': 'Herb Gray (Deputy Prime Minister, Lib.', 'EncryptedText': '1001000 1100101 1110010 1100010 100000 1000111 1110010 1100001 1111001 100000 101000 1000100 1100101 1110000 1110101 1110100 1111001 100000 1010000 1110010 1101001 1101101 1100101 100000 1001101 1101001 1101110 1101001 1110011 1110100 1100101 1110010 101100 100000 1001100 1101001 1100010 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1001000 1100101 1110010 1100010 100000 1000111 1110010 1100001 1111001 100000 101000 1000100 1100101 1110000 1110101 1110100 1111001 100000 1010000 1110010 1101001 1101101 1100101 100000 1001101 1101001 1101110 1101001 1110011 1110100 1100101 1110010 101100 100000 1001100 1101001 1100010 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_KYkfarzd():
    # {'PlainText Sentences': 'Living in the province of Ontario I am quite aware of the kinds of arguments that are being made.', 'Encrypted Texts': {'PlainText': 'Living in the province of Ontario I am quite aware of the kinds of arguments that are being made.', 'EncryptedText': b'JRUXM2LOM4QGS3RAORUGKIDQOJXXM2LOMNSSA33GEBHW45DBOJUW6ICJEBQW2IDROVUXIZJAMF3WC4TFEBXWMIDUNBSSA23JNZSHGIDPMYQGC4THOVWWK3TUOMQHI2DBOQQGC4TFEBRGK2LOM4QG2YLEMUXA====', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'JRUXM2LOM4QGS3RAORUGKIDQOJXXM2LOMNSSA33GEBHW45DBOJUW6ICJEBQW2IDROVUXIZJAMF3WC4TFEBXWMIDUNBSSA23JNZSHGIDPMYQGC4THOVWWK3TUOMQHI2DBOQQGC4TFEBRGK2LOM4QG2YLEMUXA===='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_EOaJqpBF():
    # {'PlainText Sentences': 'I should also say that I will not stray, as has been mentioned earlier.', 'Encrypted Texts': {'PlainText': 'I should also say that I will not stray, as has been mentioned earlier.', 'EncryptedText': '492073686f756c6420616c736f20736179207468617420492077696c6c206e6f742073747261792c20617320686173206265656e206d656e74696f6e6564206561726c6965722e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("492073686f756c6420616c736f20736179207468617420492077696c6c206e6f742073747261792c20617320686173206265656e206d656e74696f6e6564206561726c6965722e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_DdizXhiu():
    # {'PlainText Sentences': 'Often, misfortune brings people together, and that is what we saw.', 'Encrypted Texts': {'PlainText': 'Often, misfortune brings people together, and that is what we saw.', 'EncryptedText': b'T2Z0ZW4sIG1pc2ZvcnR1bmUgYnJpbmdzIHBlb3BsZSB0b2dldGhlciwgYW5kIHRoYXQgaXMgd2hhdCB3ZSBzYXcu', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'T2Z0ZW4sIG1pc2ZvcnR1bmUgYnJpbmdzIHBlb3BsZSB0b2dldGhlciwgYW5kIHRoYXQgaXMgd2hhdCB3ZSBzYXcu'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_qyDRUpaD():
    # {'PlainText Sentences': "I congratulate President Paul Speck and General Manager Gerry Ginsberg on the festival's endeavours.", 'Encrypted Texts': {'PlainText': "I congratulate President Paul Speck and General Manager Gerry Ginsberg on the festival's endeavours.", 'EncryptedText': '4920636f6e67726174756c61746520507265736964656e74205061756c20537065636b20616e642047656e6572616c204d616e616765722047657272792047696e7362657267206f6e2074686520666573746976616c277320656e646561766f7572732e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("4920636f6e67726174756c61746520507265736964656e74205061756c20537065636b20616e642047656e6572616c204d616e616765722047657272792047696e7362657267206f6e2074686520666573746976616c277320656e646561766f7572732e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_FSprBwXg():
    # {'PlainText Sentences': 'Individuals need to question proposed candidates, to get to know them, to understand their point of view, to determine if they have the philosophy that is so much defined for us in footprints in the snow.', 'Encrypted Texts': {'PlainText': 'Individuals need to question proposed candidates, to get to know them, to understand their point of view, to determine if they have the philosophy that is so much defined for us in footprints in the snow.', 'EncryptedText': b'JFXGI2LWNFSHKYLMOMQG4ZLFMQQHI3ZAOF2WK43UNFXW4IDQOJXXA33TMVSCAY3BNZSGSZDBORSXGLBAORXSAZ3FOQQHI3ZANNXG65ZAORUGK3JMEB2G6IDVNZSGK4TTORQW4ZBAORUGK2LSEBYG62LOOQQG6ZRAOZUWK5ZMEB2G6IDEMV2GK4TNNFXGKIDJMYQHI2DFPEQGQYLWMUQHI2DFEBYGQ2LMN5ZW64DIPEQHI2DBOQQGS4ZAONXSA3LVMNUCAZDFMZUW4ZLEEBTG64RAOVZSA2LOEBTG633UOBZGS3TUOMQGS3RAORUGKIDTNZXXOLQ=', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'JFXGI2LWNFSHKYLMOMQG4ZLFMQQHI3ZAOF2WK43UNFXW4IDQOJXXA33TMVSCAY3BNZSGSZDBORSXGLBAORXSAZ3FOQQHI3ZANNXG65ZAORUGK3JMEB2G6IDVNZSGK4TTORQW4ZBAORUGK2LSEBYG62LOOQQG6ZRAOZUWK5ZMEB2G6IDEMV2GK4TNNFXGKIDJMYQHI2DFPEQGQYLWMUQHI2DFEBYGQ2LMN5ZW64DIPEQHI2DBOQQGS4ZAONXSA3LVMNUCAZDFMZUW4ZLEEBTG64RAOVZSA2LOEBTG633UOBZGS3TUOMQGS3RAORUGKIDTNZXXOLQ='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_xbNzsXkV():
    # {'PlainText Sentences': '* * * \nLIBERAL PARTY \nMr. Jason Kenney (Calgary Southeast, Ref.', 'Encrypted Texts': {'PlainText': '* * * \nLIBERAL PARTY \nMr. Jason Kenney (Calgary Southeast, Ref.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_AkUNcjLU():
    # {'PlainText Sentences': 'These companies are real and these banks and this competition is real.', 'Encrypted Texts': {'PlainText': 'These companies are real and these banks and this competition is real.', 'EncryptedText': '- .... . ... . \n -.-. --- -- .--. .- -. .. . ... \n .- .-. . \n .-. . .- .-.. \n .- -. -.. \n - .... . ... . \n -... .- -. -.- ... \n .- -. -.. \n - .... .. ... \n -.-. --- -- .--. . - .. - .. --- -. \n .. ... \n .-. . .- .-.. .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config("- .... . ... . 
 -.-. --- -- .--. .- -. .. . ... 
 .- .-. . 
 .-. . .- .-.. 
 .- -. -.. 
 - .... . ... . 
 -... .- -. -.- ... 
 .- -. -.. 
 - .... .. ... 
 -.-. --- -- .--. . - .. - .. --- -. 
 .. ... 
 .-. . .- .-.. .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_LpepJsXq():
    # {'PlainText Sentences': 'We are fed up.', 'Encrypted Texts': {'PlainText': 'We are fed up.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_ByQxVBDX():
    # {'PlainText Sentences': 'We have very few butcher shops.', 'Encrypted Texts': {'PlainText': 'We have very few butcher shops.', 'EncryptedText': '5765206861766520766572792066657720627574636865722073686f70732e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("5765206861766520766572792066657720627574636865722073686f70732e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_CAnYBXiy():
    # {'PlainText Sentences': 'That is out of the blue.', 'Encrypted Texts': {'PlainText': 'That is out of the blue.', 'EncryptedText': '84 104 97 116 32 105 115 32 111 117 116 32 111 102 32 116 104 101 32 98 108 117 101 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("84 104 97 116 32 105 115 32 111 117 116 32 111 102 32 116 104 101 32 98 108 117 101 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_kKOxhCXS():
    # {'PlainText Sentences': "The letters stated that habitats can be geographically dispersed and are not confined within political boundaries, but must each be effectively protected to ensure a species' well-being.", 'Encrypted Texts': {'PlainText': "The letters stated that habitats can be geographically dispersed and are not confined within political boundaries, but must each be effectively protected to ensure a species' well-being.", 'EncryptedText': '546865206c6574746572732073746174656420746861742068616269746174732063616e2062652067656f67726170686963616c6c792064697370657273656420616e6420617265206e6f7420636f6e66696e65642077697468696e20706f6c69746963616c20626f756e6461726965732c20627574206d7573742065616368206265206566666563746976656c792070726f74656374656420746f20656e7375726520612073706563696573272077656c6c2d6265696e672e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("546865206c6574746572732073746174656420746861742068616269746174732063616e2062652067656f67726170686963616c6c792064697370657273656420616e6420617265206e6f7420636f6e66696e65642077697468696e20706f6c69746963616c20626f756e6461726965732c20627574206d7573742065616368206265206566666563746976656c792070726f74656374656420746f20656e7375726520612073706563696573272077656c6c2d6265696e672e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_lQKBdvMf():
    # {'PlainText Sentences': 'We hope to put this in place as quickly as possible with the co-operation of parliament.', 'Encrypted Texts': {'PlainText': 'We hope to put this in place as quickly as possible with the co-operation of parliament.', 'EncryptedText': '.-- . \n .... --- .--. . \n - --- \n .--. ..- - \n - .... .. ... \n .. -. \n .--. .-.. .- -.-. . \n .- ... \n --.- ..- .. -.-. -.- .-.. -.-- \n .- ... \n .--. --- ... ... .. -... .-.. . \n .-- .. - .... \n - .... . \n -.-. --- -....- --- .--. . .-. .- - .. --- -. \n --- ..-. \n .--. .- .-. .-.. .. .- -- . -. - .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".-- . 
 .... --- .--. . 
 - --- 
 .--. ..- - 
 - .... .. ... 
 .. -. 
 .--. .-.. .- -.-. . 
 .- ... 
 --.- ..- .. -.-. -.- .-.. -.-- 
 .- ... 
 .--. --- ... ... .. -... .-.. . 
 .-- .. - .... 
 - .... . 
 -.-. --- -....- --- .--. . .-. .- - .. --- -. 
 --- ..-. 
 .--. .- .-. .-.. .. .- -- . -. - .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_AQpBlecR():
    # {'PlainText Sentences': 'This has led to the taxpayer being penalized.', 'Encrypted Texts': {'PlainText': 'This has led to the taxpayer being penalized.', 'EncryptedText': '- .... .. ... \n .... .- ... \n .-.. . -.. \n - --- \n - .... . \n - .- -..- .--. .- -.-- . .-. \n -... . .. -. --. \n .--. . -. .- .-.. .. --.. . -.. .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config("- .... .. ... 
 .... .- ... 
 .-.. . -.. 
 - --- 
 - .... . 
 - .- -..- .--. .- -.-- . .-. 
 -... . .. -. --. 
 .--. . -. .- .-.. .. --.. . -.. .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_OlIGKxMs():
    # {'PlainText Sentences': 'Polish immigrants have made significant contributions to our society, especially during the world wars.', 'Encrypted Texts': {'PlainText': 'Polish immigrants have made significant contributions to our society, especially during the world wars.', 'EncryptedText': '80 111 108 105 115 104 32 105 109 109 105 103 114 97 110 116 115 32 104 97 118 101 32 109 97 100 101 32 115 105 103 110 105 102 105 99 97 110 116 32 99 111 110 116 114 105 98 117 116 105 111 110 115 32 116 111 32 111 117 114 32 115 111 99 105 101 116 121 44 32 101 115 112 101 99 105 97 108 108 121 32 100 117 114 105 110 103 32 116 104 101 32 119 111 114 108 100 32 119 97 114 115 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("80 111 108 105 115 104 32 105 109 109 105 103 114 97 110 116 115 32 104 97 118 101 32 109 97 100 101 32 115 105 103 110 105 102 105 99 97 110 116 32 99 111 110 116 114 105 98 117 116 105 111 110 115 32 116 111 32 111 117 114 32 115 111 99 105 101 116 121 44 32 101 115 112 101 99 105 97 108 108 121 32 100 117 114 105 110 103 32 116 104 101 32 119 111 114 108 100 32 119 97 114 115 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_ExOWRmIR():
    # {'PlainText Sentences': "Why is the Canadian taxpayer paying the senator's salary?", 'Encrypted Texts': {'PlainText': "Why is the Canadian taxpayer paying the senator's salary?", 'EncryptedText': "?yralas s'rotanes eht gniyap reyapxat naidanaC eht si yhW", 'CipherUsed': 'Reverse'}}
    cfg = make_default_config("?yralas s'rotanes eht gniyap reyapxat naidanaC eht si yhW")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_JDvpwyVN():
    # {'PlainText Sentences': 'The member from Mississauga is doing the one on youth entrepreneurship.', 'Encrypted Texts': {'PlainText': 'The member from Mississauga is doing the one on youth entrepreneurship.', 'EncryptedText': b'VGhlIG1lbWJlciBmcm9tIE1pc3Npc3NhdWdhIGlzIGRvaW5nIHRoZSBvbmUgb24geW91dGggZW50cmVwcmVuZXVyc2hpcC4=', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'VGhlIG1lbWJlciBmcm9tIE1pc3Npc3NhdWdhIGlzIGRvaW5nIHRoZSBvbmUgb24geW91dGggZW50cmVwcmVuZXVyc2hpcC4='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_vCBNBVBQ():
    # {'PlainText Sentences': 'members:\nOn division.', 'Encrypted Texts': {'PlainText': 'members:\nOn division.', 'EncryptedText': '109 101 109 98 101 114 115 58 10 79 110 32 100 105 118 105 115 105 111 110 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("109 101 109 98 101 114 115 58 10 79 110 32 100 105 118 105 115 105 111 110 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_jYutMiRL():
    # {'PlainText Sentences': 'We think it much more important to be more transparent and have very clear objectives.', 'Encrypted Texts': {'PlainText': 'We think it much more important to be more transparent and have very clear objectives.', 'EncryptedText': '5765207468696e6b206974206d756368206d6f726520696d706f7274616e7420746f206265206d6f7265207472616e73706172656e7420616e642068617665207665727920636c656172206f626a656374697665732e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("5765207468696e6b206974206d756368206d6f726520696d706f7274616e7420746f206265206d6f7265207472616e73706172656e7420616e642068617665207665727920636c656172206f626a656374697665732e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_WqIDMBUW():
    # {'PlainText Sentences': 'Lyle Vanclief (Minister of Agriculture and Agri-Food, Lib.', 'Encrypted Texts': {'PlainText': 'Lyle Vanclief (Minister of Agriculture and Agri-Food, Lib.', 'EncryptedText': '.-.. -.-- .-.. . \n ...- .- -. -.-. .-.. .. . ..-. \n -.--. -- .. -. .. ... - . .-. \n --- ..-. \n .- --. .-. .. -.-. ..- .-.. - ..- .-. . \n .- -. -.. \n .- --. .-. .. -....- ..-. --- --- -.. --..-- \n .-.. .. -... .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".-.. -.-- .-.. . 
 ...- .- -. -.-. .-.. .. . ..-. 
 -.--. -- .. -. .. ... - . .-. 
 --- ..-. 
 .- --. .-. .. -.-. ..- .-.. - ..- .-. . 
 .- -. -.. 
 .- --. .-. .. -....- ..-. --- --- -.. --..-- 
 .-.. .. -... .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_EXLcImPr():
    # {'PlainText Sentences': 'We will never stand for it.', 'Encrypted Texts': {'PlainText': 'We will never stand for it.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_DdxouYbX():
    # {'PlainText Sentences': 'This House would never condone such government action.', 'Encrypted Texts': {'PlainText': 'This House would never condone such government action.', 'EncryptedText': b'KRUGS4ZAJBXXK43FEB3W65LMMQQG4ZLWMVZCAY3PNZSG63TFEBZXKY3IEBTW65TFOJXG2ZLOOQQGCY3UNFXW4LQ=', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'KRUGS4ZAJBXXK43FEB3W65LMMQQG4ZLWMVZCAY3PNZSG63TFEBZXKY3IEBTW65TFOJXG2ZLOOQQGCY3UNFXW4LQ='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_hiKrrUnD():
    # {'PlainText Sentences': 'Mr. Gerry Ritz:\nMadam Speaker, there was a lot verbiage but I am not sure there was too much meat.', 'Encrypted Texts': {'PlainText': 'Mr. Gerry Ritz:\nMadam Speaker, there was a lot verbiage but I am not sure there was too much meat.', 'EncryptedText': '77 114 46 32 71 101 114 114 121 32 82 105 116 122 58 10 77 97 100 97 109 32 83 112 101 97 107 101 114 44 32 116 104 101 114 101 32 119 97 115 32 97 32 108 111 116 32 118 101 114 98 105 97 103 101 32 98 117 116 32 73 32 97 109 32 110 111 116 32 115 117 114 101 32 116 104 101 114 101 32 119 97 115 32 116 111 111 32 109 117 99 104 32 109 101 97 116 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("77 114 46 32 71 101 114 114 121 32 82 105 116 122 58 10 77 97 100 97 109 32 83 112 101 97 107 101 114 44 32 116 104 101 114 101 32 119 97 115 32 97 32 108 111 116 32 118 101 114 98 105 97 103 101 32 98 117 116 32 73 32 97 109 32 110 111 116 32 115 117 114 101 32 116 104 101 114 101 32 119 97 115 32 116 111 111 32 109 117 99 104 32 109 101 97 116 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_hLVjTIwj():
    # {'PlainText Sentences': 'Hon.', 'Encrypted Texts': {'PlainText': 'Hon.', 'EncryptedText': '72 111 110 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("72 111 110 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_mmuphggo():
    # {'PlainText Sentences': 'Does the Prime Minister stand by his statement that labour standards do not belong in trade agreements or does he agree with President Clinton?', 'Encrypted Texts': {'PlainText': 'Does the Prime Minister stand by his statement that labour standards do not belong in trade agreements or does he agree with President Clinton?', 'EncryptedText': b'446F657320746865205072696D65204D696E6973746572207374616E64206279206869732073746174656D656E742074686174206C61626F7572207374616E646172647320646F206E6F742062656C6F6E6720696E2074726164652061677265656D656E7473206F7220646F6573206865206167726565207769746820507265736964656E7420436C696E746F6E3F', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'446F657320746865205072696D65204D696E6973746572207374616E64206279206869732073746174656D656E742074686174206C61626F7572207374616E646172647320646F206E6F742062656C6F6E6720696E2074726164652061677265656D656E7473206F7220646F6573206865206167726565207769746820507265736964656E7420436C696E746F6E3F'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_oLvrGMSd():
    # {'PlainText Sentences': 'Last week I asked him, not once, not twice, but three times, as did the parliamentary secretary, to deal directly with the RCMP if he has allegations to make.', 'Encrypted Texts': {'PlainText': 'Last week I asked him, not once, not twice, but three times, as did the parliamentary secretary, to deal directly with the RCMP if he has allegations to make.', 'EncryptedText': '76 97 115 116 32 119 101 101 107 32 73 32 97 115 107 101 100 32 104 105 109 44 32 110 111 116 32 111 110 99 101 44 32 110 111 116 32 116 119 105 99 101 44 32 98 117 116 32 116 104 114 101 101 32 116 105 109 101 115 44 32 97 115 32 100 105 100 32 116 104 101 32 112 97 114 108 105 97 109 101 110 116 97 114 121 32 115 101 99 114 101 116 97 114 121 44 32 116 111 32 100 101 97 108 32 100 105 114 101 99 116 108 121 32 119 105 116 104 32 116 104 101 32 82 67 77 80 32 105 102 32 104 101 32 104 97 115 32 97 108 108 101 103 97 116 105 111 110 115 32 116 111 32 109 97 107 101 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("76 97 115 116 32 119 101 101 107 32 73 32 97 115 107 101 100 32 104 105 109 44 32 110 111 116 32 111 110 99 101 44 32 110 111 116 32 116 119 105 99 101 44 32 98 117 116 32 116 104 114 101 101 32 116 105 109 101 115 44 32 97 115 32 100 105 100 32 116 104 101 32 112 97 114 108 105 97 109 101 110 116 97 114 121 32 115 101 99 114 101 116 97 114 121 44 32 116 111 32 100 101 97 108 32 100 105 114 101 99 116 108 121 32 119 105 116 104 32 116 104 101 32 82 67 77 80 32 105 102 32 104 101 32 104 97 115 32 97 108 108 101 103 97 116 105 111 110 115 32 116 111 32 109 97 107 101 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_JbjvWuro():
    # {'PlainText Sentences': 'Hon.', 'Encrypted Texts': {'PlainText': 'Hon.', 'EncryptedText': '486f6e2e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("486f6e2e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_ZGNigXgg():
    # {'PlainText Sentences': 'That is not in their interest.', 'Encrypted Texts': {'PlainText': 'That is not in their interest.', 'EncryptedText': '1010100 1101000 1100001 1110100 100000 1101001 1110011 100000 1101110 1101111 1110100 100000 1101001 1101110 100000 1110100 1101000 1100101 1101001 1110010 100000 1101001 1101110 1110100 1100101 1110010 1100101 1110011 1110100 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1010100 1101000 1100001 1110100 100000 1101001 1110011 100000 1101110 1101111 1110100 100000 1101001 1101110 100000 1110100 1101000 1100101 1101001 1110010 100000 1101001 1101110 1110100 1100101 1110010 1100101 1110011 1110100 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_oLvhlniI():
    # {'PlainText Sentences': 'In addition to saving many lives, medicine has extended life, holding death further at bay.', 'Encrypted Texts': {'PlainText': 'In addition to saving many lives, medicine has extended life, holding death further at bay.', 'EncryptedText': '496e206164646974696f6e20746f20736176696e67206d616e79206c697665732c206d65646963696e652068617320657874656e646564206c6966652c20686f6c64696e672064656174682066757274686572206174206261792e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("496e206164646974696f6e20746f20736176696e67206d616e79206c697665732c206d65646963696e652068617320657874656e646564206c6966652c20686f6c64696e672064656174682066757274686572206174206261792e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_HkguhLSH():
    # {'PlainText Sentences': 'Clear and defined debt reduction targets and debt reduction legislation must be put in place.', 'Encrypted Texts': {'PlainText': 'Clear and defined debt reduction targets and debt reduction legislation must be put in place.', 'EncryptedText': '1000011 1101100 1100101 1100001 1110010 100000 1100001 1101110 1100100 100000 1100100 1100101 1100110 1101001 1101110 1100101 1100100 100000 1100100 1100101 1100010 1110100 100000 1110010 1100101 1100100 1110101 1100011 1110100 1101001 1101111 1101110 100000 1110100 1100001 1110010 1100111 1100101 1110100 1110011 100000 1100001 1101110 1100100 100000 1100100 1100101 1100010 1110100 100000 1110010 1100101 1100100 1110101 1100011 1110100 1101001 1101111 1101110 100000 1101100 1100101 1100111 1101001 1110011 1101100 1100001 1110100 1101001 1101111 1101110 100000 1101101 1110101 1110011 1110100 100000 1100010 1100101 100000 1110000 1110101 1110100 100000 1101001 1101110 100000 1110000 1101100 1100001 1100011 1100101 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1000011 1101100 1100101 1100001 1110010 100000 1100001 1101110 1100100 100000 1100100 1100101 1100110 1101001 1101110 1100101 1100100 100000 1100100 1100101 1100010 1110100 100000 1110010 1100101 1100100 1110101 1100011 1110100 1101001 1101111 1101110 100000 1110100 1100001 1110010 1100111 1100101 1110100 1110011 100000 1100001 1101110 1100100 100000 1100100 1100101 1100010 1110100 100000 1110010 1100101 1100100 1110101 1100011 1110100 1101001 1101111 1101110 100000 1101100 1100101 1100111 1101001 1110011 1101100 1100001 1110100 1101001 1101111 1101110 100000 1101101 1110101 1110011 1110100 100000 1100010 1100101 100000 1110000 1110101 1110100 100000 1101001 1101110 100000 1110000 1101100 1100001 1100011 1100101 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_vKOzEFLc():
    # {'PlainText Sentences': 'As a result of Bill C-31 the association will be able to investigate complaints and to impose a range of penalties appropriate to the situation should fault occur.', 'Encrypted Texts': {'PlainText': 'As a result of Bill C-31 the association will be able to investigate complaints and to impose a range of penalties appropriate to the situation should fault occur.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_QLLFbfMC():
    # {'PlainText Sentences': 'I am thinking of Singer employers, among others.', 'Encrypted Texts': {'PlainText': 'I am thinking of Singer employers, among others.', 'EncryptedText': b'SSBhbSB0aGlua2luZyBvZiBTaW5nZXIgZW1wbG95ZXJzLCBhbW9uZyBvdGhlcnMu', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'SSBhbSB0aGlua2luZyBvZiBTaW5nZXIgZW1wbG95ZXJzLCBhbW9uZyBvdGhlcnMu'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_OmAtkKgc():
    # {'PlainText Sentences': 'We look forward to that later.', 'Encrypted Texts': {'PlainText': 'We look forward to that later.', 'EncryptedText': b'5765206C6F6F6B20666F727761726420746F2074686174206C617465722E', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'5765206C6F6F6B20666F727761726420746F2074686174206C617465722E'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_vpaTWHwf():
    # {'PlainText Sentences': 'I want the members and the people who are watching this debate to understand that we have international agreements when it comes to the flowing of rivers and other bodies of water south.', 'Encrypted Texts': {'PlainText': 'I want the members and the people who are watching this debate to understand that we have international agreements when it comes to the flowing of rivers and other bodies of water south.', 'EncryptedText': '.htuos retaw fo seidob rehto dna srevir fo gniwolf eht ot semoc ti nehw stnemeerga lanoitanretni evah ew taht dnatsrednu ot etabed siht gnihctaw era ohw elpoep eht dna srebmem eht tnaw I', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".htuos retaw fo seidob rehto dna srevir fo gniwolf eht ot semoc ti nehw stnemeerga lanoitanretni evah ew taht dnatsrednu ot etabed siht gnihctaw era ohw elpoep eht dna srebmem eht tnaw I")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_InEsDUsv():
    # {'PlainText Sentences': 'There are some other provisions that could have been addressed in a more comprehensive review of the legislation in committee if this bill had been put forward a little earlier than it has been.', 'Encrypted Texts': {'PlainText': 'There are some other provisions that could have been addressed in a more comprehensive review of the legislation in committee if this bill had been put forward a little earlier than it has been.', 'EncryptedText': '- .... . .-. . \n .- .-. . \n ... --- -- . \n --- - .... . .-. \n .--. .-. --- ...- .. ... .. --- -. ... \n - .... .- - \n -.-. --- ..- .-.. -.. \n .... .- ...- . \n -... . . -. \n .- -.. -.. .-. . ... ... . -.. \n .. -. \n .- \n -- --- .-. . \n -.-. --- -- .--. .-. . .... . -. ... .. ...- . \n .-. . ...- .. . .-- \n --- ..-. \n - .... . \n .-.. . --. .. ... .-.. .- - .. --- -. \n .. -. \n -.-. --- -- -- .. - - . . \n .. ..-. \n - .... .. ... \n -... .. .-.. .-.. \n .... .- -.. \n -... . . -. \n .--. ..- - \n ..-. --- .-. .-- .- .-. -.. \n .- \n .-.. .. - - .-.. . \n . .- .-. .-.. .. . .-. \n - .... .- -. \n .. - \n .... .- ... \n -... . . -. .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config("- .... . .-. . 
 .- .-. . 
 ... --- -- . 
 --- - .... . .-. 
 .--. .-. --- ...- .. ... .. --- -. ... 
 - .... .- - 
 -.-. --- ..- .-.. -.. 
 .... .- ...- . 
 -... . . -. 
 .- -.. -.. .-. . ... ... . -.. 
 .. -. 
 .- 
 -- --- .-. . 
 -.-. --- -- .--. .-. . .... . -. ... .. ...- . 
 .-. . ...- .. . .-- 
 --- ..-. 
 - .... . 
 .-.. . --. .. ... .-.. .- - .. --- -. 
 .. -. 
 -.-. --- -- -- .. - - . . 
 .. ..-. 
 - .... .. ... 
 -... .. .-.. .-.. 
 .... .- -.. 
 -... . . -. 
 .--. ..- - 
 ..-. --- .-. .-- .- .-. -.. 
 .- 
 .-.. .. - - .-.. . 
 . .- .-. .-.. .. . .-. 
 - .... .- -. 
 .. - 
 .... .- ... 
 -... . . -. .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_qlgZujqA():
    # {'PlainText Sentences': "It is unbelievable that the government could do this while food bank usage is on the rise, while the environment of our nation is being ``degregated''  at a rapid rate and while public service workers are not getting the equity and equality they deserve.", 'Encrypted Texts': {'PlainText': "It is unbelievable that the government could do this while food bank usage is on the rise, while the environment of our nation is being ``degregated''  at a rapid rate and while public service workers are not getting the equity and equality they deserve.", 'EncryptedText': '497420697320756e62656c69657661626c6520746861742074686520676f7665726e6d656e7420636f756c6420646f2074686973207768696c6520666f6f642062616e6b207573616765206973206f6e2074686520726973652c207768696c652074686520656e7669726f6e6d656e74206f66206f7572206e6174696f6e206973206265696e67206060646567726567617465642727202061742061207261706964207261746520616e64207768696c65207075626c6963207365727669636520776f726b65727320617265206e6f742067657474696e67207468652065717569747920616e6420657175616c697479207468657920646573657276652e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("497420697320756e62656c69657661626c6520746861742074686520676f7665726e6d656e7420636f756c6420646f2074686973207768696c6520666f6f642062616e6b207573616765206973206f6e2074686520726973652c207768696c652074686520656e7669726f6e6d656e74206f66206f7572206e6174696f6e206973206265696e67206060646567726567617465642727202061742061207261706964207261746520616e64207768696c65207075626c6963207365727669636520776f726b65727320617265206e6f742067657474696e67207468652065717569747920616e6420657175616c697479207468657920646573657276652e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_rAZtYnqv():
    # {'PlainText Sentences': 'He knows that the issue we are dealing with is an international one which involves the smuggling of human beings.', 'Encrypted Texts': {'PlainText': 'He knows that the issue we are dealing with is an international one which involves the smuggling of human beings.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_wtTEERMn():
    # {'PlainText Sentences': "colleague reminds me, that it sucked out of the province of Alberta in the name of interventionism, in the name of ``we have all the answers for you''.", 'Encrypted Texts': {'PlainText': "colleague reminds me, that it sucked out of the province of Alberta in the name of interventionism, in the name of ``we have all the answers for you''.", 'EncryptedText': '636f6c6c65616775652072656d696e6473206d652c2074686174206974207375636b6564206f7574206f66207468652070726f76696e6365206f6620416c626572746120696e20746865206e616d65206f6620696e74657276656e74696f6e69736d2c20696e20746865206e616d65206f662060607765206861766520616c6c2074686520616e737765727320666f7220796f7527272e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("636f6c6c65616775652072656d696e6473206d652c2074686174206974207375636b6564206f7574206f66207468652070726f76696e6365206f6620416c626572746120696e20746865206e616d65206f6620696e74657276656e74696f6e69736d2c20696e20746865206e616d65206f662060607765206861766520616c6c2074686520616e737765727320666f7220796f7527272e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_FlmMcqQv():
    # {'PlainText Sentences': 'First, it helps to further privatize the Canada Mortgage and Housing Corporation.', 'Encrypted Texts': {'PlainText': 'First, it helps to further privatize the Canada Mortgage and Housing Corporation.', 'EncryptedText': b'46697273742C2069742068656C707320746F206675727468657220707269766174697A65207468652043616E616461204D6F72746761676520616E6420486F7573696E6720436F72706F726174696F6E2E', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'46697273742C2069742068656C707320746F206675727468657220707269766174697A65207468652043616E616461204D6F72746761676520616E6420486F7573696E6720436F72706F726174696F6E2E'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_ZNVmbQBP():
    # {'PlainText Sentences': 'Late last week, five studies were released on the assessment of the 1994 reform, and these were not carried out by Bloc Quebecois experts or by experts wishing to express their opinions but by experts on the government payroll.', 'Encrypted Texts': {'PlainText': 'Late last week, five studies were released on the assessment of the 1994 reform, and these were not carried out by Bloc Quebecois experts or by experts wishing to express their opinions but by experts on the government payroll.', 'EncryptedText': b'TGF0ZSBsYXN0IHdlZWssIGZpdmUgc3R1ZGllcyB3ZXJlIHJlbGVhc2VkIG9uIHRoZSBhc3Nlc3NtZW50IG9mIHRoZSAxOTk0IHJlZm9ybSwgYW5kIHRoZXNlIHdlcmUgbm90IGNhcnJpZWQgb3V0IGJ5IEJsb2MgUXVlYmVjb2lzIGV4cGVydHMgb3IgYnkgZXhwZXJ0cyB3aXNoaW5nIHRvIGV4cHJlc3MgdGhlaXIgb3BpbmlvbnMgYnV0IGJ5IGV4cGVydHMgb24gdGhlIGdvdmVybm1lbnQgcGF5cm9sbC4=', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'TGF0ZSBsYXN0IHdlZWssIGZpdmUgc3R1ZGllcyB3ZXJlIHJlbGVhc2VkIG9uIHRoZSBhc3Nlc3NtZW50IG9mIHRoZSAxOTk0IHJlZm9ybSwgYW5kIHRoZXNlIHdlcmUgbm90IGNhcnJpZWQgb3V0IGJ5IEJsb2MgUXVlYmVjb2lzIGV4cGVydHMgb3IgYnkgZXhwZXJ0cyB3aXNoaW5nIHRvIGV4cHJlc3MgdGhlaXIgb3BpbmlvbnMgYnV0IGJ5IGV4cGVydHMgb24gdGhlIGdvdmVybm1lbnQgcGF5cm9sbC4='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_UKimPgwP():
    # {'PlainText Sentences': 'He is supposed to have some answers.', 'Encrypted Texts': {'PlainText': 'He is supposed to have some answers.', 'EncryptedText': '72 101 32 105 115 32 115 117 112 112 111 115 101 100 32 116 111 32 104 97 118 101 32 115 111 109 101 32 97 110 115 119 101 114 115 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("72 101 32 105 115 32 115 117 112 112 111 115 101 100 32 116 111 32 104 97 118 101 32 115 111 109 101 32 97 110 115 119 101 114 115 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_qohvgwaX():
    # {'PlainText Sentences': 'The high altitude areas escaped glaciation and served as a refuge to the biota during the Wisconsin glacial stage.', 'Encrypted Texts': {'PlainText': 'The high altitude areas escaped glaciation and served as a refuge to the biota during the Wisconsin glacial stage.', 'EncryptedText': '.egats laicalg nisnocsiW eht gnirud atoib eht ot egufer a sa devres dna noitaicalg depacse saera edutitla hgih ehT', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".egats laicalg nisnocsiW eht gnirud atoib eht ot egufer a sa devres dna noitaicalg depacse saera edutitla hgih ehT")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_sGSQYDxZ():
    # {'PlainText Sentences': 'I will now move on to the issue of abolishing conditional sentences for violent offenders.', 'Encrypted Texts': {'PlainText': 'I will now move on to the issue of abolishing conditional sentences for violent offenders.', 'EncryptedText': '1001001 100000 1110111 1101001 1101100 1101100 100000 1101110 1101111 1110111 100000 1101101 1101111 1110110 1100101 100000 1101111 1101110 100000 1110100 1101111 100000 1110100 1101000 1100101 100000 1101001 1110011 1110011 1110101 1100101 100000 1101111 1100110 100000 1100001 1100010 1101111 1101100 1101001 1110011 1101000 1101001 1101110 1100111 100000 1100011 1101111 1101110 1100100 1101001 1110100 1101001 1101111 1101110 1100001 1101100 100000 1110011 1100101 1101110 1110100 1100101 1101110 1100011 1100101 1110011 100000 1100110 1101111 1110010 100000 1110110 1101001 1101111 1101100 1100101 1101110 1110100 100000 1101111 1100110 1100110 1100101 1101110 1100100 1100101 1110010 1110011 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1001001 100000 1110111 1101001 1101100 1101100 100000 1101110 1101111 1110111 100000 1101101 1101111 1110110 1100101 100000 1101111 1101110 100000 1110100 1101111 100000 1110100 1101000 1100101 100000 1101001 1110011 1110011 1110101 1100101 100000 1101111 1100110 100000 1100001 1100010 1101111 1101100 1101001 1110011 1101000 1101001 1101110 1100111 100000 1100011 1101111 1101110 1100100 1101001 1110100 1101001 1101111 1101110 1100001 1101100 100000 1110011 1100101 1101110 1110100 1100101 1101110 1100011 1100101 1110011 100000 1100110 1101111 1110010 100000 1110110 1101001 1101111 1101100 1100101 1101110 1110100 100000 1101111 1100110 1100110 1100101 1101110 1100100 1100101 1110010 1110011 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_owdoItsk():
    # {'PlainText Sentences': 'However, when the federal government found it did not have a legal leg to stand on, it quietly dropped the lawsuit and finally started negotiations two months ago.', 'Encrypted Texts': {'PlainText': 'However, when the federal government found it did not have a legal leg to stand on, it quietly dropped the lawsuit and finally started negotiations two months ago.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_GwUiijXz():
    # {'PlainText Sentences': 'Allan Rock \nMr. Chuck Strahl \nHon.', 'Encrypted Texts': {'PlainText': 'Allan Rock \nMr. Chuck Strahl \nHon.', 'EncryptedText': '65 108 108 97 110 32 82 111 99 107 32 10 77 114 46 32 67 104 117 99 107 32 83 116 114 97 104 108 32 10 72 111 110 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("65 108 108 97 110 32 82 111 99 107 32 10 77 114 46 32 67 104 117 99 107 32 83 116 114 97 104 108 32 10 72 111 110 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_MaCrlIml():
    # {'PlainText Sentences': 'In committee and in the House our party has tried to put forward the best balanced approach which we feel will do the most in the end for the protection of the environment.', 'Encrypted Texts': {'PlainText': 'In committee and in the House our party has tried to put forward the best balanced approach which we feel will do the most in the end for the protection of the environment.', 'EncryptedText': '.. -. \n -.-. --- -- -- .. - - . . \n .- -. -.. \n .. -. \n - .... . \n .... --- ..- ... . \n --- ..- .-. \n .--. .- .-. - -.-- \n .... .- ... \n - .-. .. . -.. \n - --- \n .--. ..- - \n ..-. --- .-. .-- .- .-. -.. \n - .... . \n -... . ... - \n -... .- .-.. .- -. -.-. . -.. \n .- .--. .--. .-. --- .- -.-. .... \n .-- .... .. -.-. .... \n .-- . \n ..-. . . .-.. \n .-- .. .-.. .-.. \n -.. --- \n - .... . \n -- --- ... - \n .. -. \n - .... . \n . -. -.. \n ..-. --- .-. \n - .... . \n .--. .-. --- - . -.-. - .. --- -. \n --- ..-. \n - .... . \n . -. ...- .. .-. --- -. -- . -. - .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".. -. 
 -.-. --- -- -- .. - - . . 
 .- -. -.. 
 .. -. 
 - .... . 
 .... --- ..- ... . 
 --- ..- .-. 
 .--. .- .-. - -.-- 
 .... .- ... 
 - .-. .. . -.. 
 - --- 
 .--. ..- - 
 ..-. --- .-. .-- .- .-. -.. 
 - .... . 
 -... . ... - 
 -... .- .-.. .- -. -.-. . -.. 
 .- .--. .--. .-. --- .- -.-. .... 
 .-- .... .. -.-. .... 
 .-- . 
 ..-. . . .-.. 
 .-- .. .-.. .-.. 
 -.. --- 
 - .... . 
 -- --- ... - 
 .. -. 
 - .... . 
 . -. -.. 
 ..-. --- .-. 
 - .... . 
 .--. .-. --- - . -.-. - .. --- -. 
 --- ..-. 
 - .... . 
 . -. ...- .. .-. --- -. -- . -. - .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_OPUrzuAy():
    # {'PlainText Sentences': 'Mr. Speaker, I ask you to consider whether or not the denial of my access to committee draft papers available to other members of the committee constitutes an obstruction of a member and therefore constitutes a prima facie question of privilege.', 'Encrypted Texts': {'PlainText': 'Mr. Speaker, I ask you to consider whether or not the denial of my access to committee draft papers available to other members of the committee constitutes an obstruction of a member and therefore constitutes a prima facie question of privilege.', 'EncryptedText': b'TXIuIFNwZWFrZXIsIEkgYXNrIHlvdSB0byBjb25zaWRlciB3aGV0aGVyIG9yIG5vdCB0aGUgZGVuaWFsIG9mIG15IGFjY2VzcyB0byBjb21taXR0ZWUgZHJhZnQgcGFwZXJzIGF2YWlsYWJsZSB0byBvdGhlciBtZW1iZXJzIG9mIHRoZSBjb21taXR0ZWUgY29uc3RpdHV0ZXMgYW4gb2JzdHJ1Y3Rpb24gb2YgYSBtZW1iZXIgYW5kIHRoZXJlZm9yZSBjb25zdGl0dXRlcyBhIHByaW1hIGZhY2llIHF1ZXN0aW9uIG9mIHByaXZpbGVnZS4=', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'TXIuIFNwZWFrZXIsIEkgYXNrIHlvdSB0byBjb25zaWRlciB3aGV0aGVyIG9yIG5vdCB0aGUgZGVuaWFsIG9mIG15IGFjY2VzcyB0byBjb21taXR0ZWUgZHJhZnQgcGFwZXJzIGF2YWlsYWJsZSB0byBvdGhlciBtZW1iZXJzIG9mIHRoZSBjb21taXR0ZWUgY29uc3RpdHV0ZXMgYW4gb2JzdHJ1Y3Rpb24gb2YgYSBtZW1iZXIgYW5kIHRoZXJlZm9yZSBjb25zdGl0dXRlcyBhIHByaW1hIGZhY2llIHF1ZXN0aW9uIG9mIHByaXZpbGVnZS4='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_CLpDckbY():
    # {'PlainText Sentences': 'MULTILATERAL AGREEMENT ON INVESTMENT \nMr. Svend J. Robinson (Burnaby-Douglas, NDP):\nThey note that the MAI is the latest in a series of regional and global agreements which in the name of liberalizing trade and investment expands the powers of multinational corporations at the expense of the powers of governments to intervene in the marketplace on behalf of our social, cultural, environmental and health care goals.', 'Encrypted Texts': {'PlainText': 'MULTILATERAL AGREEMENT ON INVESTMENT \nMr. Svend J. Robinson (Burnaby-Douglas, NDP):\nThey note that the MAI is the latest in a series of regional and global agreements which in the name of liberalizing trade and investment expands the powers of multinational corporations at the expense of the powers of governments to intervene in the marketplace on behalf of our social, cultural, environmental and health care goals.', 'EncryptedText': '77 85 76 84 73 76 65 84 69 82 65 76 32 65 71 82 69 69 77 69 78 84 32 79 78 32 73 78 86 69 83 84 77 69 78 84 32 10 77 114 46 32 83 118 101 110 100 32 74 46 32 82 111 98 105 110 115 111 110 32 40 66 117 114 110 97 98 121 45 68 111 117 103 108 97 115 44 32 78 68 80 41 58 10 84 104 101 121 32 110 111 116 101 32 116 104 97 116 32 116 104 101 32 77 65 73 32 105 115 32 116 104 101 32 108 97 116 101 115 116 32 105 110 32 97 32 115 101 114 105 101 115 32 111 102 32 114 101 103 105 111 110 97 108 32 97 110 100 32 103 108 111 98 97 108 32 97 103 114 101 101 109 101 110 116 115 32 119 104 105 99 104 32 105 110 32 116 104 101 32 110 97 109 101 32 111 102 32 108 105 98 101 114 97 108 105 122 105 110 103 32 116 114 97 100 101 32 97 110 100 32 105 110 118 101 115 116 109 101 110 116 32 101 120 112 97 110 100 115 32 116 104 101 32 112 111 119 101 114 115 32 111 102 32 109 117 108 116 105 110 97 116 105 111 110 97 108 32 99 111 114 112 111 114 97 116 105 111 110 115 32 97 116 32 116 104 101 32 101 120 112 101 110 115 101 32 111 102 32 116 104 101 32 112 111 119 101 114 115 32 111 102 32 103 111 118 101 114 110 109 101 110 116 115 32 116 111 32 105 110 116 101 114 118 101 110 101 32 105 110 32 116 104 101 32 109 97 114 107 101 116 112 108 97 99 101 32 111 110 32 98 101 104 97 108 102 32 111 102 32 111 117 114 32 115 111 99 105 97 108 44 32 99 117 108 116 117 114 97 108 44 32 101 110 118 105 114 111 110 109 101 110 116 97 108 32 97 110 100 32 104 101 97 108 116 104 32 99 97 114 101 32 103 111 97 108 115 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("77 85 76 84 73 76 65 84 69 82 65 76 32 65 71 82 69 69 77 69 78 84 32 79 78 32 73 78 86 69 83 84 77 69 78 84 32 10 77 114 46 32 83 118 101 110 100 32 74 46 32 82 111 98 105 110 115 111 110 32 40 66 117 114 110 97 98 121 45 68 111 117 103 108 97 115 44 32 78 68 80 41 58 10 84 104 101 121 32 110 111 116 101 32 116 104 97 116 32 116 104 101 32 77 65 73 32 105 115 32 116 104 101 32 108 97 116 101 115 116 32 105 110 32 97 32 115 101 114 105 101 115 32 111 102 32 114 101 103 105 111 110 97 108 32 97 110 100 32 103 108 111 98 97 108 32 97 103 114 101 101 109 101 110 116 115 32 119 104 105 99 104 32 105 110 32 116 104 101 32 110 97 109 101 32 111 102 32 108 105 98 101 114 97 108 105 122 105 110 103 32 116 114 97 100 101 32 97 110 100 32 105 110 118 101 115 116 109 101 110 116 32 101 120 112 97 110 100 115 32 116 104 101 32 112 111 119 101 114 115 32 111 102 32 109 117 108 116 105 110 97 116 105 111 110 97 108 32 99 111 114 112 111 114 97 116 105 111 110 115 32 97 116 32 116 104 101 32 101 120 112 101 110 115 101 32 111 102 32 116 104 101 32 112 111 119 101 114 115 32 111 102 32 103 111 118 101 114 110 109 101 110 116 115 32 116 111 32 105 110 116 101 114 118 101 110 101 32 105 110 32 116 104 101 32 109 97 114 107 101 116 112 108 97 99 101 32 111 110 32 98 101 104 97 108 102 32 111 102 32 111 117 114 32 115 111 99 105 97 108 44 32 99 117 108 116 117 114 97 108 44 32 101 110 118 105 114 111 110 109 101 110 116 97 108 32 97 110 100 32 104 101 97 108 116 104 32 99 97 114 101 32 103 111 97 108 115 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_znvmSIIO():
    # {'PlainText Sentences': 'On the other hand, we know that tax agreements are nothing new.', 'Encrypted Texts': {'PlainText': 'On the other hand, we know that tax agreements are nothing new.', 'EncryptedText': '.wen gnihton era stnemeerga xat taht wonk ew ,dnah rehto eht nO', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".wen gnihton era stnemeerga xat taht wonk ew ,dnah rehto eht nO")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_WFiQjIBd():
    # {'PlainText Sentences': 'The petitioners are calling for serious penalties for people who cause pain and harm to animals and they suggest an educational program to help judges understand the seriousness of this offence.', 'Encrypted Texts': {'PlainText': 'The petitioners are calling for serious penalties for people who cause pain and harm to animals and they suggest an educational program to help judges understand the seriousness of this offence.', 'EncryptedText': '546865207065746974696f6e657273206172652063616c6c696e6720666f7220736572696f75732070656e616c7469657320666f722070656f706c652077686f206361757365207061696e20616e64206861726d20746f20616e696d616c7320616e642074686579207375676765737420616e20656475636174696f6e616c2070726f6772616d20746f2068656c70206a756467657320756e6465727374616e642074686520736572696f75736e657373206f662074686973206f6666656e63652e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("546865207065746974696f6e657273206172652063616c6c696e6720666f7220736572696f75732070656e616c7469657320666f722070656f706c652077686f206361757365207061696e20616e64206861726d20746f20616e696d616c7320616e642074686579207375676765737420616e20656475636174696f6e616c2070726f6772616d20746f2068656c70206a756467657320756e6465727374616e642074686520736572696f75736e657373206f662074686973206f6666656e63652e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_taJnvLzU():
    # {'PlainText Sentences': 'I cannot help but think that in the end it is destructive of our collective well-being to have governments dependent in the way they have become on revenue from gambling, dependent so much so that they are always looking for opportunities to expand this revenue base.', 'Encrypted Texts': {'PlainText': 'I cannot help but think that in the end it is destructive of our collective well-being to have governments dependent in the way they have become on revenue from gambling, dependent so much so that they are always looking for opportunities to expand this revenue base.', 'EncryptedText': b'JEQGGYLONZXXIIDIMVWHAIDCOV2CA5DINFXGWIDUNBQXIIDJNYQHI2DFEBSW4ZBANF2CA2LTEBSGK43UOJ2WG5DJOZSSA33GEBXXK4RAMNXWY3DFMN2GS5TFEB3WK3DMFVRGK2LOM4QHI3ZANBQXMZJAM5XXMZLSNZWWK3TUOMQGIZLQMVXGIZLOOQQGS3RAORUGKIDXMF4SA5DIMV4SA2DBOZSSAYTFMNXW2ZJAN5XCA4TFOZSW45LFEBTHE33NEBTWC3LCNRUW4ZZMEBSGK4DFNZSGK3TUEBZW6IDNOVRWQIDTN4QHI2DBOQQHI2DFPEQGC4TFEBQWY53BPFZSA3DPN5VWS3THEBTG64RAN5YHA33SOR2W42LUNFSXGIDUN4QGK6DQMFXGIIDUNBUXGIDSMV3GK3TVMUQGEYLTMUXA====', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'JEQGGYLONZXXIIDIMVWHAIDCOV2CA5DINFXGWIDUNBQXIIDJNYQHI2DFEBSW4ZBANF2CA2LTEBSGK43UOJ2WG5DJOZSSA33GEBXXK4RAMNXWY3DFMN2GS5TFEB3WK3DMFVRGK2LOM4QHI3ZANBQXMZJAM5XXMZLSNZWWK3TUOMQGIZLQMVXGIZLOOQQGS3RAORUGKIDXMF4SA5DIMV4SA2DBOZSSAYTFMNXW2ZJAN5XCA4TFOZSW45LFEBTHE33NEBTWC3LCNRUW4ZZMEBSGK4DFNZSGK3TUEBZW6IDNOVRWQIDTN4QHI2DBOQQHI2DFPEQGC4TFEBQWY53BPFZSA3DPN5VWS3THEBTG64RAN5YHA33SOR2W42LUNFSXGIDUN4QGK6DQMFXGIIDUNBUXGIDSMV3GK3TVMUQGEYLTMUXA===='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_RmwbkDYi():
    # {'PlainText Sentences': '):\nMadam Speaker, first I compliment the member for Durham on his continuing work and interest in this area.', 'Encrypted Texts': {'PlainText': '):\nMadam Speaker, first I compliment the member for Durham on his continuing work and interest in this area.', 'EncryptedText': '.aera siht ni tseretni dna krow gniunitnoc sih no mahruD rof rebmem eht tnemilpmoc I tsrif ,rekaepS madaM\n:)', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".aera siht ni tseretni dna krow gniunitnoc sih no mahruD rof rebmem eht tnemilpmoc I tsrif ,rekaepS madaM
:)")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_XziqjjHv():
    # {'PlainText Sentences': 'This annual debt service bill is enough to run the governments of Newfoundland, P.E.I., Nova Scotia, New Brunswick, Manitoba, Saskatchewan and Alberta for an entire year with enough left over to pay the entire public debts of Newfoundland, New Brunswick and P.E.I.', 'Encrypted Texts': {'PlainText': 'This annual debt service bill is enough to run the governments of Newfoundland, P.E.I., Nova Scotia, New Brunswick, Manitoba, Saskatchewan and Alberta for an entire year with enough left over to pay the entire public debts of Newfoundland, New Brunswick and P.E.I.', 'EncryptedText': b'KRUGS4ZAMFXG45LBNQQGIZLCOQQHGZLSOZUWGZJAMJUWY3BANFZSAZLON52WO2BAORXSA4TVNYQHI2DFEBTW65TFOJXG2ZLOORZSA33GEBHGK53GN52W4ZDMMFXGILBAKAXEKLSJFYWCATTPOZQSAU3DN52GSYJMEBHGK5ZAIJZHK3TTO5UWG2ZMEBGWC3TJORXWEYJMEBJWC43LMF2GG2DFO5QW4IDBNZSCAQLMMJSXE5DBEBTG64RAMFXCAZLOORUXEZJAPFSWC4RAO5UXI2BAMVXG65LHNAQGYZLGOQQG65TFOIQHI3ZAOBQXSIDUNBSSAZLOORUXEZJAOB2WE3DJMMQGIZLCORZSA33GEBHGK53GN52W4ZDMMFXGILBAJZSXOICCOJ2W443XNFRWWIDBNZSCAUBOIUXESLQ=', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'KRUGS4ZAMFXG45LBNQQGIZLCOQQHGZLSOZUWGZJAMJUWY3BANFZSAZLON52WO2BAORXSA4TVNYQHI2DFEBTW65TFOJXG2ZLOORZSA33GEBHGK53GN52W4ZDMMFXGILBAKAXEKLSJFYWCATTPOZQSAU3DN52GSYJMEBHGK5ZAIJZHK3TTO5UWG2ZMEBGWC3TJORXWEYJMEBJWC43LMF2GG2DFO5QW4IDBNZSCAQLMMJSXE5DBEBTG64RAMFXCAZLOORUXEZJAPFSWC4RAO5UXI2BAMVXG65LHNAQGYZLGOQQG65TFOIQHI3ZAOBQXSIDUNBSSAZLOORUXEZJAOB2WE3DJMMQGIZLCORZSA33GEBHGK53GN52W4ZDMMFXGILBAJZSXOICCOJ2W443XNFRWWIDBNZSCAUBOIUXESLQ='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_rwXsoQER():
    # {'PlainText Sentences': 'If my hon.', 'Encrypted Texts': {'PlainText': 'If my hon.', 'EncryptedText': '.. ..-. \n -- -.-- \n .... --- -. .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".. ..-. 
 -- -.-- 
 .... --- -. .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_aZsoyjDp():
    # {'PlainText Sentences': "Workers who have been laid off and are without resources kill their wives and children because they are unable to provide for them.''", 'Encrypted Texts': {'PlainText': "Workers who have been laid off and are without resources kill their wives and children because they are unable to provide for them.''", 'EncryptedText': '87 111 114 107 101 114 115 32 119 104 111 32 104 97 118 101 32 98 101 101 110 32 108 97 105 100 32 111 102 102 32 97 110 100 32 97 114 101 32 119 105 116 104 111 117 116 32 114 101 115 111 117 114 99 101 115 32 107 105 108 108 32 116 104 101 105 114 32 119 105 118 101 115 32 97 110 100 32 99 104 105 108 100 114 101 110 32 98 101 99 97 117 115 101 32 116 104 101 121 32 97 114 101 32 117 110 97 98 108 101 32 116 111 32 112 114 111 118 105 100 101 32 102 111 114 32 116 104 101 109 46 39 39', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("87 111 114 107 101 114 115 32 119 104 111 32 104 97 118 101 32 98 101 101 110 32 108 97 105 100 32 111 102 102 32 97 110 100 32 97 114 101 32 119 105 116 104 111 117 116 32 114 101 115 111 117 114 99 101 115 32 107 105 108 108 32 116 104 101 105 114 32 119 105 118 101 115 32 97 110 100 32 99 104 105 108 100 114 101 110 32 98 101 99 97 117 115 101 32 116 104 101 121 32 97 114 101 32 117 110 97 98 108 101 32 116 111 32 112 114 111 118 105 100 101 32 102 111 114 32 116 104 101 109 46 39 39")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_SQUDAxxc():
    # {'PlainText Sentences': 'David Anderson \nMr. Peter MacKay \nHon.', 'Encrypted Texts': {'PlainText': 'David Anderson \nMr. Peter MacKay \nHon.', 'EncryptedText': '68 97 118 105 100 32 65 110 100 101 114 115 111 110 32 10 77 114 46 32 80 101 116 101 114 32 77 97 99 75 97 121 32 10 72 111 110 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("68 97 118 105 100 32 65 110 100 101 114 115 111 110 32 10 77 114 46 32 80 101 116 101 114 32 77 97 99 75 97 121 32 10 72 111 110 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_rDSeOCzv():
    # {'PlainText Sentences': 'Why do we not use tougher sanctions on them?', 'Encrypted Texts': {'PlainText': 'Why do we not use tougher sanctions on them?', 'EncryptedText': '87 104 121 32 100 111 32 119 101 32 110 111 116 32 117 115 101 32 116 111 117 103 104 101 114 32 115 97 110 99 116 105 111 110 115 32 111 110 32 116 104 101 109 63', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("87 104 121 32 100 111 32 119 101 32 110 111 116 32 117 115 101 32 116 111 117 103 104 101 114 32 115 97 110 99 116 105 111 110 115 32 111 110 32 116 104 101 109 63")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_LZxDqKbS():
    # {'PlainText Sentences': 'The Acting Speaker (Ms. Thibeault):\nI have already recognized the hon.', 'Encrypted Texts': {'PlainText': 'The Acting Speaker (Ms. Thibeault):\nI have already recognized the hon.', 'EncryptedText': b'VGhlIEFjdGluZyBTcGVha2VyIChNcy4gVGhpYmVhdWx0KToKSSBoYXZlIGFscmVhZHkgcmVjb2duaXplZCB0aGUgaG9uLg==', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'VGhlIEFjdGluZyBTcGVha2VyIChNcy4gVGhpYmVhdWx0KToKSSBoYXZlIGFscmVhZHkgcmVjb2duaXplZCB0aGUgaG9uLg=='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_GChxOvGQ():
    # {'PlainText Sentences': 'Why does the hon.', 'Encrypted Texts': {'PlainText': 'Why does the hon.', 'EncryptedText': '87 104 121 32 100 111 101 115 32 116 104 101 32 104 111 110 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("87 104 121 32 100 111 101 115 32 116 104 101 32 104 111 110 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_haxlnKrf():
    # {'PlainText Sentences': 'Could the Minister of Foreign Affairs tell us why he is boycotting this international forum and wants to exclude Quebec once again?', 'Encrypted Texts': {'PlainText': 'Could the Minister of Foreign Affairs tell us why he is boycotting this international forum and wants to exclude Quebec once again?', 'EncryptedText': b'436F756C6420746865204D696E6973746572206F6620466F726569676E20416666616972732074656C6C2075732077687920686520697320626F79636F7474696E67207468697320696E7465726E6174696F6E616C20666F72756D20616E642077616E747320746F206578636C75646520517565626563206F6E636520616761696E3F', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'436F756C6420746865204D696E6973746572206F6620466F726569676E20416666616972732074656C6C2075732077687920686520697320626F79636F7474696E67207468697320696E7465726E6174696F6E616C20666F72756D20616E642077616E747320746F206578636C75646520517565626563206F6E636520616761696E3F'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_mKxUfNVK():
    # {'PlainText Sentences': 'FISHERIES \nMrs. Diane Ablonczy (Calgary-Nose Hill, Ref.', 'Encrypted Texts': {'PlainText': 'FISHERIES \nMrs. Diane Ablonczy (Calgary-Nose Hill, Ref.', 'EncryptedText': '.feR ,lliH esoN-yraglaC( yzcnolbA enaiD .srM\n SEIREHSIF', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".feR ,lliH esoN-yraglaC( yzcnolbA enaiD .srM
 SEIREHSIF")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_nNmEDzPC():
    # {'PlainText Sentences': 'member who just spoke said that more subsidies for Canadian farmers are not the answer.', 'Encrypted Texts': {'PlainText': 'member who just spoke said that more subsidies for Canadian farmers are not the answer.', 'EncryptedText': '109 101 109 98 101 114 32 119 104 111 32 106 117 115 116 32 115 112 111 107 101 32 115 97 105 100 32 116 104 97 116 32 109 111 114 101 32 115 117 98 115 105 100 105 101 115 32 102 111 114 32 67 97 110 97 100 105 97 110 32 102 97 114 109 101 114 115 32 97 114 101 32 110 111 116 32 116 104 101 32 97 110 115 119 101 114 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("109 101 109 98 101 114 32 119 104 111 32 106 117 115 116 32 115 112 111 107 101 32 115 97 105 100 32 116 104 97 116 32 109 111 114 101 32 115 117 98 115 105 100 105 101 115 32 102 111 114 32 67 97 110 97 100 105 97 110 32 102 97 114 109 101 114 115 32 97 114 101 32 110 111 116 32 116 104 101 32 97 110 115 119 101 114 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_JUkQNfgS():
    # {'PlainText Sentences': 'Hon.', 'Encrypted Texts': {'PlainText': 'Hon.', 'EncryptedText': '1001000 1101111 1101110 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1001000 1101111 1101110 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_LoowJSrq():
    # {'PlainText Sentences': 'For those 4% to 5% that cannot come to an agreement, someone has to make the agreement for them.', 'Encrypted Texts': {'PlainText': 'For those 4% to 5% that cannot come to an agreement, someone has to make the agreement for them.', 'EncryptedText': b'Rm9yIHRob3NlIDQlIHRvIDUlIHRoYXQgY2Fubm90IGNvbWUgdG8gYW4gYWdyZWVtZW50LCBzb21lb25lIGhhcyB0byBtYWtlIHRoZSBhZ3JlZW1lbnQgZm9yIHRoZW0u', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'Rm9yIHRob3NlIDQlIHRvIDUlIHRoYXQgY2Fubm90IGNvbWUgdG8gYW4gYWdyZWVtZW50LCBzb21lb25lIGhhcyB0byBtYWtlIHRoZSBhZ3JlZW1lbnQgZm9yIHRoZW0u'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_KmwKewbo():
    # {'PlainText Sentences': 'colleague has to say about that?', 'Encrypted Texts': {'PlainText': 'colleague has to say about that?', 'EncryptedText': '?taht tuoba yas ot sah eugaelloc', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config("?taht tuoba yas ot sah eugaelloc")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Hex_epYbYwrA():
    # {'PlainText Sentences': 'Farmers are looking for some options or alternatives in addition to some short term help to get them through the present situation which has seen their incomes drop so drastically through no fault of their own.', 'Encrypted Texts': {'PlainText': 'Farmers are looking for some options or alternatives in addition to some short term help to get them through the present situation which has seen their incomes drop so drastically through no fault of their own.', 'EncryptedText': '4661726d65727320617265206c6f6f6b696e6720666f7220736f6d65206f7074696f6e73206f7220616c7465726e61746976657320696e206164646974696f6e20746f20736f6d652073686f7274207465726d2068656c7020746f20676574207468656d207468726f756768207468652070726573656e7420736974756174696f6e20776869636820686173207365656e20746865697220696e636f6d65732064726f7020736f2064726173746963616c6c79207468726f756768206e6f206661756c74206f66207468656972206f776e2e', 'CipherUsed': 'Hex'}}
    cfg = make_default_config("4661726d65727320617265206c6f6f6b696e6720666f7220736f6d65206f7074696f6e73206f7220616c7465726e61746976657320696e206164646974696f6e20746f20736f6d652073686f7274207465726d2068656c7020746f20676574207468656d207468726f756768207468652070726573656e7420736974756174696f6e20776869636820686173207365656e20746865697220696e636f6d65732064726f7020736f2064726173746963616c6c79207468726f756768206e6f206661756c74206f66207468656972206f776e2e")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_PHxXBFHs():
    # {'PlainText Sentences': 'Hon.', 'Encrypted Texts': {'PlainText': 'Hon.', 'EncryptedText': '.noH', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".noH")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_HkKTYKvT():
    # {'PlainText Sentences': 'Hon.', 'Encrypted Texts': {'PlainText': 'Hon.', 'EncryptedText': '1001000 1101111 1101110 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1001000 1101111 1101110 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_teroqFTp():
    # {'PlainText Sentences': "Canada's beginnings and its future is due to its wonderful multicultural nature, citizens who came to Canada from all over the globe.", 'Encrypted Texts': {'PlainText': "Canada's beginnings and its future is due to its wonderful multicultural nature, citizens who came to Canada from all over the globe.", 'EncryptedText': '67 97 110 97 100 97 39 115 32 98 101 103 105 110 110 105 110 103 115 32 97 110 100 32 105 116 115 32 102 117 116 117 114 101 32 105 115 32 100 117 101 32 116 111 32 105 116 115 32 119 111 110 100 101 114 102 117 108 32 109 117 108 116 105 99 117 108 116 117 114 97 108 32 110 97 116 117 114 101 44 32 99 105 116 105 122 101 110 115 32 119 104 111 32 99 97 109 101 32 116 111 32 67 97 110 97 100 97 32 102 114 111 109 32 97 108 108 32 111 118 101 114 32 116 104 101 32 103 108 111 98 101 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("67 97 110 97 100 97 39 115 32 98 101 103 105 110 110 105 110 103 115 32 97 110 100 32 105 116 115 32 102 117 116 117 114 101 32 105 115 32 100 117 101 32 116 111 32 105 116 115 32 119 111 110 100 101 114 102 117 108 32 109 117 108 116 105 99 117 108 116 117 114 97 108 32 110 97 116 117 114 101 44 32 99 105 116 105 122 101 110 115 32 119 104 111 32 99 97 109 101 32 116 111 32 67 97 110 97 100 97 32 102 114 111 109 32 97 108 108 32 111 118 101 114 32 116 104 101 32 103 108 111 98 101 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_FPSNgXGU():
    # {'PlainText Sentences': 'John Manley \nMr. Scott Brison \nHon.', 'Encrypted Texts': {'PlainText': 'John Manley \nMr. Scott Brison \nHon.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base64_BpLfrrNf():
    # {'PlainText Sentences': 'There is much controversy with private members bills because many of us believe they do not go anywhere unless the cabinet agrees.', 'Encrypted Texts': {'PlainText': 'There is much controversy with private members bills because many of us believe they do not go anywhere unless the cabinet agrees.', 'EncryptedText': b'VGhlcmUgaXMgbXVjaCBjb250cm92ZXJzeSB3aXRoIHByaXZhdGUgbWVtYmVycyBiaWxscyBiZWNhdXNlIG1hbnkgb2YgdXMgYmVsaWV2ZSB0aGV5IGRvIG5vdCBnbyBhbnl3aGVyZSB1bmxlc3MgdGhlIGNhYmluZXQgYWdyZWVzLg==', 'CipherUsed': 'Base64'}}
    cfg = make_default_config("b'VGhlcmUgaXMgbXVjaCBjb250cm92ZXJzeSB3aXRoIHByaXZhdGUgbWVtYmVycyBiaWxscyBiZWNhdXNlIG1hbnkgb2YgdXMgYmVsaWV2ZSB0aGV5IGRvIG5vdCBnbyBhbnl3aGVyZSB1bmxlc3MgdGhlIGNhYmluZXQgYWdyZWVzLg=='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_tXZQHxtv():
    # {'PlainText Sentences': 'I listened to the minister say that he felt that the time was not right for that kind of consultation.', 'Encrypted Texts': {'PlainText': 'I listened to the minister say that he felt that the time was not right for that kind of consultation.', 'EncryptedText': '73 32 108 105 115 116 101 110 101 100 32 116 111 32 116 104 101 32 109 105 110 105 115 116 101 114 32 115 97 121 32 116 104 97 116 32 104 101 32 102 101 108 116 32 116 104 97 116 32 116 104 101 32 116 105 109 101 32 119 97 115 32 110 111 116 32 114 105 103 104 116 32 102 111 114 32 116 104 97 116 32 107 105 110 100 32 111 102 32 99 111 110 115 117 108 116 97 116 105 111 110 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("73 32 108 105 115 116 101 110 101 100 32 116 111 32 116 104 101 32 109 105 110 105 115 116 101 114 32 115 97 121 32 116 104 97 116 32 104 101 32 102 101 108 116 32 116 104 97 116 32 116 104 101 32 116 105 109 101 32 119 97 115 32 110 111 116 32 114 105 103 104 116 32 102 111 114 32 116 104 97 116 32 107 105 110 100 32 111 102 32 99 111 110 115 117 108 116 97 116 105 111 110 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_RwPPaWUG():
    # {'PlainText Sentences': 'Now that progressive conservative measures like free trade and the GST-which will bring $24 billion in revenues-have helped it get rich, the government could introduce legislation to fight poverty.', 'Encrypted Texts': {'PlainText': 'Now that progressive conservative measures like free trade and the GST-which will bring $24 billion in revenues-have helped it get rich, the government could introduce legislation to fight poverty.', 'EncryptedText': '78 111 119 32 116 104 97 116 32 112 114 111 103 114 101 115 115 105 118 101 32 99 111 110 115 101 114 118 97 116 105 118 101 32 109 101 97 115 117 114 101 115 32 108 105 107 101 32 102 114 101 101 32 116 114 97 100 101 32 97 110 100 32 116 104 101 32 71 83 84 45 119 104 105 99 104 32 119 105 108 108 32 98 114 105 110 103 32 36 50 52 32 98 105 108 108 105 111 110 32 105 110 32 114 101 118 101 110 117 101 115 45 104 97 118 101 32 104 101 108 112 101 100 32 105 116 32 103 101 116 32 114 105 99 104 44 32 116 104 101 32 103 111 118 101 114 110 109 101 110 116 32 99 111 117 108 100 32 105 110 116 114 111 100 117 99 101 32 108 101 103 105 115 108 97 116 105 111 110 32 116 111 32 102 105 103 104 116 32 112 111 118 101 114 116 121 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("78 111 119 32 116 104 97 116 32 112 114 111 103 114 101 115 115 105 118 101 32 99 111 110 115 101 114 118 97 116 105 118 101 32 109 101 97 115 117 114 101 115 32 108 105 107 101 32 102 114 101 101 32 116 114 97 100 101 32 97 110 100 32 116 104 101 32 71 83 84 45 119 104 105 99 104 32 119 105 108 108 32 98 114 105 110 103 32 36 50 52 32 98 105 108 108 105 111 110 32 105 110 32 114 101 118 101 110 117 101 115 45 104 97 118 101 32 104 101 108 112 101 100 32 105 116 32 103 101 116 32 114 105 99 104 44 32 116 104 101 32 103 111 118 101 114 110 109 101 110 116 32 99 111 117 108 100 32 105 110 116 114 111 100 117 99 101 32 108 101 103 105 115 108 97 116 105 111 110 32 116 111 32 102 105 103 104 116 32 112 111 118 101 114 116 121 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Binary_XFPmRCBN():
    # {'PlainText Sentences': 'Hon.', 'Encrypted Texts': {'PlainText': 'Hon.', 'EncryptedText': '1001000 1101111 1101110 101110', 'CipherUsed': 'Binary'}}
    cfg = make_default_config("1001000 1101111 1101110 101110")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_TLrbYuNs():
    # {'PlainText Sentences': 'If federal politicians are not going to do what they say they are going to do, how is it that we can trust them to govern the country?', 'Encrypted Texts': {'PlainText': 'If federal politicians are not going to do what they say they are going to do, how is it that we can trust them to govern the country?', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_IGqduRiB():
    # {'PlainText Sentences': 'Mr. Peter MacKay:\nMr. Speaker, I thank my learned friend for the comment.', 'Encrypted Texts': {'PlainText': 'Mr. Peter MacKay:\nMr. Speaker, I thank my learned friend for the comment.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_qZFOvMQg():
    # {'PlainText Sentences': 'Paul Martin (Minister of Finance, Lib.', 'Encrypted Texts': {'PlainText': 'Paul Martin (Minister of Finance, Lib.', 'EncryptedText': b'KBQXK3BAJVQXE5DJNYQCQTLJNZUXG5DFOIQG6ZRAIZUW4YLOMNSSYICMNFRC4===', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'KBQXK3BAJVQXE5DJNYQCQTLJNZUXG5DFOIQG6ZRAIZUW4YLOMNSSYICMNFRC4==='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_euGeeGnH():
    # {'PlainText Sentences': 'I understand they are spreading across the provinces and it is into Alberta now.', 'Encrypted Texts': {'PlainText': 'I understand they are spreading across the provinces and it is into Alberta now.', 'EncryptedText': '.. \n ..- -. -.. . .-. ... - .- -. -.. \n - .... . -.-- \n .- .-. . \n ... .--. .-. . .- -.. .. -. --. \n .- -.-. .-. --- ... ... \n - .... . \n .--. .-. --- ...- .. -. -.-. . ... \n .- -. -.. \n .. - \n .. ... \n .. -. - --- \n .- .-.. -... . .-. - .- \n -. --- .-- .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".. 
 ..- -. -.. . .-. ... - .- -. -.. 
 - .... . -.-- 
 .- .-. . 
 ... .--. .-. . .- -.. .. -. --. 
 .- -.-. .-. --- ... ... 
 - .... . 
 .--. .-. --- ...- .. -. -.-. . ... 
 .- -. -.. 
 .. - 
 .. ... 
 .. -. - --- 
 .- .-.. -... . .-. - .- 
 -. --- .-- .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_CyqFzVHg():
    # {'PlainText Sentences': 'These groups include aboriginals, women and athletes with disabilities.', 'Encrypted Texts': {'PlainText': 'These groups include aboriginals, women and athletes with disabilities.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Ascii_jPreWXgt():
    # {'PlainText Sentences': "(The House adjourned at 2.17 p.m.) \nEDITED HANSARD * NUMBER 196 \nCONTENTS \nMonday, March 15, 1999 \nPOINTS OF ORDER \nTabling of Documents \nMr. Peter Adams \nPRIVATE MEMBERS' BUSINESS \nYOUNG OFFENDERS ACT \nBill C-260.", 'Encrypted Texts': {'PlainText': "(The House adjourned at 2.17 p.m.) \nEDITED HANSARD * NUMBER 196 \nCONTENTS \nMonday, March 15, 1999 \nPOINTS OF ORDER \nTabling of Documents \nMr. Peter Adams \nPRIVATE MEMBERS' BUSINESS \nYOUNG OFFENDERS ACT \nBill C-260.", 'EncryptedText': '40 84 104 101 32 72 111 117 115 101 32 97 100 106 111 117 114 110 101 100 32 97 116 32 50 46 49 55 32 112 46 109 46 41 32 10 69 68 73 84 69 68 32 72 65 78 83 65 82 68 32 42 32 78 85 77 66 69 82 32 49 57 54 32 10 67 79 78 84 69 78 84 83 32 10 77 111 110 100 97 121 44 32 77 97 114 99 104 32 49 53 44 32 49 57 57 57 32 10 80 79 73 78 84 83 32 79 70 32 79 82 68 69 82 32 10 84 97 98 108 105 110 103 32 111 102 32 68 111 99 117 109 101 110 116 115 32 10 77 114 46 32 80 101 116 101 114 32 65 100 97 109 115 32 10 80 82 73 86 65 84 69 32 77 69 77 66 69 82 83 39 32 66 85 83 73 78 69 83 83 32 10 89 79 85 78 71 32 79 70 70 69 78 68 69 82 83 32 65 67 84 32 10 66 105 108 108 32 67 45 50 54 48 46', 'CipherUsed': 'Ascii'}}
    cfg = make_default_config("40 84 104 101 32 72 111 117 115 101 32 97 100 106 111 117 114 110 101 100 32 97 116 32 50 46 49 55 32 112 46 109 46 41 32 10 69 68 73 84 69 68 32 72 65 78 83 65 82 68 32 42 32 78 85 77 66 69 82 32 49 57 54 32 10 67 79 78 84 69 78 84 83 32 10 77 111 110 100 97 121 44 32 77 97 114 99 104 32 49 53 44 32 49 57 57 57 32 10 80 79 73 78 84 83 32 79 70 32 79 82 68 69 82 32 10 84 97 98 108 105 110 103 32 111 102 32 68 111 99 117 109 101 110 116 115 32 10 77 114 46 32 80 101 116 101 114 32 65 100 97 109 115 32 10 80 82 73 86 65 84 69 32 77 69 77 66 69 82 83 39 32 66 85 83 73 78 69 83 83 32 10 89 79 85 78 71 32 79 70 70 69 78 68 69 82 83 32 65 67 84 32 10 66 105 108 108 32 67 45 50 54 48 46")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_zmhltHte():
    # {'PlainText Sentences': 'Mr. John Herron (Fundy-Royal, PC):\nMr. Speaker, it is a great opportunity to be able to question a government minister on any issue, and especially one of the importance that our farmers have been experiencing throughout the country, whether it was a commodity issue that took place last year or the farm income crisis which they have currently.', 'Encrypted Texts': {'PlainText': 'Mr. John Herron (Fundy-Royal, PC):\nMr. Speaker, it is a great opportunity to be able to question a government minister on any issue, and especially one of the importance that our farmers have been experiencing throughout the country, whether it was a commodity issue that took place last year or the farm income crisis which they have currently.', 'EncryptedText': '-- .-. .-.-.- \n .--- --- .... -. \n .... . .-. .-. --- -. \n -.--. ..-. ..- -. -.. -.-- -....- .-. --- -.-- .- .-.. --..-- \n .--. -.-. -.--.- ---...  -- .-. .-.-.- \n ... .--. . .- -.- . .-. --..-- \n .. - \n .. ... \n .- \n --. .-. . .- - \n --- .--. .--. --- .-. - ..- -. .. - -.-- \n - --- \n -... . \n .- -... .-.. . \n - --- \n --.- ..- . ... - .. --- -. \n .- \n --. --- ...- . .-. -. -- . -. - \n -- .. -. .. ... - . .-. \n --- -. \n .- -. -.-- \n .. ... ... ..- . --..-- \n .- -. -.. \n . ... .--. . -.-. .. .- .-.. .-.. -.-- \n --- -. . \n --- ..-. \n - .... . \n .. -- .--. --- .-. - .- -. -.-. . \n - .... .- - \n --- ..- .-. \n ..-. .- .-. -- . .-. ... \n .... .- ...- . \n -... . . -. \n . -..- .--. . .-. .. . -. -.-. .. -. --. \n - .... .-. --- ..- --. .... --- ..- - \n - .... . \n -.-. --- ..- -. - .-. -.-- --..-- \n .-- .... . - .... . .-. \n .. - \n .-- .- ... \n .- \n -.-. --- -- -- --- -.. .. - -.-- \n .. ... ... ..- . \n - .... .- - \n - --- --- -.- \n .--. .-.. .- -.-. . \n .-.. .- ... - \n -.-- . .- .-. \n --- .-. \n - .... . \n ..-. .- .-. -- \n .. -. -.-. --- -- . \n -.-. .-. .. ... .. ... \n .-- .... .. -.-. .... \n - .... . -.-- \n .... .- ...- . \n -.-. ..- .-. .-. . -. - .-.. -.-- .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config("-- .-. .-.-.- 
 .--- --- .... -. 
 .... . .-. .-. --- -. 
 -.--. ..-. ..- -. -.. -.-- -....- .-. --- -.-- .- .-.. --..-- 
 .--. -.-. -.--.- ---...  -- .-. .-.-.- 
 ... .--. . .- -.- . .-. --..-- 
 .. - 
 .. ... 
 .- 
 --. .-. . .- - 
 --- .--. .--. --- .-. - ..- -. .. - -.-- 
 - --- 
 -... . 
 .- -... .-.. . 
 - --- 
 --.- ..- . ... - .. --- -. 
 .- 
 --. --- ...- . .-. -. -- . -. - 
 -- .. -. .. ... - . .-. 
 --- -. 
 .- -. -.-- 
 .. ... ... ..- . --..-- 
 .- -. -.. 
 . ... .--. . -.-. .. .- .-.. .-.. -.-- 
 --- -. . 
 --- ..-. 
 - .... . 
 .. -- .--. --- .-. - .- -. -.-. . 
 - .... .- - 
 --- ..- .-. 
 ..-. .- .-. -- . .-. ... 
 .... .- ...- . 
 -... . . -. 
 . -..- .--. . .-. .. . -. -.-. .. -. --. 
 - .... .-. --- ..- --. .... --- ..- - 
 - .... . 
 -.-. --- ..- -. - .-. -.-- --..-- 
 .-- .... . - .... . .-. 
 .. - 
 .-- .- ... 
 .- 
 -.-. --- -- -- --- -.. .. - -.-- 
 .. ... ... ..- . 
 - .... .- - 
 - --- --- -.- 
 .--. .-.. .- -.-. . 
 .-.. .- ... - 
 -.-- . .- .-. 
 --- .-. 
 - .... . 
 ..-. .- .-. -- 
 .. -. -.-. --- -- . 
 -.-. .-. .. ... .. ... 
 .-- .... .. -.-. .... 
 - .... . -.-- 
 .... .- ...- . 
 -.-. ..- .-. .-. . -. - .-.. -.-- .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_OlUStuJZ():
    # {'PlainText Sentences': 'The regulatory framework for private pension plans should not impose undue costs on existing plans or unduly inhibit the creation of new pension plans.', 'Encrypted Texts': {'PlainText': 'The regulatory framework for private pension plans should not impose undue costs on existing plans or unduly inhibit the creation of new pension plans.', 'EncryptedText': '.snalp noisnep wen fo noitaerc eht tibihni yludnu ro snalp gnitsixe no stsoc eudnu esopmi ton dluohs snalp noisnep etavirp rof krowemarf yrotaluger ehT', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".snalp noisnep wen fo noitaerc eht tibihni yludnu ro snalp gnitsixe no stsoc eudnu esopmi ton dluohs snalp noisnep etavirp rof krowemarf yrotaluger ehT")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_nPuEGtDh():
    # {'PlainText Sentences': 'Three, the committee recommended that Canada withdraw its support for the redfish quotas given to foreign nations.', 'Encrypted Texts': {'PlainText': 'Three, the committee recommended that Canada withdraw its support for the redfish quotas given to foreign nations.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_MorseCode_LddIiEcO():
    # {'PlainText Sentences': 'He is of no comfort to native families who are now facing unfair recriminations from their neighbours.', 'Encrypted Texts': {'PlainText': 'He is of no comfort to native families who are now facing unfair recriminations from their neighbours.', 'EncryptedText': '.... . \n .. ... \n --- ..-. \n -. --- \n -.-. --- -- ..-. --- .-. - \n - --- \n -. .- - .. ...- . \n ..-. .- -- .. .-.. .. . ... \n .-- .... --- \n .- .-. . \n -. --- .-- \n ..-. .- -.-. .. -. --. \n ..- -. ..-. .- .. .-. \n .-. . -.-. .-. .. -- .. -. .- - .. --- -. ... \n ..-. .-. --- -- \n - .... . .. .-. \n -. . .. --. .... -... --- ..- .-. ... .-.-.-', 'CipherUsed': 'MorseCode'}}
    cfg = make_default_config(".... . 
 .. ... 
 --- ..-. 
 -. --- 
 -.-. --- -- ..-. --- .-. - 
 - --- 
 -. .- - .. ...- . 
 ..-. .- -- .. .-.. .. . ... 
 .-- .... --- 
 .- .-. . 
 -. --- .-- 
 ..-. .- -.-. .. -. --. 
 ..- -. ..-. .- .. .-. 
 .-. . -.-. .-. .. -- .. -. .- - .. --- -. ... 
 ..-. .-. --- -- 
 - .... . .. .-. 
 -. . .. --. .... -... --- ..- .-. ... .-.-.-")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_sRqZWqcc():
    # {'PlainText Sentences': 'Those least affected, such as Canada, signed the Ottawa agreement.', 'Encrypted Texts': {'PlainText': 'Those least affected, such as Canada, signed the Ottawa agreement.', 'EncryptedText': b'54686F7365206C656173742061666665637465642C20737563682061732043616E6164612C207369676E656420746865204F74746177612061677265656D656E742E', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'54686F7365206C656173742061666665637465642C20737563682061732043616E6164612C207369676E656420746865204F74746177612061677265656D656E742E'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_wuEfMTpT():
    # {'PlainText Sentences': 'Mr. Garry Breitkreuz:\nMr. Speaker, the member makes an excellent point.', 'Encrypted Texts': {'PlainText': 'Mr. Garry Breitkreuz:\nMr. Speaker, the member makes an excellent point.', 'EncryptedText': b'JVZC4ICHMFZHE6JAIJZGK2LUNNZGK5L2HIFE24ROEBJXAZLBNNSXELBAORUGKIDNMVWWEZLSEBWWC23FOMQGC3RAMV4GGZLMNRSW45BAOBXWS3TUFY======', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'JVZC4ICHMFZHE6JAIJZGK2LUNNZGK5L2HIFE24ROEBJXAZLBNNSXELBAORUGKIDNMVWWEZLSEBWWC23FOMQGC3RAMV4GGZLMNRSW45BAOBXWS3TUFY======'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_RpmnxZha():
    # {'PlainText Sentences': 'In other words, dead weeks or small earning weeks were being folded into the package which brought down the average.', 'Encrypted Texts': {'PlainText': 'In other words, dead weeks or small earning weeks were being folded into the package which brought down the average.', 'EncryptedText': b'JFXCA33UNBSXEIDXN5ZGI4ZMEBSGKYLEEB3WKZLLOMQG64RAONWWC3DMEBSWC4TONFXGOIDXMVSWW4ZAO5SXEZJAMJSWS3THEBTG63DEMVSCA2LOORXSA5DIMUQHAYLDNNQWOZJAO5UGSY3IEBRHE33VM5UHIIDEN53W4IDUNBSSAYLWMVZGCZ3FFY======', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'JFXCA33UNBSXEIDXN5ZGI4ZMEBSGKYLEEB3WKZLLOMQG64RAONWWC3DMEBSWC4TONFXGOIDXMVSWW4ZAO5SXEZJAMJSWS3THEBTG63DEMVSCA2LOORXSA5DIMUQHAYLDNNQWOZJAO5UGSY3IEBRHE33VM5UHIIDEN53W4IDUNBSSAYLWMVZGCZ3FFY======'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Reverse_fvxulHWn():
    # {'PlainText Sentences': 'Members of visible minorities represent only a small proportion of upper level management positions.', 'Encrypted Texts': {'PlainText': 'Members of visible minorities represent only a small proportion of upper level management positions.', 'EncryptedText': '.snoitisop tnemeganam level reppu fo noitroporp llams a ylno tneserper seitironim elbisiv fo srebmeM', 'CipherUsed': 'Reverse'}}
    cfg = make_default_config(".snoitisop tnemeganam level reppu fo noitroporp llams a ylno tneserper seitironim elbisiv fo srebmeM")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_xBmsMrSe():
    # {'PlainText Sentences': 'In fact, since 1991 we have been involved in the efforts by the international community to put an end to the violence and the taking of innocent lives, and to restore peace to this region, within either the UN or NATO.', 'Encrypted Texts': {'PlainText': 'In fact, since 1991 we have been involved in the efforts by the international community to put an end to the violence and the taking of innocent lives, and to restore peace to this region, within either the UN or NATO.', 'EncryptedText': b'JFXCAZTBMN2CYIDTNFXGGZJAGE4TSMJAO5SSA2DBOZSSAYTFMVXCA2LOOZXWY5TFMQQGS3RAORUGKIDFMZTG64TUOMQGE6JAORUGKIDJNZ2GK4TOMF2GS33OMFWCAY3PNVWXK3TJOR4SA5DPEBYHK5BAMFXCAZLOMQQHI3ZAORUGKIDWNFXWYZLOMNSSAYLOMQQHI2DFEB2GC23JNZTSA33GEBUW43TPMNSW45BANRUXMZLTFQQGC3TEEB2G6IDSMVZXI33SMUQHAZLBMNSSA5DPEB2GQ2LTEBZGKZ3JN5XCYIDXNF2GQ2LOEBSWS5DIMVZCA5DIMUQFKTRAN5ZCATSBKRHS4===', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'JFXCAZTBMN2CYIDTNFXGGZJAGE4TSMJAO5SSA2DBOZSSAYTFMVXCA2LOOZXWY5TFMQQGS3RAORUGKIDFMZTG64TUOMQGE6JAORUGKIDJNZ2GK4TOMF2GS33OMFWCAY3PNVWXK3TJOR4SA5DPEBYHK5BAMFXCAZLOMQQHI3ZAORUGKIDWNFXWYZLOMNSSAYLOMQQHI2DFEB2GC23JNZTSA33GEBUW43TPMNSW45BANRUXMZLTFQQGC3TEEB2G6IDSMVZXI33SMUQHAZLBMNSSA5DPEB2GQ2LTEBZGKZ3JN5XCYIDXNF2GQ2LOEBSWS5DIMVZCA5DIMUQFKTRAN5ZCATSBKRHS4==='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base16_YhdxccbQ():
    # {'PlainText Sentences': 'My hon.', 'Encrypted Texts': {'PlainText': 'My hon.', 'EncryptedText': b'4D7920686F6E2E', 'CipherUsed': 'Base16'}}
    cfg = make_default_config("b'4D7920686F6E2E'")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Vigenere_sKDdoOOP():
    # {'PlainText Sentences': 'The Chair is very interested in this debate too.', 'Encrypted Texts': {'PlainText': 'The Chair is very interested in this debate too.', 'EncryptedText': None, 'CipherUsed': 'Vigenere'}}
    cfg = make_default_config("None")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 

def test_Base32_FhubZqkA():
    # {'PlainText Sentences': 'Why I am not sure.', 'Encrypted Texts': {'PlainText': 'Why I am not sure.', 'EncryptedText': b'K5UHSICJEBQW2IDON52CA43VOJSS4===', 'CipherUsed': 'Base32'}}
    cfg = make_default_config("b'K5UHSICJEBQW2IDON52CA43VOJSS4==='")
    cfg["debug"] = "TRACE"
    result = main(cfg)

    assert result["IsPlaintext?"] == True 
