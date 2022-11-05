#created by Yuecheng Ma at 2022-11-4 8:08PM, Weblinks https://thomasma.ca, https://wordpress.thomasma.ca
#=================================
#runtimes
#=================================
import webbrowser as wb
import sys
#=================================
#main programs
#=================================
def nothing():
    print('Survery, do you have a good internet (more then 250MB/s) if yes please type \x1B[4mY\x1B[0mes, if no please type \x1B[4mN\x1B[0mo:')
    internet = input()
    if internet == "Y" or "y" or "yes" or "Yes":
        wb.open('https://thomasma.ca/8k.mp4')
        print('I dont think my 土豆级别 server can handle 8k but goodluck')
    elif internet == "N" or "n" or "no" or "No":
        wb.open('https://thomasma.ca/1080.mp4')
    else:
        wb.open('https://www.speedtest.net')
#=================================
def Lunch_Concert():
    print("Lunch Concert - https://dmoj.ca/problem/ccc21s3")
    input = sys.stdin.readline
    p = []
    w = []
    d = []
    n = int(input())
    def move(c: int) -> int:
        time = 0
        for a in range(n):
            leftRange = p[a]-d[a]
            rightRange = p[a]+d[a]

            if c >= leftRange and c<= rightRange:
                continue

            closest = rightRange
            if abs(c-leftRange) < abs(c-rightRange):
                closest = leftRange
            time += w[a]*abs(closest-c)
        return time
    if __name__ == '__main__':
        l = 1e9
        r = 0
        for a in range(n):
            data = input().strip()
            data = data.split()
            p.append(int(data[0]))
            w.append(int(data[1]))
            d.append(int(data[2]))
            l = min(l, p[a])
            r = max(r, p[a])
        best = 1e18
        for _ in range(60):
            delta = int((r-l)/3)
            m1 = l+delta
            m2 = r-delta
            x1 = move(m1)
            x2 = move(m2)
            best = min(best, x1)
            best = min(best, x2)
            if x1 < x2:
                r = m2
            else:
                l = m1
        print(best)
        exit()
#=================================
#program selector
#=================================
print('Choose which program do you want to run, type \033[4m1\033[0m for \033[4mLunch Concert\033[0m made by Thomas:')
choose = input()
if choose.isdigit():
    choose = int(choose)
    if choose == 1:
        Lunch_Concert()
    else:
        nothing()
else:
    nothing()

