import pytest

def rgb(r,g,b):
   hex_strs = [hex(min(max(0,n), 255))[2:].upper() for n in [r, g, b]] # turns int to a hex string, omitting the 0x at the begging
   formatted_hex_strs = [h if len(h)==2 else "0" + h for h in hex_strs] # adds a leading 0 if none exists
   return formatted_hex_strs[0]+formatted_hex_strs[1]+formatted_hex_strs[2] # concats and returns

@pytest.mark.parametrize('r, g, b, value', [
      (0,0,0,"000000"),
      (1,2,3,"010203"),
      (255,255,255,"FFFFFF"),
      (254,253,252,"FEFDFC"),
      (-20,275,125,"00FF7D")
])
def test_rgb(r, g, b, value):
        assert rgb(r,g,b) == value