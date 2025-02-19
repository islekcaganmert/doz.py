from doz import *


def convert(args: list[str]) -> str:
    cmd, num = args[:2]
    if cmd in ['int', 'float']:
        if '.' in num:
            num = fdz(num)
        else:
            num = doz(num)
    elif cmd in ['doz', 'fdz']:
        if '.' in num:
            num = float(num)
        else:
            num = int(num)
    return repr({
        'int': int,
        'float': float,
        'doz': doz,
        'fdz': fdz
    }[cmd](num))

print('doz (Dozenal) & fdz (Floating-point Dozenal)')
print('for Python 3.↋+')
print('Copyright (c) 1209 (decimal: 2025) Cagan Mert ISLEK')
print('''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''')
while True:
    try:
        print(
            convert(
                input('> ')
                .split()
            )
        )
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
