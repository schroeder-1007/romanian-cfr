import re

INPUT_FILE = 'RoLLex.txt'

def latin_to_ipa(lat):
    #TODO should we apply gn > ŋn here?
    #TODO intervocalic i > jj and u > w; initial i > j and u > w
        #actually, seems like vatasescu's latin handles u/w distinction fine
    #Velarized l in coda seems irrelevant for Romanian outcomes.
    ipa_dict = {
        'a' : 'a',
        'e' : 'e',
        'i' : 'i',
        'o' : 'o',
        'u' : 'u',
        'y' : 'y',
        'A' : 'aː',
        'E' : 'eː',
        'I' : 'iː',
        'O' : 'oː',
        'U' : 'uː',
        'Y' : 'yː',
        'p' : 'p',
        't' : 't',
        'c' : 'k',
        'b' : 'b',
        'd' : 'd',
        'g' : 'g',
        'f' : 'f',
        's' : 's',
        'h' : 'h',
        'm' : 'm',
        'n' : 'n',
        'r' : 'r',
        'l' : 'l',
        'v' : 'w',
        'z' : 'z',
        'K' : 'kʰ',
        'P' : 'pʰ',
        'T' : 'tʰ',
        'x' : 'k s',
        '1' : 'a e̯',
        '2' : 'a u̯',
        '3' : 'o e̯',
        '4' : 'k w'
    }
    digraphs = {
        'ae' : '1',
        'au' : '2',
        'oe' : '3',
        'q' : '4',
        'ch' : 'K',
        'ph' : 'P',
        'th' : 'T',
    }

    #replace digraphs with single chars
    for key, val in digraphs.items():
        lat = lat.replace(key,val)

    #construct ipa string
    ipa = ''
    for char in lat:
        ipa += ipa_dict[char] + ' '
    return ipa

def romanian_to_ipa(rom):
    #TODO final i > j except when after cons+liquid
    ipa_dict = {
        'a' : 'a',
        'e' : 'e',
        'i' : 'i',
        'o' : 'o',
        'u' : 'u',
        'ă' : 'ə',
        'â' : 'ɨ',
        'î' : 'ɨ',
        'ș' : 'ʃ',
        'ț' : 'ts',
        'b' : 'b',
        'c' : 'k',
        'd' : 'd',
        'f' : 'f',
        'g' : 'g',
        'h' : 'h',
        'j' : 'ʒ',
        'k' : 'k',
        'l' : 'l',
        'm' : 'm',
        'n' : 'n',
        'p' : 'p',
        'q' : 'k',
        'r' : 'r',
        's' : 's',
        't' : 't',
        'v' : 'v',
        'w' : 'w',
        'x' : 'k s',
        'y' : 'j',
        'z' : 'z',
        '1' : 't͡ʃ',
        '2' : 'd͡ʒ',
        '3' : 'e̯',
        '4' : 'o̯',
        '5' : 'j'
    }
    replacements = {
        'che' : 'ke',
        'chi' : 'ki',
        'ce' : '1e',
        'ci' : '1i',
        'ge' : '2e',
        'gi' : '2i',
        'ghe' : 'ge',
        'ghi' : 'gi',
        'ea' : '3a',
        'oa' : '4a',
        'ai' : 'a5',
        'au' : 'aw',
        'ei' : 'e5',
        'ii' : 'i5',
        'oi' : 'o5',
        'ou' : 'ow',
        'ui' : 'u5',
        'uu' : 'uw',
        'ăi' : 'ə5',
        'ău' : 'əw',
        'âi' : 'ɨ5',
        'âu' : 'ɨw',
        'îi' : 'ɨ5',
        'îu' : 'ɨw',
        'eo' : '3o',
        'eu' : '3u',
        'ia' : '5a',
        'ie' : '5e',
        'io' : '5o',
        'iu' : '5u',
        'ue' : 'we',
        'ua' : 'wa',
        'uă' : 'wə',
        'uî' : 'wɨ',
        'uâ' : 'wɨ',
    }

    #replace digraphs with single chars
    for key, val in replacements.items():
        rom = rom.replace(key,val)
    
    #construct ipa string
    ipa = ''
    for char in rom:
        ipa += ipa_dict[char] + ' '
    return ipa

def main():
    with open(INPUT_FILE,mode='r',encoding='utf-8') as f:
        lines = [ln.strip() for ln in f.readlines()]
        lines = [ln for ln in lines if ln != '']

    for line in lines:
        if line[0] == '$':
            match = re.search(r'[^\s^\$^\*]+>[^\s]+',line)
            if match:
                spl = match.group().split('>')
                print(spl)
                lat = spl[0].split(',')[0]
                rom = spl[1].split(',')[0]
                lat_ipa = latin_to_ipa(lat)
                rom_ipa = romanian_to_ipa(rom)
                print(lat_ipa,rom_ipa)
        else:
            #regular line
            break

if __name__ == '__main__':
    main()
