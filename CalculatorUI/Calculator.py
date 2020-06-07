# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:04:13 2020

@author: MAYANK SHAW
"""

'''Here we will make the body of the calculator
Basically the UI'''

import tkinter as tk
from tkinter import ttk


class Calc:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Calculator')
        self.win.resizable(False, False)
        self.create_body()
        
    def onClickDisplay(self, args):
        if args == 1:
            self.query.set(self.query.get() + '1')
        elif args == 2:
            self.query.set(self.query.get() + '2')
        elif args == 3:
            self.query.set(self.query.get() + '3')
        elif args == 4:
            self.query.set(self.query.get() + '4')
        elif args == 5:
            self.query.set(self.query.get() + '5')
        elif args == 6:
            self.query.set(self.query.get() + '6')
        elif args == 7:
            self.query.set(self.query.get() + '7')
        elif args == 8:
            self.query.set(self.query.get() + '8')
        elif args == 9:
            self.query.set(self.query.get() + '9')
        elif args == 0:
            self.query.set(self.query.get() + '0')
        elif args == '+':
            self.query.set(self.query.get() + '+')
        elif args == '-':
            self.query.set(self.query.get() + '-')
        elif args == '*':
            self.query.set(self.query.get() + '*')
        elif args == '/':
            self.query.set(self.query.get() + '/')
        elif args == '(':
            self.query.set(self.query.get() + '(')
        elif args == ')':
            self.query.set(self.query.get() + ')')
        elif args == 'pi':
            self.query.set(self.query.get() + 'pi')
        elif args == 'e':
            self.query.set(self.query.get() + 'e')
            
        
    def clear(self):
        output = self.query.get()
        print(output)
        self.query.set('')
        
    

    def create_body(self):
        self.stdFrame = ttk.Labelframe(self.win, text="Standard")
        self.stdFrame.grid(column=0, row=0, padx=10, pady=10)
        #Make a display box
        self.entryLabel = ttk.Label(self.stdFrame, text="Input Goes Here ", state=tk.READABLE)
        self.entryLabel.grid(column=0, row=0, sticky='W', columnspan=5)
        
        self.query = tk.StringVar()
        self.displayBox = ttk.Entry(self.stdFrame, textvariable=self.query, width=50, state='readonly', justify='right')
        self.displayBox.grid(column=0, row=1, sticky='WE', pady=5, columnspan=5)
        
        
        #make the first row of operations
        self.clear_btn = ttk.Button(self.stdFrame, text='C', command=self.clear)
        self.clear_btn.grid(column=0, row=2)
        
        self.open_para_btn = ttk.Button(self.stdFrame, text='(', command=lambda:self.onClickDisplay('('))
        self.open_para_btn.grid(column=1, row=2)
        
        self.close_para_btn = ttk.Button(self.stdFrame, text=')', command=lambda:self.onClickDisplay(')'))
        self.close_para_btn.grid(column=2, row=2)
        
        self.pi_btn = ttk.Button(self.stdFrame, text='pi', command=lambda:self.onClickDisplay('pi'))
        self.pi_btn.grid(column=3, row=2)
        
        self.eps_btn = ttk.Button(self.stdFrame, text='e', command=lambda:self.onClickDisplay('e'))
        self.eps_btn.grid(column=4, row=2)
        
        
        #make second row
        self.btn_1 = ttk.Button(self.stdFrame, text='1', command=lambda:self.onClickDisplay(1))
        self.btn_1.grid(column=0, row=3)
        
        self.btn_2 = ttk.Button(self.stdFrame, text='2', command=lambda:self.onClickDisplay(2))
        self.btn_2.grid(column=1, row=3)
        
        self.btn_3 = ttk.Button(self.stdFrame, text='3', command=lambda:self.onClickDisplay(3))
        self.btn_3.grid(column=2, row=3)
        
        self.btn_4 = ttk.Button(self.stdFrame, text='4', command=lambda:self.onClickDisplay(4))
        self.btn_4.grid(column=3, row=3)
        
        self.btn_5 = ttk.Button(self.stdFrame, text='5', command=lambda:self.onClickDisplay(5))
        self.btn_5.grid(column=4, row=3)
        
        #make third row
        self.btn_6 = ttk.Button(self.stdFrame, text='6', command=lambda:self.onClickDisplay(6))
        self.btn_6.grid(column=0, row=4)
        
        self.btn_7 = ttk.Button(self.stdFrame, text='7', command=lambda:self.onClickDisplay(7))
        self.btn_7.grid(column=1, row=4)
        
        self.btn_8 = ttk.Button(self.stdFrame, text='8', command=lambda:self.onClickDisplay(8))
        self.btn_8.grid(column=2, row=4)
        
        self.btn_9 = ttk.Button(self.stdFrame, text='9', command=lambda:self.onClickDisplay(9))
        self.btn_9.grid(column=3, row=4)
        
        self.btn_0 = ttk.Button(self.stdFrame, text='0', command=lambda:self.onClickDisplay(0))
        self.btn_0.grid(column=4, row=4)
        
        #make fourth row
        self.btn_plus = ttk.Button(self.stdFrame, text='+', command=lambda:self.onClickDisplay('+'))
        self.btn_plus.grid(column=0, row=5)
        
        self.btn_minus = ttk.Button(self.stdFrame, text='-', command=lambda:self.onClickDisplay('-'))
        self.btn_minus.grid(column=1, row=5)
        
        self.btn_mul = ttk.Button(self.stdFrame, text='*', command=lambda:self.onClickDisplay('*'))
        self.btn_mul.grid(column=2, row=5)
        
        self.btn_div = ttk.Button(self.stdFrame, text='/', command=lambda:self.onClickDisplay('/'))
        self.btn_div.grid(column=3, row=5)
        
        self.btn_res = ttk.Button(self.stdFrame, text='=', command=self.evaluate_query)
        self.btn_res.grid(column=4, row=5)
        
         #Make a result box
        self.resLabel = ttk.Label(self.stdFrame, text="Result Comes Here ")
        self.resLabel.grid(column=0, row=6, sticky='W', columnspan=5)
        
        self.result = tk.StringVar()
        self.resultBox = ttk.Entry(self.stdFrame, textvariable=self.result, width=50, state='readonly', justify='right')
        self.resultBox.grid(column=0, row=7, sticky='WE', pady=5, columnspan=5)
        
    def evaluate_query(self):
        express_str = self.query.get()
        express_str = express_str.replace('pi','3.14')
        express_str = express_str.replace('e', '2.73')
        res = self.get_tokens(express_str)
        print(res)
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            return 0
        
        def applyOp(a, b, op):
            if op == '+': return a+b
            if op == '-': return a-b
            if op == '*': return a*b
            if op == '/': return a/b
            
        values, ops, i = [], [], 0
        op_types = ['+','-','*','/','(',')']
        while i<len(res):
            if res[i] == ' ':  # if whitespace ignore it
                i += 1
                continue
            elif res[i] == '(':         # if  ( push it into ops stack
                ops.append(res[i])
                
            elif res[i] not in op_types:
                values.append(float(res[i]))
                
            elif res[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    
                    values.append(applyOp(val1, val2, op))
                
                ops.pop()  # pop opening bracket
                
            else:
                while (len(ops) != 0 and precedence(ops[-1]) >= precedence(res[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    
                    values.append(applyOp(val1, val2, op))
                ops.append(res[i])
                
            i += 1
        
        #entire expression has been parsed at this point, apply remaining ops to remaining values
        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            
            values.append(applyOp(val1, val2, op))
            
        final_ans = values[-1]
        print('Final: ',final_ans)
        
        #return answer to result tab
        self.result.set(final_ans)
        
                
    def get_tokens(self, exp_str):
        tokens = ['']
        
        for i in exp_str.replace(" ",""):
            if (i.isdigit() or i=='.' ) and (tokens[-1].isdigit() or tokens[-1] == '.' or '.'  in tokens[-1]):
                tokens[-1] = tokens[-1]+i
            else:
                tokens.append(i)
        return tokens[1:]
            
        
if __name__=='__main__':
    clc = Calc()
    clc.win.mainloop()