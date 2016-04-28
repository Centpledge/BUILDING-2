import execjs
execjs.eval("'red yellow blue'.split(' ')")
ctx = execjs.compile("""


    function add(x, y) {
         return x + y;
    }

    
 """)
print ctx.call("add", 1, 2)
print execjs.eval("'red yellow blue'.split(' ')")


a = execjs.compile("""

    function eiei(x,y){
    return x*y;
    }
""")

print a.call("eiei",2,4)


