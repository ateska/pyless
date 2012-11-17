# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 lesscss.g 2012-11-17 00:46:29

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
FUNCTION=38
STAR=33
N_Selectors=11
EOF=-1
MEDIA_SYM=20
INCLUDES=35
LBRACKET=32
RPAREN=39
NAME=56
GREATER=29
ESCAPE=53
DIMENSION=90
STRINGESC=88
NL=91
COMMENT=84
N_Media=9
D=61
E=62
F=63
G=64
A=58
RBRACE=22
B=59
C=60
L=69
IMPORT_SYM=17
NMCHAR=55
M=70
N=71
O=72
H=65
I=66
J=67
NUMBER=42
K=68
U=78
T=77
W=80
V=79
Q=74
P=73
S=76
R=75
CDO=85
CDC=86
PERCENTAGE=43
URL=57
Y=82
X=81
URI=19
Z=83
PAGE_SYM=25
WS=89
DASHMATCH=36
EMS=45
N_RuleSet=10
NONASCII=51
N_Page=8
N_Declarations=12
LBRACE=21
N_Import=6
LENGTH=44
LPAREN=87
IMPORTANT_SYM=40
TIME=48
COMMA=18
N_StyleSheet=4
IDENT=23
PLUS=28
FREQ=49
RBRACKET=37
DOT=31
CHARSET_SYM=14
ANGLE=47
HASH=30
HEXCHAR=50
N_CharSet=5
MINUS=27
SOLIDUS=41
SEMI=16
UNICODE=52
COLON=26
NMSTART=54
N_Declaration=13
OPEQ=34
FONTFACE_SYM=24
EXS=46
N_FontFace=7
STRING=15

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "N_StyleSheet", "N_CharSet", "N_Import", "N_FontFace", "N_Page", "N_Media", 
    "N_RuleSet", "N_Selectors", "N_Declarations", "N_Declaration", "CHARSET_SYM", 
    "STRING", "SEMI", "IMPORT_SYM", "COMMA", "URI", "MEDIA_SYM", "LBRACE", 
    "RBRACE", "IDENT", "FONTFACE_SYM", "PAGE_SYM", "COLON", "MINUS", "PLUS", 
    "GREATER", "HASH", "DOT", "LBRACKET", "STAR", "OPEQ", "INCLUDES", "DASHMATCH", 
    "RBRACKET", "FUNCTION", "RPAREN", "IMPORTANT_SYM", "SOLIDUS", "NUMBER", 
    "PERCENTAGE", "LENGTH", "EMS", "EXS", "ANGLE", "TIME", "FREQ", "HEXCHAR", 
    "NONASCII", "UNICODE", "ESCAPE", "NMSTART", "NMCHAR", "NAME", "URL", 
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "COMMENT", 
    "CDO", "CDC", "LPAREN", "STRINGESC", "WS", "DIMENSION", "NL"
]




class lesscssParser(Parser):
    grammarFileName = "lesscss.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(lesscssParser, self).__init__(input, state, *args, **kwargs)

        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )

        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class styleSheet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.styleSheet_return, self).__init__()

            self.tree = None




    # $ANTLR start "styleSheet"
    # lesscss.g:48:1: styleSheet : ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* bodylist ) ;
    def styleSheet(self, ):

        retval = self.styleSheet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF4 = None
        charSet1 = None

        imports2 = None

        bodylist3 = None


        EOF4_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_bodylist = RewriteRuleSubtreeStream(self._adaptor, "rule bodylist")
        stream_charSet = RewriteRuleSubtreeStream(self._adaptor, "rule charSet")
        stream_imports = RewriteRuleSubtreeStream(self._adaptor, "rule imports")
        try:
            try:
                # lesscss.g:49:5: ( ( charSet )? ( imports )* bodylist EOF -> ^( N_StyleSheet ( charSet )? ( imports )* bodylist ) )
                # lesscss.g:49:9: ( charSet )? ( imports )* bodylist EOF
                pass 
                # lesscss.g:49:9: ( charSet )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == CHARSET_SYM) :
                    alt1 = 1
                if alt1 == 1:
                    # lesscss.g:49:9: charSet
                    pass 
                    self._state.following.append(self.FOLLOW_charSet_in_styleSheet149)
                    charSet1 = self.charSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_charSet.add(charSet1.tree)



                # lesscss.g:50:9: ( imports )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == IMPORT_SYM) :
                        alt2 = 1


                    if alt2 == 1:
                        # lesscss.g:50:9: imports
                        pass 
                        self._state.following.append(self.FOLLOW_imports_in_styleSheet160)
                        imports2 = self.imports()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_imports.add(imports2.tree)


                    else:
                        break #loop2
                self._state.following.append(self.FOLLOW_bodylist_in_styleSheet171)
                bodylist3 = self.bodylist()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_bodylist.add(bodylist3.tree)
                EOF4=self.match(self.input, EOF, self.FOLLOW_EOF_in_styleSheet181) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF4)

                # AST Rewrite
                # elements: bodylist, imports, charSet
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 53:13: -> ^( N_StyleSheet ( charSet )? ( imports )* bodylist )
                    # lesscss.g:53:16: ^( N_StyleSheet ( charSet )? ( imports )* bodylist )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_StyleSheet, "N_StyleSheet"), root_1)

                    # lesscss.g:53:31: ( charSet )?
                    if stream_charSet.hasNext():
                        self._adaptor.addChild(root_1, stream_charSet.nextTree())


                    stream_charSet.reset();
                    # lesscss.g:53:40: ( imports )*
                    while stream_imports.hasNext():
                        self._adaptor.addChild(root_1, stream_imports.nextTree())


                    stream_imports.reset();
                    self._adaptor.addChild(root_1, stream_bodylist.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "styleSheet"

    class charSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.charSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "charSet"
    # lesscss.g:60:1: charSet : CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) ;
    def charSet(self, ):

        retval = self.charSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CHARSET_SYM5 = None
        STRING6 = None
        SEMI7 = None

        CHARSET_SYM5_tree = None
        STRING6_tree = None
        SEMI7_tree = None
        stream_CHARSET_SYM = RewriteRuleTokenStream(self._adaptor, "token CHARSET_SYM")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_STRING = RewriteRuleTokenStream(self._adaptor, "token STRING")

        try:
            try:
                # lesscss.g:61:5: ( CHARSET_SYM STRING SEMI -> ^( N_CharSet STRING ) )
                # lesscss.g:61:9: CHARSET_SYM STRING SEMI
                pass 
                CHARSET_SYM5=self.match(self.input, CHARSET_SYM, self.FOLLOW_CHARSET_SYM_in_charSet234) 
                if self._state.backtracking == 0:
                    stream_CHARSET_SYM.add(CHARSET_SYM5)
                STRING6=self.match(self.input, STRING, self.FOLLOW_STRING_in_charSet236) 
                if self._state.backtracking == 0:
                    stream_STRING.add(STRING6)
                SEMI7=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_charSet238) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI7)

                # AST Rewrite
                # elements: STRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 62:9: -> ^( N_CharSet STRING )
                    # lesscss.g:62:12: ^( N_CharSet STRING )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_CharSet, "N_CharSet"), root_1)

                    self._adaptor.addChild(root_1, stream_STRING.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "charSet"

    class imports_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.imports_return, self).__init__()

            self.tree = None




    # $ANTLR start "imports"
    # lesscss.g:69:1: imports : IMPORT_SYM importUrl ( medium ( COMMA medium )* )? SEMI -> ^( N_Import importUrl ( medium )* ) ;
    def imports(self, ):

        retval = self.imports_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT_SYM8 = None
        COMMA11 = None
        SEMI13 = None
        importUrl9 = None

        medium10 = None

        medium12 = None


        IMPORT_SYM8_tree = None
        COMMA11_tree = None
        SEMI13_tree = None
        stream_IMPORT_SYM = RewriteRuleTokenStream(self._adaptor, "token IMPORT_SYM")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_importUrl = RewriteRuleSubtreeStream(self._adaptor, "rule importUrl")
        stream_medium = RewriteRuleSubtreeStream(self._adaptor, "rule medium")
        try:
            try:
                # lesscss.g:70:5: ( IMPORT_SYM importUrl ( medium ( COMMA medium )* )? SEMI -> ^( N_Import importUrl ( medium )* ) )
                # lesscss.g:70:9: IMPORT_SYM importUrl ( medium ( COMMA medium )* )? SEMI
                pass 
                IMPORT_SYM8=self.match(self.input, IMPORT_SYM, self.FOLLOW_IMPORT_SYM_in_imports277) 
                if self._state.backtracking == 0:
                    stream_IMPORT_SYM.add(IMPORT_SYM8)
                self._state.following.append(self.FOLLOW_importUrl_in_imports279)
                importUrl9 = self.importUrl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_importUrl.add(importUrl9.tree)
                # lesscss.g:70:30: ( medium ( COMMA medium )* )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENT) :
                    alt4 = 1
                if alt4 == 1:
                    # lesscss.g:70:31: medium ( COMMA medium )*
                    pass 
                    self._state.following.append(self.FOLLOW_medium_in_imports282)
                    medium10 = self.medium()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_medium.add(medium10.tree)
                    # lesscss.g:70:38: ( COMMA medium )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == COMMA) :
                            alt3 = 1


                        if alt3 == 1:
                            # lesscss.g:70:39: COMMA medium
                            pass 
                            COMMA11=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_imports285) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA11)
                            self._state.following.append(self.FOLLOW_medium_in_imports287)
                            medium12 = self.medium()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_medium.add(medium12.tree)


                        else:
                            break #loop3



                SEMI13=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_imports293) 
                if self._state.backtracking == 0:
                    stream_SEMI.add(SEMI13)

                # AST Rewrite
                # elements: importUrl, medium
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 71:9: -> ^( N_Import importUrl ( medium )* )
                    # lesscss.g:71:12: ^( N_Import importUrl ( medium )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Import, "N_Import"), root_1)

                    self._adaptor.addChild(root_1, stream_importUrl.nextTree())
                    # lesscss.g:71:33: ( medium )*
                    while stream_medium.hasNext():
                        self._adaptor.addChild(root_1, stream_medium.nextTree())


                    stream_medium.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "imports"

    class importUrl_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.importUrl_return, self).__init__()

            self.tree = None




    # $ANTLR start "importUrl"
    # lesscss.g:75:1: importUrl : ( STRING | URI );
    def importUrl(self, ):

        retval = self.importUrl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set14 = None

        set14_tree = None

        try:
            try:
                # lesscss.g:76:5: ( STRING | URI )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set14 = self.input.LT(1)
                if self.input.LA(1) == STRING or self.input.LA(1) == URI:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set14))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "importUrl"

    class media_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.media_return, self).__init__()

            self.tree = None




    # $ANTLR start "media"
    # lesscss.g:85:1: media : MEDIA_SYM medium ( COMMA medium )* LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( medium )+ ( ruleSet )* ) ;
    def media(self, ):

        retval = self.media_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MEDIA_SYM15 = None
        COMMA17 = None
        LBRACE19 = None
        RBRACE21 = None
        medium16 = None

        medium18 = None

        ruleSet20 = None


        MEDIA_SYM15_tree = None
        COMMA17_tree = None
        LBRACE19_tree = None
        RBRACE21_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_MEDIA_SYM = RewriteRuleTokenStream(self._adaptor, "token MEDIA_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_medium = RewriteRuleSubtreeStream(self._adaptor, "rule medium")
        stream_ruleSet = RewriteRuleSubtreeStream(self._adaptor, "rule ruleSet")
        try:
            try:
                # lesscss.g:86:5: ( MEDIA_SYM medium ( COMMA medium )* LBRACE ( ruleSet )* RBRACE -> ^( N_Media ( medium )+ ( ruleSet )* ) )
                # lesscss.g:86:7: MEDIA_SYM medium ( COMMA medium )* LBRACE ( ruleSet )* RBRACE
                pass 
                MEDIA_SYM15=self.match(self.input, MEDIA_SYM, self.FOLLOW_MEDIA_SYM_in_media360) 
                if self._state.backtracking == 0:
                    stream_MEDIA_SYM.add(MEDIA_SYM15)
                self._state.following.append(self.FOLLOW_medium_in_media362)
                medium16 = self.medium()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_medium.add(medium16.tree)
                # lesscss.g:86:24: ( COMMA medium )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == COMMA) :
                        alt5 = 1


                    if alt5 == 1:
                        # lesscss.g:86:25: COMMA medium
                        pass 
                        COMMA17=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_media365) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA17)
                        self._state.following.append(self.FOLLOW_medium_in_media367)
                        medium18 = self.medium()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_medium.add(medium18.tree)


                    else:
                        break #loop5
                LBRACE19=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_media379) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE19)
                # lesscss.g:88:13: ( ruleSet )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == IDENT or LA6_0 == COLON or (HASH <= LA6_0 <= STAR)) :
                        alt6 = 1


                    if alt6 == 1:
                        # lesscss.g:88:13: ruleSet
                        pass 
                        self._state.following.append(self.FOLLOW_ruleSet_in_media393)
                        ruleSet20 = self.ruleSet()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_ruleSet.add(ruleSet20.tree)


                    else:
                        break #loop6
                RBRACE21=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_media404) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE21)

                # AST Rewrite
                # elements: medium, ruleSet
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 90:9: -> ^( N_Media ( medium )+ ( ruleSet )* )
                    # lesscss.g:90:12: ^( N_Media ( medium )+ ( ruleSet )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Media, "N_Media"), root_1)

                    # lesscss.g:90:22: ( medium )+
                    if not (stream_medium.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_medium.hasNext():
                        self._adaptor.addChild(root_1, stream_medium.nextTree())


                    stream_medium.reset()
                    # lesscss.g:90:30: ( ruleSet )*
                    while stream_ruleSet.hasNext():
                        self._adaptor.addChild(root_1, stream_ruleSet.nextTree())


                    stream_ruleSet.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "media"

    class medium_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.medium_return, self).__init__()

            self.tree = None




    # $ANTLR start "medium"
    # lesscss.g:97:1: medium : IDENT ;
    def medium(self, ):

        retval = self.medium_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT22 = None

        IDENT22_tree = None

        try:
            try:
                # lesscss.g:98:5: ( IDENT )
                # lesscss.g:98:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT22=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_medium445)
                if self._state.backtracking == 0:

                    IDENT22_tree = self._adaptor.createWithPayload(IDENT22)
                    self._adaptor.addChild(root_0, IDENT22_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "medium"

    class fontface_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fontface_return, self).__init__()

            self.tree = None




    # $ANTLR start "fontface"
    # lesscss.g:105:1: fontface : FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) ;
    def fontface(self, ):

        retval = self.fontface_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FONTFACE_SYM23 = None
        LBRACE24 = None
        RBRACE26 = None
        declarationset25 = None


        FONTFACE_SYM23_tree = None
        LBRACE24_tree = None
        RBRACE26_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_FONTFACE_SYM = RewriteRuleTokenStream(self._adaptor, "token FONTFACE_SYM")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:106:5: ( FONTFACE_SYM LBRACE declarationset RBRACE -> ^( N_FontFace declarationset ) )
                # lesscss.g:106:7: FONTFACE_SYM LBRACE declarationset RBRACE
                pass 
                FONTFACE_SYM23=self.match(self.input, FONTFACE_SYM, self.FOLLOW_FONTFACE_SYM_in_fontface467) 
                if self._state.backtracking == 0:
                    stream_FONTFACE_SYM.add(FONTFACE_SYM23)
                LBRACE24=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_fontface469) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE24)
                self._state.following.append(self.FOLLOW_declarationset_in_fontface471)
                declarationset25 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset25.tree)
                RBRACE26=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_fontface473) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE26)

                # AST Rewrite
                # elements: declarationset
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 107:9: -> ^( N_FontFace declarationset )
                    # lesscss.g:107:12: ^( N_FontFace declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_FontFace, "N_FontFace"), root_1)

                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fontface"

    class bodylist_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodylist_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodylist"
    # lesscss.g:111:1: bodylist : ( bodyset )* ;
    def bodylist(self, ):

        retval = self.bodylist_return()
        retval.start = self.input.LT(1)

        root_0 = None

        bodyset27 = None



        try:
            try:
                # lesscss.g:112:5: ( ( bodyset )* )
                # lesscss.g:112:7: ( bodyset )*
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:112:7: ( bodyset )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == MEDIA_SYM or (IDENT <= LA7_0 <= COLON) or (HASH <= LA7_0 <= STAR)) :
                        alt7 = 1


                    if alt7 == 1:
                        # lesscss.g:112:7: bodyset
                        pass 
                        self._state.following.append(self.FOLLOW_bodyset_in_bodylist511)
                        bodyset27 = self.bodyset()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bodyset27.tree)


                    else:
                        break #loop7



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bodylist"

    class bodyset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.bodyset_return, self).__init__()

            self.tree = None




    # $ANTLR start "bodyset"
    # lesscss.g:116:1: bodyset : ( ruleSet | media | page | fontface );
    def bodyset(self, ):

        retval = self.bodyset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ruleSet28 = None

        media29 = None

        page30 = None

        fontface31 = None



        try:
            try:
                # lesscss.g:117:5: ( ruleSet | media | page | fontface )
                alt8 = 4
                LA8 = self.input.LA(1)
                if LA8 == IDENT or LA8 == COLON or LA8 == HASH or LA8 == DOT or LA8 == LBRACKET or LA8 == STAR:
                    alt8 = 1
                elif LA8 == MEDIA_SYM:
                    alt8 = 2
                elif LA8 == PAGE_SYM:
                    alt8 = 3
                elif LA8 == FONTFACE_SYM:
                    alt8 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # lesscss.g:117:7: ruleSet
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_ruleSet_in_bodyset530)
                    ruleSet28 = self.ruleSet()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, ruleSet28.tree)


                elif alt8 == 2:
                    # lesscss.g:118:7: media
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_media_in_bodyset538)
                    media29 = self.media()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, media29.tree)


                elif alt8 == 3:
                    # lesscss.g:119:7: page
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_page_in_bodyset546)
                    page30 = self.page()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, page30.tree)


                elif alt8 == 4:
                    # lesscss.g:120:7: fontface
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fontface_in_bodyset554)
                    fontface31 = self.fontface()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fontface31.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bodyset"

    class page_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.page_return, self).__init__()

            self.tree = None




    # $ANTLR start "page"
    # lesscss.g:124:1: page : PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) ;
    def page(self, ):

        retval = self.page_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PAGE_SYM32 = None
        LBRACE34 = None
        RBRACE36 = None
        pseudoPage33 = None

        declarationset35 = None


        PAGE_SYM32_tree = None
        LBRACE34_tree = None
        RBRACE36_tree = None
        stream_PAGE_SYM = RewriteRuleTokenStream(self._adaptor, "token PAGE_SYM")
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        stream_pseudoPage = RewriteRuleSubtreeStream(self._adaptor, "rule pseudoPage")
        try:
            try:
                # lesscss.g:125:5: ( PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE -> ^( N_Page ( pseudoPage )? declarationset ) )
                # lesscss.g:125:7: PAGE_SYM ( pseudoPage )? LBRACE declarationset RBRACE
                pass 
                PAGE_SYM32=self.match(self.input, PAGE_SYM, self.FOLLOW_PAGE_SYM_in_page575) 
                if self._state.backtracking == 0:
                    stream_PAGE_SYM.add(PAGE_SYM32)
                # lesscss.g:125:16: ( pseudoPage )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == COLON) :
                    alt9 = 1
                if alt9 == 1:
                    # lesscss.g:125:16: pseudoPage
                    pass 
                    self._state.following.append(self.FOLLOW_pseudoPage_in_page577)
                    pseudoPage33 = self.pseudoPage()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_pseudoPage.add(pseudoPage33.tree)



                LBRACE34=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_page580) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE34)
                self._state.following.append(self.FOLLOW_declarationset_in_page582)
                declarationset35 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset35.tree)
                RBRACE36=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_page584) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE36)

                # AST Rewrite
                # elements: pseudoPage, declarationset
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 126:9: -> ^( N_Page ( pseudoPage )? declarationset )
                    # lesscss.g:126:12: ^( N_Page ( pseudoPage )? declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Page, "N_Page"), root_1)

                    # lesscss.g:126:21: ( pseudoPage )?
                    if stream_pseudoPage.hasNext():
                        self._adaptor.addChild(root_1, stream_pseudoPage.nextTree())


                    stream_pseudoPage.reset();
                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "page"

    class pseudoPage_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudoPage_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudoPage"
    # lesscss.g:130:1: pseudoPage : COLON IDENT -> IDENT ;
    def pseudoPage(self, ):

        retval = self.pseudoPage_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON37 = None
        IDENT38 = None

        COLON37_tree = None
        IDENT38_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")

        try:
            try:
                # lesscss.g:131:5: ( COLON IDENT -> IDENT )
                # lesscss.g:131:7: COLON IDENT
                pass 
                COLON37=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudoPage621) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON37)
                IDENT38=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudoPage623) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(IDENT38)

                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 131:19: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudoPage"

    class unaryOperator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.unaryOperator_return, self).__init__()

            self.tree = None




    # $ANTLR start "unaryOperator"
    # lesscss.g:134:1: unaryOperator : ( MINUS | PLUS );
    def unaryOperator(self, ):

        retval = self.unaryOperator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set39 = None

        set39_tree = None

        try:
            try:
                # lesscss.g:135:5: ( MINUS | PLUS )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set39 = self.input.LT(1)
                if (MINUS <= self.input.LA(1) <= PLUS):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set39))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "unaryOperator"

    class property_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.property_return, self).__init__()

            self.tree = None




    # $ANTLR start "property"
    # lesscss.g:140:1: property : IDENT ;
    def property(self, ):

        retval = self.property_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT40 = None

        IDENT40_tree = None

        try:
            try:
                # lesscss.g:141:5: ( IDENT )
                # lesscss.g:141:7: IDENT
                pass 
                root_0 = self._adaptor.nil()

                IDENT40=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_property676)
                if self._state.backtracking == 0:

                    IDENT40_tree = self._adaptor.createWithPayload(IDENT40)
                    self._adaptor.addChild(root_0, IDENT40_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "property"

    class ruleSet_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.ruleSet_return, self).__init__()

            self.tree = None




    # $ANTLR start "ruleSet"
    # lesscss.g:145:1: ruleSet : selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ^( N_Selectors ( selector )+ ) declarationset ) ;
    def ruleSet(self, ):

        retval = self.ruleSet_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA42 = None
        LBRACE44 = None
        RBRACE46 = None
        selector41 = None

        selector43 = None

        declarationset45 = None


        COMMA42_tree = None
        LBRACE44_tree = None
        RBRACE46_tree = None
        stream_RBRACE = RewriteRuleTokenStream(self._adaptor, "token RBRACE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LBRACE = RewriteRuleTokenStream(self._adaptor, "token LBRACE")
        stream_selector = RewriteRuleSubtreeStream(self._adaptor, "rule selector")
        stream_declarationset = RewriteRuleSubtreeStream(self._adaptor, "rule declarationset")
        try:
            try:
                # lesscss.g:146:5: ( selector ( COMMA selector )* LBRACE declarationset RBRACE -> ^( N_RuleSet ^( N_Selectors ( selector )+ ) declarationset ) )
                # lesscss.g:146:7: selector ( COMMA selector )* LBRACE declarationset RBRACE
                pass 
                self._state.following.append(self.FOLLOW_selector_in_ruleSet694)
                selector41 = self.selector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_selector.add(selector41.tree)
                # lesscss.g:146:16: ( COMMA selector )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == COMMA) :
                        alt10 = 1


                    if alt10 == 1:
                        # lesscss.g:146:17: COMMA selector
                        pass 
                        COMMA42=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_ruleSet697) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA42)
                        self._state.following.append(self.FOLLOW_selector_in_ruleSet699)
                        selector43 = self.selector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_selector.add(selector43.tree)


                    else:
                        break #loop10
                LBRACE44=self.match(self.input, LBRACE, self.FOLLOW_LBRACE_in_ruleSet703) 
                if self._state.backtracking == 0:
                    stream_LBRACE.add(LBRACE44)
                self._state.following.append(self.FOLLOW_declarationset_in_ruleSet705)
                declarationset45 = self.declarationset()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declarationset.add(declarationset45.tree)
                RBRACE46=self.match(self.input, RBRACE, self.FOLLOW_RBRACE_in_ruleSet707) 
                if self._state.backtracking == 0:
                    stream_RBRACE.add(RBRACE46)

                # AST Rewrite
                # elements: declarationset, selector
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 147:9: -> ^( N_RuleSet ^( N_Selectors ( selector )+ ) declarationset )
                    # lesscss.g:147:12: ^( N_RuleSet ^( N_Selectors ( selector )+ ) declarationset )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_RuleSet, "N_RuleSet"), root_1)

                    # lesscss.g:147:24: ^( N_Selectors ( selector )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Selectors, "N_Selectors"), root_2)

                    # lesscss.g:147:38: ( selector )+
                    if not (stream_selector.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_selector.hasNext():
                        self._adaptor.addChild(root_2, stream_selector.nextTree())


                    stream_selector.reset()

                    self._adaptor.addChild(root_1, root_2)
                    self._adaptor.addChild(root_1, stream_declarationset.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "ruleSet"

    class selector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.selector_return, self).__init__()

            self.tree = None




    # $ANTLR start "selector"
    # lesscss.g:150:1: selector : simpleSelector ( combinator simpleSelector )* ;
    def selector(self, ):

        retval = self.selector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simpleSelector47 = None

        combinator48 = None

        simpleSelector49 = None



        try:
            try:
                # lesscss.g:151:5: ( simpleSelector ( combinator simpleSelector )* )
                # lesscss.g:151:7: simpleSelector ( combinator simpleSelector )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_simpleSelector_in_selector747)
                simpleSelector47 = self.simpleSelector()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, simpleSelector47.tree)
                # lesscss.g:151:22: ( combinator simpleSelector )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == IDENT or LA11_0 == COLON or (PLUS <= LA11_0 <= STAR)) :
                        alt11 = 1


                    if alt11 == 1:
                        # lesscss.g:151:23: combinator simpleSelector
                        pass 
                        self._state.following.append(self.FOLLOW_combinator_in_selector750)
                        combinator48 = self.combinator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, combinator48.tree)
                        self._state.following.append(self.FOLLOW_simpleSelector_in_selector752)
                        simpleSelector49 = self.simpleSelector()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, simpleSelector49.tree)


                    else:
                        break #loop11



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "selector"

    class combinator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.combinator_return, self).__init__()

            self.tree = None




    # $ANTLR start "combinator"
    # lesscss.g:155:10: fragment combinator : ( PLUS | GREATER | );
    def combinator(self, ):

        retval = self.combinator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS50 = None
        GREATER51 = None

        PLUS50_tree = None
        GREATER51_tree = None

        try:
            try:
                # lesscss.g:156:5: ( PLUS | GREATER | )
                alt12 = 3
                LA12 = self.input.LA(1)
                if LA12 == PLUS:
                    alt12 = 1
                elif LA12 == GREATER:
                    alt12 = 2
                elif LA12 == IDENT or LA12 == COLON or LA12 == HASH or LA12 == DOT or LA12 == LBRACKET or LA12 == STAR:
                    alt12 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae

                if alt12 == 1:
                    # lesscss.g:156:7: PLUS
                    pass 
                    root_0 = self._adaptor.nil()

                    PLUS50=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_combinator774)
                    if self._state.backtracking == 0:

                        PLUS50_tree = self._adaptor.createWithPayload(PLUS50)
                        self._adaptor.addChild(root_0, PLUS50_tree)



                elif alt12 == 2:
                    # lesscss.g:157:7: GREATER
                    pass 
                    root_0 = self._adaptor.nil()

                    GREATER51=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_combinator782)
                    if self._state.backtracking == 0:

                        GREATER51_tree = self._adaptor.createWithPayload(GREATER51)
                        self._adaptor.addChild(root_0, GREATER51_tree)



                elif alt12 == 3:
                    # lesscss.g:159:5: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "combinator"

    class simpleSelector_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.simpleSelector_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleSelector"
    # lesscss.g:161:1: simpleSelector : ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ );
    def simpleSelector(self, ):

        retval = self.simpleSelector_return()
        retval.start = self.input.LT(1)

        root_0 = None

        elementName52 = None

        elementSubsequent53 = None

        elementSubsequent54 = None



        try:
            try:
                # lesscss.g:162:5: ( elementName ( ( esPred )=> elementSubsequent )* | ( ( esPred )=> elementSubsequent )+ )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IDENT or LA15_0 == STAR) :
                    alt15 = 1
                elif (LA15_0 == COLON or (HASH <= LA15_0 <= LBRACKET)) :
                    alt15 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae

                if alt15 == 1:
                    # lesscss.g:162:7: elementName ( ( esPred )=> elementSubsequent )*
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_elementName_in_simpleSelector805)
                    elementName52 = self.elementName()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, elementName52.tree)
                    # lesscss.g:162:19: ( ( esPred )=> elementSubsequent )*
                    while True: #loop13
                        alt13 = 2
                        alt13 = self.dfa13.predict(self.input)
                        if alt13 == 1:
                            # lesscss.g:162:20: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector812)
                            elementSubsequent53 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent53.tree)


                        else:
                            break #loop13


                elif alt15 == 2:
                    # lesscss.g:163:7: ( ( esPred )=> elementSubsequent )+
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:163:7: ( ( esPred )=> elementSubsequent )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14 = self.input.LA(1)
                        if LA14 == HASH:
                            LA14_2 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1


                        elif LA14 == DOT:
                            LA14_3 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1


                        elif LA14 == LBRACKET:
                            LA14_4 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1


                        elif LA14 == COLON:
                            LA14_5 = self.input.LA(2)

                            if (self.synpred2_lesscss()) :
                                alt14 = 1



                        if alt14 == 1:
                            # lesscss.g:163:8: ( esPred )=> elementSubsequent
                            pass 
                            self._state.following.append(self.FOLLOW_elementSubsequent_in_simpleSelector827)
                            elementSubsequent54 = self.elementSubsequent()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, elementSubsequent54.tree)


                        else:
                            if cnt14 >= 1:
                                break #loop14

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simpleSelector"

    class esPred_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.esPred_return, self).__init__()

            self.tree = None




    # $ANTLR start "esPred"
    # lesscss.g:166:1: esPred : ( HASH | DOT | LBRACKET | COLON );
    def esPred(self, ):

        retval = self.esPred_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set55 = None

        set55_tree = None

        try:
            try:
                # lesscss.g:167:5: ( HASH | DOT | LBRACKET | COLON )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set55 = self.input.LT(1)
                if self.input.LA(1) == COLON or (HASH <= self.input.LA(1) <= LBRACKET):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set55))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "esPred"

    class elementSubsequent_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementSubsequent_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementSubsequent"
    # lesscss.g:170:1: elementSubsequent : ( HASH | cssClass | attrib | pseudo );
    def elementSubsequent(self, ):

        retval = self.elementSubsequent_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH56 = None
        cssClass57 = None

        attrib58 = None

        pseudo59 = None


        HASH56_tree = None

        try:
            try:
                # lesscss.g:171:5: ( HASH | cssClass | attrib | pseudo )
                alt16 = 4
                LA16 = self.input.LA(1)
                if LA16 == HASH:
                    alt16 = 1
                elif LA16 == DOT:
                    alt16 = 2
                elif LA16 == LBRACKET:
                    alt16 = 3
                elif LA16 == COLON:
                    alt16 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # lesscss.g:171:7: HASH
                    pass 
                    root_0 = self._adaptor.nil()

                    HASH56=self.match(self.input, HASH, self.FOLLOW_HASH_in_elementSubsequent883)
                    if self._state.backtracking == 0:

                        HASH56_tree = self._adaptor.createWithPayload(HASH56)
                        self._adaptor.addChild(root_0, HASH56_tree)



                elif alt16 == 2:
                    # lesscss.g:172:7: cssClass
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cssClass_in_elementSubsequent891)
                    cssClass57 = self.cssClass()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cssClass57.tree)


                elif alt16 == 3:
                    # lesscss.g:173:7: attrib
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_attrib_in_elementSubsequent899)
                    attrib58 = self.attrib()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, attrib58.tree)


                elif alt16 == 4:
                    # lesscss.g:174:7: pseudo
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pseudo_in_elementSubsequent907)
                    pseudo59 = self.pseudo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pseudo59.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elementSubsequent"

    class cssClass_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.cssClass_return, self).__init__()

            self.tree = None




    # $ANTLR start "cssClass"
    # lesscss.g:178:1: cssClass : DOT a= IDENT -> IDENT ;
    def cssClass(self, ):

        retval = self.cssClass_return()
        retval.start = self.input.LT(1)

        root_0 = None

        a = None
        DOT60 = None

        a_tree = None
        DOT60_tree = None
        stream_IDENT = RewriteRuleTokenStream(self._adaptor, "token IDENT")
        stream_DOT = RewriteRuleTokenStream(self._adaptor, "token DOT")

        try:
            try:
                # lesscss.g:179:5: ( DOT a= IDENT -> IDENT )
                # lesscss.g:179:7: DOT a= IDENT
                pass 
                DOT60=self.match(self.input, DOT, self.FOLLOW_DOT_in_cssClass925) 
                if self._state.backtracking == 0:
                    stream_DOT.add(DOT60)
                a=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_cssClass929) 
                if self._state.backtracking == 0:
                    stream_IDENT.add(a)
                if self._state.backtracking == 0:
                    a.setText('.' + a.getText()); 


                # AST Rewrite
                # elements: IDENT
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 181:9: -> IDENT
                    self._adaptor.addChild(root_0, stream_IDENT.nextNode())



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "cssClass"

    class elementName_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.elementName_return, self).__init__()

            self.tree = None




    # $ANTLR start "elementName"
    # lesscss.g:185:1: elementName : ( IDENT | STAR );
    def elementName(self, ):

        retval = self.elementName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set61 = None

        set61_tree = None

        try:
            try:
                # lesscss.g:186:5: ( IDENT | STAR )
                # lesscss.g:
                pass 
                root_0 = self._adaptor.nil()

                set61 = self.input.LT(1)
                if self.input.LA(1) == IDENT or self.input.LA(1) == STAR:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set61))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "elementName"

    class attrib_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.attrib_return, self).__init__()

            self.tree = None




    # $ANTLR start "attrib"
    # lesscss.g:190:1: attrib : LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET ;
    def attrib(self, ):

        retval = self.attrib_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LBRACKET62 = None
        IDENT63 = None
        set64 = None
        set65 = None
        RBRACKET66 = None

        LBRACKET62_tree = None
        IDENT63_tree = None
        set64_tree = None
        set65_tree = None
        RBRACKET66_tree = None

        try:
            try:
                # lesscss.g:191:5: ( LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET )
                # lesscss.g:191:7: LBRACKET IDENT ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )? RBRACKET
                pass 
                root_0 = self._adaptor.nil()

                LBRACKET62=self.match(self.input, LBRACKET, self.FOLLOW_LBRACKET_in_attrib999)
                if self._state.backtracking == 0:

                    LBRACKET62_tree = self._adaptor.createWithPayload(LBRACKET62)
                    self._adaptor.addChild(root_0, LBRACKET62_tree)

                IDENT63=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_attrib1014)
                if self._state.backtracking == 0:

                    IDENT63_tree = self._adaptor.createWithPayload(IDENT63)
                    self._adaptor.addChild(root_0, IDENT63_tree)

                # lesscss.g:195:13: ( ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING ) )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((OPEQ <= LA17_0 <= DASHMATCH)) :
                    alt17 = 1
                if alt17 == 1:
                    # lesscss.g:196:17: ( OPEQ | INCLUDES | DASHMATCH ) ( IDENT | STRING )
                    pass 
                    set64 = self.input.LT(1)
                    if (OPEQ <= self.input.LA(1) <= DASHMATCH):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set64))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    set65 = self.input.LT(1)
                    if self.input.LA(1) == STRING or self.input.LA(1) == IDENT:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set65))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse





                RBRACKET66=self.match(self.input, RBRACKET, self.FOLLOW_RBRACKET_in_attrib1264)
                if self._state.backtracking == 0:

                    RBRACKET66_tree = self._adaptor.createWithPayload(RBRACKET66)
                    self._adaptor.addChild(root_0, RBRACKET66_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "attrib"

    class pseudo_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.pseudo_return, self).__init__()

            self.tree = None




    # $ANTLR start "pseudo"
    # lesscss.g:210:1: pseudo : COLON ( IDENT | FUNCTION expr RPAREN ) ;
    def pseudo(self, ):

        retval = self.pseudo_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON67 = None
        IDENT68 = None
        FUNCTION69 = None
        RPAREN71 = None
        expr70 = None


        COLON67_tree = None
        IDENT68_tree = None
        FUNCTION69_tree = None
        RPAREN71_tree = None

        try:
            try:
                # lesscss.g:211:5: ( COLON ( IDENT | FUNCTION expr RPAREN ) )
                # lesscss.g:211:7: COLON ( IDENT | FUNCTION expr RPAREN )
                pass 
                root_0 = self._adaptor.nil()

                COLON67=self.match(self.input, COLON, self.FOLLOW_COLON_in_pseudo1277)
                if self._state.backtracking == 0:

                    COLON67_tree = self._adaptor.createWithPayload(COLON67)
                    self._adaptor.addChild(root_0, COLON67_tree)

                # lesscss.g:211:13: ( IDENT | FUNCTION expr RPAREN )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == IDENT) :
                    alt18 = 1
                elif (LA18_0 == FUNCTION) :
                    alt18 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae

                if alt18 == 1:
                    # lesscss.g:211:15: IDENT
                    pass 
                    IDENT68=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_pseudo1281)
                    if self._state.backtracking == 0:

                        IDENT68_tree = self._adaptor.createWithPayload(IDENT68)
                        self._adaptor.addChild(root_0, IDENT68_tree)



                elif alt18 == 2:
                    # lesscss.g:211:23: FUNCTION expr RPAREN
                    pass 
                    FUNCTION69=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_pseudo1285)
                    if self._state.backtracking == 0:

                        FUNCTION69_tree = self._adaptor.createWithPayload(FUNCTION69)
                        self._adaptor.addChild(root_0, FUNCTION69_tree)

                    self._state.following.append(self.FOLLOW_expr_in_pseudo1287)
                    expr70 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr70.tree)
                    RPAREN71=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_pseudo1289)
                    if self._state.backtracking == 0:

                        RPAREN71_tree = self._adaptor.createWithPayload(RPAREN71)
                        self._adaptor.addChild(root_0, RPAREN71_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pseudo"

    class declarationset_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declarationset_return, self).__init__()

            self.tree = None




    # $ANTLR start "declarationset"
    # lesscss.g:215:1: declarationset : declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ ;
    def declarationset(self, ):

        retval = self.declarationset_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI73 = None
        SEMI75 = None
        declaration72 = None

        declaration74 = None


        SEMI73_tree = None
        SEMI75_tree = None
        stream_SEMI = RewriteRuleTokenStream(self._adaptor, "token SEMI")
        stream_declaration = RewriteRuleSubtreeStream(self._adaptor, "rule declaration")
        try:
            try:
                # lesscss.g:216:5: ( declaration ( SEMI declaration )* ( SEMI )? -> ( declaration )+ )
                # lesscss.g:216:7: declaration ( SEMI declaration )* ( SEMI )?
                pass 
                self._state.following.append(self.FOLLOW_declaration_in_declarationset1309)
                declaration72 = self.declaration()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_declaration.add(declaration72.tree)
                # lesscss.g:216:19: ( SEMI declaration )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == SEMI) :
                        LA19_1 = self.input.LA(2)

                        if (LA19_1 == IDENT) :
                            alt19 = 1




                    if alt19 == 1:
                        # lesscss.g:216:20: SEMI declaration
                        pass 
                        SEMI73=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1312) 
                        if self._state.backtracking == 0:
                            stream_SEMI.add(SEMI73)
                        self._state.following.append(self.FOLLOW_declaration_in_declarationset1314)
                        declaration74 = self.declaration()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_declaration.add(declaration74.tree)


                    else:
                        break #loop19
                # lesscss.g:216:39: ( SEMI )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == SEMI) :
                    alt20 = 1
                if alt20 == 1:
                    # lesscss.g:216:39: SEMI
                    pass 
                    SEMI75=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_declarationset1318) 
                    if self._state.backtracking == 0:
                        stream_SEMI.add(SEMI75)




                # AST Rewrite
                # elements: declaration
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 216:45: -> ( declaration )+
                    # lesscss.g:216:48: ( declaration )+
                    if not (stream_declaration.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_declaration.hasNext():
                        self._adaptor.addChild(root_0, stream_declaration.nextTree())


                    stream_declaration.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declarationset"

    class declaration_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.declaration_return, self).__init__()

            self.tree = None




    # $ANTLR start "declaration"
    # lesscss.g:220:1: declaration : property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) ;
    def declaration(self, ):

        retval = self.declaration_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON77 = None
        property76 = None

        expr78 = None

        prio79 = None


        COLON77_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_property = RewriteRuleSubtreeStream(self._adaptor, "rule property")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_prio = RewriteRuleSubtreeStream(self._adaptor, "rule prio")
        try:
            try:
                # lesscss.g:221:5: ( property COLON expr ( prio )? -> ^( N_Declaration property expr ( prio )? ) )
                # lesscss.g:221:7: property COLON expr ( prio )?
                pass 
                self._state.following.append(self.FOLLOW_property_in_declaration1342)
                property76 = self.property()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_property.add(property76.tree)
                COLON77=self.match(self.input, COLON, self.FOLLOW_COLON_in_declaration1344) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON77)
                self._state.following.append(self.FOLLOW_expr_in_declaration1346)
                expr78 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(expr78.tree)
                # lesscss.g:221:27: ( prio )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == IMPORTANT_SYM) :
                    alt21 = 1
                if alt21 == 1:
                    # lesscss.g:221:27: prio
                    pass 
                    self._state.following.append(self.FOLLOW_prio_in_declaration1348)
                    prio79 = self.prio()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_prio.add(prio79.tree)




                # AST Rewrite
                # elements: property, prio, expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 221:33: -> ^( N_Declaration property expr ( prio )? )
                    # lesscss.g:221:36: ^( N_Declaration property expr ( prio )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(N_Declaration, "N_Declaration"), root_1)

                    self._adaptor.addChild(root_1, stream_property.nextTree())
                    self._adaptor.addChild(root_1, stream_expr.nextTree())
                    # lesscss.g:221:66: ( prio )?
                    if stream_prio.hasNext():
                        self._adaptor.addChild(root_1, stream_prio.nextTree())


                    stream_prio.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "declaration"

    class prio_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.prio_return, self).__init__()

            self.tree = None




    # $ANTLR start "prio"
    # lesscss.g:225:1: prio : IMPORTANT_SYM ;
    def prio(self, ):

        retval = self.prio_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORTANT_SYM80 = None

        IMPORTANT_SYM80_tree = None

        try:
            try:
                # lesscss.g:226:5: ( IMPORTANT_SYM )
                # lesscss.g:226:7: IMPORTANT_SYM
                pass 
                root_0 = self._adaptor.nil()

                IMPORTANT_SYM80=self.match(self.input, IMPORTANT_SYM, self.FOLLOW_IMPORTANT_SYM_in_prio1384)
                if self._state.backtracking == 0:

                    IMPORTANT_SYM80_tree = self._adaptor.createWithPayload(IMPORTANT_SYM80)
                    self._adaptor.addChild(root_0, IMPORTANT_SYM80_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prio"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # lesscss.g:229:1: expr : term ( operator term )* ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        term81 = None

        operator82 = None

        term83 = None



        try:
            try:
                # lesscss.g:230:5: ( term ( operator term )* )
                # lesscss.g:230:7: term ( operator term )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_term_in_expr1405)
                term81 = self.term()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, term81.tree)
                # lesscss.g:230:12: ( operator term )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == COMMA) :
                        LA22_2 = self.input.LA(2)

                        if (LA22_2 == STRING or LA22_2 == URI or (MINUS <= LA22_2 <= PLUS) or LA22_2 == HASH or LA22_2 == FUNCTION or (NUMBER <= LA22_2 <= FREQ)) :
                            alt22 = 1
                        elif (LA22_2 == IDENT) :
                            LA22_4 = self.input.LA(3)

                            if ((STRING <= LA22_4 <= SEMI) or (COMMA <= LA22_4 <= URI) or (RBRACE <= LA22_4 <= IDENT) or (COLON <= LA22_4 <= PLUS) or (HASH <= LA22_4 <= DOT) or (FUNCTION <= LA22_4 <= FREQ)) :
                                alt22 = 1




                    elif (LA22_0 == STRING or LA22_0 == URI or LA22_0 == IDENT or (MINUS <= LA22_0 <= PLUS) or LA22_0 == HASH or LA22_0 == FUNCTION or (SOLIDUS <= LA22_0 <= FREQ)) :
                        alt22 = 1


                    if alt22 == 1:
                        # lesscss.g:230:13: operator term
                        pass 
                        self._state.following.append(self.FOLLOW_operator_in_expr1408)
                        operator82 = self.operator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, operator82.tree)
                        self._state.following.append(self.FOLLOW_term_in_expr1410)
                        term83 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, term83.tree)


                    else:
                        break #loop22



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class operator_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.operator_return, self).__init__()

            self.tree = None




    # $ANTLR start "operator"
    # lesscss.g:234:10: fragment operator : ( SOLIDUS | COMMA | );
    def operator(self, ):

        retval = self.operator_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SOLIDUS84 = None
        COMMA85 = None

        SOLIDUS84_tree = None
        COMMA85_tree = None

        try:
            try:
                # lesscss.g:235:5: ( SOLIDUS | COMMA | )
                alt23 = 3
                LA23 = self.input.LA(1)
                if LA23 == SOLIDUS:
                    alt23 = 1
                elif LA23 == COMMA:
                    alt23 = 2
                elif LA23 == STRING or LA23 == URI or LA23 == IDENT or LA23 == MINUS or LA23 == PLUS or LA23 == HASH or LA23 == FUNCTION or LA23 == NUMBER or LA23 == PERCENTAGE or LA23 == LENGTH or LA23 == EMS or LA23 == EXS or LA23 == ANGLE or LA23 == TIME or LA23 == FREQ:
                    alt23 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # lesscss.g:235:7: SOLIDUS
                    pass 
                    root_0 = self._adaptor.nil()

                    SOLIDUS84=self.match(self.input, SOLIDUS, self.FOLLOW_SOLIDUS_in_operator1432)
                    if self._state.backtracking == 0:

                        SOLIDUS84_tree = self._adaptor.createWithPayload(SOLIDUS84)
                        self._adaptor.addChild(root_0, SOLIDUS84_tree)



                elif alt23 == 2:
                    # lesscss.g:236:7: COMMA
                    pass 
                    root_0 = self._adaptor.nil()

                    COMMA85=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_operator1440)
                    if self._state.backtracking == 0:

                        COMMA85_tree = self._adaptor.createWithPayload(COMMA85)
                        self._adaptor.addChild(root_0, COMMA85_tree)



                elif alt23 == 3:
                    # lesscss.g:238:5: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "operator"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # lesscss.g:240:1: term : ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set87 = None
        STRING88 = None
        IDENT89 = None
        URI90 = None
        unaryOperator86 = None

        function91 = None

        hexColor92 = None


        set87_tree = None
        STRING88_tree = None
        IDENT89_tree = None
        URI90_tree = None

        try:
            try:
                # lesscss.g:241:5: ( ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ ) | STRING | IDENT | URI | function | hexColor )
                alt25 = 6
                LA25 = self.input.LA(1)
                if LA25 == MINUS or LA25 == PLUS or LA25 == NUMBER or LA25 == PERCENTAGE or LA25 == LENGTH or LA25 == EMS or LA25 == EXS or LA25 == ANGLE or LA25 == TIME or LA25 == FREQ:
                    alt25 = 1
                elif LA25 == STRING:
                    alt25 = 2
                elif LA25 == IDENT:
                    LA25_3 = self.input.LA(2)

                    if (LA25_3 == COLON or LA25_3 == DOT) :
                        alt25 = 5
                    elif ((STRING <= LA25_3 <= SEMI) or (COMMA <= LA25_3 <= URI) or (RBRACE <= LA25_3 <= IDENT) or (MINUS <= LA25_3 <= PLUS) or LA25_3 == HASH or (FUNCTION <= LA25_3 <= FREQ)) :
                        alt25 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 25, 3, self.input)

                        raise nvae

                elif LA25 == URI:
                    alt25 = 4
                elif LA25 == FUNCTION:
                    alt25 = 5
                elif LA25 == HASH:
                    alt25 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # lesscss.g:241:7: ( unaryOperator )? ( NUMBER | PERCENTAGE | LENGTH | EMS | EXS | ANGLE | TIME | FREQ )
                    pass 
                    root_0 = self._adaptor.nil()

                    # lesscss.g:241:7: ( unaryOperator )?
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if ((MINUS <= LA24_0 <= PLUS)) :
                        alt24 = 1
                    if alt24 == 1:
                        # lesscss.g:241:7: unaryOperator
                        pass 
                        self._state.following.append(self.FOLLOW_unaryOperator_in_term1463)
                        unaryOperator86 = self.unaryOperator()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unaryOperator86.tree)



                    set87 = self.input.LT(1)
                    if (NUMBER <= self.input.LA(1) <= FREQ):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set87))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt25 == 2:
                    # lesscss.g:252:7: STRING
                    pass 
                    root_0 = self._adaptor.nil()

                    STRING88=self.match(self.input, STRING, self.FOLLOW_STRING_in_term1620)
                    if self._state.backtracking == 0:

                        STRING88_tree = self._adaptor.createWithPayload(STRING88)
                        self._adaptor.addChild(root_0, STRING88_tree)



                elif alt25 == 3:
                    # lesscss.g:253:7: IDENT
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT89=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_term1628)
                    if self._state.backtracking == 0:

                        IDENT89_tree = self._adaptor.createWithPayload(IDENT89)
                        self._adaptor.addChild(root_0, IDENT89_tree)



                elif alt25 == 4:
                    # lesscss.g:254:7: URI
                    pass 
                    root_0 = self._adaptor.nil()

                    URI90=self.match(self.input, URI, self.FOLLOW_URI_in_term1636)
                    if self._state.backtracking == 0:

                        URI90_tree = self._adaptor.createWithPayload(URI90)
                        self._adaptor.addChild(root_0, URI90_tree)



                elif alt25 == 5:
                    # lesscss.g:255:7: function
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_function_in_term1644)
                    function91 = self.function()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, function91.tree)


                elif alt25 == 6:
                    # lesscss.g:256:7: hexColor
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_hexColor_in_term1652)
                    hexColor92 = self.hexColor()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, hexColor92.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "term"

    class function_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.function_return, self).__init__()

            self.tree = None




    # $ANTLR start "function"
    # lesscss.g:260:1: function : ( fnct_name fnct_args RPAREN | fnct_name expr RPAREN );
    def function(self, ):

        retval = self.function_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RPAREN95 = None
        RPAREN98 = None
        fnct_name93 = None

        fnct_args94 = None

        fnct_name96 = None

        expr97 = None


        RPAREN95_tree = None
        RPAREN98_tree = None

        try:
            try:
                # lesscss.g:261:5: ( fnct_name fnct_args RPAREN | fnct_name expr RPAREN )
                alt26 = 2
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # lesscss.g:261:7: fnct_name fnct_args RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fnct_name_in_function1670)
                    fnct_name93 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fnct_name93.tree)
                    self._state.following.append(self.FOLLOW_fnct_args_in_function1672)
                    fnct_args94 = self.fnct_args()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fnct_args94.tree)
                    RPAREN95=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1674)
                    if self._state.backtracking == 0:

                        RPAREN95_tree = self._adaptor.createWithPayload(RPAREN95)
                        self._adaptor.addChild(root_0, RPAREN95_tree)



                elif alt26 == 2:
                    # lesscss.g:262:7: fnct_name expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fnct_name_in_function1682)
                    fnct_name96 = self.fnct_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fnct_name96.tree)
                    self._state.following.append(self.FOLLOW_expr_in_function1684)
                    expr97 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr97.tree)
                    RPAREN98=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_function1686)
                    if self._state.backtracking == 0:

                        RPAREN98_tree = self._adaptor.createWithPayload(RPAREN98)
                        self._adaptor.addChild(root_0, RPAREN98_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "function"

    class fnct_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_name"
    # lesscss.g:265:1: fnct_name : ( IDENT ( COLON | DOT )+ )* FUNCTION ;
    def fnct_name(self, ):

        retval = self.fnct_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT99 = None
        set100 = None
        FUNCTION101 = None

        IDENT99_tree = None
        set100_tree = None
        FUNCTION101_tree = None

        try:
            try:
                # lesscss.g:266:5: ( ( IDENT ( COLON | DOT )+ )* FUNCTION )
                # lesscss.g:266:7: ( IDENT ( COLON | DOT )+ )* FUNCTION
                pass 
                root_0 = self._adaptor.nil()

                # lesscss.g:266:7: ( IDENT ( COLON | DOT )+ )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == IDENT) :
                        alt28 = 1


                    if alt28 == 1:
                        # lesscss.g:266:8: IDENT ( COLON | DOT )+
                        pass 
                        IDENT99=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_name1704)
                        if self._state.backtracking == 0:

                            IDENT99_tree = self._adaptor.createWithPayload(IDENT99)
                            self._adaptor.addChild(root_0, IDENT99_tree)

                        # lesscss.g:266:14: ( COLON | DOT )+
                        cnt27 = 0
                        while True: #loop27
                            alt27 = 2
                            LA27_0 = self.input.LA(1)

                            if (LA27_0 == COLON or LA27_0 == DOT) :
                                alt27 = 1


                            if alt27 == 1:
                                # lesscss.g:
                                pass 
                                set100 = self.input.LT(1)
                                if self.input.LA(1) == COLON or self.input.LA(1) == DOT:
                                    self.input.consume()
                                    if self._state.backtracking == 0:
                                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set100))
                                    self._state.errorRecovery = False

                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed

                                    mse = MismatchedSetException(None, self.input)
                                    raise mse




                            else:
                                if cnt27 >= 1:
                                    break #loop27

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(27, self.input)
                                raise eee

                            cnt27 += 1


                    else:
                        break #loop28
                FUNCTION101=self.match(self.input, FUNCTION, self.FOLLOW_FUNCTION_in_fnct_name1716)
                if self._state.backtracking == 0:

                    FUNCTION101_tree = self._adaptor.createWithPayload(FUNCTION101)
                    self._adaptor.addChild(root_0, FUNCTION101_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_name"

    class fnct_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_args_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_args"
    # lesscss.g:269:10: fragment fnct_args : fnct_arg ( COMMA fnct_arg )* ;
    def fnct_args(self, ):

        retval = self.fnct_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA103 = None
        fnct_arg102 = None

        fnct_arg104 = None


        COMMA103_tree = None

        try:
            try:
                # lesscss.g:270:5: ( fnct_arg ( COMMA fnct_arg )* )
                # lesscss.g:270:7: fnct_arg ( COMMA fnct_arg )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1735)
                fnct_arg102 = self.fnct_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fnct_arg102.tree)
                # lesscss.g:270:16: ( COMMA fnct_arg )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == COMMA) :
                        alt29 = 1


                    if alt29 == 1:
                        # lesscss.g:270:17: COMMA fnct_arg
                        pass 
                        COMMA103=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_fnct_args1738)
                        if self._state.backtracking == 0:

                            COMMA103_tree = self._adaptor.createWithPayload(COMMA103)
                            self._adaptor.addChild(root_0, COMMA103_tree)

                        self._state.following.append(self.FOLLOW_fnct_arg_in_fnct_args1740)
                        fnct_arg104 = self.fnct_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fnct_arg104.tree)


                    else:
                        break #loop29



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_args"

    class fnct_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.fnct_arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "fnct_arg"
    # lesscss.g:273:1: fnct_arg : IDENT OPEQ expr ;
    def fnct_arg(self, ):

        retval = self.fnct_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT105 = None
        OPEQ106 = None
        expr107 = None


        IDENT105_tree = None
        OPEQ106_tree = None

        try:
            try:
                # lesscss.g:274:5: ( IDENT OPEQ expr )
                # lesscss.g:274:7: IDENT OPEQ expr
                pass 
                root_0 = self._adaptor.nil()

                IDENT105=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_fnct_arg1759)
                if self._state.backtracking == 0:

                    IDENT105_tree = self._adaptor.createWithPayload(IDENT105)
                    self._adaptor.addChild(root_0, IDENT105_tree)

                OPEQ106=self.match(self.input, OPEQ, self.FOLLOW_OPEQ_in_fnct_arg1761)
                if self._state.backtracking == 0:

                    OPEQ106_tree = self._adaptor.createWithPayload(OPEQ106)
                    self._adaptor.addChild(root_0, OPEQ106_tree)

                self._state.following.append(self.FOLLOW_expr_in_fnct_arg1763)
                expr107 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr107.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fnct_arg"

    class hexColor_return(ParserRuleReturnScope):
        def __init__(self):
            super(lesscssParser.hexColor_return, self).__init__()

            self.tree = None




    # $ANTLR start "hexColor"
    # lesscss.g:277:1: hexColor : HASH ;
    def hexColor(self, ):

        retval = self.hexColor_return()
        retval.start = self.input.LT(1)

        root_0 = None

        HASH108 = None

        HASH108_tree = None

        try:
            try:
                # lesscss.g:278:5: ( HASH )
                # lesscss.g:278:7: HASH
                pass 
                root_0 = self._adaptor.nil()

                HASH108=self.match(self.input, HASH, self.FOLLOW_HASH_in_hexColor1780)
                if self._state.backtracking == 0:

                    HASH108_tree = self._adaptor.createWithPayload(HASH108)
                    self._adaptor.addChild(root_0, HASH108_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "hexColor"

    # $ANTLR start "synpred1_lesscss"
    def synpred1_lesscss_fragment(self, ):
        # lesscss.g:162:20: ( esPred )
        # lesscss.g:162:21: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred1_lesscss809)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred1_lesscss"



    # $ANTLR start "synpred2_lesscss"
    def synpred2_lesscss_fragment(self, ):
        # lesscss.g:163:8: ( esPred )
        # lesscss.g:163:9: esPred
        pass 
        self._state.following.append(self.FOLLOW_esPred_in_synpred2_lesscss824)
        self.esPred()

        self._state.following.pop()


    # $ANTLR end "synpred2_lesscss"




    # Delegated rules

    def synpred2_lesscss(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred2_lesscss_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_lesscss(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_lesscss_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\22\3\uffff\4\0\3\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\41\3\uffff\4\0\3\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\2\10\uffff\1\1"
        )

    DFA13_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\3\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\1\1\2\uffff\1\1\1\uffff\1\1\2\uffff\1\7\1\uffff\2\1"
        u"\1\4\1\5\1\6\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #13

    class DFA13(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA13_4 = input.LA(1)

                 
                index13_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA13_5 = input.LA(1)

                 
                index13_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA13_6 = input.LA(1)

                 
                index13_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA13_7 = input.LA(1)

                 
                index13_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred1_lesscss()):
                    s = 10

                elif (True):
                    s = 1

                 
                input.seek(index13_7)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 13, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\27\1\32\1\17\1\27\1\uffff\1\17\1\uffff"
        )

    DFA26_max = DFA.unpack(
        u"\1\46\1\37\1\61\1\46\1\uffff\1\61\1\uffff"
        )

    DFA26_accept = DFA.unpack(
        u"\4\uffff\1\2\1\uffff\1\1"
        )

    DFA26_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA26_transition = [
        DFA.unpack(u"\1\1\16\uffff\1\2"),
        DFA.unpack(u"\1\3\4\uffff\1\3"),
        DFA.unpack(u"\1\4\3\uffff\1\4\3\uffff\1\5\3\uffff\2\4\1\uffff\1"
        u"\4\7\uffff\1\4\3\uffff\10\4"),
        DFA.unpack(u"\1\1\2\uffff\1\3\4\uffff\1\3\6\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\2\uffff\2\4\3\uffff\1\4\2\uffff\3\4\1\uffff\2"
        u"\4\2\uffff\1\6\3\uffff\2\4\1\uffff\11\4"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #26

    class DFA26(DFA):
        pass


 

    FOLLOW_charSet_in_styleSheet149 = frozenset([17, 20, 23, 24, 25, 26, 30, 31, 32, 33])
    FOLLOW_imports_in_styleSheet160 = frozenset([17, 20, 23, 24, 25, 26, 30, 31, 32, 33])
    FOLLOW_bodylist_in_styleSheet171 = frozenset([])
    FOLLOW_EOF_in_styleSheet181 = frozenset([1])
    FOLLOW_CHARSET_SYM_in_charSet234 = frozenset([15])
    FOLLOW_STRING_in_charSet236 = frozenset([16])
    FOLLOW_SEMI_in_charSet238 = frozenset([1])
    FOLLOW_IMPORT_SYM_in_imports277 = frozenset([15, 19])
    FOLLOW_importUrl_in_imports279 = frozenset([16, 23])
    FOLLOW_medium_in_imports282 = frozenset([16, 18])
    FOLLOW_COMMA_in_imports285 = frozenset([23])
    FOLLOW_medium_in_imports287 = frozenset([16, 18])
    FOLLOW_SEMI_in_imports293 = frozenset([1])
    FOLLOW_set_in_importUrl0 = frozenset([1])
    FOLLOW_MEDIA_SYM_in_media360 = frozenset([23])
    FOLLOW_medium_in_media362 = frozenset([18, 21])
    FOLLOW_COMMA_in_media365 = frozenset([23])
    FOLLOW_medium_in_media367 = frozenset([18, 21])
    FOLLOW_LBRACE_in_media379 = frozenset([22, 23, 26, 30, 31, 32, 33])
    FOLLOW_ruleSet_in_media393 = frozenset([22, 23, 26, 30, 31, 32, 33])
    FOLLOW_RBRACE_in_media404 = frozenset([1])
    FOLLOW_IDENT_in_medium445 = frozenset([1])
    FOLLOW_FONTFACE_SYM_in_fontface467 = frozenset([21])
    FOLLOW_LBRACE_in_fontface469 = frozenset([23])
    FOLLOW_declarationset_in_fontface471 = frozenset([22])
    FOLLOW_RBRACE_in_fontface473 = frozenset([1])
    FOLLOW_bodyset_in_bodylist511 = frozenset([1, 20, 23, 24, 25, 26, 30, 31, 32, 33])
    FOLLOW_ruleSet_in_bodyset530 = frozenset([1])
    FOLLOW_media_in_bodyset538 = frozenset([1])
    FOLLOW_page_in_bodyset546 = frozenset([1])
    FOLLOW_fontface_in_bodyset554 = frozenset([1])
    FOLLOW_PAGE_SYM_in_page575 = frozenset([21, 26])
    FOLLOW_pseudoPage_in_page577 = frozenset([21])
    FOLLOW_LBRACE_in_page580 = frozenset([23])
    FOLLOW_declarationset_in_page582 = frozenset([22])
    FOLLOW_RBRACE_in_page584 = frozenset([1])
    FOLLOW_COLON_in_pseudoPage621 = frozenset([23])
    FOLLOW_IDENT_in_pseudoPage623 = frozenset([1])
    FOLLOW_set_in_unaryOperator0 = frozenset([1])
    FOLLOW_IDENT_in_property676 = frozenset([1])
    FOLLOW_selector_in_ruleSet694 = frozenset([18, 21])
    FOLLOW_COMMA_in_ruleSet697 = frozenset([23, 26, 30, 31, 32, 33])
    FOLLOW_selector_in_ruleSet699 = frozenset([18, 21])
    FOLLOW_LBRACE_in_ruleSet703 = frozenset([23])
    FOLLOW_declarationset_in_ruleSet705 = frozenset([22])
    FOLLOW_RBRACE_in_ruleSet707 = frozenset([1])
    FOLLOW_simpleSelector_in_selector747 = frozenset([1, 23, 26, 28, 29, 30, 31, 32, 33])
    FOLLOW_combinator_in_selector750 = frozenset([23, 26, 30, 31, 32, 33])
    FOLLOW_simpleSelector_in_selector752 = frozenset([1, 23, 26, 28, 29, 30, 31, 32, 33])
    FOLLOW_PLUS_in_combinator774 = frozenset([1])
    FOLLOW_GREATER_in_combinator782 = frozenset([1])
    FOLLOW_elementName_in_simpleSelector805 = frozenset([1, 23, 26, 30, 31, 32, 33])
    FOLLOW_elementSubsequent_in_simpleSelector812 = frozenset([1, 23, 26, 30, 31, 32, 33])
    FOLLOW_elementSubsequent_in_simpleSelector827 = frozenset([1, 23, 26, 30, 31, 32, 33])
    FOLLOW_set_in_esPred0 = frozenset([1])
    FOLLOW_HASH_in_elementSubsequent883 = frozenset([1])
    FOLLOW_cssClass_in_elementSubsequent891 = frozenset([1])
    FOLLOW_attrib_in_elementSubsequent899 = frozenset([1])
    FOLLOW_pseudo_in_elementSubsequent907 = frozenset([1])
    FOLLOW_DOT_in_cssClass925 = frozenset([23])
    FOLLOW_IDENT_in_cssClass929 = frozenset([1])
    FOLLOW_set_in_elementName0 = frozenset([1])
    FOLLOW_LBRACKET_in_attrib999 = frozenset([23])
    FOLLOW_IDENT_in_attrib1014 = frozenset([34, 35, 36, 37])
    FOLLOW_set_in_attrib1055 = frozenset([15, 23])
    FOLLOW_set_in_attrib1163 = frozenset([37])
    FOLLOW_RBRACKET_in_attrib1264 = frozenset([1])
    FOLLOW_COLON_in_pseudo1277 = frozenset([23, 38])
    FOLLOW_IDENT_in_pseudo1281 = frozenset([1])
    FOLLOW_FUNCTION_in_pseudo1285 = frozenset([15, 19, 23, 27, 28, 30, 38, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_expr_in_pseudo1287 = frozenset([39])
    FOLLOW_RPAREN_in_pseudo1289 = frozenset([1])
    FOLLOW_declaration_in_declarationset1309 = frozenset([1, 16])
    FOLLOW_SEMI_in_declarationset1312 = frozenset([23])
    FOLLOW_declaration_in_declarationset1314 = frozenset([1, 16])
    FOLLOW_SEMI_in_declarationset1318 = frozenset([1])
    FOLLOW_property_in_declaration1342 = frozenset([26])
    FOLLOW_COLON_in_declaration1344 = frozenset([15, 19, 23, 27, 28, 30, 38, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_expr_in_declaration1346 = frozenset([1, 40])
    FOLLOW_prio_in_declaration1348 = frozenset([1])
    FOLLOW_IMPORTANT_SYM_in_prio1384 = frozenset([1])
    FOLLOW_term_in_expr1405 = frozenset([1, 15, 18, 19, 23, 27, 28, 30, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_operator_in_expr1408 = frozenset([15, 19, 23, 27, 28, 30, 38, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_term_in_expr1410 = frozenset([1, 15, 18, 19, 23, 27, 28, 30, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_SOLIDUS_in_operator1432 = frozenset([1])
    FOLLOW_COMMA_in_operator1440 = frozenset([1])
    FOLLOW_unaryOperator_in_term1463 = frozenset([42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_set_in_term1474 = frozenset([1])
    FOLLOW_STRING_in_term1620 = frozenset([1])
    FOLLOW_IDENT_in_term1628 = frozenset([1])
    FOLLOW_URI_in_term1636 = frozenset([1])
    FOLLOW_function_in_term1644 = frozenset([1])
    FOLLOW_hexColor_in_term1652 = frozenset([1])
    FOLLOW_fnct_name_in_function1670 = frozenset([23])
    FOLLOW_fnct_args_in_function1672 = frozenset([39])
    FOLLOW_RPAREN_in_function1674 = frozenset([1])
    FOLLOW_fnct_name_in_function1682 = frozenset([15, 19, 23, 27, 28, 30, 38, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_expr_in_function1684 = frozenset([39])
    FOLLOW_RPAREN_in_function1686 = frozenset([1])
    FOLLOW_IDENT_in_fnct_name1704 = frozenset([26, 31])
    FOLLOW_set_in_fnct_name1706 = frozenset([23, 26, 31, 38])
    FOLLOW_FUNCTION_in_fnct_name1716 = frozenset([1])
    FOLLOW_fnct_arg_in_fnct_args1735 = frozenset([1, 18])
    FOLLOW_COMMA_in_fnct_args1738 = frozenset([23])
    FOLLOW_fnct_arg_in_fnct_args1740 = frozenset([1, 18])
    FOLLOW_IDENT_in_fnct_arg1759 = frozenset([34])
    FOLLOW_OPEQ_in_fnct_arg1761 = frozenset([15, 19, 23, 27, 28, 30, 38, 42, 43, 44, 45, 46, 47, 48, 49])
    FOLLOW_expr_in_fnct_arg1763 = frozenset([1])
    FOLLOW_HASH_in_hexColor1780 = frozenset([1])
    FOLLOW_esPred_in_synpred1_lesscss809 = frozenset([1])
    FOLLOW_esPred_in_synpred2_lesscss824 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("lesscssLexer", lesscssParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
