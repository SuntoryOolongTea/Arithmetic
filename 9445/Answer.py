import functools
import re

class Answer:
#这是用于生成任何题目文件的结果到Answers.txt中的类

    def __init__(self, FileName):
        self.file = FileName
        self.OpenAFile()

    def mul_divOperation(self, s):
        sub_str = re.search('(\d+\.?\d*[*/]-?\d+\.?\d*)', s)
        while sub_str:
            sub_str = sub_str.group()
            if sub_str.count('*'):
                l_num, r_num = sub_str.split('*')
                s = s.replace(sub_str, str(float(l_num) * float(r_num)))
            else:
                l_num, r_num = sub_str.split('/')
                s = s.replace(sub_str, str(float(l_num) / float(r_num)))
            sub_str = re.search('(\d+\.?\d*[*/]\d+\.?\d*)', s)
        return s

    def add_minusOperation(self, s):
        s = '+' + s
        tmp = re.findall('[+\-]\d+\.?\d*', s)
        s = str(functools.reduce(lambda x, y: float(x) + float(y), tmp))
        return s

    def compute(self, formula):
        formula = self.mul_divOperation(formula)
        formula = self.add_minusOperation(formula)
        return formula

    def calc(self, formula):
        """计算程序入口"""
        if (formula[0] == '(' and formula[len(formula) - 1] == ')'):
            formula = formula.replace('(', '')
            formula = formula.replace(')', '')
        formula = re.sub('[^.()/*÷\-+0-9]', "", formula)  # 清除非算式符号
        if (formula[1] == '.'):
            formula = formula.replace(formula[0:2], '')  # 计算含有题目序列号的标准算式
        has_parenthesise = formula.count('(')
        while has_parenthesise:
            sub_parenthesise = re.search('\([^()]*\)', formula)  # 匹配最内层括号
            if sub_parenthesise:
                formula = formula.replace(sub_parenthesise.group(), self.compute(sub_parenthesise.group()[1:-1]))
            else:
                has_parenthesise = False
        ret = self.compute(formula)
        return ret

    def Transfer(self, formula):
        '这是一个把小数字符串转换成分数的函数'
        i = formula.find('.')
        if (i != -1 and formula.find('-') == -1):  # 如果存在小数点，只取小数点后三位
            e = float(formula[0:i + 4])
            intE = int(e)
            term = round(e - intE, 4)  # 小数部分四舍五入
            if (term == 0): return formula[:i]
            termD = term * 1000
            Deno = 1000
            if (termD % 333 == 0): Deno = 999  # 优化小学生算术题中常出现的1/3
            while (termD != Deno):  # 求最大公约数以化简
                if (Deno > termD): Deno = Deno - termD
                if (termD > Deno): termD = termD - Deno
            term = int(term * 1000 / termD)
            Deno = int(1000 / termD)
            if (intE != 0): answers = [str(intE), '\'', str(term), '/', str(Deno)]
            if (intE == 0): answers = [str(term), '/', str(Deno)]
            answers = ''.join(answers)
            return answers
        else:
            return formula

    def OpenAFile(self):
        fileE = open(self.file, "r+")
        string = fileE.read()
        fileE.close()
        string = string.replace('÷', '/')
        out = ""
        for line in string.splitlines():
            # out = out + self.compute(line) + '\n'
            out = out.replace('+', '')
            out = out + self.Transfer(self.calc(line)) + '\n'
        fileA = open("Answers.txt", "w+")
        print('生成答案结束，文件名为answer.txt')
        print(out, file=fileA)
        fileA.close()