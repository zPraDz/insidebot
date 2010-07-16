###########################################################
##             USER-CONFIGURATION SECTION                ##
###########################################################

BUILD_SPEED = .15  ## This is the time between actions.
                  ## increase this number to make the bot go slower, decrease it
                  ## to make it go faster.

CMD_PREFIX  = "." ## Change this to change what triggers the bot responds to
                  ## A one letter thing works best.
                  ## Good prefixes: !@#$%*()_+-=.,?|><
                  ## Bad prefixes: /\&~` ' "


SILENT_MODE = 0     ## If 1, the bot will only send error messages
                    ## ie: failed copy/paste/backup/restore
                    ## if 0, the bot will send all messages


ABSOLUTE_SILENT_MODE = 0 ## if 1, the bot will produce no messages whatsoever.

valid_blocks = [1,3,4,5,6,12,13,14,15,16,17,18,19,20,21,22,23,24,
                             25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
                             41,42,44,45,46,47,48,49 ]
block_names  = {              "stone":1, "dirt":3, "cobblestone":4, "wood":5,
                              "sappling":6, "tree":6, "sand":12, "gravel":13,
                              "gold":14, "goldore":14, "iron":15, "ironore":15,
                              "coal":16, "treetrunk":17, "trunk":17, "leaves":18,
                              "sponge":19, "glass":20, "red":21, "orange":22,
                              "yellow":23, "lightgreen":24, "green":25, "aqua":26,
                              "aquagreen":26, "cyan":27, "blue":28, "purple":29,
                              "indigo":30, "violet":31, "magenta":32, "pink":33,
                              "black":34, "grey":35, "white":36, "yellow flower":37,
                              "rose":38, "redrose":38, "redflower":38,
                              "red mushroom":39, "brown mushroom":40, "gold block":41,
                              "ironblock":42, "stair":44, "brick":45, "tnt":46,
                              "bookcase":47, "mossy cobblestone":48, "green cobblestone":48,
                              "obsidian":49,"blank":0
                }

###########################################################
##        USER-CONFIGURATION SECTION ENDS HERE           ##
##   If you don't know what you're doing, don't change   ##
##   anything below this line. If you do, you are 100%   ##
##     on your own (unless it's a genuine programming    ##
##                      question).                       ##
###########################################################