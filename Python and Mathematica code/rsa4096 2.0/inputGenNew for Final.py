'''
Created on 2013-6-13

@author: fatestudio
'''
WIDTH = 32
BYTES = WIDTH / 4
ADDR = 7
SSIZE = 2 ** ADDR
TOTALBIT = WIDTH * SSIZE
m = 17555138354946113191141010309033626261506170611135471526354579215981238085834524547740315849324880781158639249182737547366981179404960923829194416882503485085848182600170715683902659269020498168229402187359487369299193972129197772247141905173302697475832536265048518193930668434175352994376184146558931651303002292987717320706926089312207674911049302498665888188599392584101799552096456267229224488749319106235222906107947625275060164243221291030559243187544269633275025972382150717043095405143910038416311535159461906279370243107425063578323272112035737965461708575574149884779334005006337920179933158918985296826224384473521474735539140964139892957487338467374588961258543587338945796308902111663848726154348875217007564921316789307131918025934771659546984551605715982755963209936979867302211183990738234101411363983648159585194340426689908218758758611436509155181778768859364794260008730241236400517907563749470585822571718510358701601387373501325685612060824814047853843976245211261955398334250472844321554624475555320206753526853222895260720715190400718725066079635005699720190336383345020852905052124227370707133635389457094415022926741814341280786252814913193157076942669884844089932018236043725198465813263226599219621752093
print(hex(m))
e = 5
n = 0x84c5b4763fe31d0347fc816ac16e2284c10faa4003ba33db73f7ba8e0445d656de3a5db5154ed51212093d26ac512b01f18dd1eed77c96c0084f3dd6415af341ee52bdb6d1020a15d9ed17e3cc0e95ee8d103ed3cc667e971773308cdc6b13ab2e47dc0e959f3a518cfe5cd12d5db79ba2a7ae1f3ac7652ccdf8440407295e4299901c0475491bc354c56c9a9cc9af4ec9546b439f9d01298a449ebe89d9bf020067dba8589890086a17b9af5b569643d037cdff7c240d4969d495dd81355c53f0e642f43328ad088ded3c9691eb79fa5d5f576cdeb8fc4c7b297d0b0e5e18baf320cd576d14475b349aae908fb5262cc703806984c8199921167d8fcf23cae883333218bd91a1b7f03edca7e2dcaa37f463b337d20b5d59db610487c89da11b62397bc701762741bab9f87ff50592859be3cecb8c497c68a8c24d4244ef7febe8e5b4617589a82b5a702cfa93ea5c4ed8f33418f3d4e7115804f92283868a29678a5aa33b6fe5078c5fe8f8dc3bf364eb8ac8ce8a245e6b33138131c541013d0326324dfb695ffb3a1890c78092b4d42b28fef02b9c014ea5ac06d864c2f2e39403560d97dae38d9d643c25fbb230bbd92a4aa2b410d93c4efbc8d60b21fbac78255d6807923986bb968a437d5c8dfc5eda92d864ac5db9d707107e855c384429e821a4c74803e31ba1621582283d15a9ec0806705fca161622bd795fec898fL
print n
r = 2 ** 4096 % n
t = (2 ** 4096) ** 2 % n
nprime0 = 0xa3b18a91
ns = str(hex(n))[2:len(str(hex(n))) - 1][::-1]
ms = str(hex(m))[2:len(str(hex(m))) - 1][::-1]
es = str(hex(e))[2:len(str(hex(e)))][::-1]
rs = str(hex(r))[2:len(str(hex(r))) - 1][::-1]
ts = str(hex(t))[2:len(str(hex(t))) - 1][::-1]
nprime0s = str(hex(nprime0))[2:len(str(hex(nprime0))) - 1]
print(ns)
print(len(ns))
print(ms)
print(len(ms))
print(es)
print(len(es))
print(rs)
print(len(rs))
print(ts)
print(len(ts))
print(nprime0s)
print(len(nprime0s))

def boundaryPrint2(ms, i, headstr):
    if(len(ms) >= i * BYTES + BYTES):   # much larger
        print(headstr + ms[i * BYTES : i * BYTES + BYTES][::-1] + ";")
    elif(len(ms) <= i * BYTES):          # much smaller
        print(headstr + "00000000;")
    else:                               # in between
        for j in range(BYTES):
            if(len(ms) <= i * BYTES + j):
                zeros = ""                  # generate zeros string
                for k in range(BYTES - j):
                    zeros = zeros + "0"
                if(j == 0):
                    print(headstr + zeros + ";")
                else:
                    print(headstr + zeros + ms[i * BYTES : ][::-1] + ";")
                break
    
#print("nprime0 = 32'h" + nprime0s + ";")
for i in range(SSIZE):
    print("#20")
    boundaryPrint2(ms, i, "m_buf1 = 32'h")
    boundaryPrint2(es, i, "m_buf2 = 32'h")
    boundaryPrint2(ns, i, "m_buf3 = 32'h")
    boundaryPrint2(rs, i, "m_buf4 = 32'h")
    boundaryPrint2(ts, i, "m_buf5 = 32'h")
#    boundaryPrint2(ns, i, "n_in[" + str(i) + "] = 32'h")
#    boundaryPrint2(rs, i, "c_bar[`DATA_WIDTH * " + str(i) + " +: `DATA_WIDTH] = 32'h")
#    boundaryPrint2(ts, i, "t[`DATA_WIDTH * " + str(i) + " +: `DATA_WIDTH] = 32'h")