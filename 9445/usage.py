import time

from Genera import Genera
from Verify import Verify
from Answer import Answer
from Judge import Judge
from optparse import OptionParser

usage = "[<-n> + 数字] 确定题目条数 [<-r> + 数字] 确定数字范围 \n 可选参数: \n <-u> 生成有负数出现的题目 \n [<-a> + (filename)] 回答filename文件的题目 \n [<-e> + (filename)] 批改filename文件的题目"
parser = OptionParser() # usage
# parser.print_help()
parser.add_option("-n", action='store', type='int', dest='Numbers', help="生成Numbers条无负数结果的算式,输出文件是StandExercises.txt")
parser.add_option("-r", action='store', type='int', dest='Range', help="指定数字Range范围")
parser.add_option("-u", action='store', type='string', dest='ProExFile', help="生成Numbers条有负数结果的算式,输出文件时Exercises.txt")
parser.add_option("-a", action='store', type='string', dest='AnsFile', help="指定题目文件,并生成答案到Answers.txt")
parser.add_option("-e", action='store', type='string', dest='JudgeFile', help="指定用户答案文件,并将其和标准Answers.txt对比")
options, args = parser.parse_args()
print(options.Numbers, options.Range, options.ProExFile)
if options.Numbers is not None and options.Range:  #  and options.ProExFile
    '生成Numbers条有负数结果的算式, 再将其标准化(去除中间过程有负数结果的算式以及/后面有0的非法算式), 输出文件是StandExercises.txt'
    t = int(round(time.time() * 1000))
    fileE = Genera(options.Numbers, options.Range)
    fileStand = Verify(fileE.filename)
    print('next: is time:')
    t = int(round(time.time() * 1000))-t
    print(t)
    print('ms')# 微秒级时间戳
if options.Numbers and options.Range and options.ProExFile and options.AnsFile:
    '生成Numbers条有负数结果的算式, 再将其标准化(去除中间过程有负数结果的算式以及/后面有0的非法算式), 输出文件是StandExercises.txt'
    t = time.time()
    fileE = Genera(options.Numbers, options.Range)
    t-= t
    fileStand = Verify(fileE.filename)
    fileA = Answer(options.AnsFile)
    print(str(t)+'ms')

if options.AnsFile and not options.Numbers:
    '回答-a后面的filename题目文件,并输出结果到Answers.txt文件'
    fileA = Answer(options.AnsFile)

if options.ProExFile and options.Numbers and options.Range and not options.AnsFile:
    '生成Numbers条有负数结果的算式, 生成文件是Exercises.txt'
    fileE = Genera(options.Numbers, options.Range)

if options.JudgeFile and not options.Numbers and not options.Range and not options.ProExFile:
    '-e 接一个用户的答案文件, 并将其和标准答案文件Answers.txt比较'
    FileA = Judge(options.JudgeFile, "Answers.txt")
if options.Numbers:
    print('asdads')


if __name__ == '__main__':
    pass