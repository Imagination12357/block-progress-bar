def isSafe(n, a, b):
    return (a<=n and n<=b) or (b<=n and n<=a)

def clip(n, a, b):
    return min(max(n,a),b) if a<=b else min(max(n,b),a)

#TODO: Docstring, README
#TODO: Customizing position or hiding of current/max and direction of progress bar
class ProgressBar():
    def __init__(self, now_value:float=0, max_value:float=1, char:int=10, do_clip:bool=True, space:str=' '):
        self.string_table={
            0.125:'▏',
            0.25 :'▎',
            0.375:'▍',
            0.5  :'▌',
            0.625:'▋',
            0.75 :'▊',
            0.875:'▉',
            1    :'█'
        }
        self.max = max_value
        self.char = char
        self.do_clip = do_clip
        self.space = space
        if not isSafe(now_value, 0, max_value):
            if do_clip:
                self.now = clip(now_value, 0, max_value)
            else:
                raise ValueError(f"'now' must be between 0 and {max_value}, but got {now_value}")
        else:
            self.now = now_value


    def setAbsolute(self, now_value:float):
        if not isSafe(now_value, 0, self.max):
            if self.do_clip:
                self.now = clip(now_value, 0, self.max)
            else:
                raise ValueError(f"'now' must be between 0 and {self.max}, but got {now_value}")
        else:
            self.now = now_value
    
    def addAbsolute(self, delta:float):

        self.now += delta

        if not isSafe(self.now, 0, self.max):
            if self.do_clip:
                self.now = clip(self.now, 0, self.max)
            else:
                raise ValueError(f"'now' must be between 0 and {self.max}, but you tried to add {self.now} with {delta}")
    
    def setPercentage(self, now_percentage:float):
        now_value = (now_percentage/100) * self.max
        if not isSafe(now_value, 0, self.max):
            if self.do_clip:
                self.now = clip(now_value, 0, self.max)
            else:
                raise ValueError(f"percentage must be between 0 and 100, but got {now_percentage}")
        else:
            self.now = now_value

    def addPercentage(self, delta_percentage:float):
        
        self.now += (delta_percentage/100) * self.max
        
        if not isSafe(self.now, 0, self.max):
            if self.do_clip:
                self.now = clip(self.now, 0, self.max)
            else:
                raise ValueError(f"'now' must be between 0 and {self.max}, but you tried to make it into {self.now}")

    def setNormalized(self, now_normed:float):
        now_value = (now_normed) * self.max
        if not isSafe(now_value, 0, self.max):
            if self.do_clip:
                self.now = clip(now_value, 0, self.max)
            else:
                raise ValueError(f"Normalized value must be between 0 and 1, but got {now_normed}")
        else:
            self.now = now_value

    def addNormalized(self, delta_normed:float):
        
        self.now += (delta_normed) * self.max
        
        if not isSafe(self.now, 0, self.max):
            if self.do_clip:
                self.now = clip(self.now, 0, self.max)
            else:
                raise ValueError(f"'now' must be between 0 and {self.max}, but you tried to make it into {self.now}")

    def render(self):
        now_char = (self.now/self.max)*self.char
        full_char = int(now_char)
        rest_char = round((now_char % 1)*8)/8
        space_char = self.char - full_char - (0 if rest_char==0.0 else 1)
        return '█'*full_char + (self.string_table[rest_char] if rest_char != 0.0 else '') + self.space*space_char

if __name__ == '__main__':
    import random
    for i in range(10):
        value=random.random()
        print(f'{ProgressBar(value,1,char=50).render()}|{value:.3f}/1')
