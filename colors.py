import dataclasses
import regex

from pprint import pprint

COLOR_RE = regex.compile(r'(?<=#)(?P<red>\w{2})(?P<green>\w{2})(?P<blue>\w{2})')
    
class ColorComponent:
    
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f'_{name}'
        
    def __get__(self, obj, objtype=None):  
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        setattr(obj, self.private_name, int(value, 16))

        
@dataclasses.dataclass
class RGB():
    red: ColorComponent = ColorComponent()
    green: ColorComponent = ColorComponent()
    blue: ColorComponent = ColorComponent()
    
def get_component_colors(line):
    match COLOR_RE.search(line):
        case None:
            return (line,)
        case m:
            return (line, RGB(**m.groupdict()))
        
def main():

    with open('gruvbox_hard_theme.txt') as fp:
        lines = [s.strip() for s in fp]

    all_colors = list((get_component_colors(line) for line in lines))
    pprint(all_colors)
    
if __name__ == '__main__':
    main()
